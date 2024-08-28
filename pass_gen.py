
import string
import random




if __name__ == "__main__":
    s1 = string.ascii_lowercase

    s2= string.ascii_uppercase

    s3 = string.digits

    s4 = string.punctuation

    all_chars = s1 + s2 + s3 + s4


    length = int(input("Enter password length: "))


    s= []

    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    
    random.shuffle(s)

    print("".join(s[0:length]))

    
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
   
    print(f"Generated Password: {password}")

