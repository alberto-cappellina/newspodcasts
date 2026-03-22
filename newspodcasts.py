from core.configuration.loader import load_config
from core.graph.graph_provider import provide_graph


def main() -> None:

    # load configuraion
    config = load_config(path="configuration.yaml")

    # get core graph
    graph = provide_graph()

    # draw graph
    # graph.get_graph().draw_mermaid_png(output_file_path='testing123.png')

    # start
    graph.invoke(input={"config": config})


if __name__ == "__main__":
    main()
