def transformSentence(sentence):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    atn = {alpha[index]:index for index in range(26)}
    index = 0
    final = list()
    words =  sentence.split()

    for word in words:
        op = word[0]

        for index in range(1, len(word)):

            if atn[word[index-1].lower()] < atn[word[index].lower()]:
                op += word[index].upper()
            
            elif atn[word[index-1].lower()] > atn[word[index].lower()]:
                op += word[index].lower()

            else:
                op += word[index]
        
        final.append(op)

    return " ".join(final)


if __name__ == "__main__":
    print(transformSentence("coOL dog"))
