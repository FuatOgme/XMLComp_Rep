import xml.etree.ElementTree as ET
import gzip
from lxml import etree


def CreateContainerFiles(containerDict, filePath):
    tree = etree.parse(filePath)
    root = tree.getroot()
    for key, value in containerDict.items():
        valList = root.findall(key)
        containerName = value[0]
        attrName = ""
        if len(value)>1:
            attrName = value[1]

        with gzip.open('out/' + containerName + '.txt.gz', 'wb') as f:
            for elm in valList:
                if attrName == "":
                    if elm.text is not None:
                        f.write(str.encode(elm.text+"\n"))
                else:
                    attrVal = elm.attrib[attrName]
                    f.write(str.encode(attrVal+"\n"))
    return

def CreateStructureFile(structStr):
    with gzip.open('out/structure' + '.txt.gz', 'wb') as f:
        f.write(str.encode(structStr))
    return

def CreateElmDictFile(dict):
    dictStr = ""
    for key,value in dict.items():
        dictStr += value[0] + " " + value[1] + "\r\n"
    with gzip.open('out/elements' + '.txt.gz', 'wb') as f:
        f.write(str.encode(dictStr))
    return

def CreateAttrDictFile(dict):
    dictStr = ""
    for key, value in dict.items():
        dictStr += value[0] + " " + value[1] + "\r\n"
    with gzip.open('out/attributes' + '.txt.gz', 'wb') as f:
        f.write(str.encode(dictStr))
    return

def Compress(filePath):
    elemDict = {}
    attrDict = {}
    elemPath = "."
    elmId = 0
    attrId = 0
    struct = ""
    contDict = {}
    contId = 0
    contElmpath = "."

    for event, elem in ET.iterparse(filePath, events=("start", "end")):
        if event == "start":
            if elmId > 0:
                elemPath = elemPath + "/" + elem.tag
            if elemPath not in elemDict:  # element sözlüğe atılıyor
                elemDict[elemPath] = ["T" + str(elmId), elem.tag]
                elmId += 1
            struct += elemDict[elemPath][0] + " "

            if contId > 0:
                contElmpath = contElmpath + "/" + elem.tag
            if elem.text != "" and (contElmpath not in contDict): #container sözlüğe ekleniyor
                contDict[contElmpath] = ["C" + str(contId)]
                contId += 1
            struct += contDict[contElmpath][0] + " "


            if len(elem.attrib)> 0:
                for key, value in elem.attrib.items():
                    attPath = contElmpath + "[@" + key + "]"
                    if value != "" and (attPath not in contDict): #container sözlüğe ekleniyor
                        contDict[attPath] = ["C" + str(contId), key]
                        contId += 1
                    struct += contDict[attPath][0] + " "

            if len(elem.attrib) > 0:
                for key, value in elem.attrib.items(): #attributeler sözlüğe atılıyor
                    attPath = elemPath + "[@" + key + "]"
                    if attPath not in attrDict:
                        attrDict[attPath] = ["A" + str(attrId), key]
                        attrId += 1
                    struct += attrDict[attPath][0] + " "
        if event == "end":
            struct += "/ "
            elemPath = elemPath.rsplit('/', 1)[0]
            contElmpath = contElmpath.rsplit('/', 1)[0]
        elem.clear()

    CreateContainerFiles(contDict, filePath)
    CreateStructureFile(struct)
    CreateElmDictFile(elemDict)
    CreateAttrDictFile(attrDict)
    # print(struct)
    return



  # file = open('out/' + containerName + '.txt', 'w')
        # for elm in valList:
        #     if attrName == "":
        #         file.write("%s\n" % elm.text)
        #     else:
        #         attrVal = elm.attrib[attrName]
        #         file.write("%s\n" % attrVal)
        # file.close()
