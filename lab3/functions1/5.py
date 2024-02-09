from itertools import permutations

def print_permutations():
    s = input("String : ")
    perms = permutations(s) 
    
    print("All permutations : ")
    for perm in perms:
        print(''.join(perm))
       

print_permutations()
