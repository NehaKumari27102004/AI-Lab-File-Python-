# Functions for union and intersection
def find_union(set1, set2):
    return set1 | set2    # union

def find_intersection(set1, set2):
    return set1 & set2    # intersection


# Taking input and converting directly into sets
set1 = set(map(int, input("Enter elements of Set 1 (space separated): ").split()))
set2 = set(map(int, input("Enter elements of Set 2 (space separated): ").split()))

# Results
print("\nSet 1:", set1)
print("Set 2:", set2)

print("\nUnion:", find_union(set1, set2))
print("Intersection:", find_intersection(set1, set2))
