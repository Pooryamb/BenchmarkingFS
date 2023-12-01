import pandas as pd
from FS_header import FS_header
from get_nonov_hits import get_nonov_hits
import sys


inpath = sys.argv[1]
outpath = sys.argv[2]


alidf = pd.read_csv(inpath, sep="\t", header=None, names = FS_header)
alidf["bits__alnlen"] = alidf["bits"]/alidf["alnlen"]

alidf = alidf.sort_values(by=["query", "bits__alnlen"], ascending = [True, False]).reset_index(drop=True)

best_hits = get_nonov_hits(alidf)
best_hits.to_csv(outpath, sep="\t", index=None)
