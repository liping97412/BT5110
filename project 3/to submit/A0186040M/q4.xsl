<?xml version="1.0" encoding="UTF-8" ?>
<xsl:transform xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="text" encoding="iso-8859-1"/>

  <xsl:strip-space elements="*" />

  <xsl:template match="/">
    <xsl:text>Rank,Country or territory,Total length of land borders (km),Total surface area (km2),Border/area ratio (km/km2)</xsl:text>
    <xsl:text>&#xa;</xsl:text>
    <xsl:apply-templates select="//table[@class='wikitable sortable jquery-tablesorter']/tbody[1]"/>     
</xsl:template>

  <xsl:template match="tr">
      <xsl:value-of select="translate(td[1],'&#10;','')"/>,<xsl:value-of select="translate(td[2],'&#10;','')"/>,<xsl:value-of select="translate(td[3],'&#10;','')"/>,<xsl:value-of select="translate(td[4],'&#10;','')"/>,<xsl:value-of select="td[5]"/>
  </xsl:template>
</xsl:transform>