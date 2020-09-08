
######################################################################################################
# DAY 2

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = int(
            capacity) if capacity > MIN_CAPACITY else MIN_CAPACITY
        self.hash_table = [None for i in range(self.capacity)]
        self.num_of_elements = 0

    def print_arr(self):
        # return f'Hash Table: {self.hash_table}'

        resultt = ""
        for index, val in enumerate(self.hash_table):

            if val != None:
                while val is not None:
                    resultt += f'\ {index} {val.key} , {val.value} \ || '
                    val = val.next

            else:
                resultt += f'{index} None || '

        return resultt + "\nLoad factor: " + str(self.get_load_factor())

    def get_num_slots(self):
        pass
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.hash_table)

    def get_load_factor(self):
        pass
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.num_of_elements/self.get_num_slots()

    def fnv1(self, key):
        pass
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        hash = self.hash_index(key)

        current_value = self.hash_table[hash]

        while current_value is not None:
            if key == current_value.key:
                current_value.value = value
                return
            current_value = current_value.next

        key_value_pair = HashTableEntry(key, value)
        key_value_pair.next = self.hash_table[hash]
        self.hash_table[hash] = key_value_pair
        self.num_of_elements += 1
        if(self.get_load_factor() > 0.7):
            print("greater than 0.7")
            self.resize(self.capacity*2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hash = self.hash_index(key)
        current_value = self.hash_table[hash]

        if current_value is None:
            return f"Couldn't find the provided key!"
        elif current_value.key == key:
            self.hash_table[hash] = current_value.next
            self.num_of_elements -= 1
            if(self.get_load_factor() < 0.2):
                print("less than 0.2")
                self.resize(self.capacity/2)

            # current_value = current_value.next ?
        else:
            while current_value.next is not None:

                if current_value.next.key == key:

                    current_value.next = current_value.next.next
                    self.num_of_elements -= 1
                    if(self.get_load_factor() < 0.2):
                        print("less than 0.2")
                        self.resize(self.capacity/2)
                    return
                current_value = current_value.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hash = self.hash_index(key)
        current_value = self.hash_table[hash]

        if current_value is None:
            return None
        else:
            while current_value is not None:
                if current_value.key == key:
                    return current_value.value
                current_value = current_value.next

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        new_hash_table = HashTable(new_capacity)
        for index, val in enumerate(self.hash_table):
            if val != None:
                print(val.value)
                while val is not None:
                    new_hash_table.put(
                        self.hash_table[index].key, self.hash_table[index].value)
                    val = val.next

        self.capacity = new_hash_table.capacity
        self.hash_table = new_hash_table.hash_table
        self.num_of_elements = new_hash_table.num_of_elements
    #     self.capacity = int(
    #         new_capacity) if new_capacity > MIN_CAPACITY else MIN_CAPACITY
    #     print(f'sonuc: {self.capacity}')
    #     new_hash = [None for i in range(self.capacity)]

    #     for index, val in enumerate(self.hash_table):
    #         if val != None:
    #             while val is not None:
    #                 self.rehash(
    #                     self.hash_table[index].key, self.hash_table[index].value, new_hash)
    #                 val = val.next

    #     self.hash_table = new_hash

    # def rehash(self, key, value, new_hash):
    #     hash = self.hash_index(key)

    #     current_value = new_hash[hash]

    #     while current_value is not None:
    #         if key == current_value.key:
    #             current_value.value = value
    #             return
    #         current_value = current_value.next

    #     key_value_pair = HashTableEntry(key, value)
    #     key_value_pair.next = new_hash[hash]
    #     new_hash[hash] = key_value_pair

    def getCapacity(self):
        return self.capacity


#########################
# ht = HashTable(8)
# print(f'HashTable -> { ht.print_arr()}')
# ht.put("line_1", "'Twas brillig, and the slithy toves")
# ht.put("line_1", "'line_1 updated")
# ht.put("line_4", "'line_1 updated")
# ht.put("line_5", "'line_1 updated")
# ht.put("line_3", "'line_1 updated")
# ht.put("line_6", "'line_1 updated")

# #ht.put("1_line", "same spot ")
# ht.put("line_2", "yenisi")
# print(f'Min capacity: {ht.getCapacity()}')
# print(f'HashTable -> { ht.print_arr()}')
# print(f'Min capacity: {ht.getCapacity()}')
# print(ht.delete("line_1"))
# print(ht.delete("line_3"))
# print(ht.delete("line_4"))
# print(f'HashTable -> { ht.print_arr()}')
# print(f'Min capacity: {ht.getCapacity()}')


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")


######################################################################################################
# DAY 1

# class HashTableEntry:
#     """
#     Linked List hash table key/value pair
#     """

#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None


# # Hash table can't have fewer than this many slots
# MIN_CAPACITY = 8


# class HashTable:
#     """
#     A hash table that with `capacity` buckets
#     that accepts string keys
#     Implement this.
#     """

#     def __init__(self, capacity):
#         # Your code here
#         self.capacity = capacity if capacity > MIN_CAPACITY else MIN_CAPACITY
#         self.hash_table = [None for i in range(self.capacity)]

#     def __str__(self):
#         return f'Hash Table: {self.hash_table}'

#     def get_num_slots(self):
#         pass
#         """
#         Return the length of the list you're using to hold the hash
#         table data. (Not the number of items stored in the hash table,
#         but the number of slots in the main list.)
#         One of the tests relies on this.
#         Implement this.
#         """
#         # Your code here

#     def get_load_factor(self):
#         pass
#         """
#         Return the load factor for this hash table.
#         Implement this.
#         """
#         # Your code here

#     def fnv1(self, key):
#         pass
#         """
#         FNV-1 Hash, 64-bit
#         Implement this, and/or DJB2.
#         """

#         # Your code here

#     def djb2(self, key):
#         hash = 5381
#         for c in key:
#             hash = (hash * 33) + ord(c)
#         return hash
#         """
#         DJB2 hash, 32-bit
#         Implement this, and/or FNV-1.
#         """
#         # Your code here

#     def hash_index(self, key):
#         """
#         Take an arbitrary key and return a valid integer index
#         between within the storage capacity of the hash table.
#         """
#         # return self.fnv1(key) % self.capacity
#         return self.djb2(key) % self.capacity

#     def put(self, key, value):
#         """
#         Store the value with the given key.
#         Hash collisions should be handled with Linked List Chaining.
#         Implement this.
#         """
#         hash = self.hash_index(key)
#         key_value = HashTableEntry(key, value)
#         self.hash_table[hash] = key_value

#     def delete(self, key):
#         """
#         Remove the value stored with the given key.
#         Print a warning if the key is not found.
#         Implement this.
#         """
#         hash = self.hash_index(key)
#         self.hash_table[hash] = None

#     def get(self, key):
#         """
#         Retrieve the value stored with the given key.
#         Returns None if the key is not found.
#         Implement this.
#         """
#         hash = self.hash_index(key)
#         if(self.hash_table[hash]):
#             return self.hash_table[hash].value
#         else:
#             return None

#     def resize(self, new_capacity):
#         """
#         Changes the capacity of the hash table and
#         rehashes all key/value pairs.
#         Implement this.
#         """

#         # Your code here


# #########################
# # ht = HashTable(8)
# # ht.put("line_1", "'Twas brillig, and the slithy toves")
# # print(ht.hash_index("line_1"))
# # print(ht.get("line_1"))
# # ht.delete("line_1")
# # print(ht.get("line_1"))
# # print(ht)
# if __name__ == "__main__":
#     ht = HashTable(8)

#     ht.put("line_1", "'Twas brillig, and the slithy toves")
#     ht.put("line_2", "Did gyre and gimble in the wabe:")
#     ht.put("line_3", "All mimsy were the borogoves,")
#     ht.put("line_4", "And the mome raths outgrabe.")
#     ht.put("line_5", '"Beware the Jabberwock, my son!')
#     ht.put("line_6", "The jaws that bite, the claws that catch!")
#     ht.put("line_7", "Beware the Jubjub bird, and shun")
#     ht.put("line_8", 'The frumious Bandersnatch!"')
#     ht.put("line_9", "He took his vorpal sword in hand;")
#     ht.put("line_10", "Long time the manxome foe he sought--")
#     ht.put("line_11", "So rested he by the Tumtum tree")
#     ht.put("line_12", "And stood awhile in thought.")

#     print("")

#     # Test storing beyond capacity
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     print("")
