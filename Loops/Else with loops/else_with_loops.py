i = 0
while i < 5:
    print('it\'s less than 5')
    i += 1
else:
    print('and now it\'s 5')

for i in range(1, 5):
    if(i == 3):
        break
    print(i)
else:
    print("for loop is done")

print("Outside the for loop")
