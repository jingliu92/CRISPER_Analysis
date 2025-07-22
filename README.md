# CRISPER_Analysis

## What is CRISPR-Cas systems?

CRISPR-Cas is an adaptive prokaryotic immune system found in about 50% of bacteria and 87% of archaea species. This system specifically protects its host from foreign DNA or RNA. CRISPR-Cas system consists of **two main** elements that function in tandem: **CRISPR arrays** and **cas genes**. CRISPR array is the locus of a
genome that includes palindromic repetitive sequences, called **repeats**, that are interspaced with short variable DNA sequences -**“spacers”**.  Some of the spacers in the CRISPR arrays match sequences from mobile genetic elements, such as viruses and plasmids, serving as a record of previous encounters with these
invaders. CRISPR arrays and cas operons are usually co-localized in the genome but could also be located in separate loci. Together with Cas proteins encoded in the cas operon, CRISPR arrays act against invading foreign nucleic acids.

## How CRISPR-Cas system Function?
CRISPR-Cas systems are diverse and have various proteins, and biomolecular mechanisms, although all systems act in **three** general steps: **adaptation, crRNA biogenesis, and interference**: 
1. During the **adaptation step**, the CRISPR-Cas system acquires new spacers derived from foreign nucleic acids, referred to as “protospacers”. This process is usually done by Cas 1 and Cas 2 proteins - the core adaptation module in all CRISPR-Cas systems. These proteins bind the target protospacer and introduce it between the leader region and the first
repeat, yielding a duplication of the repeat and the addition of the new spacer.
2. During the **crRNA biogenesis** stage, the CRISPR array is transcribed into a long pre-CRISPR RNA (pre-crRNA), which is further processed into small CRISPR RNAs (crRNAs) by Cas proteins.
3. Finally, during the **interference** stage, the complex of Cas proteins (effector module) is guided by crRNA to target and destroy an intruder nucleic acid.

<img width="1000" height="900" alt="image" src="https://github.com/user-attachments/assets/58aa0ffe-9c6a-46b5-9616-37841ba7360e" />

## Application of CRISPR-Cas for epidemiological typing
Composition of the CRISPR arrays that store information about previous infections is a powerful marker of the microevolution of an organism.  
Analyze CRISPR loci of pathogens from Whole Genome Sequencing (WGS) data of various isolates in order to **enhance strain differentiation**.  Timme et al. presented in 2013 the first large-scale S. enterica phylogeny inferred from a new reference-free k-mer approach of gathering single nucleotide polymorphisms (SNPs) from whole genomes and discussed the significance of the diversity of CRISPR loci in understanding the evolution of pathogenicity. Another paper studied the genetic diversity and evolutionary history of CRISPR loci and cas genes among 427 S. enterica genomes representing 64 various serovars.

## Objective of Current Project 
Use CRISPR-based approach to determine whether clinical E. coli O157 isolates are linked to produce, beef, or both.

**Limitations of SNP-Based Outbreak Tracking** 

In a fast-spreading outbreak (e.g., foodborne E. coli over days/weeks), isolates from different sources might show 0–1 SNP difference. This makes it hard to differentiate between sources (e.g., farm vs. processing plant).

CRISPR-based approach for E. coli O157 outbreak tracing using WGS data. CRISPR typing (or spoligotyping) uses the pattern of spacers and repeats to differentiate strains.
1. E. coli has two main CRISPR loci: CRISPR1 and CRISPR2, sometimes also CRISPR3 and CRISPR4.
2. In E. coli O157:H7, CRISPR arrays are present and can vary among strains, allowing for subtyping within O157.

