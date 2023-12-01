import pandas as pd

def overlap(range1, range2):
    maxstart = max(range1[0], range2[0])
    minend   = min(range1[1], range2[1])
    return minend - maxstart

def get_nonov_hits(df, id_col="query",  startcol="qstart", endcol="qend"):
    last_q = ''
    all_selected_hits = []
    query_hits = []
    for index,row in df.iterrows():
        if row[id_col] != last_q:
            all_selected_hits = all_selected_hits + query_hits
            query_hits = [row]
        else:
            is_ov = False
            for hit in query_hits:
                ov = overlap((row[startcol], row[endcol]), (hit[startcol], hit[endcol]))
                if ov >=0 :
                    is_ov = True
                    break
            if not(is_ov):
                query_hits.append(row)
        last_q = row[id_col]
    all_selected_hits = all_selected_hits + query_hits
    return pd.DataFrame(all_selected_hits)
