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
        # Input validation
        if email is None:
            raise Exception("Cannot decode None value. Please provide a valid encoded email string.")
        
        if not isinstance(email, str):
            raise Exception(f"Invalid input type. Expected string, got {type(email).__name__}.")
        
        if len(email) < 2:
            raise Exception("Encoded email string too short. Minimum length is 2 characters.")
        
        # Check if string length is even (required for hex pairs)
        if len(email) % 2 != 0:
            raise Exception("Invalid encoded email format. String length must be even for proper hex decoding.")
        
        # Validate hex characters
        try:
            # Test if the entire string is valid hex
            int(email, 16)
        except ValueError:
            raise Exception(f"Invalid encoded email format. String contains non-hexadecimal characters: '{email}'")
        
        n=2
        final_email=""
        
        try:
            r=int(email[:n], base=16) #Hexadecimal
        except ValueError:
            raise Exception("Invalid encoded email format. Unable to extract decoding key from first two characters.")
        
        while len(email) - n > 0:
            n += 2
            try:
                ascii_value=int(email[n-2:n], base=16) ^ r
                if ascii_value < 0 or ascii_value > 127:
                    raise Exception(f"Decoded character has invalid ASCII value: {ascii_value}. Expected value between 0-127.")
                final_email += chr(ascii_value)
            except ValueError:
                raise Exception(f"Invalid hex pair at position {n-2}: '{email[n-2:n]}'")
            except (OverflowError, ValueError) as e:
                raise Exception(f"Error decoding character at position {n-2}: {str(e)}")
        
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
        # Input validation
        if email is None:
            raise Exception("Cannot encode None value. Please provide a valid email string.")
        
        if not isinstance(email, str):
            raise Exception(f"Invalid input type. Expected string, got {type(email).__name__}.")
        
        if len(email) == 0:
            raise Exception("Cannot encode empty string. Please provide a valid email.")
        
        r = get_random_r()
        encoded_email = hex(r)[2:] # Since first 2 letters is the decoder key (r)

        try:
            for char in email:
                ascii_code = ord(char)
                # Validate ASCII range for proper encoding
                if ascii_code > 127:
                    raise Exception(f"Character '{char}' (ASCII {ascii_code}) is outside the supported ASCII range (0-127).")
                
                ascii_code ^= r
                hex_code = hex(ascii_code)[2:]

                # some hex might be less than 10 but we want pair always
                # so append 0 to number less than 10
                hex_string = '0' + hex_code if len(hex_code) < 2 else hex_code

                encoded_email += hex_string
        except (ValueError, OverflowError) as e:
            raise Exception(f"Error encoding character '{char}': {str(e)}")

        encoded_email_list.append(encoded_email)

    return encoded_email_list

if __name__ == "__main__":
    print("[1] Encode")
    print("[2] Decode")
    
    try:
        option = int(input("CHOOSE: "))
    except ValueError:
        print("[!] Invalid input. Please enter a number (1 or 2).")
        exit(1)
    except KeyboardInterrupt:
        print("\n[!] Operation cancelled by user.")
        exit(0)

    if option == 1:
        print("Encode mode - Enter emails to encode (Ctrl+C to exit)")
        while True:
            try:
                email_input = input("E-Mail: ").strip()
                if not email_input:
                    print("[!] Empty input. Please enter a valid email.")
                    continue
                result = encode(email_input)
                print(f"Encoded: {result[0]}")
            except KeyboardInterrupt:
                print("\n[!] Exiting encode mode.")
                break
            except Exception as e:
                print(f"[!] Error: {e}")
                
    elif option == 2:
        print("Decode mode - Enter encoded strings to decode (Ctrl+C to exit)")
        while True:
            try:
                string_input = input("String: ").strip()
                if not string_input:
                    print("[!] Empty input. Please enter a valid encoded string.")
                    continue
                result = decode(string_input)
                print(f"Decoded: {result[0]}")
            except KeyboardInterrupt:
                print("\n[!] Exiting decode mode.")
                break
            except Exception as e:
                print(f"[!] Error: {e}")
                
    else:
        print("[!] Invalid option. Please choose 1 for Encode or 2 for Decode.")
        exit(1)
