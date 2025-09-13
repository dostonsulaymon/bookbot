def sort_on(items):
    return items["num"]


def get_words_count(text):
    text_list = text.split()
    count = len(text_list)
    return count


def get_chars_count(text):
    chars_count = {}

    text_list = text.split()

    for word in text_list:
        for char in word:
            lower = char.lower()

            if lower not in chars_count:
                chars_count[lower] = 1
            else:
                chars_count[lower] += 1

    return chars_count


def sort_dictionary(dictionary):
    my_list = []
    for value in dictionary.items():
        temp_dictionary = {"char": "", "num": 0}
        temp_dictionary["char"] = value[0]
        temp_dictionary["num"] = value[1]

        my_list.append(temp_dictionary)

    my_list.sort(reverse=True, key=sort_on)
    
    return my_list
