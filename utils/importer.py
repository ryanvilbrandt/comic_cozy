import re
from xml.etree import ElementTree


def get_namespace(xml_path):
    with open(xml_path) as f:
        namespaces = re.findall(r"xmlns:(.*?)=\"(.*?)\"", f.read())
    return dict(namespaces)


def get_comic_data(item, ns):
    return {
        "title": item.find("title").text,
        "post_date": item.find("pubDate").text,
        "path": "",
        "guid": item.find("guid").text,
        "alt_text": "",
        "tags": [child.text for child in item.findall("category")],
        "text": item.find("content:encoded", ns).text,
    }


def get_comics(xml_path):
    ns = get_namespace(xml_path)

    tree = ElementTree.parse(xml_path)
    root = tree.getroot()
    assert root.tag == "rss"
    channel = root[0]
    assert channel.tag == "channel"

    version = channel.find("wp:wxr_version", ns).text
    assert version == "1.2"

    return [get_comic_data(item, ns) for item in channel.findall("item")]
