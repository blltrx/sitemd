#!/usr/bin/python3
import sys
import markdown as md
import htmlconfig as html

HELP_MESSAGE = """
python main.py <markdown path> <OPTIONAL arguments>
    -v               : verbose, includes [DEBUG] infomation
    -o <output path> : uses stated output path instead of YAML frontmatter
    -r <root path>   : uses stated root path for output instead of 'htmlconfig.py'
    --exclude-extra  : DOES NOT add a navigation 'TOPBAR' or 'FOOTER' to <body> in final output
    --exclude-head   : DOES NOT add 'HEADERS' into <head> defined in final output
requires htmlconfig.py 'TOP' variable, and unless excluded, 'HEADERS', 'TOPBAR' and 'FOOTER'
requires markdown from pip 'pip install markdown'
"""

DEBUG = False
EXCLUDE_EXTRA = False
EXCLUDE_HEAD = False
MARKDOWN_EXTENTIONS = ['extra']
path = ""
root = ""

# argument definitions
argvars = sys.argv[1:]
infile = argvars[0]
if infile == "README.md":
    exit(0)
if "-v" in argvars:
    DEBUG = True
if "--exclude-extra" in argvars:
    EXCLUDE_EXTRA = True
    if DEBUG:
        print("[DEBUG] EXCLUDE_EXTRA = True")
if "--exclude-head" in argvars:
    EXCLUDE_HEAD = True
    if DEBUG:
        print("[DEBUG] EXCLUDE_HEAD = True")
if "-r" in argvars:
    root = argvars[argvars.index("-r")+1]
if "-o" in argvars:
    path = argvars[argvars.index("-o")+1]
if "-h" in argvars or "--help" in argvars or "-help" in argvars:
    print(HELP_MESSAGE)
    sys.exit(0)


def addHashMarkToHTML(htmlstring: str) -> str:
    """return htmlstring but with decorative element
    added infront of the first instance of heading 1"""
    try:
        h1index = htmlstring.index("<h1>")
        HASHMARKSTRING = '<h1 class="title"><span class="hash">#</span>'
        (htmlstring) = (
            htmlstring[:h1index] +
            HASHMARKSTRING +
            htmlstring[h1index+4:])
        # 4 is the length of the substring
        return htmlstring
    except ValueError:
        return htmlstring


def createPageString(contentstring: str) -> str:
    """return string of html file with parameters in 'htmlconfig.py',
    with content defined in an input string in html format"""
    header = ""
    topbar = ""
    footer = ""
    if not EXCLUDE_HEAD:
        header = html.HEADERS
    if not EXCLUDE_EXTRA:
        topbar = html.TOPBAR
        footer = html.FOOTER
    return f"""
{html.TOP}
<head>
{header}
</head>

<body>
<div class="contentWrap">
{topbar}
{contentstring}
{footer}
</div>
</body>
</html>
"""


def seperate_yaml(filestring: str) -> tuple[dict[str, str], str]:
    """
    extract YAML heading from filestring, and return YAML as a dictionary and
    filestring with YAML header removed"""
    startindex = filestring.find("---")
    endindex = filestring.find("---", 5)
    yaml = ""
    body = ""
    if startindex != 0:
        return ({"": ""}, filestring)
    yamlstring = filestring[startindex+4:endindex-1]
    yaml = dict(subString.split(": ") for subString in yamlstring.split("\n"))
    body = filestring[endindex+4:]
    return (yaml, body)


def convert(inputpath: str) -> tuple[dict[str, str], str]:
    """take a path to a plain text file in markdown,
    and return an html page based on 'htmlconfig.py'
    is dependant on 'seperate_yaml'"""
    if DEBUG:
        print(f"[DEBUG]: opening file {inputpath}")
    with open(inputpath, "r") as f:
        filestring = f.read()
        f.close()
    if DEBUG:
        print(f"[DEBUG]: reading file {inputpath}")
    yaml, bodymd = seperate_yaml(filestring)
    html_content_string = md.markdown(bodymd, extensions=MARKDOWN_EXTENTIONS)

    if DEBUG:
        print(f"[DEBUG]: extracted YAML heading {yaml}")
    if DEBUG:
        print("[DEBUG]: converted body to html")
    pagestring = createPageString(html_content_string)
    return yaml, pagestring


def main() -> None:
    global path, root
    yaml, pagestring = convert(infile)
    pagestring = addHashMarkToHTML(pagestring)
    if DEBUG:
        print("[DEBUG]: attempting to save file")
    try:
        if path == "":
            path = yaml['path']
        if root == "":
            root = html.ROOT
        outputpath = f"{root}/{path}"
        with open(outputpath, "w") as f:
            f.write(pagestring)
            f.close()
        print(f"[HTML]: output at '{outputpath}'")
    except FileNotFoundError as exception:
        if DEBUG:
            print(f"[DEBUG]: {exception}")
            sys.exit("""
                [ERROR]: Directory path invalid.
                Check it exists, if not create it.""")
        else:
            sys.exit("""
                [ERROR]: Directory path invalid.
                Check it exists, if not create it.
                Run with -v for DEBUG infomation")""")


if __name__ == "__main__":
    main()
