import tomllib
PAGE_HEADING = """
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
    <title>rose / bellatrix</title>
    <link>https://roseis.gay</link>
    <description>rss feed for bellatrix.dev and roseis.gay</description>
    """

PAGE_END = """
</channel>
</rss>
"""


def xmlify(title: str, links: list[str] | None, description: str) -> str:
    link_string = ""
    if links:
        for link in links:
            link_string += f"<link> {link} </link>\n\t\t"
    return f"""
    <item>
        <title> {title} </title>
        <description> {description} </description>
        {link_string}
    </item>
    """


def main():
    with open("rss.toml", "rb") as f:
        toml = tomllib.load(f)

    page_body = ""
    for item in toml['item']:
        title = item.get('title')
        links = item.get('links')
        description = item.get('description')
        page_body += xmlify(title, links, description)

    with open("public/rss.xml", "w") as f:
        f.write(PAGE_HEADING + page_body + PAGE_END)


if __name__ == "__main__":
    main()
