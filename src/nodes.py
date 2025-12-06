# src/nodes.py
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from src.config import get_creative_model, get_strict_model
from src.state import AgentState
from src.tools import calculate_bmi_tool
from prompts.templates import (
    get_router_prompt, get_routine_prompt, 
    get_supplement_prompt, get_chat_prompt, get_extractor_prompt
)

# Inicializar modelos y cadenas una sola vez
llm_creative = get_creative_model()
llm_strict = get_strict_model()

router_chain = get_router_prompt() | llm_strict | StrOutputParser()
chat_chain = get_chat_prompt() | llm_creative | StrOutputParser()
extractor_chain = get_extractor_prompt() | llm_strict | JsonOutputParser()


# --- DEFINICIÓN DE NODOS ---

def router_node(state: AgentState):
    print("--- 1. ROUTER NODE ---")
    intent = router_chain.invoke({"input": state["input_text"]})
    clean_intent = intent.strip().lower()
    
    if "bmi" in clean_intent: final = "bmi"
    elif "rout" in clean_intent: final = "routine"
    else: final = "chat"
    
    return {"intent": final}



def routine_node(state: AgentState):
    print("--- 2A. ROUTINE GENERATOR (Sequential) ---")
    # Instanciar prompts aquí para usarlos en secuencia
    routine_p = get_routine_prompt()
    supplement_p = get_supplement_prompt()
    
    # Paso 1
    rutina = llm_creative.invoke(routine_p.format(input=state["input_text"]))
    # Paso 2
    consejo = llm_creative.invoke(supplement_p.format(routine=rutina))
    
    final_response = f"💪 TU PLAN DE GUERRA:\n{rutina}\n\n💊 CONSEJO PRO:\n{consejo}"
    return {"final_output": final_response}



def bmi_node(state: AgentState):
    print("--- 2B. BMI CALCULATOR (Tool) ---")
    try:
        data = extractor_chain.invoke({"input": state["input_text"]})
        if data and 'weight' in data and 'height' in data:
            result = calculate_bmi_tool(float(data['weight']), float(data['height']))
            response = f"📊 ANÁLISIS CORPORAL:\n{result}"
        else:
            response = "Para calcular tu BMI necesito peso (kg) y altura (m). Ej: '80kg 1.80m'."
    except Exception as e:
        response = f"No pude extraer los datos. Intenta con formato '80kg 1.80m'. Error: {e}"
        
    return {"final_output": response}



def chat_node(state: AgentState):
    print("--- 2C. MOTIVATIONAL CHAT ---")
    response = chat_chain.invoke({"input": state["input_text"]})
    return {"final_output": response}
