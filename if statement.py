is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and  is_tall:
    print("You are not a male and tall")
else:
    print("You are not a male nor tall")

if is_male and is_tall:
    print("You are a male and tall")
else:
    print("You are not a male and not tall")