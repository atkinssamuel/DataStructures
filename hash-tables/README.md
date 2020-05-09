#### Hash Tables (Hash Maps)
The purpose of a hash table is to enable fast lookup of values that can be expected. Hash tables can be used to enable more efficient solutions to problems. 

#### Functions
##### Get Hash Index
The purpose of this function is to retrieve the index of a given key for the purpose of lookup. The hash function can be anything that promotes index uniqueness.
##### Add
This function adds a given key-value pair to the hash table. If the key already exists in the hash table, that key's value pair is updated. Otherwise, the key-value pair is appended to the list at the index retrieved by the "Get Hash Index" function.
##### Lookup
This function looks up the value at a given key. 
##### Remove
This function removes the element with the given key.