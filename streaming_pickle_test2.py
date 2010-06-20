from sPickle import *
import sys

UPPER_BOUND = 1000000
#UPPER_BOUND = 100

if sys.argv[1] == 'load':
  for elt in s_load(open('test2.spickle')):
    print type(elt), elt

if sys.argv[1] == 'load_heavy':
  d = dict(s_load(open('test2.spickle')))
  for elt in d.iteritems():
    print type(elt), elt

elif sys.argv[1] == 'dump':
  d = {}
  for i in range(UPPER_BOUND):
    d[i] = -1 * i

  outf = open('test2.spickle', 'w')
  s_dump(d.iteritems(), outf)
  outf.close()

