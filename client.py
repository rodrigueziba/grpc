import grpc
import text_storage_pb2
import text_storage_pb2_grpc
from text_storage_pb2 import Empty
from datetime import datetime


def run_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = text_storage_pb2_grpc.TextStorageServiceStub(channel)

    while True:
        print("1. Almacenar texto")
        print("2. Consultar texto")
        print("3. Salir")
        choice = input("Elija una opción: ")

        if choice == '1':
            text_to_store = input("Ingrese el texto a almacenar: ")
            request = text_storage_pb2.TextRequest(text=text_to_store)
            stub.StoreText(request)
            print("Texto almacenado con éxito.")
        elif choice == '2':
            text_to_query = input("Ingrese el texto a consultar: ")
            request = text_storage_pb2.TextRequest(text=text_to_query)
            response = stub.QueryText(request)

            if response.timestamp != -1:
                timestamp = datetime.utcfromtimestamp(response.timestamp).strftime('%Y-%m-%d %H:%M:%S UTC')
                print(f"El texto fue aceptado en: {timestamp}")
            else:
                print("Texto no encontrado.")
        elif choice == '3':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    run_client()
