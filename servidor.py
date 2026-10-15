import time
import grpc
from concurrent import futures

import inventario_pb2
import inventario_pb2_grpc

EXISTENCIAS = {
    "P001": (5, "Colima"),
    "P002": (40, "Colima"),
    "P003": (12, "Manzanillo"),
    "P004": (0, "Colima"),
    "P005": (7, "Tecoman"),
    "P006": (3, "Colima"),
}


class InventarioServicio(inventario_pb2_grpc.InventarioServicer):

    def ConsultarExistencia(self, request, context):
        if request.clave not in EXISTENCIAS:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                f"No existe el producto {request.clave}"
            )

        cantidad, almacen = EXISTENCIAS[request.clave]

        return inventario_pb2.Existencia(
            clave=request.clave,
            cantidad=cantidad,
            almacen=almacen
        )

    def VigilarExistencia(self, request, context):
        if request.clave not in EXISTENCIAS:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                f"No existe el producto {request.clave}"
            )

        cantidad, almacen = EXISTENCIAS[request.clave]

        for _ in range(4):
            if not context.is_active():
                return

            yield inventario_pb2.Existencia(
                clave=request.clave,
                cantidad=cantidad,
                almacen=almacen
            )

            cantidad = max(0, cantidad - 1)
            time.sleep(1)


servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
inventario_pb2_grpc.add_InventarioServicer_to_server(
    InventarioServicio(), servidor
)
servidor.add_insecure_port("[::]:50052")
servidor.start()
print("Servidor de Inventario escuchando en el puerto 50052...")
servidor.wait_for_termination()