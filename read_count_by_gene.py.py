###########################################
# Author: Jose Huguet-Tapia               #
# Email: jhuguet@ufl.edu                  #
# Last modified: 2023/04/27; Pei-Ling Yu  #
###########################################

import subprocess
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
