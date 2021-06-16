# Loop
letters3 = ['q', 'c', 'j', 'a', 'e', 'o', 'b', 'f']
for item in letters3:
    print(item)

# To be able to return INDEX and VALUES both together we ca use 'ENUMERATE" method
letters3 = ['q', 'c', 'j', 'a', 'e', 'o', 'b', 'f']
for index, item in enumerate(letters3):
    print(index, item)


# To be able to return INDEX and VALUES both , but starting with Specific INDEX  then we ca use 'ENUMERATE" method
    letters3 = ['q', 'c', 'j', 'a', 'e', 'o', 'b', 'f']
    for index, item in enumerate(letters3, start=1):
        print(index, item)
