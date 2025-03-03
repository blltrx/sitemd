#!/usr/bin/python3
import tomllib
INPUT_ROOT = "content/"
PATH = "/home/blltrx/devel/sitemd/public/feed.xml"
PAGE_HEADING = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">

<channel>
    <title>rose / bellatrix</title>
    <link>https://roseis.gay/feed.xml</link>
    <language>en-gb</language>
    <copyright>rose / bellatrix &#x2117;</copyright>
    <description>rss feed for bellatrix.dev and roseis.gay</description>
    """

PAGE_END = """
</channel>
</rss>
"""


def xmlify(title: str, link: str, description: str) -> str:
    return f"""
    <item>
        <title> {title} </title>
        <description> {description} </description>
        <link> {link} </link>
    </item>
    """


def main():
    with open(INPUT_ROOT + "rss.toml", "rb") as f:
        toml = tomllib.load(f)

    page_body = ""
    for item in toml['item']:
        title = item.get('title')
        link = item.get('link')
        description = item.get('description')
        page_body += xmlify(title, link, description)

    with open(PATH, "w") as f:
        f.write(PAGE_HEADING + page_body + PAGE_END)
        print(f"[RSSF]: output at '{PATH}'")


if __name__ == "__main__":
    main()
