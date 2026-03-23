from core.common.podcast import Podcast
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

    file_input = [{"path": '/Users/albertocappellina/sources/trashcode/newspodcasts/temporary-work/test.mp3',
                   "podcast": Podcast(
                       id="outpost",
                       title="outpost",
                       link="https://www.ilpost.it/tag/outpost/"
                       , language="it",
                       author="Daniele Raineri",
                       category="news"
                   )
                   }]

    graph.invoke(input={"config": config,
                             "file_to_publish": file_input

                        #           '/Users/albertocappellina/sources/trashcode/newspodcasts/temporary-work/art2.txt',
                        #           '/Users/albertocappellina/sources/trashcode/newspodcasts/temporary-work/art3.txt',
                        #           '/Users/albertocappellina/sources/trashcode/newspodcasts/temporary-work/art4.txt',
                        #  ]
                        })


if __name__ == "__main__":
    main()
