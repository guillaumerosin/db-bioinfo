#!/usr/bin/env python3
import time


class Read:
    def __init__(self, count, seq):
        self.count = int(count)
        self.seq = seq

    def __repr__(self):
        return f"{self.count} {self.seq}"


# === Chargement des reads ===
def load_reads(filename):
    reads = []
    with open(filename) as f:
        for line in f:
            c, s = line.strip().split()
            reads.append(Read(c, s))
    return reads


# === Filtrage des reads count > 1 ===
def filter_reads(reads):
    return [r for r in reads if r.count > 1]


# === Écriture dans un fichier ===
def write_reads(reads, output_filename):
    with open(output_filename, "w") as f:
        for r in reads:
            f.write(f"{r.count} {r.seq}\n")


# ===== MAIN =====
input_file = "C:/Users/KINGC/OneDrive/Bureau/Cours master/M1 - Quad 2/Bio-info/seq_clustered.txt"  # fichier du script précédent
output_file = "C:/Users/KINGC/OneDrive/Bureau/Cours master/M1 - Quad 2/Bio-info/seq_filtered.txt"  # fichier après suppression des reads à 1

start_time = time.time()  # début du chrono

reads = load_reads(input_file)
print("Nombre de reads avant filtrage :", len(reads))

reads = filter_reads(reads)
print("Nombre de reads après filtrage :", len(reads))

write_reads(reads, output_file)
print("Résultat écrit dans :", output_file)

end_time = time.time()  # fin du chrono
elapsed = end_time - start_time
print(f"Temps écoulé : {elapsed:.2f} secondes")
