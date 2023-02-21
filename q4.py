# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
def is_leap_year(a_year):
    """Determine if a given year is a leap year"""
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0 and a_year % 100 == 0 and a_year == 0):
        return True 
    else: return False 
print(is_leap_year(2020))
 

