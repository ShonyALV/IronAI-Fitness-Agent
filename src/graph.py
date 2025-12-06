# src/graph.py
from langgraph.graph import StateGraph, START, END
from src.state import AgentState
from src.nodes import router_node, routine_node, bmi_node, chat_node

def create_workflow():
    workflow = StateGraph(AgentState)

    # Agregar nodos
    workflow.add_node("router", router_node)
    workflow.add_node("routine_agent", routine_node)
    workflow.add_node("bmi_agent", bmi_node)
    workflow.add_node("chat_agent", chat_node)

    # Definir flujo
    workflow.add_edge(START, "router")

    def decide_next_step(state):
        return state["intent"] + "_agent"

    workflow.add_conditional_edges(
        "router",
        decide_next_step,
        {
            "routine_agent": "routine_agent",
            "bmi_agent": "bmi_agent",
            "chat_agent": "chat_agent"
        }
    )

    workflow.add_edge("routine_agent", END)
    workflow.add_edge("bmi_agent", END)
    workflow.add_edge("chat_agent", END)

    return workflow.compile()
