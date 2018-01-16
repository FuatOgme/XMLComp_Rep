import gzip

def GetElementTag(tag):
    elmIndex = tag[1:]
    i = 0
    with gzip.open("out/elements.txt.gz",'r') as f:
        for lineByte in f:
            if str(i) == elmIndex:
                line = lineByte.decode("utf-8")
                lineArr = str.split(line)
                return lineArr[1]
            else:
                i+=1
    return

def GetAttributeTag(tag):
    elmIndex = tag[1]
    i = 0
    with gzip.open("out/attributes.txt.gz",'r') as f:
        for lineByte in f:
            if str(i) == elmIndex:
                line = lineByte.decode("utf-8")
                lineArr = str.split(line)
                return lineArr[1]
            else:
                i+=1
    return

contHistory = {}
def GetContainerValue(tag):
    if tag not in contHistory:
        contHistory[tag] = 0
    else:
        contHistory[tag] += 1
    i = 0
    with gzip.open("out/"+ tag +".txt.gz",'r') as f:
        for lineByte in f:
            if i == contHistory[tag]:
                line = lineByte.decode("utf-8")
                return line.rstrip()
            else:
                i+=1
    return

def replace_right(source, target, replacement, replacements=None):
    return replacement.join(source.rsplit(target, replacements))

def EvaluateXML(struct):
    print(struct)
    structList = struct.split(" ")

    lastType = 0

    XML = ""
    elm = ""
    attr = ""
    contVal = ""
    tagStack = []
    for tag in structList:
        if str.startswith(tag,"T"):
            elm = GetElementTag(tag)
            XML += "<" +elm + ">"
            tagStack.append([0,elm])
        elif str.startswith(tag,"A"):
            attr = GetAttributeTag(tag)
            XML = replace_right(XML,">"," " + attr + "=",1)
            tagStack.append([1,attr])
        elif str.startswith(tag,"C"):
            contVal = GetContainerValue(tag)
            if contVal is not None:
                if tagStack[-1][0] == 0: #son tip element ise
                    # XML += ">" + contVal
                    XML += contVal
                else: #son tip attr ise
                    XML += "\"" +contVal
            # todo ?
        elif str.startswith(tag,"/"):
             lastTag = tagStack.pop()
             if lastTag[0] == 0:#son tip element ise
                 XML += "</" + lastTag[1] + ">"
             else:#son tip attr ise
                 XML += "\" >"
    print(XML)
    return XML

def Decompress(folderPath, outFilePath):
    bytes = None
    with gzip.open(folderPath+'\structure.txt.gz', 'r') as f:
        bytes = f.readline()
    XML = ""
    if bytes is not None:
        XML = EvaluateXML(bytes.decode("utf-8"))

    if XML != "":
        f = open(outFilePath, "w")
        f.write(XML)
    return