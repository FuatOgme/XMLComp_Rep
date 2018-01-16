import Compress
import Decompress
import os

# path için mac'te /  windowsta \
filePath = "examples" + os.sep + "shakespeare.xml"
folderPath = "out"
outFilePath = "result" + os.sep + "shakespeare.xml"

Compress.Compress(filePath)
Decompress.Decompress(folderPath, outFilePath)