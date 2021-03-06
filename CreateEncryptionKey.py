import random

class Encryption:

    def __init__(self, p, q):
        self.p = p
        self.q = q


    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a


    def coprime(self, a, b):
        return self.gcd(a, b) == 1


    def find_e(self, n, phi_n):
        available = []
        for j in range(2,phi_n):
            if (self.coprime(j,phi_n) == True):
                available.append(j)
        return random.choice(available)


    def create_encryption_keys(self):
        n = self.p * self.q
        phi_n = (self.p-1) * (self.q-1)
        e = self.find_e(n, phi_n)
        encryption_keys = [e,n]

        return encryption_keys




