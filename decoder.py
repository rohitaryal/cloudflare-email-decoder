import random

def decode(*email_list):
    """
    Returns a list[] of decoded emails.
    Will throw an `Exception` in case of invalid
    or empty email(s).
    """
    
    if len(email_list) == 0:
        raise Exception("No obfuscated email(s) supplied to decode.")
    
    decoded_email_list = []
        
    for email in email_list:
        if len(email) < 2:
            raise Exception("Invalid email probably.")
        
        n=2
        final_email=""
        r=int(email[:n], base=16) #Hexadecimal
        
        while len(email) - n > 0: # Other exception may be generated here
            n += 2
            ascii_value=int(email[n-2:n], base=16) ^ r
            final_email += chr(ascii_value)
        
        decoded_email_list.append(final_email)
            
    return decoded_email_list

def get_random_r():
    min = 26  # 0x1a
    max = 255 # 0xff
    random_number = random.randrange(min, max + 1) # max and min inclusive

    return random_number

def encode(*email_list):
    """
    Returns a list[] of encoded emails.
    Will throw `Exception` in case of empty
    email(s) supplied
    """

    if len(email_list) == 0:
        raise Exception("No email(s) supplied to encode.")

    encoded_email_list = []

    for email in email_list:
        r = get_random_r()
        encoded_email = hex(r)[2:] # Since first 2 letters is the decoder key (r)

        for char in email:  # Other exception may be generated here
            ascii_code = ord(char)
            ascii_code ^= r
            hex_code = hex(ascii_code)[2:]

            # some hex might be less than 10 but we want pair always
            # so append 0 to number less than 10
            hex_string = '0' + hex_code if len(hex_code) < 2 else hex_code

            encoded_email += hex_string

        encoded_email_list.append(encoded_email)

    return encoded_email_list

if __name__ == "__main__":
    print("[1] Encode")
    print("[2] Decode")
    option = int(input("CHOOSE: "))

    if option == 1:
        while True:
            print(encode(input("E-Mail: ")))
    elif option == 2:
        while True:
            print(decode(input("String: ")))
    else:
        print("[!] Invalid option")
        exit(0)
