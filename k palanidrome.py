import sys

MOD = 10**9 + 7

def getSum(N):
    res = 1
    for _ in range(N):
        res = (res * 26) % MOD
    if N % 2 == 0:
        res = (res * res) % MOD
    else:
        res = (res * res * 26) % MOD
    return res

def main():
    N = int(sys.stdin.readline().strip())
    result = getSum(N)
    print(result)

if __name__ == "__main__":
    main()
