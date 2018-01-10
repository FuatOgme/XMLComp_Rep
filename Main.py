import xml.etree.ElementTree as ET
import os

#path için mac'te /  windowsta \
filePath = "examples"+ os.sep +"shakespeare.xml"


dict = {}
elemPath = ""
prevElemArray = []
arr = []
for event, elem in ET.iterparse(filePath,events=("start","end")):
    if event == "start":
        if len(prevElemArray) > 0:
            elemPath = "/".join(prevElemArray) + "/" + elem.tag
        else :
            elemPath = elem.tag
        arr.append(elemPath)
        prevElemArray.append(elem.tag)
    if event == "end":
        prevElemArray.pop()
        elemPath = ""
    # if elemPath != "" and elemPath not in dict:
    #     dict[elemPath] = elem.text
    #     elemPath = ""
    elem.clear()


x = 5
#
# if elemPath != "":
#     elemPath += "/" + elem.tag
# else:
#     elemPath += elem.tag
# arr.append(elemPath)


# tree = ElementTree()
# tree.parse(open('file.xml'))
# root = tree.getroot()
#
# def print_abs_path(root, path=None):
#     if path is None:
#         path = [root.tag]
#
#     for child in root:
#         text = child.text.strip()
#         new_path = path[:]
#         new_path.append(child.tag)
#         if text:
#             print '/{0}, {1}'.format('/'.join(new_path), text)
#         print_abs_path(child, new_path)
#
# print_abs_path(root)