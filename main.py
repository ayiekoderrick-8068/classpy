# STRING QUESTIONS 

# 1. First three characters
def first_three(text):
    if len(text) < 3:
        return text
    return text[:3]

print("String Q1 Results:")
print(first_three('ipy'))
print(first_three('python'))


# 2. Caesar encryption
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                start = ord('A')
                result += chr((ord(char) - start + shift) % 26 + start)
            # Handle lowercase letters
            else:
                start = ord('a')
                result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

print("\nString Q2 Result:")
print(caesar_encrypt("Hello World", 3))


# 3. Remove duplicate characters
def remove_duplicates(text):
    seen = ""
    for char in text:
        if char not in seen:
            seen += char
    return seen

print("\nString Q3 Result:")
print(remove_duplicates("pythonexercises"))


# 4. Delete all occurrences of a specified character
def delete_char(text, char_to_remove):
    result = ""
    for char in text:
        if char != char_to_remove:
            result += char
    return result

orig_str = "Delete all occurrences of a specified character in a given string"
print("\nString Q4 Result:")
print("Original string:\n" + orig_str)
print("Modified string:\n" + delete_char(orig_str, 'a'))


# 5. Count leap years in a range string
def count_leap_years(year_range):
    # Split the string by the dash
    parts = year_range.split("-")
    start_year = int(parts[0])
    end_year = int(parts[1])
    
    count = 0
    for year in range(start_year, end_year + 1):
        # Leap year math check
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            count += 1
    return count

print("\nString Q5 Results:")
print(count_leap_years("1981-1991"))
print(count_leap_years("2000-2020"))


# 6. Insert space before capital letters
def add_spaces(word):
    result = ""
    for char in word:
        if char.isupper() and result != "":
            result += " " + char
        else:
            result += char
    return result

print("\nString Q6 Results:")
print(add_spaces("PythonExercises"))
print(add_spaces("PythonExercisesPracticeSolution"))




# LIST QUESTIONS 

# 1. Square numbers between 1 and 30 (print first and last 5 elements)
squares = []
for i in range(1, 31):
    square = i * i
    if square >= 1 and square <= 30:
        squares.append(square)

# Print first 5 and last 5 combined or whatever fits
print("List Q1 Result:")
print("Valid squares inside range:", squares)


# 2. Difference between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
difference = []
for item in list1:
    if item not in list2:
        difference.append(item)
for item in list2:
    if item not in list1:
        difference.append(item)

print("\nList Q2 Result:")
print(difference)


# 3. Concatenate list with range 1 to n
sample_list = ['p', 'q']
n = 5
concatenated = []
for i in range(1, n + 1):
    for letter in sample_list:
        concatenated.append(letter + str(i))

print("\nList Q3 Result:")
print(concatenated)


# 4. Convert lists to a list of dictionaries
names = ["Black", "Red", "Maroon", "Yellow"]
codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
dict_list = []
for i in range(len(names)):
    new_dict = {'color_name': names[i], 'color_code': codes[i]}
    dict_list.append(new_dict)

print("\nList Q4 Result:")
print(dict_list)


# 5. Move all zeros to the end
orig_list = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
no_zeros = []
zeros_only = []
for num in orig_list:
    if num == 0:
        zeros_only.append(0)
    else:
        no_zeros.append(num)
final_list = no_zeros + zeros_only

print("\nList Q5 Result:")
print(final_list)


# 6. Round, min/max, multiply by 5, unique ascending order output
floats_list = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
rounded_list = []
for num in floats_list:
    rounded_list.append(round(num))

min_val = min(rounded_list)
max_val = max(rounded_list)

# Multiply unique numbers by 5
unique_nums = []
for num in rounded_list:
    if num not in unique_nums:
        unique_nums.append(num)
unique_nums.sort()

mult_output = ""
for num in unique_nums:
    mult_output += str(num * 5) + " "

print("\nList Q6 Result:")
print("Minimum value:", min_val)
print("Maximum value:", max_val)
print("Result:\n" + mult_output.strip())


# 7. Count number of lists inside a list
def count_nested_lists(big_list):
    count = 0
    for item in big_list:
        if type(item) == list:
            count += 1
    return count

