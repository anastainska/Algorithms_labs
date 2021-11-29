from merge_sort import mergesort
# array_test = [9, 12]  # 1
# array_test = [9, 10]  # 2
# array_test = [9, 10, 12, 14, 15, 40, 50, 51, 52, 53, 54, 55, 56, 57, 0, 0, 0, 0]  # 12
# array_test = [1, 0, 0]  # 3

# array_test = []  # 0
# array_test = [0, 0, 0, 0]  # 4
# array_test = [14, 15, 0, 0]  # 4


def poker(array):
    if len(array) == 0:
        return 0

    max_jokers = 0
    sorted_array = mergesort(array, 'asc')
    for x in sorted_array:
        if x == 0:
            max_jokers = max_jokers + 1

    working_array = list(dict.fromkeys(sorted_array))

    if max_jokers != 0:
        working_array.pop(0)

    if len(working_array) == 0:
        print([])
        return max_jokers
    elif len(working_array) == 1:
        print(working_array)
        return max_jokers + 1

    max_difference = max_jokers + 1
    diff_list = []

    for idx, val in enumerate(working_array):
        if idx != len(working_array) - 1:
            diff = working_array[idx + 1] - working_array[idx]
            diff_list.append(diff)

    temp_arr = []
    main_array = []
    temp_jokers = max_jokers
    for num_idx, num in enumerate(working_array):
        temp_arr.append(working_array[num_idx])
        for diff_idx, diff in enumerate(diff_list, start=num_idx):
            if diff_idx == len(diff_list):
                break
            elif diff_list[diff_idx] == 1:
                temp_arr.append(working_array[diff_idx + 1])
            elif (diff_list[diff_idx] > 1) & (max_jokers > 0) & (diff_list[diff_idx] <= max_difference):
                used_jokers = diff_list[diff_idx] - 1
                for x in range(used_jokers):
                    temp_arr.append(0)
                temp_arr.append(working_array[diff_idx + 1])
                max_jokers = max_jokers - used_jokers
            else:
                break
        for x in range(max_jokers):
            temp_arr.append(0)
        main_array.append(temp_arr)
        temp_arr = []
        max_jokers = temp_jokers
    result = 0
    end_idx = 0
    for idx, x in enumerate(main_array):
        if len(x) > result:
            result = len(x)
            end_idx = idx
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
