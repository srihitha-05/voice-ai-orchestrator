from typing import TypedDict
from langgraph.graph import StateGraph, END

from langgraph_flow.evaluator import evaluate_lead


class GraphState(TypedDict):
    transcript: str
    status: str


def evaluation_node(state: GraphState):

    status = evaluate_lead(state["transcript"])

    return {
        "transcript": state["transcript"],
        "status": status
    }


builder = StateGraph(GraphState)

builder.add_node("evaluation", evaluation_node)

builder.set_entry_point("evaluation")

builder.add_edge("evaluation", END)

graph = builder.compile()