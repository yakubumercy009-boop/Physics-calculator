def sum_numbers(numbers):
    """Sum a list of numbers"""
    return sum(numbers)

def average_numbers(numbers):
    """Returns average/mean of numbers in a list"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median_mode(numbers):
    """Returns the median and mode of the list"""
    if not numbers:
        return None, None
    med = statistics.median(numbers)
    try:
        mod = statistics.mode(numbers)
    except statistics.StatisticsError:
        counter = Counter(numbers)
        max_count = max(counter.values())
        mod = [k for k, v in counter.items() if v == max_count]
    return med, mod

if __name__ =="__main__":
    nums = ["2" "4" "6" "8" "10"]
    print("Sum:", sum_numbers(nums))
    print("Average:", average_numbers(nums))
    median, mode = median_mode(nums)
    print("Median:", median)
    print("Mode:", mode)