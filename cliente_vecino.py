# Cliente del servicio Reseñas (equipo vecino) · Reto de integración
# Contrato del vecino: resenas.proto · Qué hace y con qué datos probar: servicios/resenas/README.md
# Antes de correrlo, el servidor del vecino debe estar corriendo (README.md, paso 5).
import grpc

import resenas_pb2
import resenas_pb2_grpc

canal = grpc.insecure_channel("localhost:50053")
stub = resenas_pb2_grpc.ResenasStub(canal)

print("=== Parte 1 · PromedioProducto con un dato válido ===")
peticion_valida = resenas_pb2.ResenaRequest(clave="P001")
respuesta_valida = stub.PromedioProducto(peticion_valida)
print(f"Producto: {respuesta_valida.clave} | Promedio: {respuesta_valida.promedio} | Total reseñas: {respuesta_valida.total}")

print("\n=== Parte 2 · PromedioProducto con un dato que provoca error ===")
peticion_invalida = resenas_pb2.ResenaRequest(clave="P999")
try:
    stub.PromedioProducto(peticion_invalida)
except grpc.RpcError as e:
    print(f"Error esperado - Código: {e.code().name}")
    print(f"Detalles: {e.details()}")

print("\n=== Parte 3 · ListarResenas (streaming) ===")
try:
    for resena in stub.ListarResenas(peticion_valida):
        print(f"[{resena.estrellas} estrellas] {resena.autor}: {resena.comentario}")
except grpc.RpcError as e:
    print(f"Error en streaming - Código: {e.code().name}")
    print(f"Detalles: {e.details()}")