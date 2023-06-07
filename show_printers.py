def find_colon_index(txt):
    return txt.find(':')


text = 'model:HP'

print(text[:find_colon_index(text)])
print(text[find_colon_index(text) + 1:])
print(find_colon_index(text))
