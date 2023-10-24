import grpc
import text_storage_pb2
import text_storage_pb2_grpc
from concurrent import futures
import time

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class TextStorageService(text_storage_pb2_grpc.TextStorageServiceServicer):
    text_data = {}

    def StoreText(self, request, context):
        self.text_data[request.text] = int(time.time())
        return text_storage_pb2.Empty()

    def GetTimestamp(self, request, context):
        timestamp = self.text_data.get(request.text, -1)
        return text_storage_pb2.TimestampResponse(timestamp=timestamp)

    def QueryText(self, request, context):
        timestamp = self.text_data.get(request.text, -1)
        return text_storage_pb2.TimestampResponse(timestamp=timestamp)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    text_storage_pb2_grpc.add_TextStorageServiceServicer_to_server(TextStorageService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
