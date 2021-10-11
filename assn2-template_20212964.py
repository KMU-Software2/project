import time
import random

# Define function of sequential search.
def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if target == nbrs[i]:
            return i
    return "Not in list."


# Define function of recursive-binary search.
def recbinsearch(L, l, u, target):
    if l > u:
        return "Not in list."
    midNum = L[(l + u) // 2]
    if target == midNum:
        return None
    if target < midNum:
        u = (l + u) // 2 - 1
    else:
        l = (l + u) // 2 + 1
    return recbinsearch(L, l, u, target)

### Make list of numbers.
numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]
numbers = sorted(numbers)

# Make list of targets.
numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]


# sequential search
ts = time.time()
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == "Not in list.":
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))


# recursive-binary search
ts = time.time()
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers), target)
    if idx == "Not in list.":
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))
