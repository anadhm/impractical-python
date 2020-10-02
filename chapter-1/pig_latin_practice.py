"""Take a word as input and form its Pig Latin equivalent."""

def main():
    """
    Forms the Pig Latin equivalent of a given word.
    
    If the word begins with a consonant, moves the consonant 
    to the end and add -ay. If it begins with a vowel, 
    add -way to the end.
    """
    print("Welcome to the Pig Latin Practice!\n")
    while True:
        word_before=input(
            "Please input the word you want to \
            turn into Pig Latin (or n to quit):\n\nn")
        word_after=""
        if word_before.lower()=="n":
            break
        if word_before[0] in ["a","e","u","i","o"]:
            word_after=word_before+"way"
        else:
            word_after=word_before[1:]+word_before[0]+"ay"
        print("Pig Latin of {}:{}\n".format(word_before,word_after))
    input("Press Enter to quit.")
if __name__=="__main__":
    main()
