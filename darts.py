# Chad Wilson
# Add your names here

# functions
def double(lst):
    return [x * 2 for x in lst]

def triple(lst):
	return [x * 3 for x in lst[:-1]]

# global variables
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25]
doubled_numbers = double(numbers)
tripled_numbers = triple(numbers)

# main
def main():
    print(numbers)
    print(doubled_numbers)
    print(tripled_numbers)
    return


if __name__ == "__main__":
    main()
