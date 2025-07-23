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

### Step 3: Data Aggregation & Comparative Analysis
✅ Objective:

To compare:

**1. CRISPR-Cas system subtypes (e.g., Type I-E, I-F) across isolates from clinical, bovine, and produce sources**

**2. Spacer content (presence/absence matrix)**

**3. Assess if certain CRISPR types or spacers are enriched in a particular source**


## Why Compare CRISPR-Cas Subtypes Across Isolates?
**1. Source-Specific Evolutionary Signatures**
  
   Different environments (e.g., human gut, cattle intestine, plant surfaces) apply different selective pressures on E. coli. These can lead to:
   - Divergence in CRISPR-Cas system architecture
   - Loss, acquisition, or replacement of cas genes
   - Shift in subtype frequencies (e.g., some subtypes may be more prevalent in cattle-associated isolates)

By comparing subtypes, you can detect whether: **Clinical isolates share CRISPR-Cas system subtypes more frequently with bovine or produce isolates**; **Certain subtypes are unique or enriched in a specific source**

**2. Horizontal Gene Transfer (HGT) and Adaptation**

CRISPR-Cas systems can be horizontally transferred. If clinical and bovine isolates share the same subtype and cas operon structure, it may:
- Indicate recent common ancestry or horizontal gene transfer
- Strengthen the case that clinical strains are linked to animal sources
- Conversely, distinct subtypes suggest separate evolutionary paths.

**3. Contextualizing Spacer Data**

CRISPR-Cas subtypes define: 
- The mechanism by which new spacers are acquired
- The type of protospacer-adjacent motifs (PAMs) recognized
- The rate and fidelity of spacer integration

So, when you later compare spacer profiles: Knowing the subtype adds confidence — e.g., **two strains with Type I-E systems sharing many spacers is more meaningful than if they had different systems**.

**4. Validate CRISPR-Cas Locus Integrity**
Not all isolates have intact or functional CRISPR-Cas systems. Some clinical isolates may:
- Lack adaptation modules (e.g., cas1/cas2)
- Have incomplete interference modules
- Comparing completeness across sources tells you: Whether certain sources tend to maintain active immune systems, which could relate to phage exposure or ecological niche.

<img width="754" height="291" alt="image" src="https://github.com/user-attachments/assets/370d212a-4dd8-4a7c-9fa1-bb8c9d6b674c" />


**Parse Cas Operons with Metadata**
```
# File to use: CRISPR_Cas.tab or cas_operons.tab from each isolate’s output
nano summarize_cas_types.py
```

```
import os
import pandas as pd

# === File paths ===
metadata_file = "metadata.csv"          # your file
base_dir = "CRISPRCasTyper_outputs"     # path to output folders
output_file = "CRISPRCas_Subtype_Summary.tsv"

# === Load metadata ===
metadata = pd.read_csv(metadata_file)
metadata = metadata.set_index('Isolate')

results = []

# Loop through existing CRISPRCasTyper result folders
for isolate_id in os.listdir(base_dir):
    cas_file = os.path.join(base_dir, isolate_id, "cas_operons.tab")
    
    if not os.path.isfile(cas_file):
        print(f"Skipping {isolate_id}: cas_operons.tab not found")
        continue

    try:
        df = pd.read_csv(cas_file, sep='\t')
        source = metadata.loc[isolate_id, 'Source'] if isolate_id in metadata.index else "Unknown"

        for _, row in df.iterrows():
            results.append({
                'Isolate_ID': isolate_id,
                'Source': source,
                'Cas_Subtype': row.get('Best_type', 'NA'),
                'Interference_%': row.get('Complete_Interference', 'NA'),
                'Adaptation_%': row.get('Complete_Adaptation', 'NA')
            })

    except Exception as e:
        print(f"Error parsing {cas_file}: {e}")

# Create and export DataFrame
summary_df = pd.DataFrame(results)
summary_df.to_csv(output_file, sep='\t', index=False)

print(f"\n✅ Summary saved to {output_file}")
```
```
python summarize_cas_types.py
```

### Results interpretation
Based on the CRISPRCas_Subtype_Summary.tsv, all isolates Cas subtypes are type I-E. This indicates: 
**Subtype Is Not a Differentiating Feature, Because all isolates share the same Cas subtype (I-E), this feature cannot distinguish between: Clinical vs. bovine vs. produce sources**

## Analyzing and Comparing Spacer Profiles Across Your E. coli O157 Isolates
This will help you assess whether clinical isolates share spacer content with bovine or produce isolates.

