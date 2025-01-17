def f(word):
    wave = []
    for index in range(len(word)):
        new_word = ""
        for index_2 in range(len(word)):
            if index == index_2:
                new_word += word[index_2].upper()
            else:
                new_word += word[index_2]
        wave.append(new_word)
    return "-".join(wave)



if __name__ == "__main__":
    print(f("hello"))