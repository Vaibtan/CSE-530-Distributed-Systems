# market.py

import grpc
from concurrent import futures
import market_pb2
import market_pb2_grpc
from threading import Thread, Lock

class MarketServer(market_pb2_grpc.MarketServiceServicer):
    def __init__(self, market_address, max_sellers = 10):
        self.address = market_address
        self.max_sellers = max_sellers
        self.sellers = {}
        self.lock = Lock()


    def RegisterSeller(self, request, context):
        self.lock.acquire()
        seller_address = request.address
        seller_uuid = request.uuid
        print(f"JOIN REQUEST FROM {seller_uuid}-{seller_address}")
        
        if seller_uuid in self.sellers:
            print(f"Seller {seller_address} is already registered.")
            self.lock.release()
            return market_pb2.RegisterSellerResponse(status = "FAILED")
        
        if(len(self.sellers) < self.max_sellers):
            try:
                self.sellers[seller_uuid] = seller_address
                print(f"Seller {seller_address} registered successfully.")
                self.lock.release()
                return market_pb2.RegisterServerResponse(status = "SUCCESS")
            except:
                print(f"Failed to register seller")
                self.lock.release()
                return market_pb2.RegisterServerResponse(status = "FAIL")
        else:
            print(f"Failed to register seller,max seller count reached")
            self.lock.release()
            return market_pb2.RegisterServerResponse(status = "FAIL")
                    

    def NotifyClient(self, request, context):
        message = request.notification_message
        client_address = context.peer()

        if client_address in self.sellers:
            print(f"Notifying client {client_address}: {message}")
            return market_pb2.NotifyClientResponse(status = "SUCCESS")

        elif "ITEM UPDATED" in message:
            item_id = extract_item_id(message)
            interested_buyers = self.get_interested_buyers(item_id)
            for buyer_address in interested_buyers:
                self.send_notification_to_buyer(buyer_address, message)      
            return market_pb2.NotifyClientResponse(status="SUCCESS")
        else:
            print(f"Client {client_address} not found.")
            return market_pb2.NotifyClientResponse(status = "FAILURE")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    market_pb2_grpc.add_MarketServiceServicer_to_server(MarketServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("------------------------------------------------")
    print(f"----------STARTING MARKET SERVER---------------")
    print("------------------------------------------------")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
