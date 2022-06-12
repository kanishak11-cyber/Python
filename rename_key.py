target_dict = [{'name': 'John', 'age': '20'}, {
    'name': 'Bob', 'age': '30'}, {'name': 'Marry', 'age': '40'}]
new_keys = ['name', 'age']
for key, n_key in zip(target_dict.keys(), new_keys):
    target_dict[n_key] = target_dict.pop(key)
print("updated dict"+target_dict)
