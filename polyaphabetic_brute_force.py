import string
from tqdm import tqdm
import time
import string



class PolyalphabeticCipher:
    def __init__(self, key="c", alphabet=string.ascii_lowercase):
        self.key = key
        self.alphabet = alphabet
        self.key_indices = [self.alphabet.index(k) for k in self.key]

    def read_file(self, filename):
        with open(filename, 'r') as file:
            return file.read()

    def encrypt(self, text):
        text = text.lower()
        ciphertext = []
        for i, char in enumerate(text):
            if char in self.alphabet:
                key_index = self.key_indices[i % len(self.key)]
                char_index = self.alphabet.index(char)
                encrypted_char = self.alphabet[(char_index + key_index) % len(self.alphabet)]
                ciphertext.append(encrypted_char)
            else:
                ciphertext.append(char)
        return ''.join(ciphertext)

    def decrypt(self, enctext):
        plaintext = []
        for i, char in enumerate(enctext):
            if char in self.alphabet:
                key_index = self.key_indices[i % len(self.key)]
                char_index = self.alphabet.index(char)
                decrypted_char = self.alphabet[(char_index - key_index) % len(self.alphabet)]
                plaintext.append(decrypted_char)
            else:
                plaintext.append(char)
        return ''.join(plaintext)

def brute_force(encrypted_text, original_text, key):
    alphabet = string.ascii_lowercase
    key_length = len(key)
    
    def generate_keys(alphabet, length):
        if length == 0:
            yield ""
        else:
            for letter in alphabet:
                for sub_key in generate_keys(alphabet, length - 1):
                    yield letter + sub_key
    
    for potential_key in tqdm(generate_keys(alphabet, key_length), total=len(alphabet) ** key_length):
        cipher = PolyalphabeticCipher(key=potential_key, alphabet=alphabet)
        decrypted_text = cipher.decrypt(encrypted_text)
        
        if decrypted_text == original_text:
            return potential_key
    return None

def main():
    cipher = PolyalphabeticCipher(key="c", alphabet=string.ascii_lowercase)

    # Read the text from the file
    txt = cipher.read_file("file.txt")
    print("Original text:", txt)

    # Encrypt the text
    enctext = cipher.encrypt(txt)
    print("Encrypted text:")
    print(enctext)

    # Decrypt the text
    dectext = cipher.decrypt(enctext)
    print("Decrypted text:")
    print(dectext)

    # Brute-force attack to find the key
    start_time = time.time()
    search_key = brute_force(enctext, txt, key="c")
    end_time = time.time()

    if search_key:
        print(f"Found key: {search_key}")
    else:
        print("Key not found")

    print(f"Time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()


 
 