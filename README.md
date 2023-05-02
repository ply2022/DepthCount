# depthcount

A pipeline for counting read depth of targeted genes using python scripts.

### Steps in this pipeline

-  Searching database of probe sequences using genome sequence as queries to obtain BED and GFF files. 
- Extracting gff files of genes captured by probes.
- Obtaining DNA and protein sequences of captured genes for functional annotation (BlastKOALA).
- Extracting BAM file of captured genes and obtaining statistics using NanoPlot.
- Calculating total base count and the number of reads mapping to the targeted genes



