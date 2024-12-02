my_array = [1, 2, 3, 4, 5]

print(my_array)

my_array[0] = 10
my_array.append(6)
my_array.insert(1, 16)
my_array.remove(3)

print(my_array)

for item in my_array:
  print(item)

# Slicing
sub_array = my_array[1:4]
print(sub_array)