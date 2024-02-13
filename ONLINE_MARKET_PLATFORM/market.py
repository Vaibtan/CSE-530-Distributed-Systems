# market.py

import grpc
from concurrent import futures
import market_pb2
import market_pb2_grpc

class MarketServer(market_pb2_grpc.MarketServicer):
    def __init__(self):
        self.clients = {}

    def NotifyClient(self, request, context):
        client_address = request.client_address
        message = request.message

        if client_address in self.clients:
            # Send notification to client
            print(f"Notifying client {client_address}: {message}")
            return market_pb2.NotifyClientResponse(success=True)
        else:
            print(f"Client {client_address} not found.")
            return market_pb2.NotifyClientResponse(success=False)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    market_pb2_grpc.add_MarketServicer_to_server(MarketServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Market server started. Listening on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
