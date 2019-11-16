<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
    <html>
    <body>
    <h2>Queary 3a</h2>
    <xsl:for-each select="warehouses/warehouse">
     <xsl:if test="country = 'Singapore'">
    <h3>Warehouse <xsl:value-of select="id"/>, <xsl:value-of select="name"/></h3>
    <h4>Item Lists</h4>
     <ol>
    <xsl:for-each select="items/item">
     <xsl:if test="qty &gt; 975">
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