from enum import Enum
import primality_tests as ptests

class PrimalityTests(Enum):
    TRIAL = ptests.trial_primality
    TRIAL_SQUARED = ptests.trial_primality_squared

class Primes:
    def __init__(self, start=2, primality_test=PrimalityTests.TRIAL):
        self.prime = start

    def __iter__(self):
        return self

    @staticmethod
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def __next__(self):
        next_prime = self.prime + 1
        while not self.is_prime(next_prime):
            next_prime += 1
        self.prime = next_prime
        return self.prime
