if __name__ == "__main__":
    brothers = {"John", "Luke", "Kevin"}
    friends = {"Jake Kim", "Jacob Mosseri", "Jake Murphy", "Carlos", "Chris Agia", "Chris Mazzuca"}
    family = {"John", "Luke", "Kevin", "Scarlett", "Grant", "Josh", "Rachel", "Beverly", "Grandpa"}
    parents = {"Scarlett", "Grant"}
    grandparents = {"Grandpa", "Beverly"}

    # Checking if element in set O(1) on average, O(n) worst case
    print("Is John in brothers?")
    print("John" in brothers)

    # Merging brothers and friends to make a new set:
    brothers_friends = brothers.union(friends)
    print("\nBrothers union with friends:", brothers_friends)

    # Difference between family and brothers:
    print("\nFamily minus brothers:", family-brothers)

    # Sets are an efficient way to extract unique elements from a repetitive list:
    my_list = [1, 2, 4, 2, 4, 2, 1, 6, 7, 2, 0]
    unique_elements = set(my_list)
    print("\nUnique elements as a set:", unique_elements)

    # Can convert back to a list:
    unique_list = list(unique_elements)
    print("Unique elements as a list:", unique_list)