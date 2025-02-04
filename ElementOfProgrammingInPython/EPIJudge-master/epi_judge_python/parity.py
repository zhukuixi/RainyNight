from test_framework import generic_test

from sys import exit
# def parity(x: int) -> int:
#     # TODO - you fill in here.
#     count = 0 
#     while x:
#         count += x&1
#         x = x>>1
#     if count%2!=0:
#         return 1
#     else:
#         return 0

# def parity(x: int) -> int:
#     # TODO - you fill in here.
#     count = 0 
#     while x:
#         x &= x-1
#         count ^= 1
#     return count

## 1.BruteForce - O(n)
def parity(x: int) -> int:
    # TODO - you fill in here.
    answer = 0
    while x:
        if x&1:
            answer ^= 1
        x>>=1
    return answer

## 2. Drop the most right 1
def parity(x: int) -> int:
    # TODO - you fill in here.
    answer = 0
    while x:
        answer ^= 1
        x= x&(x-1)
    return answer

## 3. logN
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
