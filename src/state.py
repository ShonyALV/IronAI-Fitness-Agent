# src/state.py
from typing import TypedDict, List
from typing_extensions import TypedDict

class AgentState(TypedDict):
    input_text: str          # Lo que escribe el usuario
    intent: str              # 'routine', 'bmi', 'chat'
    user_data: dict          # Datos extraídos (peso, altura, nivel)
    history: List[str]       # Memoria de conversación
    final_output: str        # Respuesta final
