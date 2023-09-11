# Benchmarking Pfam Domain Annotation by Selecting the Closest Domain Instance Structure

This repository contains the scripts used to benchmark structure-based domain annotation. Domains are predicted by searching the query proteins against the database of the structure of domain instances and attributing the Pfam family of the highest-scoring instances to the query proteins. This Notebook benchmarks the predictions considering Pfam v35.0 and Pfam-N as the gold standard.

Jupyter Notebooks can be found in the `scripts` directory. Information about the files used by workflow can be found in the `README.md` file inside the scripts directory.

Before running the Jupyter notebooks, make sure to download the necessary raw files. You can do so with the following commands:

```
wget https://zenodo.org/record/8335990/files/BenchmarkingPfamSDB.tar.gz
tar -xf BenchmarkingPfamSDB.tar.gz
```
