# The code in this file is used to implement a hash tale using Python's built in dictionary

if __name__ == "__main__":
    print("\nDictionary Instantiation:")
    dictionary = {"Sam": 21, "Hannah": 21, "John": 17, "Luke": 14, "Kevin": 11}
    print(dictionary)
    print("\nAdding Scarlett:")
    dictionary["Scarlett"] = 49
    print(dictionary)
    print("\nPopping Sam:")
    print(dictionary.pop("Sam"))
    print(dictionary)

    print(dictionary.get("Hannah"))
    print(dictionary.get("Fake"))

