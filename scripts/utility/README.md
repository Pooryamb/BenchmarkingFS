Here, you can find the scripts used for the analysis of the benchmarking of the Foldseek alignments:


To select the highest-scoring non-overlapping hits based on bits/alnlen, use the following script:

```
python get_highest_bits__alnlen.py path_to_raw_alignments output_file_path
```

To get the B-factor for the gzipped PDB files in a Tar file in a json format, use the following command:
```
GetBFactors.py path_to_tar_file path_to_output
```
