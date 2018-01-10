from io import StringIO
from lxml import etree



dtd = etree.DTD(StringIO('<!ELEMENT a (b,c,d)>'))
dtd.elements()[0].content.right.left
