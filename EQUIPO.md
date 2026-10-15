Nuestro equipo
- Nuestro servicio: Inventario · puerto 50052 · contrato inventario.proto
- Servicio que consumimos (vecino): Reseñas · puerto 50053 · contrato resenas.proto
- Repositorio del equipo vecino: https://github.com/ariscervantes/reto-grpc-equipo-7
Integrante	Matrícula	Rol
Ricardo Anguiano Hernández (RAH-013)	20205261	Servidor
Flores Gomez Jonathan Alejandro (jjonathan27)	20207397	Cliente
Omar Díaz Ventura (Omar050928)	20206742	Integración (README, issues y prueba cruzada)


Prueba cruzada
Se ejecutó python cliente_vecino.py contra el servidor real del equipo vecino, clonado en ../vecino y escuchando en el puerto 50053. Esta fue la salida obtenida:
=== Parte 1 · PromedioProducto con un dato válido ===
Producto: P001 | Promedio: 4.5 | Total reseñas: 2

=== Parte 2 · PromedioProducto con un dato que provoca error ===
Error esperado - Código: NOT_FOUND
Detalles: El producto P999 no tiene reseñas

=== Parte 3 · ListarResenas (streaming) ===
[5 estrellas] ana: Rapida y ligera
[4 estrellas] luis: Buena bateria
Issues
Enlaces a los issues que abrieron en el repositorio del vecino o que les abrieron a ustedes (si hubo):
- No se registraron issues en los repositorios revisados.
Uso de IA (Acuerdo No. 23/2024 UdeC)
¿Usaron IA? ¿Cuál, quién y para qué?
- Ricardo Anguiano Hernández: utilizó ChatGPT como apoyo en el desarrollo y revisión de servidor.py, especialmente para comprender las llamadas gRPC y el manejo de errores con context.abort.
- Flores Gomez Jonathan Alejandro: utilizó ChatGPT como apoyo para implementar y revisar cliente_vecino.py, incluyendo las consultas, la captura de errores con try/except y el recorrido de respuestas por streaming.
- Omar Díaz Ventura: utilizó ChatGPT para solucionar problemas de configuración de Python y gRPC en Codespaces, preparar la integración, ejecutar las pruebas cruzadas y completar esta documentación.