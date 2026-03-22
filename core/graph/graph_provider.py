from langgraph.constants import START, END
from langgraph.graph import StateGraph

from core.graph import NewsPodcastState, grab_emails
from core.graph.clean_emails_node import clean_emails
from core.graph.convert_text_to_mp3_node import convert_text_to_mp3
from core.graph.nodes import GraphNode


def provide_graph():
    """Build and compile the NewsPodcast LangGraph pipeline.

    Pipeline:
        START → grab_emails → clean_emails → END

    Nodes:
        - grab_emails: fetches raw emails from Gmail and filters them
          against the configured senders/titles.
        - clean_emails: processes the filtered emails into cleaned content
          ready for podcast generation.

    Returns:
        A compiled LangGraph runnable backed by NewsPodcastState.
    """
    graph = StateGraph(NewsPodcastState)

    graph.add_node(GraphNode.GRAB_EMAILS.value, grab_emails)
    graph.add_node(GraphNode.CLEAN_EMAILS.value, clean_emails)
    graph.add_node(GraphNode.CONVERT_TEXT_FILES.value, convert_text_to_mp3)


    # START -> GRAB_EMAILS
    graph.add_edge(START, GraphNode.GRAB_EMAILS.value)
    #graph.add_edge(START,GraphNode.CONVERT_TEXT_FILES.value )

    # GRAB_EMAILS -> CLEAN_EMAILS
    graph.add_edge(GraphNode.GRAB_EMAILS.value, GraphNode.CLEAN_EMAILS.value)
    # CLEAN_EMAILS -> END
    graph.add_edge(GraphNode.CLEAN_EMAILS.value, END)

    return graph.compile()
