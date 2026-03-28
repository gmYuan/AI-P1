
# ---------------------------------------------------------------------------
words = ["hello", "world", "python", "programming"]
del words
# print(words)   # NameError: name 'words' is not defined



my_list_pop_no_index = [10, 20, 30]
# last_element = my_list_pop_no_index.pop()
# print(last_element)
# print(my_list_pop_no_index)

last_element = my_list_pop_no_index.pop(1)
print(last_element)
print(my_list_pop_no_index)
