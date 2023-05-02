###########################################
# Author: Jose Huguet-Tapia               #
# Email: jhuguet@ufl.edu                  #
# Last modified: 2023/04/27; Pei-Ling Yu  #
###########################################

import subprocess

# Set blast parameters
blastn_path = "blastn"
subject_file = "FASTA_file" # probe sequenes
query_file = "FASTA_fille" # genome sequence
outfmt = 6
word_size = 11

# Set output file names
blast_output_file = "blast_output.txt"
filtered_output_file = "filtered_output.txt"
bed_output_file = "bed_output.bed"
gff_output_file = "gff_output.gff"

# Run blast command and save output to file
blast_command = [blastn_path, "-subject", subject_file, "-query", query_file, "-outfmt", str(outfmt), "-word_size", str(word_size)]
with open(blast_output_file, "w") as f:
    subprocess.run(blast_command, stdout=f, check=True)

# Filter blast output using awk and save filtered output to file
awk_command = f"awk '{{ if($4 >= 102 && $3 >= 85) {{ print }} }}' {blast_output_file} > {filtered_output_file}"
subprocess.run(awk_command, shell=True, check=True)

# Parse filtered output and save to bed file and gff file
with open(filtered_output_file, "r") as f, open(bed_output_file, "w") as bed, open(gff_output_file, "w") as gff:
    for line in f:
        fields = line.strip().split("\t")
        query_name = fields[0]
        subject_name = fields[1]
        start = int(fields[6])
        end = int(fields[7])
        if start > end:
            start, end = end, start
        # Write to BED file
        bed.write(f"{query_name}\t{start}\t{end}\n")
        # Write to GFF file
        gff.write(f"{query_name}\tblastn\tmisc_feature\t{start}\t{end}\t.\t.\t.\tID={subject_name}\n")
