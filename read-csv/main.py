from mycsv import read_csv_to_dict_of_lists


def main():
    result = read_csv_to_dict_of_lists()
    for key,value in result.items():
        print(f"- {key}:")
        for item in value:
           print(f"     {item}")
        print()

main()



