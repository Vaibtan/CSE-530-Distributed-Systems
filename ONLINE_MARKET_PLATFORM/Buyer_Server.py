import time
import grpc
import buyer_pb2
import buyer_pb2_grpc
from concurrent import futures
from threading import Thread
import uuid
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp

#REGISTRY_ADDRESS : str = ""

#type_map : dict = {}

trial_items = {
    "1": buyer_pb2.Item(\
        item_id="1", name="iPhone", description="This is iPhone 15.", \
            category="Electronics", quantity = 5, price = 500, rating = 4.3, \
                seller_address="192.13.188.178:50051"),
    "2": buyer_pb2.Item(item_id="2", name="Laptop", \
                        description="This is a laptop.", \
                            category="Electronics", quantity=10, \
                                price=800, rating=4.5, \
                                    seller_address="192.13.188.179:50052"),
}

class BuyerServicer(buyer_pb2_grpc.BuyerServiceServicer):
    def __init__(self):
        self.items = []

    def SearchItem(self, request, context):
        items = []
        for item_id, item in trial_items.items():
            if (request.item_name == "" or request.item_name.lower() in item.name.lower()) and \
               (request.category == "" or request.category == "ANY" or request.category == item.category):
                items.append(item)
        return buyer_pb2.SearchItemResponse(items=items)

    def BuyItem(self, request, context):
        item = trial_items.get(request.item_id)
        if not item:
            return buyer_pb2.BuyItemResponse(\
                success=False, message="Item not found"
            )
        if item.quantity < request.quantity:
            return buyer_pb2.BuyItemResponse(\
                success=False, message="Not enough stock available"
            )
        item.quantity -= request.quantity
        return buyer_pb2.BuyItemResponse(\
            success=True, message="Item bought successfully"
        )

    def AddToWishList(self, request, context):
        return buyer_pb2.AddToWishListResponse(\
            success=True, message="Item added to wish list successfully"
        )

    def RateItem(self, request, context):
        return buyer_pb2.RateItemResponse(\
            success=True, message="Item rated successfully"
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    buyer_pb2_grpc.add_BuyerServicer_to_server(BuyerServicer(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()