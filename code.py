def calculate_nucleotide_frequencies(sequence):
    """
    Calculate the frequency of each nucleotide in the given DNA sequence.

    Args:
    sequence (str): A string representing the DNA sequence.

    Returns:
    dict: A dictionary where keys are nucleotides and values are their respective frequencies.
    """
    frequency_dict = dict()
    for nucleotide in sequence:
        if nucleotide not in frequency_dict:
            frequency_dict[nucleotide] = 1
        else:
            frequency_dict[nucleotide] += 1
    return frequency_dict

def print_nucleotide_frequencies(frequency_dict):
    """
    Print the relative frequency of each nucleotide in the frequency dictionary.

    Args:
    frequency_dict (dict): A dictionary containing nucleotide frequencies.
    """
    print('Nucleotide Frequencies:')
    total_count = float(sum(frequency_dict.values()))
    
    for nucleotide, count in frequency_dict.items():
        relative_frequency = count / total_count
        print(f'{nucleotide}: {relative_frequency:.4f}')

# Example usage
sequence = 'ATCTGACGCGCGCCGC'
frequencies = calculate_nucleotide_frequencies(sequence)
print_nucleotide_frequencies(frequencies)
