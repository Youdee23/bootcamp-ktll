def count_up(stop, start=0):
    for num in range(start, stop + 1):
        print(num)


def display_pattern(start, stop):
    if start <= 0:
        print('The starting number must be greater than 0')
        return
    
    if start >= stop:
        print('The starting number must be less than the stop')

    for num in range(start, stop + 1):
        print('#' * num)
    

display_pattern(15, 12)

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
# Solution(Using for loop)
for i in range(0, 11):
    print(i)

# Using while loop
digit = 0
while digit <= 10:
    print(digit)
    digit += 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
# Using for loop
for i in range(0, 11, -1):
    print(i)

# Using while loop
number = 10
while number >= 0:
    print(number)
    number -= 1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######

# Solution
for num in range(1, 8):
    print('#' * num)

# 4. Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

# Solution
for u in range(9):
    for i in range(9):
        print('#', end='')
    print()

'''
5. Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
'''
# Solution
for num in range(11):
    print(f'{str(num)} * {str(num)} = {num * num}')

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
p_languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] 
for language in p_languages:
    print(language)

# Use for loop to iterate from 0 to 100 and print only even numbers
for number in range(101):
    if number % 2 == 0:
        print(number)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for digit in range(101):
    if digit % 2 != 0:
        print(digit)

'''
7. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
The sum of all numbers is 5050.
'''

sum = 0
for number in range(101):
    sum += number
print(sum)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_evens = 0
for number in range(101):
    if number % 2 == 0:
        sum_evens += number
print(sum_evens)

sum_odds = 0
for number in range(101):
    if number % 2 != 0:
        sum_odds += number
print(sum_odds)
# The sum of all evens is 2550. And the sum of all odds is 2500.


# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
for country in countries:
    if 'land' in country:
        print(country)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in fruits[::-1]:
    print(fruit)

# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world






