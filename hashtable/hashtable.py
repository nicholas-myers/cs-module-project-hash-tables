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
        self.capacity = capacity
        self.hash_list = [None for i in range(self.capacity)]
        
    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.hash_list)
    
    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # count the total number of nodes
        # if the current load is greater than 0.7
        # resize * 2
        count = 0
        for entry in self.hash_list:
            cur_entry = entry
            if entry.next is None:
                count+=1
            while cur_entry.next:
                count+=1
                cur_entry = entry.next
        if count / self.capacity > 0.7:
            self.resize(self.capacity * 2)
                
                
                    
    
    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass
    
    def djb2(self, key):
        # """
        # DJB2 hash, 32-bit
        # Implement this, and/or FNV-1.
        # """
        # Your code here
        hash = 5381
        byte_array = key.encode("utf-8")

        for byte in byte_array:
        # the modulus keeps it 32-bit, python ints don't overflow
            hash = ((hash * 33) ^ byte) % 0xFFFFFFFF
        # print(hash)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.get_num_slots()

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        new_node = HashTableEntry(key, value)
        # print(index)
        new_node = HashTableEntry(key, value)
        if self.hash_list[index] is None:
            self.hash_list[index] = new_node
        else:
            if self.hash_list[index].key == key:
                self.hash_list[index].value = value
            self.hash_list[index].next = new_node
        # print(self.hash_list)
        
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.hash_list[index].value == None:
            print("No key found")
        if self.hash_list[index].key == key:
            self.hash_list[index].value = None
        else:
            self.hash_list[index].next.value = None
                
    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        # print(self.bucket_array[index].value)
        if self.hash_list[index].key == key:
            return self.hash_list[index].value
        else:
            return self.hash_list[index].next.value
        
    def resize_delete(self, key, new_list):
        index = self.hash_index(key)
        if self.hash_list[index].next:
            new_list.append(self.hash_list[index])
            self.hash_list[index] = self.hash_list[index].next
            self.resize_delete(self.hash_list[index].key, new_list)
        else:
            new_list.append(self.hash_list[index])
            self.hash_list[index] = None
    
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # extract everything from the hashlist and put into a new list
        new_hash_list = []
        for entry in self.hash_list:
            self.resize_delete(entry.key, new_hash_list)
        self.capacity = new_capacity
        self.hash_list = [None for i in range(new_capacity)]
        for i in new_hash_list:
            self.put(i.key, i.value)
        # reset the size and hash list
        # itereate through the new list and use our put function on every key value pair
        
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
