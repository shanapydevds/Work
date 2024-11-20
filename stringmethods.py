# String examples for demonstration
example = "hello world"
numeric_example = "12345"
alpha_example = "Python"
mixed_example = "Hello123"
whitespace_example = "   "
iterable_example = ["Hello", "world"]

# 1. capitalize()
print("capitalize():", example.capitalize())

# 2. casefold()
print("casefold():", alpha_example.casefold())

# 3. center()
print("center():", example.center(20, "-"))

# 4. count()
print("count():", example.count("l"))

# 5. encode()
print("encode():", example.encode())

# 6. endswith()
print("endswith():", example.endswith("world"))

# 7. expandtabs()
tab_example = "Hello\tWorld"
print("expandtabs():", tab_example.expandtabs(4))

# 8. find()
print("find():", example.find("world"))

# 9. format()
print("format():", "Welcome, {}!".format("Alice"))

# 10. format_map()
print("format_map():", "{name} is {age} years old".format_map({"name": "Alice", "age": 25}))

# 11. index()
print("index():", example.index("world"))

# 12. isalnum()
print("isalnum():", mixed_example.isalnum())

# 13. isalpha()
print("isalpha():", alpha_example.isalpha())

# 14. isascii()
print("isascii():", example.isascii())

# 15. isdecimal()
print("isdecimal():", numeric_example.isdecimal())

# 16. isdigit()
print("isdigit():", numeric_example.isdigit())

# 17. isidentifier()
print("isidentifier():", "variable_name".isidentifier())

# 18. islower()
print("islower():", example.islower())

# 19. isnumeric()
print("isnumeric():", numeric_example.isnumeric())

# 20. isprintable()
print("isprintable():", example.isprintable())

# 21. isspace()
print("isspace():", whitespace_example.isspace())

# 22. istitle()
title_example = "Hello World"
print("istitle():", title_example.istitle())

# 23. isupper()
print("isupper():", alpha_example.upper().isupper())

# 24. join()
print("join():", " ".join(iterable_example))

# 25. ljust()
print("ljust():", example.ljust(20, "-"))

# 26. lower()
print("lower():", alpha_example.lower())

# 27. lstrip()
strip_example = "   Hello"
print("lstrip():", strip_example.lstrip())

# 28. maketrans() and translate()
trans = str.maketrans("aeiou", "12345")
print("translate():", example.translate(trans))

# 29. partition()
print("partition():", example.partition(" "))

# 30. replace()
print("replace():", example.replace("world", "Python"))

# 31. rfind()
print("rfind():", example.rfind("l"))

# 32. rindex()
print("rindex():", example.rindex("l"))

# 33. rjust()
print("rjust():", example.rjust(20, "-"))

# 34. rpartition()
print("rpartition():", example.rpartition(" "))

# 35. rsplit()
print("rsplit():", example.rsplit(" "))

# 36. rstrip()
rstrip_example = "Hello   "
print("rstrip():", rstrip_example.rstrip())

# 37. split()
print("split():", example.split(" "))

# 38. splitlines()
multiline_example = "Hello\nWorld"
print("splitlines():", multiline_example.splitlines())

# 39. startswith()
print("startswith():", example.startswith("hello"))

# 40. strip()
strip_example = "   Hello   "
print("strip():", strip_example.strip())

# 41. swapcase()
print("swapcase():", example.swapcase())

# 42. title()
print("title():", example.title())

# 43. upper()
print("upper():", example.upper())

# 44. zfill()
print("zfill():", numeric_example.zfill(10))
