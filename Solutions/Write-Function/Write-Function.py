
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400 == 0:
        leap = True
    elif year%100 == 0:
        return leap
    elif year%4 == 0: 
        leap = True
        
    return leap