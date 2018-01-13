# import gzip
# content = "Lots of content here"
# with gzip.open('file.txt.gz', 'wb') as f:
#     f.write(content)

import gzip
content = b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccc"
with gzip.open('file.txt.gz', 'wb') as f:
    f.write(content)