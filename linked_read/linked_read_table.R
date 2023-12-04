args <- commandArgs(trailingOnly = TRUE)
chr_list = 1:22
chr_list = c(chr_list, 'X')
analysis_path = args[1]

somatic_mat = c()
for(i in chr_list){
  chromosome = paste("chr", i, sep='')
  print(chromosome)
  path = paste(analysis_path, chromosome, '/compare', sep='')
  setwd(path)
  load('data.originBulk.rda')

  somatic_data = data[which(data$type == 'somatic'), ]
  somatic_data = cbind(ID=rownames(somatic_data), somatic_data)
  somatic_mat = rbind(somatic_mat, somatic_data)
}

dim(somatic_mat)
output_path = args[2]
setwd(output_path)
write.table(somatic_mat, 'somatic_dat_no_filter.txt', col.names=T, row.names=F, sep='\t', quote=F)
