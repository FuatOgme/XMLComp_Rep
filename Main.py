import Compress
import Decompress
import os

# path için mac'te /  windowsta \
filePath = "examples" + os.sep + "short.xml"
folderPath = "out"

Compress.Compress(filePath)

Decompress.Decompress(folderPath)