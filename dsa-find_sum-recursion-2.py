def new_sum(n):
    if n==1:
        print(n)
        return 1
    return n+new_sum(n-1)

if __name__ == '__main__':
    print(new_sum(5))