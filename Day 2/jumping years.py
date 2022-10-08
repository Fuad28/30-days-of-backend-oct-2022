import math

def is_leap_year(year):
    if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        return True
    return False

def leap_year(Y: int, N: int) -> list[int] :
    """
    Gets N leap years after year, Y.

    Parameters:
    ----------
    Y: int, a year.
    N: int, a number of years after Y

    Returns:
    --------
    A list of years after Y of length N
    """

    if (type(Y) != int) or (type(N) != int):
        print("The two arguments must be integers")
        return None

    years= []

    if not is_leap_year(Y):
        next_years= [Y+1, Y+2, Y+3]
        Y= [yr for yr in next_years if is_leap_year(yr)][0]
        years.append(Y)
        
        for i in range(1, N): years.append(Y + 4*i)

    else:
        for i in range(1, N+1): years.append(Y + 4*i)
    
    print(f'Leap years {years}')
    return None


# Test
leap_year(2020.3, 3)
leap_year(2020, 3.4)
leap_year('2020', 3.5)
leap_year(2020, 3)
leap_year(1995, 5)
leap_year(2032, 4)

        
    
