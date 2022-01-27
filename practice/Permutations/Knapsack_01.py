def knapsack01(values: list, weights: list, size: int, weight: int) -> int:
    """
        Returns the maximum value that can be carried in the knapsack of the given weight.
    """

    if size == 0 or weight == 0:
        return 0
    
    if weights[size-1] > weight:
        return knapsack01(values, weights, size-1, weight)

    return max(knapsack01(values, weights, size-1, weight-weights[size-1])+values[size-1], knapsack01(values, weights, size-1, weight))



if __name__ == "__main__":

    print(knapsack01([100, 50, 150], [10, 20, 30], 3, 50))