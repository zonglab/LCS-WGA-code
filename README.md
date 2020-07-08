# MACSBA-codes

Custom codes for analyzing MACSBA sequencing data

--- Linear-Splitting Single-Cell Whole Genome Amplification Unveils Low Accumulation Rate of Somatic Mutations along with Aging in Human Cortical Neurons 

Qiangyuan Zhu1*, Yichi Niu1*, Michael Gundry1, Muchun Niu1, Chenghang Zong1,2,3#

Affiliations:
1Department of Molecular and Human Genetics,
2Cancer and Cell Biology Program,
2Dan L Duncan Comprehensive Cancer Center,
3McNair Medical Institute,
Baylor College of Medicine,
One Baylor Plaza, Houston, Texas, 77030
*These authors contributed equally to this work
#Corresponding Author: Chenghang Zong, (chenghang.zong@bcm.edu)


Alignment bash script: bwamap.sh

Variant calling and damSNV analysis bash script:denovoparser.sh 

Python codes: 

gtbulksearch.py -- used for removing germline mutations in bulk sample

localseqfilter.py  -- used for removing the variants in the sequence with significant portion of one type of nucleotide such as polyA, polyT, polyG or polyC

tripletfilter3x.py -- used for estimating de novo mutations




