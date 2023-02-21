# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    """Determine whether a list of numbers is consecutive"""
    for i in range(len(a_list)-1):
        if a_list[i]+1 != a_list[i+1]:
            return False
    return True        

print(is_consecutive([1,2,3,4]))