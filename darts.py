# Chad Wilson
# Justin Moore
# Jason Thompson
# Alexander Wiecking
# Add your names here

# functions
import time


def double(lst):
    return [x * 2 for x in lst]

def triple(lst):
    return [x * 3 for x in lst[:-1]]

def calculate_final_double(darts, score, possible_double_list):  #function to calculate possible final double
    for i in range(len(doubled_numbers)):
        if(score >= doubled_numbers[i]):
            possible_double_list.append(doubled_numbers[i])
    return possible_double_list
    
# global variables
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25]
doubled_numbers = double(numbers)
tripled_numbers = triple(numbers)


nums = numbers + doubled_numbers + tripled_numbers
all_numbers = []
[all_numbers.append(x) for x in nums if x not in all_numbers]
all_numbers.sort(reverse=True)
doubled_numbers.sort(reverse=True)
all_combinations_list = []

def recursion_hell(score, darts, includes_double, scorelist):
    if (darts <= 0) or (score <= 0): #If you're out of score or darts, return.
        return
    if darts == 1: #If it's possible to make the last shot, return.
        if score in all_numbers:
            scorelist.append(score)
            all_combinations_list.append(scorelist.copy())
            print(f"Adding {scorelist.copy()} to list.")
            scorelist.pop()
            return
            
    if not includes_double:
        for num in doubled_numbers:
            if num > score: pass
            if num == score:
                scorelist.append(num)
                all_combinations_list.append(scorelist.copy())
                print(f"Adding {scorelist.copy()} to list.")
                scorelist.pop()
                return
            scorelist.append(num)
            recursion_hell(score - num, darts -1, True, scorelist)
            scorelist.pop()
        return
        
    for num in all_numbers:
        if num > score: pass
        if num == score:
            scorelist.append(score)
            all_combinations_list.append(scorelist.copy())
            print(f"Adding {scorelist.copy()} to list.")
            scorelist.pop()
            return
        
        scorelist.append(num)
        recursion_hell(score - num, darts - 1, includes_double, scorelist)
        scorelist.pop()
        
# main
def main():
    print(numbers)
    print(doubled_numbers)
    print(tripled_numbers)
    start = time.time()
    score = input("What is your score? \n")
    darts = input("How many darts do you have? (Max of 12) \n")

    if(len(darts) == 0): # The user just hit enter
        darts = 12
    if(len(score) == 0): # The user just hit enter
        score = 501
    
    score = int(score)
    darts = int(darts)

    while(darts > 12):
        darts = int(input("Too many darts please no more than 12 \n"))
    
    possible_double_list = []
    possible_double_list = calculate_final_double(darts, score, possible_double_list)
    possible_double_list.sort(reverse=True)
    
    print(f"Possible doubles for this score: {possible_double_list}")
    print(f"All numbers: {all_numbers}")
    includes_double = False
    darts_used = 0
    numlist = []
    recursion_hell(score, darts, includes_double, numlist)
#Following code-block might be unnecessary with the previous recursion hell function   
#    while score > 0:
#        for double in possible_double_list:
#            if includes_double == True:
#               break
#           if (score - double) >= 0:
#               score -= double
#                number_list.append(double) #List for current set of darts
#                darts_used += 1
#               includes_double = True
#                break
#       for number in all_numbers:
#            if (score - number) >= 0:
#               score -= number
#               number_list.append(number)
#               darts_used += 1
#               break
#       if darts_used > darts: 
#           break


    #for i in range(len(all_combinations_list)):
        #print(all_combinations_list[i])
    
    #for x in range(len(possible_double_list)):
        #print(possible_double_list[x])

    print(f"List: {all_combinations_list}")
    end = time.time()
    input(f"Press any key to continue. Elapsed time: {(end-start)/60} minutes. ({end-start} seconds)")
    return


if __name__ == "__main__":
    main()
