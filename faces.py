# A function that takes a str as input and return the string with an emoji in place of any emoticon.
def convert(text):
    return text.replace(":)","\U0001F642").replace(":(","\U0001F641")

#The main function that prompts the user for input and calls the convert function on the input. And print out the result.
def main():
    text = input()
    text = convert(text)
    print(text)

main()