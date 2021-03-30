import grpc
import hello_pb2
import hello_pb2_grpc

from concurrent import futures


class Hello(hello_pb2_grpc.BasicServiceServicer):

    def BasicFunction(self, request, context):
        if request.request != "world!":
            context.set_details("expected grpc!")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return hello_pb2.BasicResponse()

        return hello_pb2.BasicResponse(response="Hello " + request.request)


def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    hello_pb2_grpc.add_BasicServiceServicer_to_server(Hello(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    run_server()
