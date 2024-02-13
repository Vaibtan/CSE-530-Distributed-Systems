import grpc
import seller_pb2
import seller_pb2_grpc
import market_pb2
import market_pb2_grpc

PORT_ADDRESS : str = "localhost:50052"

class SellerClient:
    def __init__(self, server_address, market_address):
        self.channel = grpc.insecure_channel(server_address)
        self.stub = seller_pb2_grpc.SellerServiceStub(self.channel)
        self.market_channel = grpc.insecure_channel(market_address)
        self.market_stub = market_pb2_grpc.MarketServiceStub(self.market_channel)

    def register_seller(self, address, uuid):
        request = seller_pb2.RegisterSellerRequest(address = address, uuid = uuid)
        response = self.stub.RegisterSeller(request)
        return response.success
    
    def sell_item(self, name, category, quantity, description, price, seller_address, seller_uuid):
        request = seller_pb2.SellItemRequest(
            name = name,
            category = category,
            quantity = quantity,
            description = description,
            price = price,
            seller_address = seller_address,
            seller_uuid = seller_uuid
        )
        response = self.stub.SellItem(request)
        return response.item_id
        
        # print("SellItem response:", response)

    def update_item(self, item_id, price, quantity):
        request = seller_pb2.UpdateItemRequest(\
            item_id = item_id, price = price, quantity = quantity)
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
        request = market_pb2.NotifyClientRequest(message=message)
        response = self.market_stub.NotifyClient(request)
        return response.success


if __name__ == '__main__':
    pass