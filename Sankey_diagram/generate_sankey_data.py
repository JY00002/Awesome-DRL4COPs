import pandas as pd
from collections import defaultdict


def generate_sankey_data(input_file, output_file):
    """
    Read raw data from Excel file and generate source-target-value format data for Sankey diagram
    Properly handle None values and all connection relationships

    Parameters:
    input_file: input.xlsx
    output_file: output.xlsx
    """
    # 1. Read Excel data
    df = pd.read_excel(input_file)

    # === Added data cleaning step ===
    def clean_value(x):
        if pd.isna(x):
            return "None"
        # Convert to string and remove leading/trailing whitespace/special characters
        x = str(x).strip()
        # Optional: standardize case (uncomment if needed)
        # x = x.lower()  # or x = x.upper()
        return x

    # Clean all relevant columns
    levels = ['Problem', 'Agent', 'State', 'Embedding', 'RL', 'Action', 'Year']
    for col in levels:
        if col in df.columns:
            df[col] = df[col].apply(clean_value)

    # 3. Create connection counter
    connection_counter = defaultdict(int)

    # 4. Process each row of data
    for _, row in df.iterrows():
        # Ensure row has sufficient data
        if len(row) >= len(levels):
            # Traverse adjacent levels (Problem→State, State→Embedding, etc.)
            for i in range(len(levels) - 1):
                source = row[levels[i]]
                target = row[levels[i + 1]]

                # Convert NaN to string "None"
                if pd.isna(source):
                    source = "None"
                if pd.isna(target):
                    target = "None"

                # Count connections (including None values)
                connection_counter[(source, target)] += 1

    # 5. Convert to DataFrame
    sankey_data = []
    for (source, target), value in connection_counter.items():
        sankey_data.append({'Source': source, 'Target': target, 'Value': value})

    result_df = pd.DataFrame(sankey_data)

    # 6. Save results
    result_df.to_excel(output_file, index=False)
    print(f"Sankey data saved to: {output_file}")
    print(f"Generated {len(result_df)} connections")
    print("Note: None values have been preserved and included in statistics")


# Usage example
if __name__ == "__main__":
    input_excel = "input.xlsx"  # Replace with your input file path
    output_excel = "output.xlsx"  # Output file path

    generate_sankey_data(input_excel, output_excel)