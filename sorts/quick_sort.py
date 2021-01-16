
def quick_sort(nums):
    """ Быстрая сотрировка"""
    n = len(nums)

    if n < 2:
        return nums

    low, same, high = [], [], []
    pivot = nums[n // 2]

    for i in range(n):
        if nums[i] < pivot:
            low.append(nums[i])
        elif nums[i] > pivot:
            high.append(nums[i])
        else:
            same.append(nums[i])

    return quick_sort(low) + same + quick_sort(high)


random_list_for_sort = [11, 5, 21, 4, 0, 9, 44, 3, 2, 8]
print("Исходный список: ", random_list_for_sort)
print("Отсортированый:  ", quick_sort(random_list_for_sort))
