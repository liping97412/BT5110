<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="students">
    <summary>
      <xsl:apply-templates select="student"/>
    </summary>
  </xsl:template>

  <xsl:template match="student">
    <grades>
      <xsl:attribute name="id" select="@id"/>
      <xsl:for-each select=".//@grade">
	    <grade>
	      <xsl:value-of select="."/>
	    </grade>
      </xsl:for-each> 
    </grades>
  </xsl:template>

</xsl:stylesheet>
