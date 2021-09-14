def getDuplicates(array: list) -> list:

    frequency = dict()
    duplicates = set()

    for element in array:
        frequency[element] = frequency.get(element, 0) + 1
        
        if frequency[element] > 1:
            duplicates.add(element)
        
    return list(duplicates)


getDuplicates([])


print(getDuplicates([4, 4, 7, 8, 8, 9]))
print(getDuplicates([2, 3, 6, 8, 90, 58, 58, 60]))