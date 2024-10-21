import pandas as pd

# Load the data
instagram_profiles_df = pd.read_excel('instagram_profiles_info.xlsx')
moroccan_keywords_df = pd.read_excel('Moroccan & Doctors Keywords/Moroccan Keywords.xlsx', header=None)
doctors_keywords_df = pd.read_excel('Moroccan & Doctors Keywords/Doctors Keywords.xlsx', header=None)

# Convert the keyword dataframes to lists of keywords
moroccan_keywords = moroccan_keywords_df[0].str.lower().tolist()
doctors_keywords = doctors_keywords_df[0].str.lower().tolist()

# Initialize lists to store the results
moroccan_doctors = []
non_moroccan_doctors = []

# Function to check if any keyword from a list is in a text
def contains_keyword(text, keywords):
    return any(keyword in text for keyword in keywords)

# Iterate through each row in the instagram profiles data
for _, row in instagram_profiles_df.iterrows():
    meta_description = str(row['Meta Description']).lower()
    address = str(row['Address']).lower()

    # Check if the row contains at least one keyword from both lists
    if (contains_keyword(meta_description, moroccan_keywords) or contains_keyword(address, moroccan_keywords)) and \
       (contains_keyword(meta_description, doctors_keywords) or contains_keyword(address, doctors_keywords)):
        moroccan_doctors.append(row)
    else:
        non_moroccan_doctors.append(row)

# Convert the results lists back to DataFrames
moroccan_doctors_df = pd.DataFrame(moroccan_doctors)
non_moroccan_doctors_df = pd.DataFrame(non_moroccan_doctors)

# Export the results to Excel files
moroccan_doctors_df.to_excel('MoroccanDoctors.xlsx', index=False)
non_moroccan_doctors_df.to_excel('nonMoroccanDoctors.xlsx', index=False)
