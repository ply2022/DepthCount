###########################################
# Author: Jose Huguet-Tapia               #
# Email: jhuguet@ufl.edu                  #
# Last modified: 2023/05/02; Pei-Ling Yu  #
###########################################
import subprocess
import pandas as pd

# Define input and ouput files
input_file = "overlapped_gene" 
input_bam = "BAM_file"
sorted_bed = "sorted.bed"
output_bed = "output.bed"  
cov_output = "coverage.txt" 
 
# Extract the relevant columns from the input file and write to the output BED file
with open(input_file, 'r') as f_in, open(output_bed, 'w') as f_out:
    for line in f_in:
        cols = line.strip().split('\t')
        out_line = '\t'.join([cols[0], cols[3], cols[4], cols[8]]) + '\n'
        f_out.write(out_line)

# Calculate coverage of each region using samtools bedcov
subprocess.run(["samtools", "-c","bedcov", sorted_bed, input_bam], stdout=open(cov_output, 'w'), check=True)

# Read the coverage.txt file into a pandas dataframe
coverage = pd.read_csv('coverage.txt', sep='\t', header=None)

# Calculate the enrichment factor
genome_size = <Define genome size>
coverage['Enrichment'] = (coverage[4] / coverage[5]) / ((coverage[2] - coverage[1]) / genome_size)

# Write the updated dataframe to a new coverage file with the enrichment factor
coverage.to_csv('coverage_enrichment.txt', sep='\t', index=False, header=False)

