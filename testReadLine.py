#!/usr/bin/python
# files1.py - first program to play with files
#
filename = "iplist.txt"

inp = open(filename, "r")
lc = 0

one_line = "Anything, just not null :-)"
 #for one_line in inp.readline() :
while one_line :
  one_line = inp.readline()
  one_line = one_line.rstrip('\n')
  ll = len(one_line)
  if ll < 1 :
    break
  lc += 1 # Not null: Bump up lines-read count
  print "Input line[%d] is %d chars: %s" % (lc, ll, one_line)

 # Done printing...
 #
inp.close
