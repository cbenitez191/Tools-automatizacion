import pyfiglet
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT ANALYSIS")
print(ascii_banner)

try:
    objetivo = input("Ingrese la dirección IP o el nombre de host: ")
    objetivo = socket.gethostbyname(objetivo)
except socket.gaierror:
    print("Error: Dirección IP o nombre de host no válido.")
    exit()

print("_" * 50)
print("Escaneando Objetivo: " + objetivo)
print("Escaneo iniciado a las: " + str(datetime.now()))
print("_" * 50)

try:
    for puerto in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  
        resultado = s.connect_ex((objetivo, puerto))
        if resultado == 0:
            print(f"El puerto {puerto} está abierto")
        s.close()
except KeyboardInterrupt:
    print("\n¡Saliendo del programa!")
    exit()
except socket.error:
    print("\n¡El servidor no responde!")
    exit()

print("_" * 50)
print("Escaneo completado.")
