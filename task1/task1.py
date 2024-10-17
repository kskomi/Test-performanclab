import sys

def circular_array(n, m):
    arr = list(range(1, n + 1))
    result = []
    index = 0

    while len(result) < n:
        result.append(arr[index])
        index = (index + m - 1) % n

    print("".join(map(str, result)))

if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    circular_array(n, m)

