from typing import Any

from langgraph.graph import StateGraph, START, END

from .state import NewsPodcastState
from .grab_emails_node import grab_emails


def build_graph() -> Any:
    builder = StateGraph(NewsPodcastState)

    builder.add_node("grab_emails", grab_emails)

    builder.add_edge(START, "grab_emails")
    builder.add_edge("grab_emails", END)

    return builder.compile()