<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/">
    <html>
      <body>
        <h2>Queary 3b</h2>
        <xsl:for-each select="warehouses/warehouse">
          <xsl:if test="country = 'Singapore'">
            <h3>Warehouse <xsl:value-of select="id"/>, <xsl:value-of select="name"/></h3>
            <h4>Largest Quantity Items</h4>
            <ol>
              <xsl:for-each select="items/item">
                <xsl:sort select="./qty" data-type="number" order="descending"/>
                <xsl:if test="position() = 1">
                  <li><xsl:value-of select="name"/>,<xsl:value-of select="qty"/></li>
                </xsl:if>
              </xsl:for-each>
            </ol>
          </xsl:if>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
