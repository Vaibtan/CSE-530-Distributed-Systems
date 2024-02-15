import grpc
import buyer_pb2
import buyer_pb2_grpc
import market_pb2
import market_pb2_grpc


class BuyerClient:
    def __init__(self, buyer_server_address, market_server_address) -> None:
        self.buyer_channel = grpc.insecure_channel(buyer_server_address)
        self.buyer_stub = buyer_pb2_grpc.BuyerServiceStub(self.channel)
        self.market_channel = grpc.insecure_channel(market_server_address)
        self.market_stub = market_pb2_grpc.MarketServiceStub(self.channel)


    def search_item(self, name="", category="ANY"):
        request = buyer_pb2.SearchItemRequest(name=name, category=category)
        response = self.buyer_stub.SearchItem(request)
        return response.items
    
    def buy_item(self, item_id, quantity, buyer_address):
        request = buyer_pb2.BuyItemRequest(item_id = item_id, quantity = quantity, buyer_address=buyer_address)
        response = self.buyer_stub.BuyItem(request)
        return response.status

    def add_to_wishlist(self, item_id, buyer_address):
        request = buyer_pb2.AddToWishlistRequest(item_id=item_id, buyer_address = buyer_address)
        response = self.buyer_stub.AddToWishlist(request)
        return response.status

    def rate_item(self, item_id, buyer_address, rating):
        request = buyer_pb2.RateItemRequest(item_id=item_id, buyer_address=buyer_address, rating=rating)
        response = self.buyer_stub.RateItem(request)
        return response.status

    def notify_market(self, updated_item):
        request = market_pb2.NotifyClientRequest(updated_item=updated_item)
        response = self.market_stub.NotifyClient(request)
        return response.status





'''
def search_item(stub, item_name="", category="ANY"):
    request = buyer_pb2.SearchItemRequest(item_name=item_name, category=category)
    response = stub.SearchItem(request)
    for item in response.items:
        print(f"Item ID: {item.item_id}, Name: {item.name}, Price: ${item.price}, Category: {item.category}")
        print(f"Description: {item.description}")
        print(f"Quantity Remaining: {item.quantity}, Rating: {item.rating}")
        print(f"Seller: {item.seller_address}")
        print()

def buy_item(stub, item_id, quantity):
    # Create a request message
    request = buyer_pb2.BuyItemRequest(item_id=item_id, quantity=quantity)
    # Call the BuyItem RPC
    response = stub.BuyItem(request)
    # Print the response
    if response.success:
        print("Item bought successfully")
    else:
        print("Failed to buy item:", response.message)

def add_to_wishlist(stub, item_id):
    # Create a request message
    request = buyer_pb2.AddToWishListRequest(item_id=item_id)
    # Call the AddToWishList RPC
    response = stub.AddToWishList(request)
    # Print the response
    if response.success:
        print("Item added to wish list successfully")
    else:
        print("Failed to add item to wish list:", response.message)

def rate_item(stub, item_id, rating):
    # Create a request message
    request = buyer_pb2.RateItemRequest(item_id=item_id, rating=rating)
    # Call the RateItem RPC
    response = stub.RateItem(request)
    # Print the response
    if response.success:
        print("Item rated successfully")
    else:
        print("Failed to rate item:", response.message)

def main():
    # Create a gRPC channel and a stub
    channel = grpc.insecure_channel('localhost:50053')
    stub = buyer_pb2_grpc.BuyerStub(channel)

if __name__ == '__main__':
    main()

'''