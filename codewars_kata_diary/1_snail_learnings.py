# %%
import numpy as np

# %%
arr = np.arange(1, 10).reshape(3, 3)
arr

# %%
# np.rot90 rotates the array 90 degrees counter-clockwise
np.rot90(arr)
# %%
# pop removes the nth element from the list and returns it
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_list.pop(0))
print(my_list)

# %%
# list(zip(*my_list)) returns a list of tuples where the first tuple contains
# the first element of each list in my_list, the second tuple contains the
# second element of each list in my_list, etc.
# thereby transposing the list of lists
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(np.array(list(zip(*my_list))))
# list(zip(*my_list))[::-1] reverses the order of the tuples
# thereby effectively rotating the list of lists 90 degrees clockwise
print(np.array(list(zip(*my_list))[::-1]))
