yapt - Yet Another Python tail'er
====

Yet Another Python tail'er is a small python-script for continuos colorization
of your log-files.

YAPt aims to be:
- Work like tail -f.
- Simple.
- Lightweight.
- Easily modified to custom needs.

Features:
- Colorizes lines starting with INFO, WARNING and ERROR.
- Wrap lines at column 80 and indent those.

Usage
-----

    $ ./yapt some.log

    $ ./yapt -h
    usage: yapt.py [-h] file
    
    A colorized version of 'tail -f'
    
    positional arguments:
      file        The file to tail.
    
    optional arguments:
      -h, --help  show this help message and exit

