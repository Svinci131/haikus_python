
import os
print "hello"

dirpath = os.path.relpath('textFiles')
fpath = os.path.join(dirpath, "timeMachine.txt")
f = open(fpath)
content = f.read()

print content
# with open('textFiles/timeMachine.txt') as f:
# 	content = f.readlines();
# READ FILE