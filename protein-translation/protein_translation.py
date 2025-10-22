def proteins(strand):
    codon_to_protein = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine", "UUC": "Phenylalanine",
        "UUA": "Leucine", "UUG": "Leucine",
        "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
        "UAU": "Tyrosine", "UAC": "Tyrosine",
        "UGU": "Cysteine", "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
    }
    protein_list = []
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]
        if codon in codon_to_protein:
            protein = codon_to_protein[codon]
            if protein == "STOP":
                break
            protein_list.append(protein)
    return protein_list
