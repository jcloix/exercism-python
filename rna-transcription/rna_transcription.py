def to_rna(dna_strand):
    # DNA → RNA map
    complement = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }

    # Build RNA strand by looking up each nucleotide in the map
    return "".join(complement[nuc] for nuc in dna_strand)
