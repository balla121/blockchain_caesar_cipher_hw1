
def encrypt(key,plaintext):
    ciphertext=""

    for i in plaintext:
      if i.isalpha():
        alphabet = ord(i)+key
        if alphabet > ord("Z"):
          alphabet -= 26
        letter = chr(alphabet)
        ciphertext+=letter

    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    for i in ciphertext:
      if i.isalpha():
        alphabet = ord(i)-key
        if alphabet < ord("A"):
          alphabet += 26
        letter = chr(alphabet)
        plaintext+=letter

    return plaintext
