#!/bin/bash
# set max wallclock time
#PBS -l walltime=72:00:00
# set name of job
#PBS -N pbs.xxxx


x1=$datadir/Split1.RG.markdup.bam
x2=$datadir/Split2.RG.markdup.bam
x3=$datadir/Split3.RG.markdup.bam


bulkfile=$datadir/bulk.fixmate.nodup.bam
indeldir==$datadir/indel/


cn=${NUM}

#GATK variant calling
java -Xmx16g -jar /data1/opt/GenomeAnalysisTK3.8.jar  -R  /data1/ref/hg19/hg19.fa  -T HaplotypeCaller -I $x1 -I $x2 -I $x3 -L /data1/zonglab/intervals/intervals.${cn}.list -o output.${cn}.vcf -mmq 50 -mbq 20 -ploidy 10 -filterNoBases -drf DuplicateRead

#GATK SNP data
java -Xmx4g -jar /data1/opt/GenomeAnalysisTK3.8.jar -T SelectVariants -R /data1/ref/hg19/hg19.fa -V output.${cn}.vcf -selectType SNP -o  snp.${cn}.vcf

#select the variants detected in two or three splits

tripletfilter2x.py snp.${cn}.vcf $x1 $x2 $x3 > malps2x.${cn}.vcf

# filter out variants in tandem, close to centromere and telomere regions and indel loci called based on bulk sequencing data. 
bedtools intersect -a malps2x.${cn}.vcf  -b /ref/hg19_tandem.bed -v > ${cn}.notandem.vcf
bedtools intersect -a ${cn}.notandem.vcf  -b /ref/cento.bed -v > ${cn}.cleanend.vcf
bedtools intersect -a ${cn}.cleanend.vcf  -b ${indeldir}/indel.total.bed  -v > ${cn}.highconf.vcf

python /data1/zonglab/scripts/gtbulksearch.py ${cn}.highconf.vcf $bulkfile 0 > ${cn}.bulkflt.vcf

# annotate the de novo variants
java -jar /data1/opt/snpEff/SnpSift.jar annotate /data1/ref/dbSNP/All_20151104.vcf ${cn}.bulkflt.vcf  > ${cn}.sifted.vcf

# filter out the de novo variants that are common variants
grep -v rs ${cn}.sifted.vcf | grep -v "^#" > denovo.${cn}.anno.vcf

# filter out the de novo variants in the sequence with significant portion of one type of nucleotide such as polyA, polyT, polyG or polyC.
cat denovo.${cn}.anno.vcf | awk '{print $1"\t"$2-10"\t"$2+10}' > denovo.${cn}.localseq.bed
seqtk subseq /data1/ref/hg19/hg19.fa   denovo.${cn}.localseq.bed -t  > denovo.${cn}.localseq.txt
python /data1/zonglab/scripts/localseqfilter.py denovo.${cn}.anno.vcf denovo.${cn}.localseq.txt  > denovovar.${cn}.anno.vcf


