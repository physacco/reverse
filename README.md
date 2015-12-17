# reverse

Reverse the content of a file, write into another file.

## Installation

`pip install reverse`

## Usage

Example 1: use the command line script *reverse*

```
$ cat foo.txt
Hello.
$ reverse foo.txt foo.txt.rev
$ cat foo.txt.rev
.olleH
$ python reverse.py foo.txt.rev foo.txt.new
$ cat foo.txt.new
Hello.
```

Example 2: use the Python module *reverse*

```
$ python
>>> import reverse
>>> reverse.reverse_file('foo.txt', 'foo.txt.rev')
>>> reverse.reverse_file('foo.txt.rev', 'foo.txt.new')
>>> open('foo.txt').read() == open('foo.txt.new').read()
True
```

