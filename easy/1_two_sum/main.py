from solution import Solution


def main():
    nums = list(map(int, input().split()))
    target = int(input())

    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)


if __name__ == "__main__":
    main()
