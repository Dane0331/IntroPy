import pandas as pd

my_types = {
        'Species' : 'string',
        'Kingdom' : 'string',
        'Class'   : 'string',
        'Assembly status' : 'string',
        'Number of genes' : 'Int64',
        'Number of proteins' : 'Int64'
    }

euk = pd.read_csv("data/eukaryotes.tsv",
    sep="\t",
    dtype = my_types,
    na_values=['-']
)

pd.set_option('display.max_columns', None)



# Checking the general structure and contents of the DataFrame
print("\neukDataFrame Info:")
print(euk.info())
print("\neukDataFrame Head:")
print(euk.head())

# Creating euk_float dataframe that has entries with size less than 4000 and drop rows with missing or NA values
euk_float = euk[euk["Size (Mb)"] < 4000].dropna()

# Displays euk_float dataframe info as well as statistics showing the maximum size value (3843.98) under 4000
print("\neuk_float DataFrame Info:")
print(euk_float.info())
print("\nStatistics for 'Size (Mb)':")
print(euk_float["Size (Mb)"].describe()) #Here we'll be able to see the maximum size of the revised dataframe

# euk_filtered dataframe based on >=1.1 ratio of no. prot and no. genes
euk_filtered = euk[(euk["Number of proteins"] / euk["Number of genes"]) >= 1.1]
euk_filtered_ratio = (euk_filtered["Number of proteins"] / euk_filtered["Number of genes"]).min()
print(f"\nThe minimum ratio of 'Number of proteins' to 'Number of genes' in euk_filtered is: {euk_filtered_ratio}")

# Shows the dataframe structure and first few rows of euk_filtered using head
print("\neuk_filtered DataFrame Info:")
print(euk_filtered.info())
print("\neuk_filtered DataFrame Head:")
print(euk.head())

# Filter for fungal species with genomes larger than 100Mb
fungal_large_genomes = euk[(euk["Kingdom"] == "Fungi") & (euk["Size (Mb)"] > 100)]

# Shows the names and count of fungal species larger than 100Mb in the new dataframe
print("\nNumber of fungal species with genomes > 100Mb:", fungal_large_genomes.shape[0])
print("\nNames of these species:")
for name in fungal_large_genomes["Species"]:
    print(name)




