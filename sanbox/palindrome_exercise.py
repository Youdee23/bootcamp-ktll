# def test_4_palindrome(word):
#     if word[0] == word[-1] and word[1] == word[-2]:
#         return True
#     return False


# test_4_palindrome("noon")

items = ['pen', 'eraser', 'ruler', 'gum', 'chalk']
stuff = ['book', 'pen', 'pencil', 'stick', 'board']

unique_items = [i for i in stuff if i not in items]
print(unique_items)


def groups_per_user(dictionary):
    new_dict = {}
    new_list = []
    for k, v in dictionary.items():
        for i in v:
            new_dict[i] = new_list
            new_list.append(k)
    return new_dict


dictionary = {'local': ['admin', 'userA'], 'public': ['admin', 'userB'], 'administrator': ['admin']}
print(groups_per_user(dictionary))
