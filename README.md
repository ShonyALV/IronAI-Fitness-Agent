# 🤖 Fitness Gym Coach AI

Individual project for the **Intelligent Agents** course at Yachay Tech University.  
This intelligent agent is built with **LangChain** and **LangGraph**, using the **Mistral 7B model in Ollama**, to act as a **virtual personal trainer** specialized in gym routines.

---

## 📌 Objective
The agent helps users to:
- Define training goals (strength, endurance, hypertrophy).
- Generate personalized weekly plans in JSON format.
- Recall previous progress through conversational and vector memory.
- Calculate calories burned based on exercise type and duration.
- Provide clear and motivational recommendations.

---

## 🏗️ Agent Architecture
The agent is built with:
- **LangChain** → Prompt engineering, RouterChain, SequentialChain, memory.
- **LangGraph** → Node flow with routing and tools.
- **Ollama (Mistral 7B)** → Lightweight and efficient LLM model.
- **Memory** → ConversationalBufferMemory + VectorStoreRetrieverMemory.
- **Tools** → Calorie calculator.

### Agent Flow
User → RouterChain → (Strength | Endurance | Hypertrophy)
→ MemoryNode → ToolNode → OutputNode

---

## 📂 Repository Structure

```bash
fitness-gym-coach-ai/                                                     \
│                                                                         \
├── src/                                                                  \
│   ├── main.py               # Agent entry point                         \
│   ├── chains/                                                           \
│   │   └── router_chain.py   # Routing logic                             \
│   ├── graph/                                                            \
│   │   └── workflow.py       # LangGraph workflow definition             \
│   ├── prompts/                                                          \
│   │   └── templates.py      # Prompt templates                          \
│   ├── tools/                                                            \
│   │   └── calculator.py     # Calorie calculation tool                  \
│   └── memory/                                                           \
│       └── setup.py          # Memory setup                              \
│                                                                         \
├── notebooks/                # Jupyter experiments                       \
├── prompts/                  # Text files with examples                  \
├── logs/                     # Interaction logs                          \
├── report/                   # Academic report (PDF)                     \
├── README.md                 # This file                                 \
├── requirements.txt          # Dependencies                              \
└── environment.yml           # Alternative Conda configuration           \
```

---

## ⚙️ Installation

### 1. Clone repository
```bash
git clone https://github.com/<your-username>/fitness-gym-coach-ai.git
cd fitness-gym-coach-ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Ollama and Mistral model

Download Ollama from [ollama.ai](https://ollama.ai/).

Then install the Mistral 7B model:

```bash
ollama pull mistral
```

---

## ▶️ Execution

Run the agent from console:

```bash
python src/main.py
```

Example interaction:

```
🤖 Fitness Gym Coach AI started...
👉 Enter your training goal: I want to gain muscle in 3 months

=== Generated Plan ===
{
  "Monday": "Squats 5x5",
  "Tuesday": "Bench press 5x5",
  ...
}
```

---

## 📊 Evaluation

The project includes:

- Prompt and output logging in `logs/`.
- Quality evaluation (clarity, usefulness, accuracy).
- Error analysis and improvements.

---

## 📚 Credits

- Author: **Jhony Peñaherrera**
- University: **Yachay Tech**
- Course: **Intelligent Agents (2025)**