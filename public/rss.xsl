<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/"
                xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">

  <style type="text/css">

  html{color:#CFCFCF;background-color:#121213;font-family: "Cascadia Code", "Courier New", monospace}

  article,aside,details,figcaption,figure,footer,header,main,menu,nav,section{display:block}

  summary{display:list-item}

  audio,canvas,progress,video{display:inline-block}

  a{background-color:transparent}
  a:active,a:hover{outline-width:0}

  body{background-color:#121213;font-size:14px;line-height:1.5;padding-right:5%;padding-left:5%}

  a{color:#24ACD4;text-decoration:none}
  a:hover{text-decoration:underline}

  .purple-box{color:#CFCFCF;background-color:#121213;color:#CFCFCF;background-color:#791EB4!important;padding:2%;margin-top:0%}

  .text-gray{color:#687079!important}
  </style>
    <html xmlns="http://www.w3.org/1999/xhtml" lang="en">
      <head>
        <title><xsl:value-of select="/rss/channel/title"/> Web Feed</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"/>
      </head>
      <body>
        <nav>
          <p class="purple-box">
            this is an rss feed. subscribe by copying the url from the address bar into your newsreader.
          </p>
          <p class="text-gray">
            visit <a href="https://aboutfeeds.com">about feeds</a> to get started with newsreaders and subscribing. it’s free.
          </p>
        </nav>
        <div>
          <header>
            <h1><xsl:value-of select="/rss/channel/title"/> feed</h1>
            <!-- <p><xsl:value-of select="/rss/channel/description"/></p> -->
            <a href="/" target="_blank">
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
        <br/>
        <xsl:value-of select="/rss/channel/copyright"/>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
