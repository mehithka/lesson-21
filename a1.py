test_dictionary = {'mehith' : 2 , 'Vijendra':2 , 'Karacasia':2, 'hello':1}
print('the original dictionsary is:',test_dictionary)

k=2
res=0

for key in test_dictionary:
    if test_dictionary[key]==k:
        res = res + 1

print("Frequency of K is: " + str(res))
