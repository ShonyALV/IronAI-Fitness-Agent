# src/config.py
from langchain_ollama import OllamaLLM

def get_creative_model():
    # Modelo Creativo (Para rutinas y motivación)
    return OllamaLLM(model="gemma3:1b", temperature=0.7)

def get_strict_model():
    # Modelo Estricto (Para extracción de datos y clasificación)
    return OllamaLLM(model="gemma3:1b", temperature=0.1)
