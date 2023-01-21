

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a male or you are tall or both")
elif is_male and not(is_tall):
    print("you're a male and not tall")
elif not(is_male) and is_tall:
    print("you are a tall woman")
else:
    print("You are not a male or tall")