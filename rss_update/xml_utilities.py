import xml.etree.ElementTree as ET

from rss_update.channel import Channel

ITUNES_NS = "http://www.itunes.com/dtds/podcast-1.0.dtd"


def create_channel_xml(channel: Channel) -> str:
    ET.register_namespace("itunes", ITUNES_NS)

    rss = ET.Element("rss", {"version": "2.0", "xmlns:itunes": ITUNES_NS})
    ch = ET.SubElement(rss, "channel")

    ET.SubElement(ch, "title").text = channel.title
    ET.SubElement(ch, "link").text = channel.link
    ET.SubElement(ch, "description").text = channel.description
    ET.SubElement(ch, "language").text = channel.language
    ET.SubElement(ch, f"{{{ITUNES_NS}}}author").text = channel.author
    ET.SubElement(ch, f"{{{ITUNES_NS}}}category", {"text": channel.category})

    for item in channel.items:
        it = ET.SubElement(ch, "item")
        ET.SubElement(it, "title").text = item.title
        ET.SubElement(it, "description").text = item.description
        ET.SubElement(it, "link").text = item.link
        ET.SubElement(it, "pubDate").text = item.pub_date.strftime("%a, %d %b %Y %H:%M:%S +0000")
        ET.SubElement(it, f"{{{ITUNES_NS}}}episode").text = str(item.episode)
        ET.SubElement(it, f"{{{ITUNES_NS}}}episodeType").text = item.episode_type
        ET.SubElement(it, f"{{{ITUNES_NS}}}duration").text = item.duration
        ET.SubElement(it, "enclosure", {"url": item.enclosure, "type": "audio/mpeg"})
        ET.SubElement(it, "guid").text = item.guid

    return ET.tostring(rss, encoding="unicode", xml_declaration=True)
