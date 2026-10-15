# Cliente del servicio Reseñas (equipo vecino) · Reto de integración
# Contrato del vecino: resenas.proto · Qué hace y con qué datos probar: servicios/resenas/README.md
# Antes de correrlo, el servidor del vecino debe estar corriendo (README.md, paso 5).
import grpc

import resenas_pb2
import resenas_pb2_grpc

canal = grpc.insecure_channel("localhost:50053")
stub = resenas_pb2_grpc.ResenasStub(canal)

print("=== Parte 1 · PromedioProducto con un dato válido ===")
# TODO: arma la petición con un dato que funcione (tabla "Datos para probar" del README del vecino),
#       llama a stub.PromedioProducto(...) e imprime los campos de la respuesta.

print("=== Parte 2 · PromedioProducto con un dato que provoca error ===")
# TODO: llama con un dato que provoque error, dentro de try/except grpc.RpcError,
#       e imprime e.code() y e.details(). El programa NO debe tronar.

print("=== Parte 3 · ListarResenas (streaming) ===")
# TODO: recorre stub.ListarResenas(...) con for e imprime cada caja en cuanto llegue.
#       Ponlo también dentro de try/except por si el servidor regresa un error.
