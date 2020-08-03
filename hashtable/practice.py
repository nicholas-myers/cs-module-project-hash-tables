# GET PUT DELETE
print(ord("d"))
print("Beej".encode())

hash_size = 8

hash_data = [None] * hash_size

def hash_funciton(s):
    byte_list = s.encode()
    total = 0
    for b in byte_list:
        total += b
        
    return total

def get_index(s):
    hash_value = hash_funciton(s)
    return hash_value % hash_size

def put(k, v):
    index = get_index(k)
    hash_data[index] = v
    
print(hash_data)