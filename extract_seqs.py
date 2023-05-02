###########################################
# Author: Jose Huguet-Tapia               #
# Email: jhuguet@ufl.edu                  #
# Last modified: 2023/04/27; Pei-Ling Yu  #
###########################################

import os
from Bio import SeqIO
from Bio.Seq import Seq

# Input file containing gene IDs in the 9th column
input_file = "overlapped_gene"

# DNA FASTA file
dna_fasta_file = "cds_from_genomic.fna"

# Initialize list to store modified gene IDs
gene_ids = []

# Open input file and extract gene IDs
with open(input_file, "r") as f:
    for line in f:
        cols = line.strip().split("\t")
        gene_id = cols[8].replace("ID=", "")
        gene_prefix = cols[0]
        modified_gene_id = gene_prefix + "." + gene_id + ".t1"
        gene_ids.append(modified_gene_id)

# Use SeqIO to extract DNA sequences
dna_records = SeqIO.parse(dna_fasta_file, "fasta")
dna_records_out = []
for record in dna_records:
    if record.id in gene_ids:
        dna_record_out = record
        dna_record_out.id = dna_record_out.id + ".dna"
        dna_record_out.description = dna_record_out.description + " DNA sequence"
        dna_records_out.append(dna_record_out)

# Write DNA sequences to new FASTA file
dna_fasta_file_out = "dna_out.fasta"
SeqIO.write(dna_records_out, dna_fasta_file_out, "fasta")

# Translate DNA sequences and write to new FASTA file
translated_records_out = []
for record in dna_records_out:
    dna_seq = record.seq
    protein_seq = dna_seq.translate()
    protein_record_out = record
    protein_record_out.seq = protein_seq
    protein_record_out.id = protein_record_out.id + ".translated"
    protein_record_out.description = protein_record_out.description + " translated sequence"
    translated_records_out.append(protein_record_out)

protein_fasta_file_out = "protein_out.fasta"
SeqIO.write(translated_records_out, protein_fasta_file_out, "fasta")
