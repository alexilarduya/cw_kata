# http://www.codewars.com/kata/vigenere-autokey-cipher-helper

class VigenereAutokeyCipher:
    def __init__(self, key, abc):
        self.key = key
        self.abc = abc
        self.abc_dict = {}
        
        for idx, ch in enumerate(abc):
            self.abc_dict[ch] = idx
        
    def encode(self, text):

        encoded = ''
        idx = 0
        tkey = '%s' % self.key
        for letter in text:
            try:            
                abc_idx = self.abc_dict[tkey[idx]]
                abc_idx += self.abc_dict[letter] 
                abc_idx = abc_idx % len(self.abc)
                
                tkey += letter # add encoded letter to key
                encoded += self.abc[abc_idx]
                idx += 1
                
            except KeyError:
                encoded += letter
        
        return encoded     
        
    def decode(self, text):
        
        decoded = ''
        idx = 0
        tkey = '%s' % self.key
        
        for letter in text:
            try:
                abc_idx = -self.abc_dict[tkey[idx]] + len(self.abc)
                abc_idx += self.abc_dict[letter] 
                abc_idx = abc_idx % len(self.abc)               

                tkey += self.abc[abc_idx]  # add decoded letter to key
                decoded += self.abc[abc_idx]
                idx += 1
                
                
                
            except KeyError:
                decoded += letter
        
        return decoded
