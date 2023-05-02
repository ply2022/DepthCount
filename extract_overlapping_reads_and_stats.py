###########################################
# Author: Jose Huguet-Tapia               #
# Email: jhuguet@ufl.edu                  #
# Last modified: 2023/04/27; Pei-Ling Yu  #
###########################################

import subprocess

# Define input and output file names
input_bam = "BAM_file" # BAM file generated from mapping filtered reads to genome
input_bed = "bed_output.bed"
output_bam = "output.bam"
nanoplot_output_bam = "nanoplot_output_bam"
sorted_bed = "sorted.bed"

# Intersect the sorted BAM file with the BED file and exclude reads with duplicate IDs
subprocess.run(f"samtools index {input_bam}", shell=True)
subprocess.run(f"sortBed -i {input_bed} > {sorted_bed}",shell=True)
subprocess.run(f"bedtools intersect -abam {input_bam} -b {input_bed} -u > {output_bam}", shell=True)
subprocess.run(f"samtools index {output_bam}", shell=True)

# Use Nanoplot to generate statistics from the output FASTQ file
subprocess.run(f"NanoPlot --bam {output_bam} -o {nanoplot_output_bam}", shell=True)
