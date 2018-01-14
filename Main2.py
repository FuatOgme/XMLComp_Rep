import xml.etree.ElementTree as ET
import os
from lxml import etree

root = etree.fromstring('<foo><bar>Data</bar><bar><baz>data</baz>'
                        '<baz>data</baz></bar></foo>')

tree = etree.ElementTree(root)
for e in root.iter():
    print(tree.getpath(e))



import gzip

#path için mac'te /  windowsta \
filePath = "examples"+ os.sep +"shakespeare.xml"

# tree = ET.parse(filePath)
# root = tree.getroot()
# y = root.findall('PERSONAE/PGROUP/PERSONA')
#
# for elm in y:
#     print(elm.text)

def AddAttrToDict(dict,elem: ET.Element, elemPath):
    if len(elem.attrib) > 0:
        for key,value in elem.attrib.items():
            attPath = elemPath +"[@" + key +"]"
            if attPath not in dict:
                dict[attPath] = value
    return


def AddElmToDict(dict, elem: ET.Element, elemPath):
    if elemPath not in dict:
            dict[elemPath] = elem.tag
    return




x = 5
