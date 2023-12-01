Here, you can find the scripts used for benchmarking domain annotation by selecting the closest domain instance structure. 

The description of the files is as follows:


1- `../greedy_hits`: The highest-scoring non-overlapping hits from the alignment of _T. brucei_ against PfamSDB using Foldseek or MMseqs2.   

2- `../PfamClanAssociation.tsv`: Shows the clan of each Pfam. If a Pfam does not belong to a clan, the ID of the Pfam is shown

3- `../PfamTb_SeedMeanlddtSize.txt`: Domains predicted by Pfam + some other information such as the avg_pLDDT of each domain

4- `../PfamTb_SeedMeanlddtSize.txt`: Domains predicted by Pfam-N + some other information such as the avg_pLDDT of each domain

5- `../plddt_pfamseeds.json`: pLDDT of residues of each Pfam seed

6- `../Tb_plddt.json`: pLDDT of residues of each protein of _T. brucei_

7- `../PrecisionRecallData`: The number of TPs and FPs for each scoring criteria threshold.

