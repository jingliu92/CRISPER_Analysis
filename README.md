# CRISPER_Analysis

## What is CRISPR-Cas systems?

RISPR-Cas is an adaptive prokaryotic immune system found in about 50% of bacteria and 87% of archaea species. This system specifically protects its host from foreign DNA or RNA. CRISPR-Cas system consists of two main elements that function in tandem: CRISPR arrays and cas genes. CRISPR array is the locus of a
genome that includes palindromic repetitive sequences, called repeats, that are interspaced with short variable DNA sequences -“spacers”.  Some of the spacers in the CRISPR arrays match sequences from mobile genetic elements, such as viruses and plasmids, serving as a record of previous encounters with these
invaders. <img width="800" height="700" alt="image" src="https://github.com/user-attachments/assets/58aa0ffe-9c6a-46b5-9616-37841ba7360e" />


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
