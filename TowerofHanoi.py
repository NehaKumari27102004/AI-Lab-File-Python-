def towers_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} → {target}")
        return
    
   
    towers_of_hanoi(n - 1, source, target, auxiliary)
    
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} → {target}")
    
    # Move the n-1 disks from auxiliary to target
    towers_of_hanoi(n - 1, auxiliary, source, target)


# --------- Input ---------
n = int(input("Enter number of disks: "))
print("The sequence of moves to solve Towers of Hanoi is:\n")
towers_of_hanoi(n, 'A', 'B', 'C')  # A=Source, B=Auxiliary, C=Target
