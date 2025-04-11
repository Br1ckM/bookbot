def count_words(string):
    word_list = string.split()
    final_count = len(word_list)
    return final_count

def count_characters(string):
    return_dict = {}
    book = string.lower()
    for i in book:
        if i in return_dict:
            return_dict[i] += 1
        else:
            return_dict[i] = 1
    return return_dict

def convert_to_sorted_list(dictionary):
    the_list = []

    for i in dictionary:
        new_dict = {}
        new_dict["name"] = i
        new_dict["value"] = dictionary[i]
        the_list.append(new_dict)

    the_list.sort(key=sort_value, reverse=True)

    return the_list

### Helpers

def sort_value(the_list):
    return the_list["value"]
