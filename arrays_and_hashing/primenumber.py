
def check_for_prime(numbers):

    if (numbers==2) | (numbers == 3) | (numbers == 5):
        return True

    if (numbers%2==0) or (numbers%3==0) or (numbers%5==0):
        return False
    
    i = 5
    while i*i <=numbers:
        if numbers%i==0 | numbers%(i+2) == 0:
            return False
        i += 6
    
    return True

for i in range(201,300):    
    if check_for_prime(i):
        print(i)

'''
211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293
'''