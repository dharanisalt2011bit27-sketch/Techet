def max_subarray_sum(arr, k):
    n = len(arr)
    if n < k:
        return "Invalid: Array smaller than window size"
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(f"Max sum of subarray size {k}:", max_subarray_sum(nums, k)) 
