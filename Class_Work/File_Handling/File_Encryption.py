# Caesar Cipher Encryption
#algorithm:-------
#Start
#Open source file in read mode
#Open new file in write mode
#Take shift value (key)
#Read each character from file
#If character is alphabet:
#Shift it by given key
#Else keep it same
#Write encrypted content into new file
#Close files
#Stop

shift = 3  # you can change shift value

with open("input.txt", "r") as source, open("encrypted.txt", "w") as dest:
    for line in source:
        encrypted_line = ""
        
        for ch in line:
            if ch.isalpha():
                if ch.islower():
                    encrypted_line += chr((ord(ch) - 97 + shift) % 26 + 97)
                else:
                    encrypted_line += chr((ord(ch) - 65 + shift) % 26 + 65)
            else:
                encrypted_line += ch
        
        dest.write(encrypted_line)

print("File encrypted successfully!")