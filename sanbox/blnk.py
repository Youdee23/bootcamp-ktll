result = lambda x: x ** 5
print(result(10))

numbers = [48, 16, 37, 4, 12, 2]
outcome = [num ** 2 for num in numbers]
print(outcome)

res = zip(numbers, outcome)
print(list(res))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_2 = [(lambda num: num ** num)(num) for num in my_list]
print(my_list_2)

numbers = [48, 16, 37, 4, 12, 2]
outcme = list(zip(map(lambda x: x ** 2, numbers), numbers))
print(outcme)


# Classwork
chem_scores = [66, 90, 59, 76, 60, 88, 74, 81, 65]
print(list(filter(lambda x: x % 2 != 0, chem_scores)))

# Another classwork
my_names = ['olumide', 'akinremi', 'josiah', 'temidayo', 'omoseun']
print(list(filter(lambda word: len(word) <= 7, my_names)))
