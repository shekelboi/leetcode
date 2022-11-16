def heightChecker(self, heights):
    expected = sorted(heights)
    return sum([1 for i, height in enumerate(heights) if height != expected[i]])
