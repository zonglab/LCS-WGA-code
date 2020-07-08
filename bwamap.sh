#!/bin/bash


bwa mem -M -t 12 /data1/ref/hg19/hg19.fa $seqdir/${sample}_${SN}_R1.fastq.gz $seqdir/${sample}_${SN}_R2.fastq.gz | samtools view -bS - > $datadir/${sample}_${SN}.bam

samtools fixmate -m -@ 12 -O bam $datadir/${sample}_${SN}.bam $datadir/${sample}_${SN}.fixmate.bam

if [ -f ${sample}_${SN}.fixmate.bam ]; then
   rm -rf ${sample}_${SN}.bam
fi

samtools sort -@ 12 ${sample}_${SN}.fixmate.bam -o ${sample}_${SN}.fixmate.sorted.bam -T /data1/tmp/


if [ -f ${sample}_${SN}.fixmate.sorted.bam ]; then
   rm -rf ${sample}_${SN}.fixmate.bam
fi

samtools markdup -@ 12  ${sample}_${SN}.fixmate.sorted.bam ${sample}_${SN}.fixmate.markdup.bam

samtools index -@ 12  ${sample}_${SN}.fixmate.markdup.bam

if [ -f ${sample}_${SN}.fixmate.markdup.bam ]; then
   rm -rf ${sample}_${SN}.fixmate.sorted.bam
fi

