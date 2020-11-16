#declaration for a list
values = []

values.append(10)
values.append(8)
values.append(7)
values.append(9)
values.append(6)
values.insert(0,3)


print(values)
print("first value",values[0])
print("last value",values[-1])

print('values/n')
for index in range(0, len(values)):
    print(values[index])
