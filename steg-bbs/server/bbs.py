import math

class BBS:

    def __init__(self, p, q, seed):

        if p % 4 != 3 or q % 4 != 3:
            raise ValueError("p and q must satisfy p ≡ 3 (mod 4)")

        self.n = p * q

        if math.gcd(seed, self.n) != 1:
            raise ValueError("seed must satisfy gcd(seed,n)=1")

        self.state = seed


    def next(self):

        self.state = (self.state * self.state) % self.n
        return self.state
