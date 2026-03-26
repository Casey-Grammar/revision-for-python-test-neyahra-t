# Task 6 Find bear
# Write a program to work out whether a line of input text contains a
# bear or not. Your program needs to find cases where the word
# appears in full, with no breaks.

def main():
    #Write your code here
    word = 'bear' 
    message = input('Message: ').lower() 
    if word in message: 
        print('This message has the word bear in it') 
    else: 
        print('') 
    # End of your code here





if __name__ == '__main__':
    main()