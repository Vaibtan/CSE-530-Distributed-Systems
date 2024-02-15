import grpc
import seller_pb2
import seller_pb2_grpc
import market_pb2
import market_pb2_grpc
from Product import Item

PORT_ADDRESS : str = "localhost:50052"

class SellerClient:
    def __init__(self, seller_server_address, market_server_address):
        self.seller_channel = grpc.insecure_channel(seller_server_address)
        self.seller_stub = seller_pb2_grpc.SellerServiceStub(self.seller_channel)
        self.market_channel = grpc.insecure_channel(market_server_address)
        self.market_stub = market_pb2_grpc.MarketServiceStub(self.market_channel)

    def register_seller(self, address, uuid):
        request = seller_pb2.RegisterSellerRequest(address = address, uuid = uuid)
        response = self.seller_stub.RegisterSeller(request)
        print(f"Registration status: {response.status}")
    
    def sell_item(self, item : Item):
        request = seller_pb2.SellItemRequest(item = item)
        response = self.seller_stub.SellItem(request)
        print(f"Sell item status: {response.status}")        

    def update_item(self, uuid, item_id, price, quantity):
        request = seller_pb2.UpdateItemRequest(\
            uuid = uuid, item_id = item_id, price = price, quantity = quantity)
        response = self.stub.UpdateItem(request)
        return response.success        

    def delete_item(self, item_id):
        request = seller_pb2.DeleteItemRequest(item_id = item_id)
        response = self.stub.DeleteItem(request)
        return response.success

    def display_seller_items(self, seller_address):
        request = seller_pb2.DisplaySellerItemsRequest(seller_address=seller_address)
        response = self.stub.DisplaySellerItems(request)
        return response.items

    def notify_market(self, message):
        request = market_pb2.NotifyClientRequest(message = message)
        response = self.market_stub.NotifyClient(request)
        print(f"Notification status: {response.status}")


'''

class SellerClient:
    def __init__(self, seller_server_address, market_server_address):
        self.seller_channel = grpc.insecure_channel(seller_server_address)
        self.seller_stub = seller_pb2_grpc.SellerStub(self.seller_channel)
        self.market_channel = grpc.insecure_channel(market_server_address)
        self.market_stub = market_pb2_grpc.MarketStub(self.market_channel)

    def register_seller(self, address, uuid):
        request = seller_pb2.RegisterSellerRequest(address=address, uuid=uuid)
        response = self.seller_stub.RegisterSeller(request)
        return response.success

    def sell_item(self, name, category, quantity, description, price, seller_address, seller_uuid):
        request = seller_pb2.SellItemRequest(
            name=name,
            category=category,
            quantity=quantity,
            description=description,
            price=price,
            seller_address=seller_address,
            seller_uuid=seller_uuid
        )
        response = self.seller_stub.SellItem(request)
        return response.item_id

    def update_item(self, item_id, price, quantity):
        request = seller_pb2.UpdateItemRequest(item_id=item_id, price=price, quantity=quantity)
        response = self.seller_stub.UpdateItem(request)
        return response.success

    def delete_item(self, item_id):
        request = seller_pb2.DeleteItemRequest(item_id=item_id)
        response = self.seller_stub.DeleteItem(request)
        return response.success

    def display_seller_items(self, seller_address):
        request = seller_pb2.DisplaySellerItemsRequest(seller_address=seller_address)
        response = self.seller_stub.DisplaySellerItems(request)
        return response.items

    def notify_market(self, message):
        request = market_pb2.NotifyClientRequest(message=message)
        response = self.market_stub.NotifyClient(request)
        return response.success

if __name__ == "__main__":
    # Example usage
    seller_client = SellerClient('localhost:50052', 'localhost:50051') # Seller server and Market server addresses
    
    # Example usage
    seller_address = "192.168.1.100:5001"
    seller_uuid = "987a515c-a6e5-11ed-906b-76aef1e817c5"
    
    seller_client.register_seller(seller_address, seller_uuid)
    message = "New seller registered: 192.168.1.100:5001, UUID: 987a515c-a6e5-11ed-906b-76aef1e817c5"
    seller_client.notify_market(message)
    print(seller_client.display_seller_items(seller_address))
    # Perform other operations as needed

'''