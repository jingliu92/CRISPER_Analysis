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
