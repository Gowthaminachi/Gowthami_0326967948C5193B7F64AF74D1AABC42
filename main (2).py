# 1.1 Implement a recursive function to calculate the factorial of a given number


def recur_factorial(n):

  if n == 1:

    return n

  else:

    return n * fact_rec(n - 1)


num = int(input("Enter a number: "))
res = fact_rec(number)
print("the factorial of {}is{}.".format(number, res))# 1.1 Implement a recursive function to calculate the factorial of a given number


def recur_factorial(n):

  if n == 1:

    return n

  else:

    return n * fact_rec(n - 1)


num = int(input("Enter a number: "))
res = fact_rec(number)
print("the factorial of {}is{}.".format(number, res))￼Not
