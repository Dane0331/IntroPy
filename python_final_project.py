import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Q1: Relationship between the length of house-elves' ears and their DNA content
def analyze_house_elves():
    data = pd.read_csv('houseelf_earlength_dna_data.csv')

    # Processing rows to categorizing ear size and calculating GC-content of the DNA
    results = []
    for index, row in data.iterrows():
        ear_length = row['earlength']
        dna_sequence = row['dnaseq']
        gc_content = (dna_sequence.count('G') + dna_sequence.count('C')) / len(dna_sequence) * 100 # Checks each sequence for how much G/C content there is
        size_category = 'large' if ear_length > 10 else 'small'
        results.append([row['id'], size_category, gc_content])

    # Creating a DataFrame for analysis results
    results_df = pd.DataFrame(results, columns=['ID', 'EarSize', 'GCContent'])

    # Calculating the average GC-content for each ear size category
    avg_gc_content = results_df.groupby('EarSize')['GCContent'].mean()
    print("Average GC-Content:")
    print(avg_gc_content)

    # Exporting to CSV file
    results_df.to_csv('grangers_analysis.csv', index=False)


# Q2: Mammals' mass relationship analysis
def analyze_mammals():
    # Importing data with error handling for malformed lines
    try:
        mammals_data = pd.read_csv('Mammal_lifehistories_v2.txt', sep='\t', skipfooter=7, na_values=['-999', '-999.00'], engine='python')
    except Exception as e:
        print("Error reading the file:", e)
        return

    # Dropping rows with missing data for data cleaning
    mammals_data.dropna(inplace=True) # This causes the total number of orders go from 17 to 12, dropping 5 orders due to na_values.

    # Plotting adult mass vs. newborn mass
    plt.figure()
    plt.scatter(mammals_data['mass(g)'], mammals_data['newborn(g)'])
    plt.xlabel('Adult Mass (g)')
    plt.ylabel('Newborn Mass (g)')
    plt.title('Adult Mass vs. Newborn Mass')
    plt.show()

    # Plotting log10 of adult mass vs. log10 of newborn mass
    plt.figure()
    plt.scatter(np.log10(mammals_data['mass(g)']), np.log10(mammals_data['newborn(g)']))
    plt.xlabel('Log10(Adult Mass) (log10 g)')
    plt.ylabel('Log10(Newborn Mass) (log10 g)')
    plt.title('Log10(Adult Mass) vs. Log10(Newborn Mass)')
    plt.show()

    # Filtering data for Rodentia
    rodentia_data = mammals_data[mammals_data['order'] == 'Rodentia']

    # Plotting log10 adult mass vs. log10 newborn mass for Rodentia
    plt.figure()
    plt.scatter(np.log10(rodentia_data['mass(g)']), np.log10(rodentia_data['newborn(g)']))
    plt.xlabel('Log10(Adult Mass) (log10 g)')
    plt.ylabel('Log10(Newborn Mass) (log10 g)')
    plt.title('Log10(Adult Mass) vs. Log10(Newborn Mass) - Rodentia')
    plt.show()

    # Plotting adult mass vs. newborn mass, axes scaled logarithmically, and colored by order
    plt.figure()
    orders = mammals_data['order'].unique()
    for order in orders:
        order_data = mammals_data[mammals_data['order'] == order]
        plt.scatter(np.log10(order_data['mass(g)']), np.log10(order_data['newborn(g)']), label=order)
    plt.xlabel('Log10(Adult Mass) (log10 g)')
    plt.ylabel('Log10(Newborn Mass) (log10 g)')
    plt.title('Log10(Adult Mass) vs. Log10(Newborn Mass) by Order')
    plt.legend(loc='best', fontsize='small')
    plt.show()

    # Plotting a subplot for each order with different colors
    orders = mammals_data['order'].unique()
    fig, axes = plt.subplots(len(orders), 1, figsize=(8, len(orders) * 3))
    colors = plt.cm.tab20(np.linspace(0, 1, len(orders))) # Makes each subplot use a different color for each order
    for i, (order, color) in enumerate(zip(orders, colors)): # Loops across each order to create individual subplots
        order_data = mammals_data[mammals_data['order'] == order]
        axes[i].scatter(np.log10(order_data['mass(g)']), np.log10(order_data['newborn(g)']), color=color)
        axes[i].set_title(order)
        axes[i].set_xlabel('Log10(Adult Mass)')
        axes[i].set_ylabel('Log10(Newborn Mass)')
    plt.tight_layout()
    plt.show()

# Running both Q1 and Q2 analyses
analyze_house_elves()
analyze_mammals()
