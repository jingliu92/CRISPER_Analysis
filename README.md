# CRISPER_Analysis


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
