# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import market_pb2 as market__pb2
import seller_pb2 as seller__pb2


class SellerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterSeller = channel.unary_unary(
                '/SellerService/RegisterSeller',
                request_serializer=market__pb2.RegisterSellerRequest.SerializeToString,
                response_deserializer=market__pb2.RegisterSellerResponse.FromString,
                )
        self.SellItem = channel.unary_unary(
                '/SellerService/SellItem',
                request_serializer=seller__pb2.SellItemRequest.SerializeToString,
                response_deserializer=seller__pb2.SellItemResponse.FromString,
                )
        self.UpdateItem = channel.unary_unary(
                '/SellerService/UpdateItem',
                request_serializer=seller__pb2.UpdateItemRequest.SerializeToString,
                response_deserializer=seller__pb2.UpdateItemResponse.FromString,
                )
        self.DeleteItem = channel.unary_unary(
                '/SellerService/DeleteItem',
                request_serializer=seller__pb2.DeleteItemRequest.SerializeToString,
                response_deserializer=seller__pb2.DeleteItemResponse.FromString,
                )
        self.DisplaySellerItems = channel.unary_unary(
                '/SellerService/DisplaySellerItems',
                request_serializer=seller__pb2.DisplaySellerItemsRequest.SerializeToString,
                response_deserializer=seller__pb2.DisplaySellerItemsResponse.FromString,
                )


class SellerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterSeller(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SellItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisplaySellerItems(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SellerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterSeller': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterSeller,
                    request_deserializer=market__pb2.RegisterSellerRequest.FromString,
                    response_serializer=market__pb2.RegisterSellerResponse.SerializeToString,
            ),
            'SellItem': grpc.unary_unary_rpc_method_handler(
                    servicer.SellItem,
                    request_deserializer=seller__pb2.SellItemRequest.FromString,
                    response_serializer=seller__pb2.SellItemResponse.SerializeToString,
            ),
            'UpdateItem': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateItem,
                    request_deserializer=seller__pb2.UpdateItemRequest.FromString,
                    response_serializer=seller__pb2.UpdateItemResponse.SerializeToString,
            ),
            'DeleteItem': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteItem,
                    request_deserializer=seller__pb2.DeleteItemRequest.FromString,
                    response_serializer=seller__pb2.DeleteItemResponse.SerializeToString,
            ),
            'DisplaySellerItems': grpc.unary_unary_rpc_method_handler(
                    servicer.DisplaySellerItems,
                    request_deserializer=seller__pb2.DisplaySellerItemsRequest.FromString,
                    response_serializer=seller__pb2.DisplaySellerItemsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SellerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SellerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterSeller(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SellerService/RegisterSeller',
            market__pb2.RegisterSellerRequest.SerializeToString,
            market__pb2.RegisterSellerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SellItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SellerService/SellItem',
            seller__pb2.SellItemRequest.SerializeToString,
            seller__pb2.SellItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SellerService/UpdateItem',
            seller__pb2.UpdateItemRequest.SerializeToString,
            seller__pb2.UpdateItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SellerService/DeleteItem',
            seller__pb2.DeleteItemRequest.SerializeToString,
            seller__pb2.DeleteItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisplaySellerItems(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SellerService/DisplaySellerItems',
            seller__pb2.DisplaySellerItemsRequest.SerializeToString,
            seller__pb2.DisplaySellerItemsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
