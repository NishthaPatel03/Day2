#In python values are passed by reference.
# It means that if we change values in function then it will changed in calling function also.

def pass_by_reference(list):
    list.append([1,2,3])
    print(list)
    return

list=[1,2,3]
pass_by_reference(list)
print(list)
