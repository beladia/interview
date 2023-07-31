class Solution:
  def Fibonacci(self, n):
    fib_number = 0
    for i in range(len(n)):
      fib_number += i
      print (fib_number)

Solution sol = Solution()
sol.Fibonacci(5)
