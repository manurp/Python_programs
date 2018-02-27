# Sorting challenge

'''
*Sort a string in such a way that
*All sorted lowercase letters are ahead of uppercase letters.
*All sorted uppercase letters are ahead of digits.
*All sorted odd digits are ahead of sorted even digits.
'''

# The one line solution
print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')



# def my_sort(str_to_sort):
#     lower_char_list = []
#     upper_char_list = []
#     numeral_list = []

#     for char in str_to_sort:
#         # If it is a numeral
#         if ord(char) < 58:
#             numeral_list.append(char)
#         # If it is a upper case letter
#         elif ord(char) < 91:
#             upper_char_list.append(char)
#         else:
#             lower_char_list.append(char)
#     return lower_char_list + upper_char_list + numeral_list


# s = input()
# s_l = my_sort(s)
# print(s_l)
