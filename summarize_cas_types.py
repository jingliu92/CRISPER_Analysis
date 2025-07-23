import os
import pandas as pd

# === File paths ===
metadata_file = "metadata.csv"
base_dir = "CRISPRCasTyper_outputs"
output_file = "CRISPRCas_Subtype_Summary.tsv"

# === Load metadata ===
metadata = pd.read_csv(metadata_file)
metadata = metadata.set_index('Isolate')

results = []

# Loop through each output folder
for folder in os.listdir(base_dir):
    if not folder.endswith("_genomic"):
        continue

    isolate_id = folder.replace("_genomic", "")
    cas_file = os.path.join(base_dir, folder, "cas_operons.tab")
    
    if not os.path.isfile(cas_file):
        print(f"Skipping {folder}: cas_operons.tab not found")
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
        print(f"Error parsing {cas_file} for {isolate_id}: {e}")

# Save combined summary
summary_df = pd.DataFrame(results)
summary_df.to_csv(output_file, sep='\t', index=False)

print(f"\n✅ Summary saved to {output_file}")
