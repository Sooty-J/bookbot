def word_count(book_string):
    count = 0 
    indiviual_words = book_string.split()
    #return indiviual_words
    for word in indiviual_words:
        count += 1
    return count

def char_count(book_content):
    characters = {}
    lower_case = book_content.lower()
    for char in lower_case:
        if char in characters:
            characters[char] = characters[char] +1
        else:
            characters[char] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def sort(my_dictionary):
    my_list = []
    for char, num in my_dictionary.items():
        dict_item = {"char":char, "num":num}
        my_list.append(dict_item)
    my_list.sort(reverse=True, key=sort_on)
    return my_list

