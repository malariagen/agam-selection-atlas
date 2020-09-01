#!/bin/bash

set -xeu

function download {
    # convenience function to download a file using wget
    # positional arguments:
    # $1 - URL to download
    # $2 (optional) - file name to save to

    if [ $# -eq 2 ]; then
        wget -c -O $2 $1
    elif [ $# -eq 1 ]; then
        wget -c $1
    fi
}

# remember working directory
wd=$(pwd)

# retrieve genome and geneset
cd $wd
vb_dir=data/external/vectorbase
mkdir -pv $vb_dir
cd $vb_dir
# TODO vectorbase.org appears down, maybe upgrading, need to update when fixed
# download https://www.vectorbase.org/download/anopheles-gambiae-pestchromosomesagamp4fagz Anopheles-gambiae-PEST_CHROMOSOMES_AgamP4.fa.gz
# gunzip --keep --force Anopheles-gambiae-PEST_CHROMOSOMES_AgamP4.fa.gz
# download https://www.vectorbase.org/download/anopheles-gambiae-pestbasefeaturesagamp412gff3gz Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.12.gff3.gz
# gunzip --keep --force Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.12.gff3.gz

# retrieve Ag1000G phase 2 sample metadata
cd $wd
samples_dir=data/external/ag1000g/phase2/AR1/samples
mkdir -pv $samples_dir
cd $samples_dir
download ftp://ngs.sanger.ac.uk/production/ag1000g/phase2/AR1/samples/samples.meta.txt

# retrieve Ag1000G phase 2 recombination maps
cd $wd
recomb_dir=data/external/ag1000g/phase2/AR1/recombination_maps
mkdir -pv $recomb_dir
cd $recomb_dir
for chrom in 2L 2R 3L 3R X;
do
    download ftp://ngs.sanger.ac.uk/production/ag1000g/phase2/AR1/recombination_maps/Ag_${chrom}.map
done

# retrieve Ag1000G phase 2 haplotype data
cd $wd
haplotypes_dir=data/external/ag1000g/phase2/AR1/haplotypes/main
mkdir -pv $haplotypes_dir
cd $haplotypes_dir
download ftp://ngs.sanger.ac.uk/production/ag1000g/phase2/AR1/haplotypes/main/haplotypes.autosomes.meta.txt
download ftp://ngs.sanger.ac.uk/production/ag1000g/phase2/AR1/haplotypes/main/haplotypes.X.meta.txt
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
    download ftp://ngs.sanger.ac.uk/production/ag1000g/phase2/AR1/haplotypes/main/zarr/$file
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
    download ftp://ngs.sanger.ac.uk/production/ag1000g/phase2/AR1/variation/main/zarr/pass/$file
    unzip -u $file
done

# retrieve Ag1000G phase 2 accessibility data
# N.B., this is big, but we only need the 'is_accessible' arrays,
# would be useful to have a zarr subset to download.
#cd $wd
#accessibility_dir=data/external/ag1000g/phase2/AR1/accessibility
#mkdir -pv $accessibility_dir
#cd $accessibility_dir
#download ftp://ngs.sanger.ac.uk/production/ag1000g/phase2/AR1/accessibility/accessibility.h5
