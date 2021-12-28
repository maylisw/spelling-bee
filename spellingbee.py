def readDict():
    with open("/usr/share/dict/words") as f:
        contents = f.read()
        contents = contents.lower()
        words = contents.splitlines()
        return set(words)
    return set()

# alpha is a set
# special is a character
def getAllValid(alpha, special):
    words = readDict()
    if not words:
        return set()
    
    alpha.add(special)
    valid_words = set()
    for word in words:
        w = set(word)
        if special not in w:
            continue
        if not w.issubset(alpha):
            continue
        valid_words.add(word)
    return valid_words

def main():
    #TODO: error check input
    letters = input("What are the letters? ").lower()
    middle_letter = input("What is the middle letter? ").lower()

    answers = getAllValid(set(letters), middle_letter)
    answers = sorted(list(answers), key=len)

    l = len(answers[0])
    print(f"--- {l} letter words ---")
    for ans in answers:
        if len(ans) != l:
            l = len(ans)
            print(f"--- {l} letter words ---")
        print(ans)

if __name__ == "__main__":
    main()