from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()

    file_path = cwd_path / file_name
    keys_list = ['unordered_numbers', 'ordered_numbers', 'dna_sequence']
    key_set = set(keys_list)

    if field not in key_set:
        return None
    else:
        with open (file_path, mode="r", encoding="utf-8") as file_obj:
            data = json.load(file_obj)
            result = data[field]
        return result


# sequential_data = [54, 2, 18, 5, 3, 31, 20, 65, -10, 300, 17, 5, -1, 0, 0, 102, 7, 8, 9, 9, -3, -5, 0, 1, 63, 82, -36, -5]
# wanted_number = 9
def linear_search(sequential_data, wanted_number):
    position = []
    count = 0
    for i, num in enumerate(sequential_data):
        if num == wanted_number:
            position.append(i)
            count += 1
    result = {"position" : position, "count" : count}
    return result


ordered_numbers = [-51, -12, -3, -3, -1, 2, 8, 13, 14, 14, 14, 21, 22, 23, 24, 25, 48, 63, 64, 70, 72, 78, 90, 102, 120]
wanted_number = 8
if wanted_number not in ordered_numbers:
    print(None)
else:

    middle_float = len(ordered_numbers) / 2
    middle = int(round(middle_float, 0))
    right_margin = -1
    left_margin = 0

    while True:
        if wanted_number == ordered_numbers[middle]:
            index = ordered_numbers[middle]
            break
        else:
            if wanted_number > ordered_numbers[middle]:
                left_margin = middle
                middle_float = len(ordered_numbers[middle:left_margin]) / 2
                middle = middle + int(round(middle_float, 0))
            if wanted_number < ordered_numbers[middle]:
                right_margin = middle
                middle_float = len(ordered_numbers[left_margin:middle]) / 2
                middle = middle - int(round(middle_float, 0))

print(index)



def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    wanted_number = 3
    wanted_number_dict = linear_search(sequential_data, wanted_number)
    print(sequential_data)
    print(wanted_number_dict)


if __name__ == "__main__":
    main()
