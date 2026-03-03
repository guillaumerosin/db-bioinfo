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


# === Redistribution uniforme des reads ===
def redistribute_uniform(reads):
    changed = True

    while changed:
        changed = False

        # Trier par longueur croissante
        reads.sort(key=lambda r: len(r.seq))

        for i, small in enumerate(reads):
            if small.count == 0:
                continue

            # Cherche uniquement les séquences plus longues
            parents = [big for big in reads[i + 1:] if small.seq in big.seq]

            if parents:
                k = len(parents)
                part = small.count // k

                if part > 0:
                    for p in parents:
                        p.count += part

                    small.count = 0
                    changed = True

        # Supprimer les séquences vidées à chaque itération
        reads = [r for r in reads if r.count > 0]

    return reads


# === Écriture du résultat dans un fichier ===
def write_reads(reads, output_filename):
    with open(output_filename, "w") as f:
        for r in reads:
            f.write(f"{r.count} {r.seq}\n")


# === MAIN ===
filename = "C:/Users/KINGC/OneDrive/Bureau/Cours master/M1 - Quad 2/Bio-info/seq_uniq.txt"
output_file = "C:/Users/KINGC/OneDrive/Bureau/Cours master/M1 - Quad 2/Bio-info/seq_merged.txt"

start_time = time.time()

reads = load_reads(filename)

print("Nombre de reads avant redistribution :", len(reads))

reads = redistribute_uniform(reads)

print("Nombre de reads après redistribution :", len(reads))

write_reads(reads, output_file)
print("Résultat écrit dans :", output_file)

end_time = time.time()  # fin du chrono
elapsed = end_time - start_time
print(f"Temps écoulé : {elapsed:.2f} secondes")
