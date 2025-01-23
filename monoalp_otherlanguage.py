import random
import string
from collections import Counter
import re

class MonoalphabeticCipher:
    def __init__(self):
        self.s = string.ascii_lowercase
        self.key = "tacosbdefghijklmnpqruvwxyz"

    def read_file(self, filename):
        with open(filename, 'r') as file:
            return file.read()

    def generate_key(self):

        return self.key

    def encrypt(self, text):
        if self.key is None:
            raise ValueError("Key has not been generated.")
        text = text.lower()
        return ''.join(self.key[self.s.index(char)] if char in self.s else char for char in text)

    def decrypt(self, enctext):
        if self.key is None:
            raise ValueError("Key has not been generated.")
        return ''.join(self.s[self.key.index(char)] if char in self.key else char for char in enctext)


class NGramAnalyzer:
    def __init__(self, top_k=20, n_gram=3):
        self.top_k = top_k
        self.n_gram = n_gram

    def ngrams(self, n, text):
        for i in range(len(text) - n + 1):
            if not re.search(r'\s', text[i:i + n]):
                yield text[i:i + n]

    def analyze(self, text):
        for N in range(self.n_gram):
            print("--------------")
            print("{}-gram (top {}):".format(N + 1, self.top_k))
            counts = Counter(self.ngrams(N + 1, text))
            sorted_counts = counts.most_common(self.top_k)
            for ngram, count in sorted_counts:
                print("{}: {}".format(ngram, count))

    def replacement(self, text):
        replace_text = text
        replace_text=replace_text.replace("t", "a")
        replace_text = replace_text.replace("s", "e")
        replace_text = replace_text.replace("o", "d")
        replace_text = replace_text.replace("l", "o")
        replace_text = replace_text.replace("j", "m")
        replace_text = replace_text.replace("h", "k")
        replace_text = replace_text.replace("i", "l")
        replace_text = replace_text.replace("f", "i")
        replace_text = replace_text.replace("r", "t")
        replace_text = replace_text.replace("p", "r")

        return replace_text

def main():
    cipher = MonoalphabeticCipher()

    # Dosyadan metni oku
    txt = cipher.read_file("anotherlanguage.txt")
    print("Original text:", txt)

    # Şifreleme anahtarını oluştur
    key = cipher.generate_key()
    print("key:", " ".join(key))

    # Metni şifrele
    enctext = cipher.encrypt(txt)
    print("Şifrelenmiş Metin:")
    print(enctext)

    #Metnin çözümü
    newtext = cipher.decrypt(enctext)
    print("Kırılmış Metin:")
    print(newtext)

    analyzer = NGramAnalyzer(top_k=20, n_gram=3)
    analyzer.analyze(enctext)

    replaced_text = analyzer.replacement(enctext)  # Orijinal metin üzerinde değişiklik yap
    print("Değiştirilmiş Metin:")
    print(replaced_text)






if __name__ == "__main__":
    main()