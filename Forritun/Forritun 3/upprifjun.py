def word_mixer(word_list):
    new_words = []
    word_list.sort()
    while len(word_list) > 5:
        new_words.append(word_list.pop(-5))
        new_words.append(word_list.pop(0))
        new_words.append(word_list.pop(-1))
        new_words.append('\n')
    return new_words


strengur = input("Sláðu inn setningu: ")
wordlist = strengur.split()
for i in range(len(wordlist)):
    if len(wordlist[i]) <= 4:
        wordlist[i] = wordlist[i].lower()
    if len(wordlist[i]) >= 6:
        wordlist[i] = wordlist[i].upper()
if len(wordlist) > 5:
    newlist = word_mixer(wordlist)
    # print(newlist)
    for i in range(len(newlist)):
        print(newlist[i], end=" ")