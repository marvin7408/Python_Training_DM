"""Write a program that asks that user to enter an article, a noun, and a verb. The program then creates a sentence of the form article noun verb.

Example output:

Enter an article? The
Enter an noun? dog
Enter a verb? barks

Sentence: "The dog barks."
"""
# Variable article, noun, verb"
article = input("Enter an Article? ")
noun = input("Enter a Noun? ")
verb = input("Enter a verb? ")

# Print result with sentence:"".
print('Sentence: "' + article, noun, verb + '."')