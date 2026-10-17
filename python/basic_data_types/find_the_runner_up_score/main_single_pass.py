# Challenge: Find the Runner-Up Score (single pass version)
# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
# Difficulty: Easy

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    biggest = float('-inf')
    runner_up = float('-inf')

    for num in arr:
        if num > biggest:
            runner_up = biggest
            biggest = num
        elif num > runner_up and num != biggest:
            runner_up = num

    print(runner_up)
