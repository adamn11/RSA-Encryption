class Alphabet:
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


    def __init__(self, alpha):
        self.alpha = alpha


    def __init__(self, num):
        self.num = num


    def alpha_to_num(self):
        return self.alphabet.index(self.alpha) + 1


    def num_to_alpha(self):
        return self.alphabet[self.num - 1]