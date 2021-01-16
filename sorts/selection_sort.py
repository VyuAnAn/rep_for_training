# Сегментируем список на две части: отсортированный и неотсортированный
# Находим наименьший элемент и меняем с первым,
# находим наименьший элемент из оставшихся и меяем со вторым и т.д.


def selection_sort(nums):
    """ Сортировка выборкой """
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
        print(nums)


random_list_for_sort = [11, 5, 21, 4, 0, 9, 44, 3, 2, 8]
print("Исходный список: ", random_list_for_sort)
selection_sort(random_list_for_sort)
print("Отсортированый:  ", random_list_for_sort)



