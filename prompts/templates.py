# prompts/templates.py
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate



# 1. Router Template
ROUTER_TEMPLATE_TEXT = """
Clasifica la intención del usuario en una de estas categorías:
- 'routine': Si pide una rutina de ejercicios, plan de entrenamiento o ejercicios para un músculo.
- 'bmi': Si menciona calcular su índice de masa corporal, o da su peso y altura explícitamente para evaluar salud.
- 'chat': Para saludos, motivación, preguntas generales de nutrición o dudas varias.

Usuario: {input}

Responde SOLO con la palabra clave (routine, bmi, o chat).
"""

def get_router_prompt():
    return ChatPromptTemplate.from_template(ROUTER_TEMPLATE_TEXT)




# 2. Routine Prompts
def get_routine_prompt():
    return ChatPromptTemplate.from_template(
        "Eres un entrenador experto. Crea una rutina breve pero intensa para: {input}. "
        "Incluye series y repeticiones. Sé directo."
    )

def get_supplement_prompt():
    return ChatPromptTemplate.from_template(
        "Basado en esta rutina: '{routine}', recomienda 1 suplemento o alimento post-entreno clave. Sé breve."
    )




# 3. Chat Motivacional (Few-Shot)
def get_chat_prompt():
    examples = [
        {"input": "No tengo ganas de ir hoy...", "output": "¡Esa es la voz de la debilidad! Levántate, solo necesitas llegar. ¡Una vez ahí, ganarás la batalla!"},
        {"input": "Es muy difícil.", "output": "¡Si fuera fácil, todo el mundo lo haría! El dolor es temporal, la gloria es para siempre. ¡Sigue!"}
    ]
    example_prompt = ChatPromptTemplate.from_messages([("human", "{input}"), ("ai", "{output}")])
    few_shot_prompt = FewShotChatMessagePromptTemplate(example_prompt=example_prompt, examples=examples)

    return ChatPromptTemplate.from_messages([
        ("system", "Eres 'IronCoach', un entrenador rudo pero motivador. Responde con energía."),
        few_shot_prompt,
        ("human", "{input}")
    ])




# 4. Extractor Prompt
def get_extractor_prompt():
    return ChatPromptTemplate.from_template(
        "Extrae el peso (kg) y altura (metros) del siguiente texto. "
        "Devuelve un JSON con claves 'weight' y 'height'. Si no encuentras, devuelve null. Texto: {input}"
    )
