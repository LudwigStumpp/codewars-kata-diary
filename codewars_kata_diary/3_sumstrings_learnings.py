# %%
import itertools

# %%
x = "1"
x.zfill(10)

# %%
a = "123"
b = "1"

for m, n in itertools.zip_longest(a, b, fillvalue="0"):
    print(m, n)

# %%
# strings are immutable so that concatenating creates a new one -> prefer lists concatenation
# appending is faster than prepending
