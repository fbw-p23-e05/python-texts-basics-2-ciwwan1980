
# Create the variable called ```text``` with the following content:  
# ```Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital ```, then count how many times the letter  ```B ``` appears in the text.

# * Your result should look like this:

# ```bash
# B appears:  3  times
# ```

text="Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"

print(f"B appears: {text.count('B')} times")