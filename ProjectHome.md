## What is it? ##

`streaming-pickle` allows you to save/load a sequence of Python data structures to/from disk in a streaming (incremental) manner, thus using far less memory than [regular pickle](http://docs.python.org/library/pickle.html).


## When is it useful? ##

`streaming-pickle` is useful for any ad-hoc data processing task involving a linear sequence of records.

For example, let's say you write a script A to perform some analysis and then dump 1 million records to disk in some textual format, with each record taking up one line.  Then you write another script B that reads in those records one line at a time and performs some more analysis.  This strategy is memory-efficient (you only need to store one record at a time in RAM) and provides the benefits of incremental stream processing.  However, you need to write the parsing and unparsing code to convert between your plaintext format and Python data structures, which is tedious and error-prone.

An alternative is to have script A create a Python list and pickle it to disk.  Then script B simply unpickles the list and iterates over it to perform its analysis.  Now you don't need to write any parsing and unparsing code, but unfortunately your scripts might consume far too much memory (they need to store the entire 1 million element list in RAM) and cannot be streamed in a pipeline.

`streaming-pickle` combines the best of both strategies: memory-efficient stream processing of persistent data without requiring any extra parsing/unparsing code.


## How do I use it? ##

`streaming-pickle` has a very similar interface to [regular pickle](http://docs.python.org/library/pickle.html).  To get start it, simply download the single source file `sPickle.py` and import it into your project.


### Basic usage ###

To save a list of Python data to disk, use `s_dump`:

```
lst = ... big list of data you want to save to disk ...
sPickle.s_dump(lst, open('lst.spkl', 'w'))
```

To load data from disk in a streaming manner, use `s_load` and iterate over its result:

```
for element in sPickle.s_load(open('lst.spkl')):
    ... process element ...
```

As you iterate, only **one** element will be loaded into memory at a time (so you can process huge lists without running out of memory).


### Advanced usage ###

`s_dump` can save **any iterable object** to disk, not just lists.  In the example below, I create a [generator expression](http://www.python.org/dev/peps/pep-0289/) that reads `input.csv`, extracts the first field in each line, processes it with `process_data()`, and saves the sequence of results to disk in the file `lst.spkl`.

```
sPickle.s_dump((process_data(line.split(',')[0]) for line in open('input.csv')), open('lst.spkl', 'w'))
```

Since we're using a generator expression, only one line from `input.csv` will be loaded into memory at a time.

Alternatively, if you don't feel comfortable pickling iterables, you can use `s_dump_elt` to save one element at a time to disk.  This code does the same thing as the above example:

```
f = open('lst.spkl', 'w')

for line in open('input.csv'):
    sPickle.s_dump_elt(process_data(line.split(',')[0]), f)

f.close()
```

Lastly, remember that you can use any file-like object with `streaming-pickle`, so you can also stream Python data over pipes or network sockets.


### Gotchas ###

Remember that `s_dump` saves an iterable object to disk, so if you try to `s_dump` a `dict`, it will actually save only its _keys_ because the default iterator for a `dict` generates its keys.  If you want to save key/value pairs, use:

```
d = ... dict you want to save to disk ...
sPickle.s_dump(d.iteritems(), open('dict.spkl', 'w'))
```

(However, `s_dump_elt` can save any picklable object to disk.)


## Contact information ##

Questions?  Complaints?  Bug reports?  Feature requests?  Please email Philip Guo (philip@pgbovine.net)