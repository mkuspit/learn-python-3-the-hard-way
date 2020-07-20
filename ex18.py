# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that args is pointless, we can actually do this
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# this one takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
	print("I got nothin'.")


print_two("Michal", "Kuspit")
print_two_again("Michal", "Kuspit")
print_one("One only")
print_none()