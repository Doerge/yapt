#!/usr/bin/env python
"""Skeleton stolen from the excellent slides of David Beazley on generators,
coroutines and similar stuff. Check out the presentation here:
http://www.slideshare.net/dabeaz/python-generator-hacking """

import time
import threading
import argparse

def follow(thefile):
  thefile.seek(0,2)   # Go to the end of the file
  while True:
    line = thefile.readline()
    if not line:
      time.sleep(0.1)   # Sleep briefly
      continue
    yield line

def color(lines):
  GREEN = '\033[32m%s\033[0m\n'
  YELLOW = '\033[33m%s\033[0m\n'
  RED = '\033[31m%s\033[0m\n'
  while True:
    for line in lines:
      # We are 'wrapping' the color-codes around the line.
      if line.endswith('\n'):
        line = line[:-1]
      if line.startswith('INFO'):
        yield GREEN % line
      if line.startswith('WARNING'):
        yield YELLOW % line
      if line.startswith('ERROR'):
        yield RED % line

def soft_wrap(lines):
  LINE_LENGTH = 80
  INDENT = 2
  STRIDE = LINE_LENGTH - INDENT
  while True:
    for line in lines:
      if len(line) < LINE_LENGTH:
        yield line
      else:
        first = line[:LINE_LENGTH]
        rest = [' '*INDENT + line[i:i+STRIDE] for i in xrange(LINE_LENGTH,len(line),STRIDE)]
        final = first + '\n' + '\n'.join(rest)
        yield final

def tail_print(filepath):
  # Pipeline:
  with open(args.filepath,'r') as logfile:
    loglines = follow(logfile)
    softlines = soft_wrap(loglines)
    colorlines = color(softlines)
    for line in colorlines:
      print line,

def htmlcolor(lines):
  GREEN = '<p id="green">%s</p>\n'
  YELLOW = '<p id="yellow">%s</p>\n'
  RED = '<p id="red">%s</p>\n'
  while True:
    for line in lines:
      # We are 'wrapping' the color-codes around the line.
      if line.endswith('\n'):
        line = line[:-1]
      if line.startswith('INFO'):
        yield GREEN % line
      if line.startswith('WARNING'):
        yield YELLOW % line
      if line.startswith('ERROR'):
        yield RED % line

def tail_serve(filepath,outfile):
  # Pipeline:
  with open(filepath,'r') as logfile:
    loglines = follow(logfile)
    colorlines = htmlcolor(loglines)
    with open(outfile,'w') as f:
      for line in colorlines:
        f.write(line)
        f.flush()
  
if __name__ == "__main__":
  # serve('access.log','colored.log')
  try:
    parser = argparse.ArgumentParser(description='A colorized version of \'tail -f\'')
    parser.add_argument('filepath', metavar='file', type=str,
                       help='The file to tail.')
    parser.add_argument('-o','--outfile', metavar='file', type=str, required=False,
                       help='If specified, writes tagged HTML to outfile, ready for serving.')
    args = parser.parse_args()
    
    if args.outfile:
      tail_serve(args.filepath,args.outfile)
    else:
      tail_print(args.filepath)
    
  except KeyboardInterrupt:
    # Hush... Cleanup please:
    print '\033[0m'
    pass
