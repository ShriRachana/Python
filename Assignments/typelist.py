l = ['magical unicorns',19,'hello',98.98,'world']


item_type_set = set() # Create an empty set to add unique item types to it.
nums = []
string_lst = []

for item in l:

    item_type = type(item) # This returns the type

    item_type_set.add(item_type)

    #Test for each data type.
    if item_type == int:
        float_item = float(item)
        nums.append(float_item)


    elif item_type == float:
        nums.append(item)

    elif item_type == str:
        string_lst.append(item)



if len(item_type_set) > 1:

    print ("The array you entered is of mixed type")

elif len(item_type_set) == 1:

    for item in item_type_set:

        if item == str:
            str_type = 'string'
            print ("The array you entered is of %s type" %(str_type))

        elif item == int:
            int_type = 'integer'
            print("The array you entered is of %s type" % (int_type))

        elif item == float:

            float_type = 'float'
            print("The array you entered is of %s type" % (float_type))

if len(string_lst) > 0:
    new_string = string_lst[0]

    for string_item in string_lst[1:]:
        new_string += ' ' + string_item

    print ('String: ' + new_string)


counter = 0.0
for number in nums:

    counter += number

print ("Sum: " + str(counter))
