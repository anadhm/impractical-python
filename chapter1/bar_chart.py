"""Calculate and show a bar chart of the most commonly used English letters."""
import pprint
from collections import defaultdict
def main():
    """
    Take a sentence and output a barchart of the frequency of its letters.
    
    Input: a string
    Output: a bar chart.
    """
    counters=defaultdict(int)
    print("Welcome to the Poor Man's Bar Chart!\n")
    while True:
        input_string=input("Please input a sentence (or n to quit):\n\n")
        if input_string=="n":
            break
        for character in input_string.lower():
            if character not in [' ',"\t","\n","\r",".",",",";",":","?","/"]:
                counters[character]+=1
        for key in counters:
            counters[key]=[key]*counters[key]
        pprint.pprint(counters,width=500)
    print("Press Enter to quit.\n")

if __name__=="__main__":
    main()