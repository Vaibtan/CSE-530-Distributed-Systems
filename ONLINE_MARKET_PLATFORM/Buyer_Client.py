import grpc
import buyer_pb2
import buyer_pb2_grpc


#PORT_ADDRESS : str = 'localhost:50053'

# buyer_client.py

def search_item(stub, item_name="", category="ANY"):
    # Create a request message
    request = buyer_pb2.SearchItemRequest(item_name=item_name, category=category)
    # Call the SearchItem RPC
    response = stub.SearchItem(request)
    # Print the response items
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
