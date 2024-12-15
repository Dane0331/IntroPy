# Defining SARS-CoV-2 FASTA file path
covid_file = 'sequence.fasta'

# Opening the FASTA file with fhand
def read_fasta(covid_file):
    sequence = '' #Empty string to store the sequence
    with open(covid_file, 'r') as fhand:
        for line in fhand:
            if line.startswith('>'): #This'll allow us to skip the header of the FASTA file, as these start with >
                continue
            sequence += line.strip() #Strips any newline characters and adds it to the sequence to make it one continuous line
    return sequence

# Reading the file and getting the sequence using the read_fasta function
sars_cov2_seq = read_fasta(covid_file)

# Finding the first occurrence of the ATG start codon and TAA, TAG, TGA stop codons
def first_codon_positions(sequence, start_codon="ATG", stop_codons=["TAA", "TAG", "TGA"]):
    start_position = sequence.find(start_codon) # Finds the first ATG start codon's position
    stop_positions = {stop: sequence.find(stop, start_position +3) for stop in stop_codons} # Allows for searching for the stop codon after the start codon with the +3 position (because it is 3 bps), while storing the index value of each of the found stop codons in the list
    stop_positions = {codon: pos for codon, pos in stop_positions.items() if pos != -1} # Filters out any non-existent stop codons if the value returned is -1, won't output anything in that case
    return start_position, stop_positions

# Locating the positions of the start codon and 3 stop codons provided
start_position, stop_positions = first_codon_positions(sars_cov2_seq)

print(f"First start codon (ATG) position: {start_position}")
for stop_codon, position in stop_positions.items(): # This allows us to now take the index values we gathered in the above "stop_positions" function and print it out as the stop codon position
    print(f"First stop codon ({stop_codon}) position: {position}")
