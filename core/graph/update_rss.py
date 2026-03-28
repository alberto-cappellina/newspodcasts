from core.common.job import Job
from core.common.podcast import Podcast
from core.file_operations.file_writer import get_temp_file_path, write_string_temp_file_at_path
from core.graph import NewsPodcastState
from rss_update.channel import Channel
from rss_update.item import Item
from rss_update.xml_utilities import create_channel_xml
from text_to_mp3_conversion.mp3_data import get_mp3_info


def get_max_episode(items: list[Item]) -> int:
    return max((item.episode for item in items), default=0) + 1


def get_channel_and_episode(podcast: Podcast, channels: dict[str, Channel]) -> tuple[Channel, int]:
    if podcast.id not in channels:
        channels[podcast.id] = Channel.with_podcast(podcast)
        return channels[podcast.id], 1
    channel = channels[podcast.id]
    return channel, get_max_episode(channel.items)


def update_rss(state: NewsPodcastState) -> NewsPodcastState:
    file_to_publish = state["file_to_publish"]


    channels_map: dict[str, Channel] = {}
    job_for_channel: dict[str, list[Job]] = {}

    # add mp3 data to item
    for file in file_to_publish:
        podcast = file.podcast
        mp3 = file.path
        duration_seconds, _ = get_mp3_info(mp3)

        channel, episode = get_channel_and_episode(podcast,channels_map)

        # create a new item for that channel
        item = Item.with_podcast(podcast, episode, duration_seconds, mp3)
        channels_map[podcast.id].items.append(item)



    for channel in channels_map.values():
        # get the xml content
        channel_content = create_channel_xml(channel)
        # write it to a temporary files
        temp_channel_content = write_string_temp_file_at_path(
            path=get_temp_file_path(".xml"),
            mail_content=channel_content
        )

        # TODO: implement FTP upload
        pass

    return state


