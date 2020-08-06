# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

cipher = "c:/Users/infin/Desktop/lambdaschool/Computer Science/Hash Tables/cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt"
def read_file(path):
    f = open(path, "r")
    text = f.read()
    f.close()
    return text
text = read_file(cipher)
# print(text)

letter_count = {}

total = 0
for l in text:
    if l.isalpha():
        total += 1
        if l not in letter_count:
            letter_count[l] = 1
        else:
            letter_count[l] += 1
        
decoder = {}
for l in letter_count:
    percentage = round((letter_count[l] / total) * 100, 2)
    letter_count[l] = percentage
    # print(f"{l}: {percentage}")
    if percentage == 5.84:
        decoder[l] = "I"
    if percentage == 6.73:
        decoder[l] = "N"
    if percentage == 2.18:
        decoder[l] = "M"
    if percentage == 6.29:
        decoder[l] = "R"
    if percentage == 11.52:
        decoder[l] = "E"
    if percentage == 2.02:
        decoder[l] = "Y"
    if percentage == 2.48:
        decoder[l] = "G"
    if percentage == 3.92:
        decoder[l] = "L"
    if percentage == 8.46:
        decoder[l] = "A"
    if percentage == 4.74:
        decoder[l] = "D"
    if percentage == 9.75:
        decoder[l] = "T"
    if percentage == 7.71:
        decoder[l] = "H"
    if percentage == 8.08:
        decoder[l] = "O"
    if percentage == 2.42:
        decoder[l] = "F"
    if percentage == 3.07:
        decoder[l] = "W"
    if percentage == 0.84:
        decoder[l] = "K"
    if percentage == 5.56:
        decoder[l] = "S"
    if percentage == 1.58:
        decoder[l] = "C"
    if percentage == 2.59:
        decoder[l] = "U"
    if percentage == 0.59:
        decoder[l] = "V"
    if percentage == 2.19:
        decoder[l] = "B"
    if percentage == 1.08:
        decoder[l] = "P"
    if percentage == .07:
        if l == "T":
            decoder[l] = "J"
        elif l == "L":
            decoder[l] = "X"
    if percentage == .03:
        decoder[l] = "Z"
    if percentage == .17:
        decoder[l] = "Q"
print(decoder)
# for key in decoder.keys():
#     print(f"{key}: {decoder[key]}")
#     new_text = text.replace(str(key), str(decoder[key]))
# print(new_text)

new_text = ""
def print_decoded_letter(letter):
    if letter.isalpha():
        if letter == 'â':
            return
        global new_text
        new_text += decoder[letter]
    else:
        new_text += letter
    return

for l in text:
    print_decoded_letter(l)
    
print(new_text)