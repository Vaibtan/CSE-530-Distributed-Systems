import grpc
import buyer_pb2
import buyer_pb2_grpc
from concurrent import futures
from threading import Thread
import uuid
from Product import Item, ALLOWED_CATEGORY_TYPES

#type_map : dict = {}


class BuyerServicer(buyer_pb2_grpc.BuyerServiceServicer):
    def __init__(self, items):
        self.items = items
        self.wishlist = {}
        self.item_ratings = {}

    def SearchItem(self, request, context):
        search_results = []
        if request.item_name and request.category:
            search_results = Item.filter_items_double(self.items, name=request.item_name, category=request.category)
        elif request.item_name:
            search_results = Item.filter_by_name(self.items, name=request.item_name)
        elif request.category:
            search_results = Item.filter_by_category(self.items, category=request.category)
        else:
            search_results = self.items

        response_items = [self._convert_to_proto(item) for item in search_results]
        response = buyer_pb2.SearchItemResponse(items=response_items)
        return response
    
    @staticmethod
    def _convert_to_proto(self, item):
        return buyer_pb2.Item(
            id=item.id,
            name=item.name,
            category=item.category,
            quantity=item.quantity,
            description=item.description,
            price=item.price,
            rating=item.rating,
            seller_address=item.seller_address
        )


    def BuyItem(self, request, context):
        item_id = request.item_id
        quantity = request.quantity
        buyer_address = request.buyer_address

        item = self._find_item_by_id(item_id)
        if not item:
            return buyer_pb2.BuyItemResponse(status="FAILED", message=f"Item with ID {item_id} not found.")

        if item.quantity < quantity:
            return buyer_pb2.BuyItemResponse(status="FAILED", message=f"Not enough stock for item with ID {item_id}.")

        item.quantity -= quantity
 #       self._notify_seller(item, quantity, buyer_address)

        return buyer_pb2.BuyItemResponse(status="SUCCESS", message="Transaction successful.")

    @staticmethod
    def _find_item_by_id(self, item_id):
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def AddToWishlist(self, request, context):
        item_id = request.item_id
        buyer_address = request.buyer_address

        if buyer_address not in self.wishlist:
            self.wishlist[buyer_address] = []
        self.wishlist[buyer_address].append(item_id)

        return buyer_pb2.AddToWishlistResponse(status="SUCCESS", message="Item added to wishlist.")
    
    def RateItem(self, request, context):
        item_id = request.item_id
        buyer_address = request.buyer_address
        rating = request.rating

        if rating < 1 or rating > 5:
            return buyer_pb2.RateItemResponse(status="FAILED", message="Rating must be between 1 and 5.")

        if buyer_address in self.item_ratings and item_id in self.item_ratings[buyer_address]:
            return buyer_pb2.RateItemResponse(status="FAILED", message="Buyer has already rated this item.")

        if buyer_address not in self.item_ratings:
            self.item_ratings[buyer_address] = {}
        self.item_ratings[buyer_address][item_id] = rating

        return buyer_pb2.RateItemResponse(status="SUCCESS", message="Item rated successfully.")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    buyer_pb2_grpc.add_BuyerServicer_to_server(BuyerServicer(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
