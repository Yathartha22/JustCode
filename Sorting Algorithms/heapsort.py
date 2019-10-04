def min_heapify(ar, n, i):

    largest = i    # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and ar[i] < ar[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and ar[largest] < ar[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        ar[i], ar[largest] = ar[largest], ar[i]    # swap

        # Heapify the root.
        min_heapify(ar, n, largest)


def build_heap(ar, n):
    for i in range(n//2 - 1, -1, -1):
        min_heapify(ar, n, i)

n = int(input())
ar = [int(i) for i in input().split()]
build_heap(ar, n)
while n > 0:
    ar[0], ar[n-1] = ar[n-1], ar[0]    # pythonic swap
    n -= 1
    min_heapify(ar, n, 0)

print(ar)
print(list(reversed(ar)))
