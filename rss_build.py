#!/usr/bin/python3
import tomllib
INPUT_ROOT = "content/"
PATH = "/home/blltrx/Devel/sitemd/public/feed.xml"
PAGE_HEADING = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="/rss.xsl" type="text/xsl"?>
<rss version="2.0">

<channel>
    <title>rose / bellatrix</title>
    <link>https://roseis.gay/feed.xml</link>
    <language>en-gb</language>
    <copyright>rose / bellatrix &#x2117;</copyright>
    <description>rss feed for roseis.gay</description>
    """

PAGE_END = """
</channel>
</rss>
"""


def xmlify(title: str, link: str, description: str, date:str) -> str:
    return f"""
    <item>
        <title>{title}</title>
        <description>{description}</description>
        <link>{link}</link>
        <pubDate>{date}</pubDate>
    </item>
    """


def main():
    with open(INPUT_ROOT + "feed.toml", "rb") as f:
        toml = tomllib.load(f)

    page_body = ""
    for item in toml['item']:
        title = item.get('title')
        link = item.get('link')
        description = item.get('description')
        date = item.get('pubDate')
        page_body += xmlify(title, link, description, date)

    with open(PATH, "w") as f:
        f.write(PAGE_HEADING + page_body + PAGE_END)
        print(f"[RSSF]: output at '{PATH}'")


if __name__ == "__main__":
    main()

# <managingEditor>hello@roseis.gay (rose)</managingEditor>
# <webMaster>hello@roseis.gay (rose)</managingEditor>
# <generator>rss_build.py in https://github.com/blltrx/sitemd</generator>
