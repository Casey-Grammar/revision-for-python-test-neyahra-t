# Task 4 Open Sesame
# Write a program to ask Ali for a password. 
# If the password is correct, the cave door will be opened. 
# Otherwise nothing will

def main():
    #Write your code here
    passcode = 'Open Sesame'
    attempt = input("Ali, what's the password?").lower().title()
    if attempt == passcode:
        print('Cave door open')
    else:
        print('')
    # End of your code here

if __name__ == '__main__':
    main()