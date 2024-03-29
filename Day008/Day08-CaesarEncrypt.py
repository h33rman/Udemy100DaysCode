print("Caesar Encryption")
print("*****************")

# Ceasar Cipher Project

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '0j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
def caesarcipher(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1 
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"The {cipher_direction}d text is {end_text}")


continue_cipher = True
while continue_cipher:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesarcipher(start_text=text, shift_amount=shift, cipher_direction=direction)
  result = input("Do you want to continue? Type 'yes' or 'no':\n")
  if result == "no":
    continue_cipher = False
    print("Goodbye")
    