print("\nList Q7 Results:")
print(count_nested_lists([[1, 3], [5, 7], [9, 11], [13, 15, 17]]))
print(count_nested_lists([[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]))






# DICTIONARY QUESTIONS 

# 1. Concatenate dictionaries
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
new_dic = {}
new_dic.update(dic1)
new_dic.update(dic2)
new_dic.update(dic3)

print("Dict Q1 Result:")
print(new_dic)


# 2. Print distinct values in a dictionary list
sample_dict_list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
unique_vals = set()
for d in sample_dict_list:
    for val in d.values():
        unique_vals.add(val)

print("\nDict Q2 Result:")
print("Unique Values:", unique_vals)


# 3. Combine dictionaries using Counter class
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
combined = Counter(d1) + Counter(d2)

print("\nDict Q3 Result:")
print(combined)


# 4. Top three items in a shop
shop_data = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Simple sorting loop for students
sorted_items = sorted(shop_data.items(), key=lambda x: x[1], reverse=True)

print("\nDict Q4 Result:")
for i in range(3):
    print(sorted_items[i][0], sorted_items[i][1])


# 5. Filter dictionary based on values (> 170)
original_org = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
filtered_dict = {}
for name, score in original_org.items():
    if score > 170:
        filtered_dict[name] = score

print("\nDict Q5 Result:")
print(filtered_dict)


# 6. Extract list of values where subject matches
def extract_subject_values(dict_list, subject):
    results = []
    for d in dict_list:
        if subject in d:
            results.append(d[subject])
    return results

marks_data = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
print("\nDict Q6 Results:")
print(extract_subject_values(marks_data, 'Science'))
print(extract_subject_values(marks_data, 'Math'))




# TUPLE QUESTIONS 

# 1. Replace the last value of tuples in a list
tuple_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
modified_tuples = []
for t in tuple_list:
    # Convert to list to change value, then convert back
    temp = list(t)
    temp[-1] = 100
    modified_tuples.append(tuple(temp))

print("Tuple Q1 Result:")
print(modified_tuples)


# 2. Remove empty tuples from a list
sample_tuples = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
cleaned_tuples = []
for t in sample_tuples:
    # Check if tuple is not empty
    if len(t) > 0:
        cleaned_tuples.append(t)

print("\nTuple Q2 Result:")
print(cleaned_tuples)


# 3. Sort a tuple by its float element (Descending order based on sample output)
item_data = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Sort using float conversion for accuracy
item_data.sort(key=lambda x: float(x[1]), reverse=True)

print("\nTuple Q3 Result:")
print(item_data)


# 4. Convert a given tuple of positive integers into a single integer
def tuple_to_int(tup):
    string_nums = ""
    for num in tup:
        string_nums += str(num)
    return int(string_nums)

print("\nTuple Q4 Results:")
print(tuple_to_int((1, 2, 3)))
print(tuple_to_int((10, 20, 40, 5, 70)))


# 5. Compute the sum of all elements of each tuple inside a list
def sum_tuple_elements(list_of_tups):
    sums = []
    for tup in list_of_tups:
        sums.append(sum(tup))
    return sums

print("\nTuple Q5 Results:")
print(sum_tuple_elements([(1, 2), (2, 3), (3, 4)]))
print(sum_tuple_elements([(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]))


# 6. Calculate the average value of numbers across columns in a tuple of tuples
def average_tuple_columns(tuple_of_tuples):
    num_of_tuples = len(tuple_of_tuples)
    num_of_elements = len(tuple_of_tuples[0])
    averages = []
    
    for i in range(num_of_elements):
        column_sum = 0
        for j in range(num_of_tuples):
            column_sum += tuple_of_tuples[j][i]
        averages.append(column_sum / num_of_tuples)
    return averages

tup_data1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
tup_data2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

print("\nTuple Q6 Results:")
print(average_tuple_columns(tup_data1))
print(average_tuple_columns(tup_data2))





# SETS QUESTIONS

my_set = {10, 20, 30, 40, 50}
other_set = {40, 50, 60, 70, 80}

# 1. Length of a set
print("Sets Q1 Result:", len(my_set))

# 2. Add member to a set
my_set.add(60)
print("Sets Q2 Result (Added 60):", my_set)

# 3. Remove item from a set
my_set.remove(10)
print("Sets Q3 Result (Removed 10):", my_set)

# 4. Intersection of sets
intersection_set = my_set.intersection(other_set)
print("Sets Q4 Result (Intersection):", intersection_set)

# 5. Union of sets
union_set = my_set.union(other_set)
print("Sets Q5 Result (Union):", union_set)

# 6. Set difference
difference_set = my_set.difference(other_set)
print("Sets Q6 Result (Difference):", difference_set)

# 7. Maximum and minimum values in a set
print("Sets Q7 Result: Max =", max(my_set), ", Min =", min(my_set))
