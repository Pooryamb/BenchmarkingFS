import pandas as pd
import warnings
warnings.filterwarnings('ignore')

Coverage_Of_PfamChoppedStruct = 0
Coverage_Of_PfamOnQueryPosThresh = 0.25
FalsePositiveThreshold = 0.25

def FindOverlap(df, region1names, region2names):
    """This is for finding the overlapped part of region2 covered in the 
    overlapped region. Please note that the region we want to find its 
    coverage, should be the second argument"""
    cov1, cov2 = region2names
    tmpdf = pd.DataFrame()
    tmpdf["MaxStart"] = df[[region1names[0], region2names[0]]].max(axis=1)
    tmpdf["MinEnd"] = df[[region1names[1], region2names[1]]].min(axis=1)
    tmpdf["covered"] = (tmpdf["MinEnd"] - tmpdf["MaxStart"] +1)/(df[cov2] - df[cov1] + 1)
    return tmpdf["covered"]


def LabelAlis(AlnDf,PfDf, pfClans,StartEndColumns, how2merge):
    """The input of the function is the alignment that have passed through the FindSeedAnns function
    and it returns the labeled alignments that are not used as seeds"""
    AlnDf = AlnDf[AlnDf["tcov"] >= Coverage_Of_PfamChoppedStruct]
    prefix = "pfam"
    AlnPfDf = AlnDf.merge(PfDf, on = "query", how = how2merge)

    AlnPfDf[ prefix + "cov"] = FindOverlap(AlnPfDf, StartEndColumns, PfDf.columns[2:4])

    AlnPfDf = AlnPfDf.merge(pfClans, left_on = prefix, right_on = "pf", how="left").drop("pf", axis=1).rename(columns={"clan":prefix+"clan"})

#******************************************************************
    
    if how2merge=="right":
        defaultvalue = -1
    else:
        defaultvalue = -1
        
    AlnPfDf["equalto"+ prefix + "preds"] = defaultvalue
    TruePosInds = (AlnPfDf["predpf"] == AlnPfDf[prefix]) & (AlnPfDf[prefix+"cov"] >= Coverage_Of_PfamOnQueryPosThresh)    
    AlnPfDf["equalto"+ prefix + "preds"][TruePosInds] = 1
    
    FalsePosInds = (AlnPfDf["predpf"] != AlnPfDf[prefix]) & (AlnPfDf[prefix+"cov"] >= FalsePositiveThreshold)    
    AlnPfDf["equalto"+ prefix + "preds"][FalsePosInds] = 0
    if how2merge=="right":
        AlnPfDf.loc[pd.isnull(AlnPfDf["target"]),"equalto"+ prefix + "preds" ] = defaultvalue
    else:
        AlnPfDf.loc[pd.isnull(AlnPfDf[prefix]),"equalto"+ prefix + "preds" ] = defaultvalue
#******************************************************************

    AlnPfDf[prefix+ "clanisidentical"] = defaultvalue
    FalsePosInds = (AlnPfDf["predclan"] != AlnPfDf[prefix + "clan"]) & (AlnPfDf[prefix+"cov"] >= FalsePositiveThreshold)    
    AlnPfDf[prefix+ "clanisidentical"][FalsePosInds] = 0
    
    TruePosInds = (AlnPfDf["predclan"] == AlnPfDf[prefix + "clan"]) & (AlnPfDf[prefix+"cov"] >= Coverage_Of_PfamOnQueryPosThresh)    
    AlnPfDf[prefix+ "clanisidentical"][TruePosInds] = 1
    if how2merge=="right":
        AlnPfDf.loc[pd.isnull(AlnPfDf["target"]),prefix+ "clanisidentical" ] = defaultvalue
    else:
        AlnPfDf.loc[pd.isnull(AlnPfDf[prefix]),"equalto"+ prefix + "preds" ] = defaultvalue

#******************************************************************
    if how2merge=="right":
        AlnPfDf = AlnPfDf.sort_values(by = ["equalto"+ prefix + "preds", prefix+ "clanisidentical"], ascending=False).drop_duplicates(PfDf.columns)
    else:
        AlnPfDf = AlnPfDf.sort_values(by = ["equalto"+ prefix + "preds", prefix+ "clanisidentical"], ascending=False).drop_duplicates(AlnDf.columns)

    AlnPfDf.reset_index(inplace=True, drop=True)

    return AlnPfDf
