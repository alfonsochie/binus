def num_atoms(amount_in_grams,atomic_weight_in_grams=196.97):
    a=6.022*(10**23)
    num_of_atoms = amount_in_grams*a/atomic_weight_in_grams
    return num_of_atoms
print(num_atoms(10))