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
Use CRISPR-based approach for E. coli O157 outbreak tracing. 

**Limitations of SNP-Based Outbreak Tracking** 

In a fast-spreading outbreak (e.g., foodborne E. coli over days/weeks), isolates from different sources might show 0–1 SNP difference. This makes it hard to differentiate between sources (e.g., farm vs. processing plant).

CRISPR-based approach for E. coli O157 outbreak tracing using WGS data. CRISPR typing (or spoligotyping) uses the pattern of spacers and repeats to differentiate strains.
1. E. coli has two main CRISPR loci: CRISPR1 and CRISPR2, sometimes also CRISPR3 and CRISPR4.
2. In E. coli O157:H7, CRISPR arrays are present and can vary among strains, allowing for subtyping within O157.

## Bioinformatics Analysis Pipeline
### Genome Dataset Collection from NCBI 

```
for dir in GCA_*; do
  cd "$dir"
  prefix=$(basename "$dir")
  for f in cds_from_genomic.fna genomic.gff; do
    [ -f "$f" ] && mv "$f" "${prefix}_${f}"
  done
  cd ..
done
```
