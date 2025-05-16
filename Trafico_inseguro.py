import os
from scapy.all import sniff, wrpcap, IP, TCP, get_if_list

# Puertos comunes de protocolos no encriptados
UNENCRYPTED_PORTS = {
    21: "FTP",
    23: "Telnet",
    25: "SMTP",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    8080: "HTTP_ALT"
}


def packet_callback(packet):
    """
    Procesa cada paquete capturado.
    Verifica si usa un protocolo no encriptado.
    """
    if packet.haslayer(TCP) and packet.haslayer(IP):
        if packet[TCP].dport in UNENCRYPTED_PORTS or packet[TCP].sport in UNENCRYPTED_PORTS:
            protocolo = UNENCRYPTED_PORTS.get(
                packet[TCP].dport, UNENCRYPTED_PORTS.get(packet[TCP].sport, "Desconocido"))
            print(f"{protocolo}: {packet[IP].src} -> {packet[IP].dst}")


def main():
    """
    Configura y ejecuta la captura de tráfico.
    """
    # Crear carpeta para guardar capturas
    carpeta_salida = "C:/Users/sopor/OneDrive/Escritorio/Capturas"
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
    archivo_salida = os.path.join(carpeta_salida, "captura_no_encriptada.pcap")

    # Mostrar interfaces disponibles
    print("Interfaces disponibles:")
    interfaces = get_if_list()
    for i, iface in enumerate(interfaces):
        print(f"{i}: {iface}")

    # Pedir al usuario que seleccione una interfaz
    try:
        opcion = int(input("Selecciona el número de la interfaz: "))
        interfaz = interfaces[opcion]
    except (ValueError, IndexError):
        print("Opción inválida.")
        return

    print(f"Capturando en la interfaz: {interfaz}")

    # Capturar paquetes
    try:
        print("Capturando paquetes con protocolos no encriptados...")
        paquetes = sniff(iface=interfaz, count=100000,
                         prn=packet_callback, filter="tcp")

        # Guardar captura
        print(f"Guardando los paquetes en: {archivo_salida}")
        wrpcap(archivo_salida, paquetes)
        print("Captura guardada.")
    except Exception as e:
        print(f"Error durante la captura: {e}")


if __name__ == "__main__":
    main()

### Para identificar la interfaz en Windows ejecuta el siguiente comando en PowerShell para listar las interfaces con su UUID:
### Get-NetAdapter | Select-Object Name, InterfaceDescription, InterfaceGuid
