###########################################
# Author: Jose Huguet-Tapia               #
# Email: jhuguet@ufl.edu                  #
# Last modified: 2023/04/27; Pei-Ling Yu  #
###########################################

bed_file = "bed_output.bed"
gff_file = "genomic.gff"
output_file = "overlapped_gene"

bed_regions = []
with open(bed_file, "r") as f:
    for line in f:
        fields = line.strip().split("\t")
        bed_regions.append((fields[0], int(fields[1]), int(fields[2])))

seen_genes = set()
with open(gff_file, "r") as f:
    with open(output_file, "w") as out:
        for line in f:
            if line.startswith("#") or "\tgene\t" not in line:
                continue
            fields = line.strip().split("\t")
            if len(fields) != 9:
                continue
            chr_name = fields[0]
            start = int(fields[3])
            end = int(fields[4])
            for bed_region in bed_regions:
                if chr_name == bed_region[0] and start <= bed_region[2] and end >= bed_region[1]:
                    gene_id = fields[8].split(";")[0].replace("ID=", "")
                    if gene_id not in seen_genes:
                        seen_genes.add(gene_id)
                        out.write(line)