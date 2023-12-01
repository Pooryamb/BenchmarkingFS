import sys
import tarfile
import io
from io import StringIO
import glob
import gzip
import os


tarFileName = sys.argv[1]
outFileName = sys.argv[2]

def ReturnPlldt(filelines):
    lastAAind = 0
    BfacList = []
    for line in filelines:
        if not(line.startswith("ATOM")):
            continue
        AAind = int(line[22:26])
        Bfac = float(line[60:66])
        if AAind != lastAAind:
            BfacList.append(Bfac)
        lastAAind = AAind
    return BfacList


ReportFile = open(outFileName,"w")

tfile = tarfile.open(tarFileName, 'r|')
ReportFile.write("{\n")
for i,t in enumerate(tfile):
    gzFile = tfile.extractfile(t)
    f = gzip.open(gzFile, 'rt')
    SeedID = t.get_info()['name'].replace(".pdb.gz", '')  #####adjust it
    fileLines = f.read().split("\n")
    LDDT = ReturnPlldt(fileLines)
    if i!=0:
        ReportFile.write(",")
    ReportFile.write("\"" + SeedID + "\":" + str(LDDT) + "\n")
ReportFile.write("}\n")

tfile.close()

ReportFile.close()
