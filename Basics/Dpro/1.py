# fib by recursion

def fib(n):
    if n == 0:
        return 0
    memo = {}
    if n in memo.keys():
        return memo.get(n)
    else:
        a = fib_rec(n, memo)
    print(memo)
    return a


def fib_rec(n, memo):
    if n in memo.keys():
        return memo.get(n)

    if n < 3:
        memo[n] = 1
        return 1
    else:
        print("calculating for ", n)
        a = fib_rec(n-1, memo) + fib_rec(n-2, memo)
        memo.update({n: a})
        return a


print(fib(20))
