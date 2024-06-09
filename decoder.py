def decode(*email_list):
    """
    Returns a list[] of decoded emails.
    Will throw an `Exception` in case of invalid
    or empty email(s).
    """
    
    if len(email_list) == 0:
        raise Exception("No email(s) supplied.")
    
    decoded_email_list = []
        
    for email in email_list:
        if len(email) < 10:
            raise Exception("Invalid email probably.")
        
        n=2
        final_email=""
        r=int(email[:n], base=16) #Hexadecimal
        
        
        while len(email) - n > 0:
            n += 2
            ascii_value=int(email[n-2:n], base=16) ^ r
            final_email += chr(ascii_value)
        
        decoded_email_list.append(final_email)
            
    return decoded_email_list