from typing import TypedDict, List
from langgraph.graph import StateGraph, END


class AgentState(TypedDict):
    user_input: str
    ai_response: str
    risk_level: str  # low, high (requires HITL)
    status: str      # processed, blocked, pending_approval
    logs: List[str]


class MedAssistWorkflow:
    def __init__(self):
        self.workflow = StateGraph(AgentState)
        self._build_graph()

    def classify_risk(self, state: AgentState):
        """Classifica se o caso é uma emergência (HITL)."""
        emergency_keywords = ["dor no peito", "falta de ar",
                              "desmai", "sangramento", "emergência"]
        user_input = state['user_input'].lower()

        if any(word in user_input for word in emergency_keywords):
            state['risk_level'] = "high"
            state['status'] = "pending_approval"
        else:
            state['risk_level'] = "low"
            state['status'] = "processed"

        return state

    def _build_graph(self):
        # Nós
        self.workflow.add_node("classify", self.classify_risk)

        # Fluxo
        self.workflow.set_entry_point("classify")
        self.workflow.add_edge("classify", END)

        self.app = self.workflow.compile()

    def run(self, user_input: str):
        initial_state = {
            "user_input": user_input,
            "ai_response": "",
            "risk_level": "low",
            "status": "initial",
            "logs": []
        }
        return self.app.invoke(initial_state)
