#!/usr/bin/python

import os
import subprocess
import sys

def main():
  if len(sys.argv) != 2:
    print("usage: %s hdfsRootPath" % (sys.argv[0]))
    exit(1)

  hdfsRootPath = sys.argv[1].rstrip('/')
  
  hdfsRootDirName = os.path.basename(hdfsRootPath)
  hdfsRootParentDirPath = os.path.dirname(hdfsRootPath)
  
  hdfsLsrCmd = "hdfs dfs -ls -R \"%s\" | awk '{ print $1 \"|\" $8 }'" % (hdfsRootPath)

  print("Running recursive list cmd: %s" % (hdfsLsrCmd))

  outLines = runCmd(hdfsLsrCmd)
  
  for outLine in outLines:
    splitted = outLine.split('|')
    hdfsItemMode = splitted[0]
    hdfsItemPath = splitted[1]

    localHdfsItemPath = hdfsItemPath.replace(hdfsRootParentDirPath + "/", "")

    isDir = hdfsItemMode[0] == 'd'

    if isDir:
      runCmd("mkdir -p \"%s\"" % (localHdfsItemPath))
    else:
      localHdfsItemDirPath = os.path.dirname(localHdfsItemPath)
      runCmd("mkdir -p \"%s\"" % (localHdfsItemDirPath))
      runCmd("touch \"%s\"" % (localHdfsItemPath))


def runCmd(cmd):
  p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  outLines = list(map(lambda l: l.strip(), p.stdout.readlines()))
  p.wait()
  
  return outLines


if __name__ == "__main__":
  main()
