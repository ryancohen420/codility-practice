"""
Explanation (in simple, question-style wording):

We need to find two positive integers A and B such that:
  - A + B = N
  - Neither A nor B contains the digit '0'

To do that:
  1. Try every A from 1 up to N–1.  
     hint: use a loop like `for A in range(1, N)`  
  2. Let B = N – A.  
     hint: compute it with `B = N - A`  
  3. Convert A and B to strings and make sure neither string has a '0'.  
     hint: check with `'0' not in str(A)` and `'0' not in str(B)`  
  4. As soon as we find such a pair, return [A, B].  
     hint: place `return [A, B]` inside the loop once the check passes

Full Problem Statement:

Given an integer N, find two positive integers A and B such that:
  • A + B = N  
  • Neither A nor B contains the digit '0' in its decimal representation

Implement a function:

    def solution(N)

that returns a list [A, B] satisfying the above. If more than one pair exists, return any one of them.

Constraints:
  • N is an integer within the range [2 .. 500_000]

Examples:
  • N = 12  
    Valid outputs: [7, 5], [5, 7], [6, 6], [4, 8]  
    Invalid: [10, 2] (because "10" has a 0), [0, 12]

  • N = 200  
    Valid outputs: [136, 64], [199, 1]

  • N = 101  
    [1, 100] is invalid (100 contains '0'); a valid output is [2, 99].

Pseudo-code:

    function solution(N):
        for A from 1 to N-1:
            B = N - A
            if noZero(A) AND noZero(B):
                return [A, B]

    function noZero(x):
        s = str(x)
        for each character c in s:
            if c == '0':
                return False
        return True
"""

def solution(N):
    for A in range(1, N):
        B = N - A
        if '0' not in str(A) and '0' not in str(B):
            return [A, B]

# --------------------------
# simple tests
if __name__ == '__main__':
    print(solution(12))   # e.g. [1, 11] or [7, 5]
    print(solution(200))  # e.g. [1, 199] or [136, 64]
    print(solution(101))  # e.g. [2, 99]
