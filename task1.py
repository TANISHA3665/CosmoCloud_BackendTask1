list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    # Create an empty dictionary to hold the merged information
    merged_dict = {}

    # Loop through each item in list_1 and add it to the merged dictionary
    for item in list_1:
        merged_dict[item['id']] = item

    # Loop through each item in list_2 and add or update it in the merged dictionary
    for item in list_2:
        if item['id'] in merged_dict:
            merged_dict[item['id']].update(item)
        else:
            merged_dict[item['id']] = item

    # Convert the merged dictionary back to a list
    merged_list = list(merged_dict.values())

    return merged_list

list_3 = merge_lists(list_1, list_2)
# print(list_3)
