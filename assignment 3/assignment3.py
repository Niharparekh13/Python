def list_to_dict(lst):
  for a in range (0,len(lst)):
    a = {lst[i]: lst[i + 1] for i in range(0, len(lst),2)}
    return a


lst = ['a', 1, 'b', 2, 'c', 3]
print(list_to_dict(lst))