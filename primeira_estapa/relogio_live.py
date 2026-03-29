import time
from datetime import datetime

def relogio_live():
    """Display a live clock that updates every second."""
    try:
        while True:
            # Get current time
            agora = datetime.now()
            hora_formatada = agora.strftime("%H:%M:%S")
            data_formatada = agora.strftime("%d/%m/%Y")
            
            # Clear and display
            print(f"\r{data_formatada} - {hora_formatada}", end="", flush=True)
            
            # Wait 1 second
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nReógio finalizado.")

if __name__ == "__main__":
    print("=== RELÓGIO AO VIVO ===\n")
    relogio_live()
