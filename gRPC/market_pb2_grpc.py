# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import market_pb2 as market__pb2


class marketStub(object):
    """seller operations
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/market/SayHello',
                request_serializer=market__pb2.HelloRequest.SerializeToString,
                response_deserializer=market__pb2.HelloReply.FromString,
                )
        self.RegisterSeller = channel.unary_unary(
                '/market/RegisterSeller',
                request_serializer=market__pb2.RegisterSellerRequest.SerializeToString,
                response_deserializer=market__pb2.RegisterSellerResponse.FromString,
                )
        self.SellItem = channel.unary_unary(
                '/market/SellItem',
                request_serializer=market__pb2.SellItemRequest.SerializeToString,
                response_deserializer=market__pb2.SellItemResponse.FromString,
                )
        self.UpdateItem = channel.unary_unary(
                '/market/UpdateItem',
                request_serializer=market__pb2.UpdateItemRequest.SerializeToString,
                response_deserializer=market__pb2.UpdateItemResponse.FromString,
                )
        self.DeleteItem = channel.unary_unary(
                '/market/DeleteItem',
                request_serializer=market__pb2.DeleteItemRequest.SerializeToString,
                response_deserializer=market__pb2.DeleteItemResponse.FromString,
                )
        self.DisplaySellerItems = channel.unary_unary(
                '/market/DisplaySellerItems',
                request_serializer=market__pb2.DisplaySellerItemsRequest.SerializeToString,
                response_deserializer=market__pb2.DisplaySellerItemsResponse.FromString,
                )
        self.SearchItem = channel.unary_unary(
                '/market/SearchItem',
                request_serializer=market__pb2.SearchItemRequest.SerializeToString,
                response_deserializer=market__pb2.SearchItemResponse.FromString,
                )
        self.BuyItem = channel.unary_unary(
                '/market/BuyItem',
                request_serializer=market__pb2.BuyItemRequest.SerializeToString,
                response_deserializer=market__pb2.BuyItemResponse.FromString,
                )
        self.AddToWishList = channel.unary_unary(
                '/market/AddToWishList',
                request_serializer=market__pb2.AddToWishListRequest.SerializeToString,
                response_deserializer=market__pb2.AddToWishListResponse.FromString,
                )
        self.RateItem = channel.unary_unary(
                '/market/RateItem',
                request_serializer=market__pb2.RateItemRequest.SerializeToString,
                response_deserializer=market__pb2.RateItemResponse.FromString,
                )


class marketServicer(object):
    """seller operations
    """

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

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

    def SearchItem(self, request, context):
        """buyer operations
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BuyItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddToWishList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RateItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_marketServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=market__pb2.HelloRequest.FromString,
                    response_serializer=market__pb2.HelloReply.SerializeToString,
            ),
            'RegisterSeller': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterSeller,
                    request_deserializer=market__pb2.RegisterSellerRequest.FromString,
                    response_serializer=market__pb2.RegisterSellerResponse.SerializeToString,
            ),
            'SellItem': grpc.unary_unary_rpc_method_handler(
                    servicer.SellItem,
                    request_deserializer=market__pb2.SellItemRequest.FromString,
                    response_serializer=market__pb2.SellItemResponse.SerializeToString,
            ),
            'UpdateItem': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateItem,
                    request_deserializer=market__pb2.UpdateItemRequest.FromString,
                    response_serializer=market__pb2.UpdateItemResponse.SerializeToString,
            ),
            'DeleteItem': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteItem,
                    request_deserializer=market__pb2.DeleteItemRequest.FromString,
                    response_serializer=market__pb2.DeleteItemResponse.SerializeToString,
            ),
            'DisplaySellerItems': grpc.unary_unary_rpc_method_handler(
                    servicer.DisplaySellerItems,
                    request_deserializer=market__pb2.DisplaySellerItemsRequest.FromString,
                    response_serializer=market__pb2.DisplaySellerItemsResponse.SerializeToString,
            ),
            'SearchItem': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchItem,
                    request_deserializer=market__pb2.SearchItemRequest.FromString,
                    response_serializer=market__pb2.SearchItemResponse.SerializeToString,
            ),
            'BuyItem': grpc.unary_unary_rpc_method_handler(
                    servicer.BuyItem,
                    request_deserializer=market__pb2.BuyItemRequest.FromString,
                    response_serializer=market__pb2.BuyItemResponse.SerializeToString,
            ),
            'AddToWishList': grpc.unary_unary_rpc_method_handler(
                    servicer.AddToWishList,
                    request_deserializer=market__pb2.AddToWishListRequest.FromString,
                    response_serializer=market__pb2.AddToWishListResponse.SerializeToString,
            ),
            'RateItem': grpc.unary_unary_rpc_method_handler(
                    servicer.RateItem,
                    request_deserializer=market__pb2.RateItemRequest.FromString,
                    response_serializer=market__pb2.RateItemResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'market', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class market(object):
    """seller operations
    """

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/market/SayHello',
            market__pb2.HelloRequest.SerializeToString,
            market__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/market/RegisterSeller',
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
        return grpc.experimental.unary_unary(request, target, '/market/SellItem',
            market__pb2.SellItemRequest.SerializeToString,
            market__pb2.SellItemResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/market/UpdateItem',
            market__pb2.UpdateItemRequest.SerializeToString,
            market__pb2.UpdateItemResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/market/DeleteItem',
            market__pb2.DeleteItemRequest.SerializeToString,
            market__pb2.DeleteItemResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/market/DisplaySellerItems',
            market__pb2.DisplaySellerItemsRequest.SerializeToString,
            market__pb2.DisplaySellerItemsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/market/SearchItem',
            market__pb2.SearchItemRequest.SerializeToString,
            market__pb2.SearchItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BuyItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/market/BuyItem',
            market__pb2.BuyItemRequest.SerializeToString,
            market__pb2.BuyItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddToWishList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/market/AddToWishList',
            market__pb2.AddToWishListRequest.SerializeToString,
            market__pb2.AddToWishListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RateItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/market/RateItem',
            market__pb2.RateItemRequest.SerializeToString,
            market__pb2.RateItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)