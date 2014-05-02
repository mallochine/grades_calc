import sys
import os

if len(sys.argv) < 2:
  print "Need one argument."
  sys.exit(0)

grades = sys.argv[1]
totalNum = 0
totalDenom = 0

with open(grades) as f:
  for line in f:
    num = int(line.split(' ')[0])
    denom = int(line.split(' ')[1])
    totalNum += num
    totalDenom += denom

print totalNum, "/", totalDenom
