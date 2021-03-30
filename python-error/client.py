import grpc
import hello_pb2
import hello_pb2_grpc


def run_client():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_pb2_grpc.BasicServiceStub(channel)
        try:
            response = stub.BasicFunction(hello_pb2.BasicRequest(request="grpc!"))
        except grpc.RpcError as e:
            print(e.code())
            print(e.details())


if __name__ == '__main__':
    run_client()
