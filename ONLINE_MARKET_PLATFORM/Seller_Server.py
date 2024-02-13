import time
import grpc
import seller_pb2
import seller_pb2_grpc
import market_pb2
import market_pb2_grpc
from concurrent import futures
from threading import Thread, Lock
from datetime import date, datetime
from Product import Item, ALLOWED_CATEGORY_TYPES

PORT_ADDRESS : str = ""


class SellerServicer(seller_pb2_grpc.SellerServiceServicer):
    def __init__(self, market_address):
        self.sellers = {}
        self.items = {}
        self.market_channel = grpc.insecure_channel(market_address)
        self.market_stub = market_pb2_grpc.MarketServiceStub(self.market_channel)
    
    def notify_market(self, message):
        request = market_pb2.NotifyClientRequest(message=message)
        response = self.market_stub.NotifyClient(request)
        return response.success
    
    def RegisterSeller(self, request, context):
        address = request.address
        uuid = request.uuid
        if address not in self.sellers:
            self.sellers[address] = uuid
            print(f"Seller registered: {address}, UUID: {uuid}")
            
            # NOTIFY_ABOUT_NEW_SELLER
            message = f"Seller registered: {address}, UUID: {uuid}"
            self.notify_market(message)
            return seller_pb2.RegisterSellerResponse(success = True)
        else:
            print(f"Seller registration failed: Address {address} already registered")
            return seller_pb2.RegisterSellerResponse(success = False)

    def SellItem(self, request, context):
        item_id = len(self.items) + 1
        self.items[item_id] = {
            'name': request.name,
            'category': request.category,
            'quantity': request.quantity,
            'description': request.description,
            'price': request.price,
            'seller_address': request.seller_address,
            'seller_uuid': request.seller_uuid
        }
        print(f"Item '{request.name}' added with ID: {item_id}")
        return seller_pb2.SellItemResponse(item_id = item_id)
    
        '''    
        self.items.append(request)
        print("Item added to seller's inventory:", request)
        return seller_pb2.SellItemResponse(\
            status=seller_pb2.SellItemResponse.Status.SUCCESS
        )
        '''

    def UpdateItem(self, request, context):
        item_id = request.item_id
        if item_id in self.items:
            self.items[item_id]['price'] = request.price
            self.items[item_id]['quantity'] = request.quantity
            self.items[item_id]['description'] = request.description
            print(f"Item {item_id} updated")

            message = f"Item {item_id} updated"
            self.notify_market(message)
            return seller_pb2.UpdateItemResponse(success = True)
        else:
            print(f"Item {item_id} not found")
            return seller_pb2.UpdateItemResponse(success = False)

    def DeleteItem(self, request, context):
        item_id = request.item_id
        if item_id in self.items:
            del self.items[item_id]
            print(f"Item {item_id} deleted")
            return seller_pb2.DeleteItemResponse(success = True)
        else:
            print(f"Item {item_id} not found")
            return seller_pb2.DeleteItemResponse(success = False)

    def DisplaySellerItems(self, request, context):
        seller_address = request.seller_address
        items_info = []
        for item_id, item_details in self.items.items():
            if item_details['seller_address'] == seller_address:
                item_info = f"Item ID: {item_id}, Name: {item_details['name']}, " \
                            f"Category: {item_details['category']}, " \
                            f"Quantity: {item_details['quantity']}, " \
                            f"Description: {item_details['description']}, " \
                            f"Price: {item_details['price']}, " \
                            f"Seller: {item_details['seller_address']}, " \
                            f"Seller UUID: {item_details['seller_uuid']}"
                items_info.append(item_info)
        print(f"Seller {seller_address} items:\n{items_info}")
        return seller_pb2.DisplaySellerItemsResponse(items = items_info)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    seller_pb2_grpc.add_SellerServicer_to_server(SellerServicer('localhost:50051'), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Seller server started. Listening on port 50052.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
