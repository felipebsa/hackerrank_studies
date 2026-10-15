# Challenge: Loops
# Link: https://www.hackerrank.com/challenges/python-loops
# Difficulty: Easy

if __name__ == '__main__':
    n = int(input())
    for i in map(lambda i: i ** 2, range(n)):
        print(i)
