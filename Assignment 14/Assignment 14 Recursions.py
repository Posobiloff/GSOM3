#2.1 a function that for a given natural number n, calculates the sum of its digits

def digits_sum(number):
    if number < 10:
        return number
    else:
        return number % 10 + digits_sum(number // 10)

#2.2. a function that for a given natural number n, calculates the sum of all numbers from 0 up to and including the given number
def progress_sum(number):
    if number == 0:
        return number
    else:
        return number + progress_sum(number-1)
    
#2.3. Fibonacci series: a recursive function that calculates the Fibonacci value for a given number.
def fibonacci_series(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci_series(number-1)+fibonacci_series(number-2)