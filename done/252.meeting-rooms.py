from functools import cmp_to_key

class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        sorted_intervals = sorted(intervals)

        for i in range(len(sorted_intervals) - 1):
            if sorted_intervals[i][1] > sorted_intervals[i + 1][0]:
                return False
            
        return True


def run_test():
    test_cases = [
        [[[0, 30], [5, 10], [15, 20]], False],
        [[[7, 10], [2, 4]], True],
        [[[7, 10], [10, 12]], True]
    ]

    for case, anwser in test_cases:
        assert(Solution().canAttendMeetings(case) == anwser)


if __name__ == '__main__':
    run_test()