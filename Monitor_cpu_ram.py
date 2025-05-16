import psutil
import time
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_uso_cpu_ram():
    try:
        while True:
            limpiar_pantalla()
            uso_cpu = psutil.cpu_percent(interval=1)
            uso_ram = psutil.virtual_memory().percent
            
            print("=== MONITOREO DEL SERVIDOR ===")
            print(f"Uso de CPU: {uso_cpu}%")
            print(f"Uso de RAM: {uso_ram}%")
            
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoreo finalizado.")

mostrar_uso_cpu_ram()
