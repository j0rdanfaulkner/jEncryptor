# Import Hash algorithms using 'hashlib'
import copy
import hashlib

# Import clipboard functionality using 'subprocess'
import subprocess

# -- CopyToClipboard --
# Parameters:   value (string that will be copied to the clipboard)
# Returns:      result of copying the hashed value to the system clipboard
def CopyToClipboard(value):
    print("The hash has been copied to your clipboard")
    cmd = 'echo ' + value.strip() + '|clip'
    return subprocess.check_call(cmd, shell=True)

# -- EncryptString --
# - Parameters: plaintext (text that needs to be encrypted)
# -             chosenMethod (user-chosen algorithm that will be used to provide a hashed version of the plain text)
# - Returns:    Hashed value of plain text
# Used to encrypt the plain text given by user using their intended encryption method, then returns the hash value to them
def EncryptString(plaintext, chosenMethod):
    match chosenMethod:
        # If user wishes to use MD5 algorithm
        case "MD5":
            # Hash 'plaintext' using this method of encryption and store it as 'md5Hash'
            md5Hash = \
            hashlib.md5(plaintext.encode()).hexdigest()
            # Return MD5 hash variable
            return md5Hash
        # If user wishes to use SHA-256 algorithm
        case "SHA-256":
            # Hash 'plaintext' using this method of encryption and store it as 'sha256Hash'
            sha256Hash = \
            hashlib.sha256(plaintext.encode()).hexdigest()
            # Return SHA-256 hash variable
            return sha256Hash
        # If chosen method could not be found, display error message in console
        case _:
            print("Unexpected error occured: Could not hash phrase successfully\nPlease try again")
            return ""
        
# -- AskForInput --
# - Parameters: versionNumber (current version of application)
# - Returns: nothing
# Used to ask user for plain text input and desired encryption method
def AskForInput(versionNumber):
    # Show application header
    print("=== jEncryptor (v." + versionNumber + ") ===")
    # Ask user for text input and store this as 'plaintext'
    plaintext = input("Enter the phrase that you need to be encrypted: ")
    # Present available options as a clear menu
    print("\n=== Encryption Menu ===")
    # Declare available encryption methods as an array
    methods = {'1': 'MD5', '2': 'SHA-256'}
    # Display these options in the console window as part of the menu
    print("Option 1 | MD5\nOption 2 | SHA-256")
    # Ask user for the number of their desired method from the menu
    choice = input("\nEnter Number of the Encryption Method: ")
    # If menu option was given correctly
    if choice in methods:
        # Find the name of the method from the array using the number they entered
        # Store this as 'chosenMethod'
        chosenMethod = methods[choice]
        # Pass the 'plaintext' and 'chosenMethod' variables to the 'encryptedText' function as parameters
        encryptedText = EncryptString(plaintext, chosenMethod)
        # Display the hashed phrase using the result returned from the 'encryptedText' function
        print("The " + chosenMethod + " hash of your phrase is: " + encryptedText)
        # Pass the hashed value to the 'CopyToClipboard' function as a parameter
        CopyToClipboard(encryptedText)
    # If user is typing something before the menu number or the name of the method itself
    elif len(choice) != 1:
        # Ask user to try again entering only the number of the menu option
        print("Please try again; make sure you are only entering the number of the method")
    # Otherwise, just show generic error message asking the user to try again
    else:
        print("Entered method could not be found, please try again")
    
# Main entry point of jEncryptor console application
versionNumber = "1.0.0.2"
# Call the 'AskForInput' function with 'versionNumber' variable as a parameter
AskForInput(versionNumber)
# Wait before exiting application
input("\nHash successfully generated...")

