def towerOfHanoi(discs: int = 5, source: str = "A", destination: str = "C", helper: str = "B") -> None:
    """
        A recursive function to generate moves for the tower of hanoi problem
    """

    if discs == 0:
        return None

    towerOfHanoi(discs-1, source, helper, destination)

    print(f"Move Disc from {source} to {destination}.")

    towerOfHanoi(discs-1, helper, destination, source)


if __name__ == "__main__":
    print(towerOfHanoi())
    print(towerOfHanoi(3))
    print(towerOfHanoi(8))
