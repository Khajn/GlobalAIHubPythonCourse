list1 = [2,4,6,8]
list2 = [1,3,5,7,9]

t = list1 + list2
for j in range (len(t)):
  t[j]*=2
  print(t[j])
print(type(t))
