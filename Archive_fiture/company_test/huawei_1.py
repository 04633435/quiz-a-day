if __name__ == "__main__":
    n = 256
    print(bin(n))
    lst = []
    for _ in range(4):
        lst.append(n & ((1 << 8)- 1))
        print(bin((1 << 8) - 1))
        n >>= 8
    print(lst)