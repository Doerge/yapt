#!/usr/bin/env python
import time
import threading
import random

def test_thread():
  tags = ['INFO','WARNING','ERROR']
  while True:
    with open('access.log','a') as f:
      f.write(random.choice(tags)+': Some comment. Yada, yada, something.Yada, yada, something.Yada, yada, something.Yada, yada, something.Yada, yada, something.Yada, yada, something.Yada, yada, something.\n')
      time.sleep(2)

if __name__ == "__main__":
  t = threading.Thread(target=test_thread())
  t.start()
