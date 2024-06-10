def take_vowel(vowel, *str_args):
    lst = []
    for str_arg in str_args:
        if str_arg[0] in vowel_list:
            lst.append(str_arg)
    return lst


vowel_list = ['a', 'e', 'i', 'o', 'u']
print(take_vowel(vowel_list, 'orange', 'banana', 'apple', 'king'))


