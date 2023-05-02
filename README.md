# readcount

A pipeline for counting read depth of targeted genes using python scripts.

### Steps in this pipeline

-  Searching database of probe sequences using genome sequence as queries to obtain BED and GFF files. 
- Extracting gff files of genes captured by probes.
- Obtaining DNA and protein sequences of captured genes for functional annotation using [BlastKOALA](https://www.kegg.jp/blastkoala/) (annotation is not included in this pipeline).
- Extracting BAM file of captured genes and obtaining statistics using NanoPlot.
- Calculating total base count and the number of reads mapping to the targeted genes

### Required file for each step
1. blast_to_bed_and_gff.py
- Probe sequences (FASTA format).
- Genome sequence (FASTA format).
2. extract_genes.py
- BED file generated from step1 (bed_output.bed)
-Genome annotation features (.gff).
3. extract_seqs.py
- Annotation features of captured genes generated from step2 (overlapped_gene).
- Coding sequences (FASTA format).
4. extract_overlapping_reads_and_stats.py
- BAM file generated from mapping filtered reads to genome.
- BED file generated from step1 (bed_output.bed).
5. read_count_by_gene.py
- Annotation features of captured genes generated from step2 (overlapped_gene).
- BAM file generated from mapping filtered reads to genome.

Citing
The research paper is under review. Please cite this pipeline as zenodo record:
>
