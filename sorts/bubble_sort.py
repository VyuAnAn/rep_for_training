# Сложность O(n^2), если список отсортирован в обратном порядке

def bubble_sort(nums):
    """ Пузырьковая сортировка """
    is_move = True
    while is_move:
        is_move = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                is_move = True


random_list_for_sort = [11, 5, 21, 4, 0, 9, 44, 3,  2, 8]
print("Исходный список: ", random_list_for_sort)
bubble_sort(random_list_for_sort)
print("Отсортированый:  ", random_list_for_sort)
