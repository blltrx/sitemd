<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/"
                xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">

  <style type="text/css">/*! normalize.css v4.1.1 | MIT License | github.com/necolas/normalize.css */

  html{font-family: "Cascadia Code", "Courier New", monospace}

  article,aside,details,figcaption,figure,footer,header,main,menu,nav,section{display:block}

  summary{display:list-item}

  audio,canvas,progress,video{display:inline-block}

  audio:not([controls]){display:none;height:0}
  progress{vertical-align:baseline}[hidden],template{display:none!important}

  a{background-color:transparent}
  a:active,a:hover{outline-width:0}


  body{font-size:14px;line-height:1.5;color:#24292e;background-color:#fff}

  a{color:#0366d6;text-decoration:none}
  a:hover{text-decoration:underline}
  .bg-white{background-color:#fff!important}

  .bg-blue{background-color:#0366d6!important}.bg-blue-light{background-color:#f1f8ff!important}.bg-gray-dark{background-color:#24292e!important}.bg-gray{background-color:#f6f8fa!important}.bg-gray-light{background-color:#fafbfc!important}.bg-green{background-color:#28a745!important}.bg-green-light{background-color:#dcffe4!important}.bg-red{background-color:#d73a49!important}.bg-red-light{background-color:#ffdce0!important}

  .bg-yellow{background-color:#ffd33d!important}.bg-yellow-light{background-color:#fff5b1!important}
  .bg-purple{background-color:#6f42c1!important}
  .bg-purple-light{background-color:#f5f0ff!important}

  .text-gray{color:#586069!important}

  .markdown-body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";font-size:16px;line-height:1.5;word-wrap:break-word}

  </style>
    <html xmlns="http://www.w3.org/1999/xhtml" lang="en">
      <head>
        <title><xsl:value-of select="/rss/channel/title"/> Web Feed</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"/>
      </head>
      <body class="bg-white">
        <nav class="container-md">
          <p class="bg-yellow-light">
            this is an rss feed.subscribe by copying the url from the address bar into your newsreader.
          </p>
          <p class="text-gray">
            visit <a href="https://aboutfeeds.com">about feeds</a> to get started with newsreaders and subscribing. it’s free.
          </p>
        </nav>
        <div class="container-md">
          <header>
            <h1><xsl:value-of select="/rss/channel/title"/> feed</h1>
            <p><xsl:value-of select="/rss/channel/description"/></p>
            <a target="_blank">
              <xsl:attribute name="href">
                <xsl:value-of select="/rss/channel/link"/>
              </xsl:attribute>
              visit website &#x2192;
            </a>
          </header>
          <h2>recent items</h2>
          <xsl:for-each select="/rss/channel/item">
            <div>
              <h3>
                <a target="_blank">
                  <xsl:attribute name="href">
                    <xsl:value-of select="link"/>
                  </xsl:attribute>
                  <xsl:value-of select="title"/>
                </a>
              </h3>
              <xsl:value-of select="description"/><br/>
              <small class="text-gray">
                published: <xsl:value-of select="pubDate" />
              </small>
            </div>
          </xsl:for-each>
        <xsl:value-of select="/rss/channel/copyright"/>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
