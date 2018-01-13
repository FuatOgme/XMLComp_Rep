import xml.etree.ElementTree as ET
import os
import gzip

# content = b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccc"
# with gzip.open('file.txt.gz', 'wb') as f:
#     f.write(content)

#path için mac'te /  windowsta \
filePath = "examples"+ os.sep +"short.xml"

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

contsDict = {}
elemPath = ""
prevElemArray = []
arr = []
for event, elem in ET.iterparse(filePath,events=("start","end")):
    if event == "start":
        if len(prevElemArray) > 0:
            elemPath = "/".join(prevElemArray) + "/" + elem.tag
        else :
            elemPath = elem.tag
        AddElmToDict(contsDict, elem, elemPath)
        AddAttrToDict(contsDict, elem, elemPath)
        prevElemArray.append(elem.tag)
        arr.append(elemPath)

    if event == "end":
        prevElemArray.pop()
        elemPath = ""
    # if elemPath != "" and elemPath not in dict:
    #     dict[elemPath] = elem.text
    #     elemPath = ""
    elem.clear()

struct = ""
for val in arr:
    struct += val
    struct += "\n"
inpt = str.encode(struct)


with gzip.open('structure.txt.gz', 'wb') as f:
    f.write(inpt)

x = 5
