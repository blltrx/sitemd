#!/usr/bin/python3
# welcome to htmlconfig.py!

# change lines between """ to edit
# constant variables should be names clearly in ALL CAPS
# with the exception of TOP, it's suggested to keep a tab (4 spaces in python3) in front of each line

ROOT = "/home/blltrx/devel/sitemd/public"

TOP = """
<!DOCTYPE html>
<html lang="en">
"""

HEADERS = """
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="website for rose / bellatrix">
    <meta property="og:title" content="blltrx" />
    <meta property="og:image" content="/assets/things.webp" />
    <title>rose / bellatrix</title>
    <link rel="stylesheet" href="/style.css" />
"""

TOPBAR = """
    <div id="nav">
      <a href="/" class="blue spacedLink">home</a>
      <span>/</span>
      <a href="/projects" class="pink spacedLink">projects</a>
      <span>/</span>
      <a href="/meta" class="white spacedLink">meta</a>
    </div>
"""

FOOTER = """
    <div id="foot" class="monospaced">
    <div>
    bellatrix.dev<br>
    roseis.gay 🏳️‍⚧️🏳️‍🌈 <br>
    <a class="coverLink" href="mailto:hello@roseis.gay">hello@roseis.gay</a><br>
    sonya nye © mmxxiv
    </div>

    <div>
    navigation<br>
    <a href="/"> home</a><br>
    <a href="/projects"> projects</a><br>
    <a href="/meta"> meta</a><br>
    </div>

    <div>
    other<br>
    <a href="/other/styleguide"> styleguide</a><br>
    </div>
    </div>
"""
