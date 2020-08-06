# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

cipher = "c:/Users/infin/Desktop/lambdaschool/Computer Science/Hash Tables/cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt"
def read_file(path):
    f = open(path, "r")
    text = f.read()
    f.close()
    return text


letter_count = {}
text = read_file(cipher)
total = 0
for l in text:
    if l.isalpha():
        total += 1
        if l not in letter_count:
            letter_count[l] = 1
        else:
            letter_count[l] += 1
        
# print(letter_count)
# print(total)
decoder = {}
for l in letter_count:
    percentage = round((letter_count[l] / total) * 100, 2)
    
    print(percentage)