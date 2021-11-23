from merge_sort import mergesort
# array_test = [9, 12]  # 1
# array_test = [9, 10]  # 2
# array_test = [9, 10, 12, 14, 15, 40, 50, 51, 52, 53, 54, 55, 56, 57, 0, 0, 0, 0]  # 12
# array_test = [1, 0, 0]  # 3

# array_test = []  # 0
# array_test = [0, 0, 0, 0]  # 4
# array_test = [14, 15, 0, 0]  # 4


def poker(array):
    # якщо пустий масив то макс послідовність 0
    if len(array) == 0:
        return 0

    max_jokers = 0
    sorted_array = mergesort(array, 'asc')
    # рахуємо джокери :)
    for x in sorted_array:
        if x == 0:
            max_jokers = max_jokers + 1

    # working_array основний масив без джокерів
    # видалити дублікати
    working_array = list(dict.fromkeys(sorted_array))

    # remove 0 from beginning якщо джокери були знайдені
    if max_jokers != 0:
        working_array.pop(0)

    # якщо довжина основного 0, то макс послідовність = кількість джокерів
    if len(working_array) == 0:
        print([])
        return max_jokers
    # якщо довжина основного масиву 1, то макс послідовність = кількість джокерів + довжина осн масиву
    # перевірка на довжину 1 потрібна для того, щоб уникнути експшина, який виникає коли створюємо масив різниць
    # пі.сі. там є working_array[idx + 1] і воно тут впаде
    elif len(working_array) == 1:
        print(working_array)
        return max_jokers + 1

    max_difference = max_jokers + 1
    diff_list = []

    # create list of differences
    for idx, val in enumerate(working_array):
        if idx != len(working_array) - 1:
            diff = working_array[idx + 1] - working_array[idx]
            diff_list.append(diff)

    temp_arr = []  # манюні масиви
    main_array = []  # великий агромний масив
    temp_jokers = max_jokers  # треба зберегти джокери, бо max_jokers в процесі циклу переписується і стає 0
    for num_idx, num in enumerate(working_array):
        temp_arr.append(working_array[num_idx])
        for diff_idx, diff in enumerate(diff_list, start=num_idx):
            # перевірка щоб diff_idx не виходив за межі масиву
            if diff_idx == len(diff_list):
                break
            # якщо різниця 1, то впихуємо число з основного масиву в темп масив
            # кста індекси diff_list залежать від working_array на + 1
            # пі.сі. на листочку покажу, якщо не понятно
            elif diff_list[diff_idx] == 1:
                temp_arr.append(working_array[diff_idx + 1])
            # тут чисто перевіряється якщо конкретна різниця менша ніж максимальна дозволена
            # кста цей вираз можна спростити але мені лєнь
            # а і чи ще залишились джокери які можна впихнути
            elif (diff_list[diff_idx] > 1) & (max_jokers > 0) & (diff_list[diff_idx] <= max_difference):
                # скік джокерів лишилось
                used_jokers = diff_list[diff_idx] - 1
                # впихнути стільки джокерів скільки було використано
                for x in range(used_jokers):
                    temp_arr.append(0)
                # впих
                temp_arr.append(working_array[diff_idx + 1])
                # тут думаю понятно
                max_jokers = max_jokers - used_jokers
            else:
                # елс брейк
                break
        # якщо в кінці залишились незаюзані джокери то туть вони впихуються
        for x in range(max_jokers):
            temp_arr.append(0)
        # впих в великий агромний масив
        main_array.append(temp_arr)
        # резет манюнього до пустого
        temp_arr = []
        # резет макс кількості джокерів до початкової
        max_jokers = temp_jokers
    # результат
    result = 0
    # то чисто щоб запрінтити найбільший масив
    end_idx = 0
    # перебігаєш по великий агромний масив і шукаєш найбільшу манюню
    for idx, x in enumerate(main_array):
        if len(x) > result:
            result = len(x)
            end_idx = idx
    # прінтер
    print(main_array[end_idx])
    return result


if __name__ == '__main__':
    text_file = open("poker_in.txt", "r")
    poker_in_list = text_file.read().split(" ")
    poker_in_list = list(map(int, poker_in_list))
    text_file.close()
    text_file2 = open("poker_out.txt", "w")
    poker_out = text_file2.write(f"{poker(poker_in_list)}")
    text_file2.close()
