# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/solutions/python

from codewars_kata_diary import testing


def snail(snail_map: list[list[int]]) -> list[int]:
    size_grid = len(snail_map)

    if size_grid == 0 or size_grid == 1:
        return snail_map[0]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited = [[False for _ in range(size_grid)] for _ in range(size_grid)]

    res: list[int] = []

    direction_idx = 0
    loc_row = 0
    loc_col = 0

    while len(res) != size_grid**2:
        # save current location
        res.append(snail_map[loc_row][loc_col])
        visited[loc_row][loc_col] = True

        # check if need to rotate
        loc_row_test = loc_row + directions[direction_idx % 4][0]
        loc_col_test = loc_col + directions[direction_idx % 4][1]
        is_out_of_square = (
            loc_row_test < 0
            or loc_row_test >= size_grid
            or loc_col_test < 0
            or loc_col_test >= size_grid
        )
        if is_out_of_square or visited[loc_row_test][loc_col_test]:
            direction_idx += 1

        # move forward
        loc_row += directions[direction_idx % 4][0]
        loc_col += directions[direction_idx % 4][1]

    return res


def snail2(snail_map: list[list[int]]) -> list[int]:
    res = []
    while snail_map:
        res += snail_map.pop(0)
        snail_map = [list(row) for row in zip(*snail_map)][::-1]
    return res


def snail3(snail_map: list[list[int]]) -> list[int]:
    import numpy as np

    res = []
    array = np.array(snail_map)
    while len(array) > 0:
        res += array[0].tolist()
        array = np.rot90(array[1:])
    return res


if __name__ == "__main__":
    test_cases = [
        [[]],
        [[1]],
        [[1, 2], [3, 4]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    ]

    answers = [
        [],
        [1],
        [1, 2, 4, 3],
        [1, 2, 3, 6, 9, 8, 7, 4, 5],
    ]

    testing.test_func(test_cases, answers, snail)
