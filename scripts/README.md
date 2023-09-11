Here, you can find the scripts used for benchmarking domain annotation by selecting the closest domain instance structure. 

The description of the files is as follows:


1- `../aln_Tb_pf_gr_fmt.tsv`: Alignment of _T. brucei_ against PfamSDB using Foldseek and selecting the highest-scoring non-overlapping hits. 

2- `../aln_Tb_pf_gr_seq_fmt.tsv`: Alignment of _T. brucei_ against PfamSDB using MMseqs2 and selecting the highest-scoring non-overlapping hits

3- `../HmmerGreedyHits.tsv`: Top HMMER hits for _T. brucei_ proteins. It can be computed from "../TbHmmer.domtbl" file and running the PrepareHMMERoutput notebook

4- `../PfamClanAssociation.tsv`: Shows the clan of each Pfam. If a Pfam does not belong to a clan, the ID of the Pfam is shown

5- `../PfamTb_SeedMeanlddtSize.txt`: Domains predicted by Pfam + some other information such as the avg_pLDDT of each domain

6- `../PfamTb_SeedMeanlddtSize.txt`: Domains predicted by Pfam-N + some other information such as the avg_pLDDT of each domain

7- `../plddt_pfamseeds.json`: pLDDT of residues of each Pfam seed

8- `../Tb_plddt.json`: pLDDT of residues of each protein of _T. brucei_

9- `../SharedTb_Pf_MM_FS.tsv`: The hits shared between Foldseek and MMseqs2 along with their alignment statistics

10- `../ProbOfTP_FPs_ovLim_bits_summary.csv`: The number of TPs and FPs for bitscore threshold reported by Foldseek

11- `../ProbOfTP_FPs_ovLim_bits_summary_seq.csv`: The number of TPs and FPs for bitscore threshold reported by MMseqs2

12- `../ProbOfTP_FPs_ovLim_prob_summary.csv`: The number of TPs and FPs for probability threshold reported by Foldseek

