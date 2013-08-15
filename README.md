yapt - Yet Another Python tail'er
====

Yet Another Python tail'er is a small python-script for continuos colorization
of your log-files.

YAPt aims to be:
- Working like tail -f.
- Simple.
- Lightweight.
- Easily modified to custom needs.

Features:
- Colorizes lines starting with INFO, WARNING and ERROR.
- Wrap lines at column 80 and indent those.
- Write tagged HTML to a file.

Usage
-----

    $ ./yapt some.log
    INFO: Here is some info in green.
    WARNING: Here is a warning in yellow.
    ERROR: This is an error in red.
    ^C
    $ ./yapt some.log -o colored.html
    
The last command switches from printing the log to std-out, to writing
tagged-html to colored.html. Included is an example-file, serve_log.html,
utilizing AJAX to dynamicly updating a view of colored.html.

For help:

    $ ./yapt -h
    usage: yapt.py [-h] [-o file] file

    A colorized version of 'tail -f'

    positional arguments:
      file                  The file to tail.

    optional arguments:
      -h, --help            show this help message and exit
      -o file, --outfile file
                            If specified, writes tagged HTML to outfile, ready for
                            serving.

