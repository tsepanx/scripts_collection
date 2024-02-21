# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import schema_pb2 as schema__pb2


class DatabaseStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PutUser = channel.unary_unary(
                '/Database/PutUser',
                request_serializer=schema__pb2.User.SerializeToString,
                response_deserializer=schema__pb2.BooleanResponse.FromString,
                )
        self.DeleteUser = channel.unary_unary(
                '/Database/DeleteUser',
                request_serializer=schema__pb2.User.SerializeToString,
                response_deserializer=schema__pb2.BooleanResponse.FromString,
                )
        self.GetUsers = channel.unary_unary(
                '/Database/GetUsers',
                request_serializer=schema__pb2.EmptyMessage.SerializeToString,
                response_deserializer=schema__pb2.UserList.FromString,
                )


class DatabaseServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PutUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DatabaseServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PutUser': grpc.unary_unary_rpc_method_handler(
                    servicer.PutUser,
                    request_deserializer=schema__pb2.User.FromString,
                    response_serializer=schema__pb2.BooleanResponse.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=schema__pb2.User.FromString,
                    response_serializer=schema__pb2.BooleanResponse.SerializeToString,
            ),
            'GetUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsers,
                    request_deserializer=schema__pb2.EmptyMessage.FromString,
                    response_serializer=schema__pb2.UserList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Database', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Database(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PutUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Database/PutUser',
            schema__pb2.User.SerializeToString,
            schema__pb2.BooleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Database/DeleteUser',
            schema__pb2.User.SerializeToString,
            schema__pb2.BooleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Database/GetUsers',
            schema__pb2.EmptyMessage.SerializeToString,
            schema__pb2.UserList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)