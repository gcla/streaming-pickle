import sPickle

lst = range(101)
sPickle.s_dump(lst, open('lst.spkl', 'w'))

sum = 0
for element in sPickle.s_load(open('lst.spkl')):
  sum += element
print sum
print

def process_data(s):
  return len(s)

sPickle.s_dump((process_data(line.split(',')[0]) for line in open('input.csv')),
               open('lst1.spkl', 'w'))

for elt in sPickle.s_load(open('lst1.spkl')):
  print elt
print

f = open('lst2.spkl', 'w')
for line in open('input.csv'):
    sPickle.s_dump_elt(process_data(line.split(',')[0]), f)
f.close()

for elt in sPickle.s_load(open('lst2.spkl')):
  print elt
print

l = range(10)
d = dict(zip(l, l))
sPickle.s_dump(d.iteritems(), open('dict.spkl', 'w'))

for e in sPickle.s_load(open('dict.spkl')):
  print e

