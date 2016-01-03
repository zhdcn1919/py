#!/system/sbin/env python
import os.path, time
import exceptions

class TypeError (Exception):
    pass

if __name__ == '__main__':
  if (len(os.sys.argv) < 1):
      raise TypeError()
  else:
      print "os.sys.argv[0]: %s" % os.sys.argv[0] # os.sys.argv[0] is the current file, in this case, file_ctime.py
  f = os.sys.argv[0]
  mtime = time.ctime(os.path.getmtime(f))
  ctime = time.ctime(os.path.getctime(f))
  print "Last modified : %s, last created time: %s" % (mtime, ctime)
