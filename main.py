import random
from Words import word_list

name = input("Adın ne: ")
print("Hoş geldin " + name + "! İyi Şanslar...")
print("Test şimdi başlıyor...\n")

def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Adam Asmaca oynayalım!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Lütfen bir harf veya kelime tahmin edin: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Harfi zaten kullandın", guess)
            elif guess not in word:
                print(guess, "kelimede yok.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("İyi iş,", guess, "kelimede var!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Kelimeyi zaten tahmin ettin", guess)
            elif guess != word:
                print(guess, "doğru kelime değil.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Geçerli bir tahmin değil.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Tebrikler, kelimeyi buldun! Sen kazandın!")
    else:
        print("Üzgünüm, deneme hakkın bitti. Kelime: " + word + ". Belki gelecek sefere!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Tekrar oynar mısın? (E/H) ").upper() == "E":
        word = get_word()
        play(word)



if __name__ == "__main__":
    main()