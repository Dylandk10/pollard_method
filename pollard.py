#This is for pollard p-1 method for finding ladder of primes and gcd
#written by Dylan Kelly for Discrete mathematics 265

#composite of odd number
n = 21
#the bound in which sets the bound for finding primes and pollard
bound = 35
#to hold all the primes in b
primes_in_b = []

#start the program
def main():
    find_primes_in_b(bound)
#method to pull all primes out of bound
def find_primes_in_b(bound):
    prime = False
    #loop through b and append all primes to array
    for i in range(2,bound):
        #get all the number between 2 and [i]
        for k in range(2, i):
            #if k > half of i pass becuase no number can be divided by more then its half
            if k > (i//2) + 1:
                continue
            #if [i] divides any number from 2-i its not prime break
            if i % k == 0:
                prime = False
                break;
            #set prime to true but keep looping
            else:
                prime = True
        #append the primes to the array
        if prime:
            primes_in_b.append(i)

    #call the next step
    p_minus_one(n, primes_in_b)

#method to preform the ladder of c with primes
def p_minus_one(n, primes_in_b):
    #the number to begin the ladder could be arbitrary
    c = 2
    #loop through prime array
    for p in primes_in_b:
        #set the power of the prime sin pwoer_prime
        power_prime = p
        #while laddering if it greater then bound stop
        while power_prime < bound:
            #raise c to the power of the prime
            c = c**p
            #mod c by the n value
            c = c % n
            #set the power prime multiplied by all primes(kinda like lcm)
            power_prime = power_prime * p
    #call th next step of finding the gcd
    g = find_gcd(c-1, n)

    #if g is 1<g<n then its valid else its not valid and most likely 1
    if g > 1 and g < n:
        print("The g is " + str(g) + " and is valid bc it's between 1<" + str(g) + "<" + str(n))
    else:
        print("The g is " + str(g) + " and g is not valid and is not between 1<" + str(g) + "<" + str(n))

#using euclidean algorithm find the gcd
def find_gcd(c_minus_one, n):
    while (n):
        c_minus_one, n = n, c_minus_one % n
    return c_minus_one

if __name__ == "__main__":
    main()
