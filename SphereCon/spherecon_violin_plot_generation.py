import pandas as pd
import seaborn as sns

# Load the TSV file into a pandas dataframe
df = pd.read_csv('/Users/anikakulkarni/Documents/RSA_Classifications/SphereCon/spherecon_merged_file_UPDATED_with4classes.tsv', delimiter='\t')

# Generate the violin plot using seaborn
sns.violinplot(x='SphereCon Value', y='Bondugula Switch Class', data=df)

# Show the plot
import matplotlib.pyplot as plt
plt.show()

# Save the plot as a PNG image
plt.savefig('spherecon_rsa_violin_plot.png')