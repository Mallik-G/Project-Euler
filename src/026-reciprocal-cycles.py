#!/usr/bin/python3
# mari wahl @2014
# marina.w4hl at gmail


'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10  =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

'''

def perm_item(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for (index, elmt) in enumerate(elements):
            other_elmts = elements[:index]+elements[index+1:]
            for permutation in perm_item(other_elmts):
                yield [elmt] + permutation


def lex_perm(l1, n):
    perm_list = list(perm_item(l1))
    return sorted(perm_list)[n-1]


def main():
    import time
    start = time.time()

    l1 = [0,1,2,3,4,5,6,7,8,9]
    n = 10**6
    print(lex_perm(l1, n))

    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))

if __name__ == '__main__':
    main()