## Bioinformatics Analysis Pipeline
### Step1: Genome Dataset Collection from NCBI 
To investigate the potential source attribution of clinical Escherichia coli O157 isolates, we applied a CRISPR-based approach focusing on strains within the SNP cluster PDS000181369.254, as identified through the NCBI Pathogen Detection platform. This cluster comprises 4,458 isolates, **from which we curated a subset of 108 isolates representing clinical, bovine, and produce sources. Selection was guided by phylogenetic proximity in the SNP tree; specifically, we selected isolates with minimal SNP differences (e.g., 0~50 SNPs) between clinical and environmental strains.**
#### Download Assembly from NCBI and Data Preparation
**Accession # of WGS isolates**
```
nano accessions.txt

GCA_012819355.1
GCA_021166015.1
GCA_021184125.1
GCA_012191205.2
GCA_012148685.1
GCA_012092775.2
GCA_004231525.3
GCA_012091855.2
GCA_011833915.1
GCA_002195475.1
GCA_012392045.2
GCA_012824515.2
GCA_012722755.2
GCA_026671015.2
GCA_030761495.2
GCA_012778035.2
GCA_012136965.2
GCA_012017725.2
GCA_011953435.2
GCA_011860765.2
GCA_011861605.2
GCA_032499945.2
GCA_012741275.1
GCA_012438845.2
GCA_012019445.2
GCA_011840145.2
GCA_025375455.2
GCA_012369445.2
GCA_015286565.2
GCA_000747455.1
GCA_015699465.1
GCA_012777515.2
GCA_017268535.2
GCA_030722125.2
GCA_012750655.2
GCA_047802525.1
GCA_029714465.3
GCA_014559605.2
GCA_025305355.2
GCA_012829095.2
GCA_012717695.2
GCA_020381505.2
GCA_012714745.2
GCA_012302805.2
GCA_012266065.2
GCA_012260345.1
GCA_014955645.2
GCA_023003305.2
GCA_020914765.2
GCA_020914705.2
GCA_020979445.2
GCA_020978845.2
GCA_020979465.2
GCA_021003695.2
GCA_021005645.2
GCA_024891135.2
GCA_011830295.2
GCA_013685255.2
GCA_014387465.2
GCA_021184915.2
GCA_042153485.2
GCA_047838695.1
GCA_017759235.2
GCA_017683585.2
GCA_028667335.2
GCA_029825875.2
GCA_031589575.2
GCA_029585815.1
GCA_032830935.1
GCA_031545225.1
GCA_031997305.1
GCA_012425765.2
GCA_012144365.2
GCA_012047315.2
GCA_014096495.2
GCA_014242775.2
GCA_014455235.2
GCA_015202325.2
GCA_011817985.2
GCA_014979465.2
GCA_012020605.2
GCA_019347555.2
GCA_019544495.2
GCA_019681615.2
GCA_020041825.2
GCA_020349605.2
GCA_012211705.2
GCA_012025385.2
GCA_011957145.2
GCA_029128165.2
GCA_027996165.2
GCA_027917935.2
GCA_029648545.2
GCA_032439805.2
GCA_040723375.2
GCA_019785505.2
GCA_025616425.2
GCA_037981075.2
GCA_040337995.2
GCA_024871825.2
GCA_032367475.2
GCA_037561345.2
GCA_012808965.2
GCA_012767535.2
GCA_013705125.1
GCA_016492925.1
GCA_018621535.1
GCA_032893465.2
```
```
./datasets  download genome accession --inputfile accessions.txt --include genome,cds,gff3

unzip ncbi_dataset.zip

ls | wc -l # Count how many files downloaded. (108 isolates)
```
**Sort .fna and .gff Files**
```
nano sort_and_rename_files.sh

#!/bin/bash

# Create destination folders
mkdir -p cds genomic_fna gff

# Loop through each GCA_* folder
for folder in GCA_*; do
  # Skip if not a directory
  [ -d "$folder" ] || continue

  # Extract the isolate name (same as folder name)
  isolate=$(basename "$folder")

  # Copy and rename cds file
  if [ -f "$folder/cds_from_genomic.fna" ]; then
    cp "$folder/cds_from_genomic.fna" "cds/${isolate}_cds_from_genomic.fna"
  fi

  # Copy and rename genomic fna file
  fna_file=$(find "$folder" -maxdepth 1 -name "*_genomic.fna" ! -name "cds_from_genomic.fna" | head -n 1)
  if [ -n "$fna_file" ]; then
    cp "$fna_file" "genomic_fna/${isolate}_genomic.fna"
  fi

  # Copy and rename gff file
  if [ -f "$folder/genomic.gff" ]; then
    cp "$folder/genomic.gff" "gff/${isolate}_genomic.gff"
  fi
done
```

```
chmod +x sort_and_rename_files.sh
./sort_and_rename_files.sh
```

### Step2: CRISPR Array and Cas Operon Identification
✅ Objective: Identify and extract:
1. **CRISPR arrays (with spacers and direct repeats)**
2. **CRISPR leader sequences**
3. **Cas operons (e.g., cas1, cas2, cas3, etc.)**
4. **Subtypes of CRISPR-Cas systems in each genome**

**Running CRISPRCasTyper** (https://github.com/Russel88/CRISPRCasTyper)
```
# Create output directory
mkdir CRISPRCasTyper_outputs

# Batch process all fna files
for file in genomic_fna/*.fna; do
    sample=$(basename "$file" .fna)
    echo "Processing $sample"
    cctyper "$file" "CRISPRCasTyper_outputs/$sample"
done
```


