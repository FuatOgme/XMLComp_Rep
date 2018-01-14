import xml.etree.ElementTree as ET
import os
import gzip
from lxml import etree


#path için mac'te /  windowsta \
filePath = "examples"+ os.sep +"short.xml"


tree = etree.parse(filePath)

#tree = etree.ElementTree(root)
root = tree.getroot()
# for elem in root.iter():
#     print(tree.getpath(elem))
    #if len(elem.attrib) > 0:
       # for key,value in elem.attrib.items():
        #    print()
            #attPath = elemPath +"[@" + key +"]"
            #if attPath not in dict:
             #   dict[attPath] = value


def AddElementToDict(dict,seqArr, elem: ET.Element, elemPath, elmId):
    if elemPath not in dict: # element sözlüğe atılıyor
        dict[elemPath] = "E" + str (elmId)
    seqArr.append(elemPath)
    return

def AddAttributeToDict(dict,seqArr,elem: ET.Element, attPath,attId):
    if attPath not in dict:
        dict[attPath] = "A" + str(attId)
    seqArr.append(attPath)

def CreateStructureSequence(seqArray, dict):
    structure = ""
    for seq in seqArray:
        structure += dict[seq]



contsDict = {}
elemPath = "."
arr = []
elmId = 0
for event, elem in ET.iterparse(filePath,events=("start","end")):
    if event == "start":
        if elmId > 0:
            elemPath = elemPath + "/" + elem.tag
        AddElementToDict(contsDict,arr, elem, elemPath, elmId)

        if len(elem.attrib) > 0:
            i=0
            for key, value in elem.attrib.items():
                attPath = elemPath + "[@" + key + "]"
                AddAttributeToDict(contsDict, arr, elem, attPath, elmId + (++i))
        elmId = elmId + 1
    if event == "end":
        elemPath = elemPath.rsplit('/', 1)[0]
    elem.clear()



y = root.findall('.country/neighbor[@direction]')
for elm in y:
    print(elm.tag)

x = 5