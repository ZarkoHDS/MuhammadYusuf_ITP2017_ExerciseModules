def jumble():
    print ("Jumbled Word Program")
    import random

    sentence_ori = "The red brown fox jumped over the lazy dog"
    sentence = sentence_ori.split()
    temp = []
    num = []

    while(len(sentence) != 0):
        random_int = random.randint(0, len(sentence)-1)
        if(random_int in num == True):
            continue
        else:
            temp.append(sentence[random_int])
            num.append(random_int)
            del sentence[random_int]

    print(" ".join(temp))
    guess = input("Make your guess: ")

    if(guess == sentence_ori):
        print("Correct!")
    else:
        print("Noob...")
