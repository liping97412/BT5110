<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" encoding="UTF-8"/>
<xsl:template match="/">
         <html>
                 <body>
                 <h2>Query 3a</h2>
                         <xsl:template match="/warehouses/warehouse[country='Singapore']">
                                 <xsl:for-each select="warehouse">
                                         <h3>Warehouse <xsl:value-of select="id"/>, <xsl:value-of select="name"/></h3>
                                         <h4 >Item Lists </h4 >
                                 <xsl:for-each select="warehouse/items/item">
                                         <xsl:if test="qty>975">
                                         <ol>
                                         <li><xsl:value-of select="name"/>,<xsl:value-of select="qty"/> </li>
                                         </ol>
                                         </xsl:if>
                                 </xsl:for-each>
                                 </xsl:for-each>
                         </xsl:template>
                 </body>
         </html>
</xsl:template>
</xsl:stylesheet>
