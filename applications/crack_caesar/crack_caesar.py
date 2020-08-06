# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

cipher = "c:/Users/infin/Desktop/lambdaschool/Computer Science/Hash Tables/cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt"
def read_file(path):
    f = open(path, "r")
    text = f.read()
    f.close()
    return text
print(read_file(cipher))