import subprocess

# Script 1:
print("Running Script 1: blast_bed_and_gff")
subprocess.call(["python", "blast_and_bed_and_gff.py"])

# Script 2
print("Running Script 2: extracting genes captured by probes")
subprocess.call(["python", "extract_genes.py"])

# Script 3
print("Running Script 3: getting DNA and aa sequences of captured genes")
subprocess.call(["python", "extract_seqs.py"])

# Script 4
print("Running Script 4: Reads on targets - covering by the probes")
subprocess.call(["python", "extract_overlapping_reads_and_stats.py"])

# Script 5
print("Running Script 5: calculating read count by gene")
subprocess.call(["python", "read_count_by_gene.py"])
