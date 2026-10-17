# Challenge: Find the Runner-Up Score
# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
# Difficulty: Easy

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    clean_list = set(arr)
    sorted_list = sorted(clean_list, reverse=True)

    print(sorted_list[1])
