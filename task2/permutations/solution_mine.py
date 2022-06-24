
test_List1 = [3, 1, 4, 1]
test_List2 = [3, 1, 4, 1, 5, 9]


def solution(l):
    import itertools
    N = len(l)
    C = 0

    # gen our dic
    lAux = [tuple(l)]
    original_numbers = {}
    while N > 0 and C <= 999:
        if (N == len(l)):
            original_numbers[N] = set(lAux)
        else:
            if N+1 in original_numbers:
                prevListofNumbers = original_numbers[N+1]
                tempList = set()
                for listitem in prevListofNumbers:
                    for j in range(len(listitem)):
                        newList = tuple(
                            [x for i, x in enumerate(listitem) if i != j])
                        tempList.add(newList)
                original_numbers[N] = tempList
        N -= 1
        C += 1

    sols2 = set()
    for idx, items in original_numbers.items():
        for numberSets in items:
            sumSet = sum(numberSets)
            # here calculate perms
            if sumSet % 3 == 0:
                biggerN = -1
                perms = set(itertools.permutations(numberSets))
                for perm in perms:
                    permNumber = int(''.join(map(str, perm)))
                    if permNumber > biggerN:
                        biggerN = permNumber
                # security concerns
                if biggerN > 0:
                    sols2.add(biggerN)

    if sols2:
        return max(sols2)
    else:
        return 0


# print(solution(test_List2))
# print(solution(test_List1))
# print(solution([0]))
# print(solution([1]))
# print(solution([3]))
# print(solution([3,1]))
