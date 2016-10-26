from CreateEncryptionKey import Encryption

def get_prime_nums():
    prime_nums = []
    while True:
        p = input("Enter p (Must be prime number): ")
        if (check_if_prime(p) == True):
            prime_nums.append(p)
            break
        else:
            print "Please choose a number that is prime"

    while True:
        q = input("Enter q (Must be prime number): ")
        if (check_if_prime(q) == True):
            prime_nums.append(q)
            break
        else:
            print "Please choose a number that is prime"

    return prime_nums


def check_if_prime(num):
    if (num == 1):
        return True

    for i in range(2, (num)):
        if num % i == 0:
            return False
        else:
            return True

# MAIN
prime = get_prime_nums()
e_key = Encryption(prime[0], prime[1])
print e_key.create_encryption_keys()