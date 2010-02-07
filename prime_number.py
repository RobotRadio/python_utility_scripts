"""
  author : robotradio
  version : 2.6.2010
  description : a collection of prime number functions.
"""

"""
  Returns a boolean flag and message that will
  describe whether the passed number is prime
  or not.
"""
def is_prime(number):
    message = ""
    primality = False
    
    if(number == 0):        
	message = "Zero is not prime."
    elif(number % 2 == 0):
        message = "The number is even, thus cannot be prime."
    else:
        square_root_of_number = number**0.5
        for test_number in range(2, int(square_root_of_number)+1):
            if number % test_number == 0:
                message = str(number) + " is not prime."
                return [primality, message]

        message = str(number) + " is prime!"
        primality = True

    return [primality, message]


"""
  Returns a collection of prime numbers in between
  2 and some upper bound value.
"""
def get_primes_in(upperNumber):
    prime_numbers = []
    for number in range(2, upperNumber):
        [aPrime, aMessage] = is_prime(number)
        if(aPrime == True):
            prime_numbers.append(number)
    return prime_numbers

"""
  Prints all the prime numbers that are between
  2 and the passed number
"""
def print_prime_numbers_in(upperBound):
    primes = get_primes_in(upperBound)
    for number in primes:
        print number
            
        
    
                
                
        
        
    
