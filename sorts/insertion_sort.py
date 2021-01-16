# выталкиваем максимальные элементы
# минимальный элемент встает на свое место

def insertion_sort(nums):
    """ Сортировка вставками """
    for i in range(1, len(nums)):
        insert_element = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > insert_element:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = insert_element


random_list_for_sort = [11, 5, 21, 4, 0, 9, 44, 3, 2, 8]
print("Исходный список: ", random_list_for_sort)
insertion_sort(random_list_for_sort)
print("Отсортированый:  ", random_list_for_sort)