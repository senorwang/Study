import os

dir = '/Users/guanwang/tmp/test'

for f in os.listdir(dir):
    d = os.path.join(dir, f)
    if (os.path.isdir(d)):
        files = os.listdir(d)
        tf = files[0]
        src = os.path.join(d, tf)
        dest = os.path.join(d, f)
        print (src + " changed to " + dest)
        os.rename(src, dest)
