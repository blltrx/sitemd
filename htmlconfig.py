#!/usr/bin/python3
# welcome to htmlconfig.py!

# change lines between """ to edit
# constant variables should be names clearly in ALL CAPS
# with the exception of TOP, it's suggested to keep a tab (4 spaces in python3) in front of each line

ROOT = "/home/blltrx/Devel/sitemd/public"

TOP = """
<!DOCTYPE html>
<html lang="en">
"""

HEADERS = """
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@xz/fonts@1/serve/cascadia-code.min.css">
    <meta name="description" content="website for rose / bellatrix">
    <meta property="og:title" content="blltrx" />
    <meta name="fediverse:creator" content="blltrxrose@transfem.social" />
    <meta property="og:image" content="/assets/azuuuma.webp" />
    <title>rose / bellatrix</title>
    <link rel="stylesheet" href="/style.css" />
"""

TOPBAR = """
    <div id="nav">
      <a href="/" class="blue spacedLink">home</a>
      <span>/</span>
      <a href="/projects" class="pink spacedLink">projects</a>
      <span>/</span>
      <a href="/meta" class="white spacedLink">about</a>
    </div>
"""

FOOTER = """
    <div id="foot" class="monospaced">
        <div>
            roseis.gay 🏳️‍⚧️🏳️‍🌈 <br>
            <a class="coverLink" href="mailto:hello@roseis.gay">hello@roseis.gay</a><br>
            rose / bellatrix © mmxxv
        </div>

        <div>
            navigation<br>
            <a href="/"> home</a><br>
            <a href="/projects"> projects</a><br>
            <a href="/meta"> meta/about</a><br>
        </div>

        <div>
            other<br>
            <a href="/other/styleguide"> styleguide</a><br>
            <a href="/feed.xml">rss feed</a><br>
        </div>
        <div>
            <a href=https://frogofthemonth.carrd.co aria-label="frog of the month">
            <img src=https://i.imgur.com/FoJSh5v.gif alt="frog of the month button" loading=lazy width=126 height=92>
            </a>
            <a href=https://alyx.sh/posts/hrt-geocities-buttons/ aria-label="alyx.sh hrt neocities button">
            <img src=/assets/8831-estrogen.gif alt="powered by estrogen" loading=lazy width=88 height=31>
            </a>
        </div>    
        </div>
"""
