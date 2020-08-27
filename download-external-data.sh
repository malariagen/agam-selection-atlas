#!/bin/bash

set -xeu

# remember working directory
wd=$(pwd)

# retrieve genome and geneset
cd $wd
vb_dir=data/external/vectorbase
mkdir -pv $vb_dir
cd $vb_dir
wget --no-clobber -O Anopheles-gambiae-PEST_CHROMOSOMES_AgamP4.fa.gz https://www.vectorbase.org/download/anopheles-gambiae-pestchromosomesagamp4fagz
gunzip --keep --force Anopheles-gambiae-PEST_CHROMOSOMES_AgamP4.fa.gz
wget --no-clobber -O Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.12.gff3.gz https://www.vectorbase.org/download/anopheles-gambiae-pestbasefeaturesagamp412gff3gz
gunzip --keep --force Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.12.gff3.gz

# retrieve Ag1000G phase 2 sample metadata
cd $wd
samples_dir=data/external/ag1000g/phase2/AR1/samples
mkdir -pv $samples_dir
cd $samples_dir
wget --no-clobber ftp://ngs.sanger.ac.uk/production/ag1000g/phase2/AR1/samples/samples.meta.txt

# retrieve Ag1000G phase 2 recombination maps
cd $wd
recomb_dir=data/external/ag1000g/phase2/AR1/recombination_maps
mkdir -pv $recomb_dir
cd $recomb_dir
for chrom in 2L 2R 3L 3R X;
do
    wget --no-clobber ftp://ngs.sanger.ac.uk/production/ag1000g/phase2/AR1/recombination_maps/Ag_${chrom}.map
done

# retrieve Ag1000G phase 2 haplotype data
cd $wd
haplotypes_dir=data/external/ag1000g/phase2/AR1/haplotypes/main
mkdir -pv $haplotypes_dir
cd $haplotypes_dir
wget --no-clobber ftp://ngs.sanger.ac.uk/production/ag1000g/phase2/AR1/haplotypes/main/haplotypes.autosomes.meta.txt
wget --no-clobber ftp://ngs.sanger.ac.uk/production/ag1000g/phase2/AR1/haplotypes/main/haplotypes.X.meta.txt
mkdir -pv zarr
cd zarr
for file in ag1000g.phase2.ar1.haplotypes.metadata.zip \
            ag1000g.phase2.ar1.haplotypes.X.variants.zip \
            ag1000g.phase2.ar1.haplotypes.X.calldata.GT.zip \
            ag1000g.phase2.ar1.haplotypes.2L.variants.zip \
            ag1000g.phase2.ar1.haplotypes.2L.calldata.GT.zip \
            ag1000g.phase2.ar1.haplotypes.2R.variants.zip \
            ag1000g.phase2.ar1.haplotypes.2R.calldata.GT.zip \
            ag1000g.phase2.ar1.haplotypes.3L.variants.zip \
            ag1000g.phase2.ar1.haplotypes.3L.calldata.GT.zip \
            ag1000g.phase2.ar1.haplotypes.3R.variants.zip \
            ag1000g.phase2.ar1.haplotypes.3R.calldata.GT.zip;
do
    wget --no-clobber ftp://ngs.sanger.ac.uk/production/ag1000g/phase2/AR1/haplotypes/main/zarr/$file
    unzip -u $file
done

# retrieve Ag1000G phase 2 unphased SNP data
cd $wd
variation_dir=data/external/ag1000g/phase2/AR1/variation/main/zarr/pass
mkdir -pv $variation_dir
cd $variation_dir
for file in ag1000g.phase2.ar1.pass.metadata.zip \
            ag1000g.phase2.ar1.pass.X.variants.zip \
            ag1000g.phase2.ar1.pass.X.calldata.GT.zip \
            ag1000g.phase2.ar1.pass.2L.variants.zip \
            ag1000g.phase2.ar1.pass.2L.calldata.GT.zip \
            ag1000g.phase2.ar1.pass.2R.variants.zip \
            ag1000g.phase2.ar1.pass.2R.calldata.GT.zip \
            ag1000g.phase2.ar1.pass.3L.variants.zip \
            ag1000g.phase2.ar1.pass.3L.calldata.GT.zip \
            ag1000g.phase2.ar1.pass.3R.variants.zip \
            ag1000g.phase2.ar1.pass.3R.calldata.GT.zip;
do
    wget --no-clobber ftp://ngs.sanger.ac.uk/production/ag1000g/phase2/AR1/variation/main/zarr/pass/$file
    unzip -u $file
done

