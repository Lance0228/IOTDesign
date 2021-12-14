# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import fib_pb2 as fib__pb2


class FibCalculatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Compute = channel.unary_unary(
                '/FibCalculator/Compute',
                request_serializer=fib__pb2.FibRequest.SerializeToString,
                response_deserializer=fib__pb2.FibResponse.FromString,
                )


class FibCalculatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Compute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FibCalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Compute': grpc.unary_unary_rpc_method_handler(
                    servicer.Compute,
                    request_deserializer=fib__pb2.FibRequest.FromString,
                    response_serializer=fib__pb2.FibResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FibCalculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FibCalculator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Compute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FibCalculator/Compute',
            fib__pb2.FibRequest.SerializeToString,
            fib__pb2.FibResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
