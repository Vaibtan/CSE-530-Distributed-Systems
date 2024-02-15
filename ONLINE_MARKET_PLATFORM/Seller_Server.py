import grpc
import seller_pb2
import seller_pb2_grpc
from concurrent import futures
from Product import Item, ALLOWED_CATEGORY_TYPES

class SellerServicer(seller_pb2_grpc.SellerServiceServicer):
    def __init__(self, seller_uuid, seller_address):
        self.address = seller_address
        self.uuid = seller_uuid 
        self.registered_sellers = {}
        self.seller_items = {}


    def RegisterSeller(self, request, context):
        address = request.address
        uuid = request.uuid
        if request.uuid in self.registered_sellers:
            return seller_pb2.RegisterSellerResponse(status = "FAILED",\
                                        message = "Seller already registered")
        else:
            self.registered_sellers[uuid] = address
            return seller_pb2.RegisterSellerResponse(status = "SUCCESS")
#            print(f"Seller registered: {address}, UUID: {uuid}")
            
#            message = f"Seller registered: {address}, UUID: {uuid}"
#            self.notify_market(message)
#            return seller_pb2.RegisterSellerResponse(status = "SUCCESS")
#        else:
#            print(f"Seller registration failed: Address {address} already registered")
#            return seller_pb2.RegisterSellerResponse(success = False)

    def SellItem(self, request, context):
        item_id = len(self.items) + 1
        item_name = request.name
        item_category = request.category
        item_quantity = request.quantity
        item_description = request.description
        item_price = request.price
        seller_uuid = request.uuid

        if item_category not in ALLOWED_CATEGORY_TYPES:
            pass

        new_item = Item(id = item_id, name = item_name, category = item_category, \
                        quantity = item_quantity, description=item_description, price=item_price, \
                        rating = 0, seller_address = self.registered_sellers.get(seller_uuid, ""))
    
        if seller_uuid in self.seller_items:
            self.seller_items[seller_uuid].append(new_item)
        else:
            self.seller_items[seller_uuid] = [new_item]

        return seller_pb2.SellItemResponse(status = "SUCCESSFUL", item_id = item_id)


    def UpdateItem(self, request, context):
        item_id = request.item_id
        new_price = request.price
        new_quantity = request.quantity
        seller_uuid = request.uuid

        seller_items = self.seller_items.get(seller_uuid, [])
        updated_item = next((item for item in seller_items if item.id == item_id), None)
        if updated_item:
            updated_item.price = new_price
            updated_item.quantity = new_quantity
            return seller_pb2.UpdateItemResponse(status = "SUCCESS")
        else:
            return seller_pb2.UpdateItemResponse(status = "FAILED", message = "Item not found")

    def DeleteItem(self, request, context):
        item_id = request.item_id
        seller_uuid = request.uuid

        seller_items = self.seller_items.get(seller_uuid, [])
        deleted_item_index = next((index for index, item in enumerate(seller_items) if item.id == item_id), None)
        if deleted_item_index is not None:
            del seller_items[deleted_item_index]
            return seller_pb2.DeleteItemResponse(status="SUCCESS")
        else:
            return seller_pb2.DeleteItemResponse(status="FAILED", message="Item not found")
    
    def DisplaySellerItems(self, request, context):
        seller_uuid = request.uuid
        seller_items = self.seller_items.get(seller_uuid, [])
        items_response = seller_pb2.DisplaySellerItemsResponse()
        for item in seller_items:
            item_info = seller_pb2.ItemInfo(
                id = item.id,
                name = item.name,
                category = item.category,
                quantity = item.quantity,
                description = item.description,
                price = item.price,
                rating = item.rating,
                seller_address = item.seller_address
            )
            items_response.items.append(item_info)
        return items_response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    seller_pb2_grpc.add_SellerServiceServicer_to_server(SellerServicer('localhost:50051'), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Seller server started. Listening on port 50052.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
