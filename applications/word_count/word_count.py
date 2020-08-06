def word_count(s):
    # Your code here
    word_count = {}
    
    if s == "":
        return word_count
    if s == '":;,.-+=/\|[]{}()*^&':
        return word_count
    lowered = s.lower()
    words = lowered.split()
    for index, w in enumerate(words):
        stripped = w.strip('":;,.-+=/\|[]{}()*^&')
        # print(stripped)
        if stripped not in word_count:
            word_count[stripped] = 1
        else:
            word_count[stripped] += 1
    return word_count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))