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
