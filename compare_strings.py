def compare_strings(str_1, str_2):
    if str_1.lower() == str_2.lower():
        return 1 
    elif len(str_1) > len(str_2):
        return 2 
    elif str_2.lower() == 'learn':
        return 3 


input_string_1 = input('Get first string: ')
input_string_2 = input('Get second string: ')

print(compare_strings(input_string_1, input_string_2))

