def merge(left, right):
    if len(left) < 1:
        return right

    if len(right) < 1:
        return left

    left_index = right_index = 0
    result = []

    while len(result) < len(left) + len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1

        else:
            result.append(right[right_index])
            right_index += 1

        if len(right) == right_index:
            result += left[left_index:]
            break

        if len(left) == left_index:
            result += right[right_index:]
            break

    return result


def merge_sort(nums):
    if len(nums) < 2:
        return nums
    else:

        pivot = len(nums) // 2
        return merge(left=merge_sort(nums[:pivot]),
                     right=merge_sort(nums[pivot:]))


random_list_for_sort = [11, 5, 21, 4, 0, 9, 44, 0, 3, 2, 8]
print("Исходный список: ", random_list_for_sort)
print("Отсортированый:  ", merge_sort(random_list_for_sort))
