import xml.etree.ElementTree as ET

from core.graph import NewsPodcastState
from rss_update.channel import Channel
from rss_update.item import Item
from rss_update.xml_utilities import create_channel_xml
from text_to_mp3_conversion.mp3_data import get_mp3_info




def get_max_episode(items: list[Item]) -> int:
    return max((item.episode for item in items), default=0) + 1




def update_rss(state: NewsPodcastState) -> NewsPodcastState:
    file_to_publish = state["file_to_publish"]
    channels: dict[str, Channel] = {}

    for file in file_to_publish:
        podcast = file["podcast"]
        mp3 = file['path']
        duration_seconds, _ = get_mp3_info(mp3)
        episode = 1

        if podcast.id not in channels:
            channels[podcast.id] = Channel.with_podcast(podcast)
        else:
            existing_channel = channels[podcast.id]
            episode = get_max_episode(existing_channel.items)

        item = Item.with_podcast(podcast, episode, duration_seconds, mp3)
        channels[podcast.id].items.append(item)


    for channel in channels:

        channel_content = create_channel_xml(channel)

    return state

