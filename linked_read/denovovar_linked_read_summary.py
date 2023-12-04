
# Summarize the concordant and disconcordant reads of each denovo variant

# import the table of concordant or disconcordant reads
linked_fi = open("somatic_dat_no_filter.txt", "r")
linked_fi.readline()

mut_dict = {}	# mutation_site: concordant reads and disconcordant reads

for linked_line in linked_fi:
	linked_info = linked_line.strip('\n').split('\t')
	mut = linked_info[1]
	composite_coverage = min(int(linked_info[2]), int(linked_info[3]))
	concordant_reads = int(linked_info[3])
	disconcordant_reads = int(linked_info[4])
	if mut in mut_dict:
		if composite_coverage > mut_dict[mut]["coverage"]:
			mut_dict[mut]["concordant"] = concordant_reads
			mut_dict[mut]["disconcordant"] = disconcordant_reads
			mut_dict[mut]["coverage"] = composite_coverage
		else:
			continue
	else:
		mut_dict[mut] = {"concordant": concordant_reads, "disconcordant": disconcordant_reads, "coverage": composite_coverage}
linked_fi.close()

print(len(mut_dict))

# import denovo variants vcf
# with 2-split filter
vcf_file = open("denovo.2x.vcf", "r")
n = 0
fo = open("2x_damage_linked_read_table.bed", "w")
for vcf_line in vcf_file:
	if vcf_line[0] == '#':
		continue
	else:
		mut_info = vcf_line.strip('\n').split('\t')
		mut = mut_info[0] + ';' + mut_info[1] + ';' + mut_info[3] + ';' + mut_info[4]		
		if mut in mut_dict:
			n += 1
			fo.write(mut_info[0]+ '\t' + str(int(mut_info[1])-1) + '\t' + mut_info[1] + '\t' + str(mut_dict[mut]['concordant']) + '\t' + str(mut_dict[mut]['disconcordant']) + '\n')

fo.close()
vcf_file.close()

print(n)




