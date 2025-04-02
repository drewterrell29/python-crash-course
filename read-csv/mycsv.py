import csv # Make sure to import csv
import sys

def read_csv_to_dict_of_lists():
    # Consider using a more specific path or handling potential errors here
    try:
        with open('csvs/products.csv', mode='r', encoding='utf-8') as file: # Assuming the file is in the same directory
            csv_reader = csv.reader(file)

            # Read all rows into a list first (safe for moderate sized files)
            all_rows = list(csv_reader)

            if not all_rows: # Handle empty file
                print("Warning: CSV file is empty.")
                return {}

            headings = all_rows[0] # Get header row
            data_rows = all_rows[1:] # Get data rows

            # --- Initialize the dictionary with empty lists ---
            mydict = {header: [] for header in headings}
            # This creates: {'ProductID': [], 'ProductName': [], ...}

            # --- Loop through data rows ---
            for row in data_rows:
                # Ensure row has the same number of columns as headings
                if len(row) == len(headings):
                    # --- Loop through cells in the row ---
                    for index, info in enumerate(row):
                        # Get the correct heading for this column
                        current_heading = headings[index]
                        # --- Append the info to the correct list ---
                        mydict[current_heading].append(info.strip()) # Use strip() to clean whitespace
                else:
                    print(f"Warning: Skipping malformed row: {row}")


            # print(headings) # You can still print headings if needed
            # print("\nResulting Dictionary (Dict of Lists):")
            # # Print nicely for verification
            # for key, value in mydict.items():
            #      print(f"- {key}: {value}")
            return mydict # Return the dictionary

    except FileNotFoundError:
        print(f"Error: File not found at 'products.csv'", file=sys.stderr)
        return None # Or raise the exception
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        return None # Or raise the exception

# # Example usage:
# product_data = read_csv_to_dict_of_lists()

# If you want to access all product names:
# if product_data:
#     print("\nAll Product Names:")
#     print(product_data.get('ProductName', []))
