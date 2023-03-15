from test_framework import generic_test
from sys import exit

def parity(x: int) -> int:
    # TODO - you fill in here.
    x ^= x>>32
    x ^= x>>16
    x ^= x>>8
    x ^= x>>4
    x ^= x>>2
    x ^= x>>1
    
    return x&1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
