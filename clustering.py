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


# === Calcul similarité simple ===
def similarity(seq1, seq2):
    if len(seq1) != len(seq2):
        return 0
    matches = sum(c1 == c2 for c1, c2 in zip(seq1, seq2))
    return matches / len(seq1)


# === Clustering 97% ===
def cluster_97(reads, sim_threshold=0.97, count_factor=10):
    changed = True

    while changed:
        changed = False

        # trier par count décroissant pour absorber les petits dans les grands
        reads.sort(key=lambda r: r.count, reverse=True)

        for i, big in enumerate(reads):
            if big.count == 0:
                continue
            for j in range(i + 1, len(reads)):
                small = reads[j]
                if small.count == 0:
                    continue

                sim = similarity(big.seq, small.seq)

                if sim >= sim_threshold and big.count >= small.count * count_factor:
                    # fusion
                    big.count += small.count
                    small.count = 0
                    changed = True

        # nettoyer les reads vidés
        reads = [r for r in reads if r.count > 0]

    return reads


# === Écriture dans un fichier ===
def write_reads(reads, output_filename):
    with open(output_filename, "w") as f:
        for r in reads:
            f.write(f"{r.count} {r.seq}\n")


# ===== MAIN =====
filename = "C:/Users/KINGC/OneDrive/Bureau/Cours master/M1 - Quad 2/Bio-info/seq_merged.txt"  # fichier d'entrée du premier script
output_file = "C:/Users/KINGC/OneDrive/Bureau/Cours master/M1 - Quad 2/Bio-info/seq_clustered.txt"  # sortie du clustering 97%

start_time = time.time()

reads = load_reads(filename)
print("Nombre de reads avant clustering :", len(reads))

reads = cluster_97(reads)

print("Nombre de reads après clustering :", len(reads))
write_reads(reads, output_file)
print("Résultat écrit dans :", output_file)

end_time = time.time()  # fin du chrono
elapsed = end_time - start_time
print(f"Temps écoulé : {elapsed:.2f} secondes")