build_spacer_matrix.py
```
import os
from Bio import SeqIO
import pandas as pd
from collections import defaultdict

# === CONFIG ===
base_dir = "CRISPRCasTyper_outputs"
output_file = "spacer_presence_absence_matrix.tsv"

spacer_dict = defaultdict(dict)
all_spacers = set()

# Loop through isolate folders
for folder in os.listdir(base_dir):
    if not folder.endswith("_genomic"):
        continue

    isolate_id = folder.replace("_genomic", "")
    spacer_folder = os.path.join(base_dir, folder, "spacers")

    if not os.path.isdir(spacer_folder):
        print(f"Warning: No spacer folder for {isolate_id}")
        continue

    # Parse all .fa files in spacer folder
    for file in os.listdir(spacer_folder):
        if not file.endswith(".fa"):
            continue
        file_path = os.path.join(spacer_folder, file)

        for record in SeqIO.parse(file_path, "fasta"):
            spacer_seq = str(record.seq)
            all_spacers.add(spacer_seq)
            spacer_dict[isolate_id][spacer_seq] = 1

# Create binary matrix
all_spacers = sorted(list(all_spacers))
matrix = pd.DataFrame(0, index=spacer_dict.keys(), columns=all_spacers)

for isolate, spacers in spacer_dict.items():
    for spacer in spacers:
        matrix.loc[isolate, spacer] = 1

# Save to TSV
matrix.to_csv(output_file, sep='\t')
print(f"\n✅ Spacer matrix saved to: {output_file}")
```

### Results interpretation
Only 6 unique spacers were identified and Three spacers are present in almost all isolates, except GCA_000747455.1 (cattle), GCA_021166015.1 (Packaged lettuce) and GCA_021184125.1 (clinical) show a different pattern (presence of other spacers).
only 6 spacers were extracted. This could indicate: **Highly clonal population (e.g., same CRISPR array in all strains)** Or CRISPR arrays are truncated or low-quality in most genomes.

## Build Phylogenetic Tree
- Define presence/absence matrix (Done)
- Compute Jaccard similarity
- Convert to Jaccard distance = 1 – similarity
- Use Neighbor-Joining (NJ) to build tree
- Visualize in iTol

build_crispr_tree.py
```
import pandas as pd
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import average, to_tree

# === Step 1: Load inputs ===
matrix = pd.read_csv("spacer_presence_absence_matrix.tsv", sep="\t", index_col=0)
metadata = pd.read_csv("metadata.csv")

# === Step 2: Merge to label rows with Source ===
metadata["Label"] = metadata["Isolate"] + "_" + metadata["Source"]
labeled = matrix.reset_index().merge(metadata, left_on="index", right_on="Isolate")
labeled_matrix = labeled.set_index("Label")[matrix.columns]
labeled_matrix.to_csv("spacer_matrix_labeled.tsv", sep="\t")
print("✅ spacer_matrix_labeled.tsv saved.")

# === Step 3: Compute Jaccard distances and NJ tree ===
dist_array = pairwise_distances(labeled_matrix.values, metric="jaccard")
condensed = squareform(dist_array)
linkage_matrix = average(condensed)

def get_newick(node, leaf_names, newick="", parentdist=0):
    if node.is_leaf():
        return "%s:%.5f%s" % (leaf_names[node.id], parentdist - node.dist, newick)
    else:
        if newick:
            newick = "):%.5f%s" % (parentdist - node.dist, newick)
        else:
            newick = ");"
        newick = get_newick(node.get_left(), leaf_names, newick, node.dist)
        newick = get_newick(node.get_right(), leaf_names, ",%s" % newick, node.dist)
        return "(%s" % newick

tree = to_tree(linkage_matrix)
leaf_names = labeled_matrix.index.tolist()
newick_str = get_newick(tree, leaf_names)

with open("nj_tree.newick", "w") as f:
    f.write(newick_str)
print("✅ NJ tree saved as nj_tree.newick")

# === Step 4: Generate iTOL color annotation ===
color_map = {
    "Clinical": "#e41a1c",
    "Bovine": "#377eb8",
    "Produce": "#4daf4a",
    "Avian": "#984ea3"
}
metadata["Color"] = metadata["Source"].map(color_map)

with open("itol_annotation.txt", "w") as f:
    f.write("DATASET_COLORSTRIP\nSEPARATOR TAB\nDATASET_LABEL\tSourceGroup\nCOLOR\t#000000\nLEGEND_TITLE\tSource\n")
    f.write("LEGEND_SHAPES\t1\t1\t1\t1\n")
    f.write("LEGEND_COLORS\t#e41a1c\t#377eb8\t#4daf4a\t#984ea3\n")
    f.write("LEGEND_LABELS\tClinical\tBovine\tProduce\tAvian\n")
    f.write("DATA\n")
    for _, row in metadata.iterrows():
        label = row["Isolate"] + "_" + row["Source"]
        color = row["Color"]
        f.write(f"{label}\t{color}\n")
print("✅ iTOL annotation saved as itol_annotation.txt")
```
<img width="1889" height="809" alt="image" src="https://github.com/user-attachments/assets/07a07beb-c7ca-45c5-b555-f945528c7f0b" />

