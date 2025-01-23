import random
from collections import Counter
import re



class PolyalphabeticCipher:
    def __init__(self, N=1000,alphabet="abcdefghijklmnopqrstuvwxyz"):
        self.N = N
        self.s = alphabet
        self.trantab_enc = [None] * N
        self.trantab_dec = [None] * N
        for i in range(N):
            mapping = random.sample(self.s, len(self.s))
            self.trantab_enc[i] = str.maketrans(self.s, "".join(mapping))
            self.trantab_dec[i] = str.maketrans("".join(mapping), self.s)

    def read_file(self, filename):
        with open(filename, 'r') as file:
            return file.read()

    def encrypt(self, text):
        text = text.lower()
        ciphertext = [None] * len(text)
        for i, char in enumerate(text):
            if char in self.s:
                ciphertext[i] = char.translate(self.trantab_enc[i % self.N])
            else:
                ciphertext[i] = char
        return ''.join(ciphertext)

    def decrypt(self, enctext):
        plaintext = [None] * len(enctext)
        for i, char in enumerate(enctext):
            if char in self.s:
                plaintext[i] = char.translate(self.trantab_dec[i % self.N])
            else:
                plaintext[i] = char
        return ''.join(plaintext)

class NGramAnalyzer:
    def __init__(self, top_k=20, n_gram=3):
        self.top_k = top_k
        self.n_gram = n_gram

    def ngrams(self, n, text):
        for i in range(len(text) - n + 1):
            if not re.search(r'\s', text[i:i + n]):
                yield text[i:i + n]

    def analyze(self, text):
        for N in range(1, self.n_gram + 1):
            print("--------------")
            print("{}-gram (top {}):".format(N, self.top_k))
            counts = Counter(self.ngrams(N, text))
            sorted_counts = counts.most_common(self.top_k)
            for ngram, count in sorted_counts:
                print("{}: {}".format(ngram, count))

    def replacement(self, text):
        replace_text = text
        return replace_text
    




def main():
    cipher = PolyalphabeticCipher(N=1000,alphabet="abcdefghijklmnopqrstuvwxyz")

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

    analyzer = NGramAnalyzer(top_k=20, n_gram=3)
    analyzer.analyze(enctext)

    replaced_text = analyzer.replacement(enctext) #Modify the encrypted text based on predefined replacements
    print("Modified text:")
    print(replaced_text)
    

if __name__ == "__main__":
    main()



#As a result, polyalphabetic encryption with a large key length of N=1000 is too strong to be broken by brute force with current technologies. We can say that it is mathematically and practically impossible to crack this password.

