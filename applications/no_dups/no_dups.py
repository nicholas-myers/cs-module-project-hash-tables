def no_dups(s):
    # Your code here
    word_count = {}
    
    words = s.split()
    if len(words) == 1:
        return s
    for index, w in enumerate(words):
        if w not in word_count:
            word_count[w] = 1
        else:
            word_count[w] += 1
    # return word_count
    return " ".join(word_count.keys())
    
    


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))