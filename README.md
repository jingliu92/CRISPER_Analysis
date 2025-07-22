# CRISPER_Analysis

## What is CRISPR-Cas systems?

CRISPR-Cas is an adaptive prokaryotic immune system found in about 50% of bacteria and 87% of archaea species. This system specifically protects its host from foreign DNA or RNA. CRISPR-Cas system consists of **two main** elements that function in tandem: **CRISPR arrays** and **cas genes**. CRISPR array is the locus of a
genome that includes palindromic repetitive sequences, called **repeats**, that are interspaced with short variable DNA sequences -**“spacers”**.  Some of the spacers in the CRISPR arrays match sequences from mobile genetic elements, such as viruses and plasmids, serving as a record of previous encounters with these
invaders. CRISPR arrays and cas operons are usually co-localized in the genome but could also be located in separate loci. Together with Cas proteins encoded in the cas operon, CRISPR arrays act against invading foreign nucleic acids.

## How CRISPR-Cas system Function?
CRISPR-Cas systems are diverse and have various proteins, and biomolecular mechanisms, although all systems act in **three** general steps: **adaptation, crRNA biogenesis, and interference**: 
1. During the **adaptation step**, the CRISPR-Cas system acquires new spacers derived from foreign
nucleic acids, referred to as “protospacers”. This process is usually
done by Cas 1 and Cas 2 proteins - the core adaptation module in all
CRISPR-Cas systems [16]. These proteins bind the target proto-
spacer and introduce it between the leader region and the first
repeat, yielding a duplication of the repeat and the addition of the
new spacer [12,17,18]


<img width="1000" height="900" alt="image" src="https://github.com/user-attachments/assets/58aa0ffe-9c6a-46b5-9616-37841ba7360e" />


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
