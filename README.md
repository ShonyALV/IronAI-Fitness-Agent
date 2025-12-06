# 🤖 Fitness Gym Coach AI

Proyecto individual para la materia **Agentes Inteligentes** en Yachay Tech.
Este agente inteligente está diseñado con **LangChain** y **LangGraph**, utilizando el modelo **Mistral 7B en Ollama**, para actuar como un **entrenador personal virtual** especializado en rutinas de gimnasio.

---

## 📌 Objetivo
El agente ayuda a los usuarios a:
- Definir objetivos de entrenamiento (fuerza, resistencia, hipertrofia).
- Generar planes semanales personalizados en formato JSON.
- Recordar progresos previos mediante memoria conversacional y vectorial.
- Calcular calorías quemadas según tipo de ejercicio y duración.
- Proporcionar recomendaciones claras y motivadoras.

---

## 🏗️ Arquitectura del Agente
El agente se construye con:
- **LangChain** → Prompt engineering, RouterChain, SequentialChain, memoria.
- **LangGraph** → Flujo de nodos con enrutamiento y herramientas.
- **Ollama (Mistral 7B)** → Modelo LLM ligero y eficiente.
- **Memoria** → ConversationalBufferMemory + VectorStoreRetrieverMemory.
- **Herramientas** → Calculadora de calorías.

### Flujo del agente
Usuario → RouterChain → (Strength | Endurance | Hypertrophy)
→ MemoryNode → ToolNode → OutputNode

---

## 📂 Organización del repositorio
fitness-gym-coach-ai/
│
├── src/
│   ├── main.py               # Punto de entrada del agente
│   ├── chains/
│   │   └── router_chain.py   # Lógica de enrutamiento
│   ├── graph/
│   │   └── workflow.py       # Definición del grafo LangGraph
│   ├── prompts/
│   │   └── templates.py      # Prompt templates
│   ├── tools/
│   │   └── calculator.py     # Herramienta de cálculo de calorías
│   └── memory/
│       └── setup.py          # Configuración de memoria
│
├── notebooks/                # Experimentos en Jupyter
├── prompts/                  # Archivos de texto con ejemplos
├── logs/                     # Registro de interacciones
├── report/                   # Informe académico (PDF)
├── README.md                 # Este archivo
├── requirements.txt          # Dependencias
└── environment.yml           # Configuración alternativa para Conda

---

## ⚙️ Instalación

### 1. Clonar repositorio
```bash
git clone https://github.com/<tu-usuario>/fitness-gym-coach-ai.git
cd fitness-gym-coach-ai

### 2. Instalar dependencias

```bash
pip install -r requirements.txt

```

### 3. Instalar Ollama y modelo Mistral

Descargar Ollama desde [ollama.ai](https://ollama.ai/).

Luego instalar el modelo Mistral 7B:

```bash
ollama pull mistral

```

---

## ▶️ Ejecución

Ejecutar el agente desde consola:

```bash
python src/main.py

```

Ejemplo de interacción:

```
🤖 Fitness Gym Coach AI iniciado...
👉 Ingresa tu objetivo de entrenamiento: Quiero ganar músculo en 3 meses

=== Plan generado ===
{
  "Lunes": "Sentadillas 5x5",
  "Martes": "Press banca 5x5",
  ...
}

```

---

## 📊 Evaluación

El proyecto incluye:

- Logging de prompts y outputs en `logs/`.
- Evaluación de calidad (claridad, utilidad, exactitud).
- Análisis de errores y mejoras.

---

## 📚 Créditos

- Autor: **Jhony Peñaherrera**
- Universidad: **Yachay Tech**
- Materia: **Agentes Inteligentes (2025)**
