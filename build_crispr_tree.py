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
