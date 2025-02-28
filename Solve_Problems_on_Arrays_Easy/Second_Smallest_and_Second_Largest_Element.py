class SecondSmallestAndSecondLargestElement:
    def __init__(self, arr):
        self.arr = arr
        self.arr_len = len(arr)

    def find_second_smallest_and_second_largest(self):
        if self.arr_len < 2:
            return None, None  # Not enough elements to find second smallest and largest

        # Initialize variables for smallest and second smallest
        smallest = float("inf")
        second_smallest = float("inf")

        # Initialize variables for largest and second largest
        largest = float("-inf")
        second_largest = float("-inf")

        for num in self.arr:
            # Finding smallest and second smallest
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif smallest < num < second_smallest:
                second_smallest = num

            # Finding largest and second largest
            if num > largest:
                second_largest = largest
                largest = num
            elif largest > num > second_largest:
                second_largest = num

        return second_smallest, second_largest


# Example usage
arr = [4, 5, 2, 3, 6, 1]
sse = SecondSmallestAndSecondLargestElement(arr)
print(sse.find_second_smallest_and_second_largest())  # Output: (2, 5)
