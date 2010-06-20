import streaming_pickle
import sys

from cPickle import load, dump

UPPER_BOUND = 1000000
#UPPER_BOUND = 100

if sys.argv[1] == 'load':
  for elt in streaming_pickle.stream_load(open('test.spickle')):
    if elt[0] % 100000 == 0:
      print type(elt), elt

elif sys.argv[1] == 'dump':
  lst = []
  for i in range(UPPER_BOUND):
    lst.append((i, i*2, i*3))

  streaming_pickle.stream_dump(lst, open('test.spickle', 'w'))

elif sys.argv[1] == 'streaming_dump':
  outf = open('test.spickle', 'w')
  for i in range(UPPER_BOUND):
    elt = (i, i*2, i*3)
    streaming_pickle.stream_dump_elt(elt, outf)
  outf.close()

elif sys.argv[1] == 'traditional_load':
  for elt in load(open('test.pickle')):
    if elt[0] % 100000 == 0:
      print type(elt), elt

elif sys.argv[1] == 'traditional_dump':
  lst = []
  for i in range(UPPER_BOUND):
    lst.append((i, i*2, i*3))

  dump(lst, open('test.pickle', 'w'))

