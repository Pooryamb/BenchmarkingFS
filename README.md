# Benchmarking Pfam Domain Annotation by Selecting the Closest Domain Instance Structure

This repository holds scripts for benchmarking the structure-based domain annotation approach. Domains are predicted by aligning query proteins against a database comprised of domain instance structures and assigning the Pfam family of the top-scoring instances to the queries. The alignment are generated using the following commands:

For Foldseek:
```
foldseek easy-search $QueryProteins $TargetDatabasePath aln_Tb_pf_gr.tsv tmp --max-seqs 1000000 -e 0.001 \
--format-output "query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,qlen,tlen,evalue,bits,alntmscore,lddt,prob,tcov" --greedy-best-hits
```
For MMseqs2:
```
mmseqs easy-search $QueryProteins $TargetDatabasePath aln_Tb_pf_gr_seq.tsv tmp --max-seqs 1000000 -e 0.001 \
--format-output "query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,qlen,tlen,evalue,bits,tcov" --greedy-best-hits
```
The output files were parsed to remove the file extensions and prefixes and to add the header to the table of hits.
Predictions are benchmarked against Pfam v35.0 and Pfam-N as gold standards.

Jupyter Notebooks used for benchmarking can be found in the `scripts` directory. Information about the files used by workflow can be found in the `README.md` file inside the scripts directory.

Before running the Jupyter notebooks, make sure to download the necessary raw files. You can do so with the following commands:

```
wget https://zenodo.org/records/10246816/files/BenchmarkingPfamSDB.tar.gz
tar -xf BenchmarkingPfamSDB.tar.gz
```

