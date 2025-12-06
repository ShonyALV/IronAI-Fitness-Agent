# main.py
import sys
import os
import logging
from src.graph import create_workflow

# Configuración de Logging (Requisito E)
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/agent.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def main():
    print("🏋️ INICIANDO IRON-AI FITNESS COACH 🏋️\n")
    app = create_workflow()
    
    # Loop de interacción
    while True:
        try:
            user_input = input("\nUsuario (o 'salir'): ")
            if user_input.lower() in ['salir', 'exit', 'quit']:
                break
            
            logger.info(f"INPUT USUARIO: {user_input}")
            
            initial_state = {
                "input_text": user_input, 
                "history": [],
                "user_data": {}
            }
            
            result = app.invoke(initial_state)
            output = result.get("final_output", "No hubo respuesta.")
            
            print(f"\n🤖 IronAI: {output}")
            logger.info(f"OUTPUT AGENTE: {output}")
            
        except Exception as e:
            logger.error(f"Error en ejecución: {e}")
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
