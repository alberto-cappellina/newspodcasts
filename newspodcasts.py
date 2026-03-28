from datetime import datetime, timezone

from core.common.podcast import Podcast
from core.common.processing_file import ProcessingFile
from core.configuration.loader import load_config
from core.graph.graph_provider import provide_graph
from email_process.gmail.models import UnprocessedEmail


def main() -> None:
    # load configuraion
    config = load_config(path="configuration.yaml")

    # get core graph
    graph = provide_graph()

    # draw graph
    # graph.get_graph().draw_mermaid_png(output_file_path='testing123.png')

    # start

    outpost_podcast = Podcast(
        id="outpost",
        title="outpost",
        link="https://www.ilpost.it/tag/outpost/",
        language="it",
        author="Daniele Raineri",
        category="news"
    )

    file_input = [ProcessingFile(
        path='/Users/albertocappellina/sources/trashcode/newspodcasts/temporary-work/test.mp3',
        podcast=outpost_podcast,
        email=UnprocessedEmail(
            message_id="123",
            from_="raineri@ilpost.it",
            subject='dont care',
            received_at=datetime.now(timezone.utc),
            matching_podcast=outpost_podcast
        )
    )]

    graph.invoke(input={"config": config,
                        "file_to_publish": file_input

                        #           '/Users/albertocappellina/sources/trashcode/newspodcasts/temporary-work/art2.txt',
                        #           '/Users/albertocappellina/sources/trashcode/newspodcasts/temporary-work/art3.txt',
                        #           '/Users/albertocappellina/sources/trashcode/newspodcasts/temporary-work/art4.txt',
                        #  ]
                        })


if __name__ == "__main__":
    main()
