import math
def main():
  text = input('Please enter your sentence here: ')
  if (len(text) < 1):
    print("Error - no text entered")
  else :
    print("\nEncryption/cipher modes available:")
    print("  1. Caeser Cipher")
    print("  2. Atbash Cipher")
    print("  3. XOR Cipher")
    try:
      choice = int(input("\nKindly enter your numerical choice here: "))
      if (choice == 1):
        shift = None
        caeser(text, shift)
      elif (choice == 2):
        atbash(text)
      elif (choice == 3):
        xor(text)
      else: 
        print("Invalid input. Please enter a valid number.")
    except ValueError:
      print("Invalid input. Please enter a valid number.")
  
def xor(text):
    if (len(text) > 255):
      print("Constraint - Text Too Long")
    else: 
      # Generate the key
      key = math.floor(((len(text) ** 2) * 9) / 5) % 256

      # Convert the text to bytes
      input_bytes = bytearray(text, 'utf-8')

      # Perform XOR encryption
      output_bytes = bytearray([b ^ key for b in input_bytes])

      # Convert each byte to a hexadecimal pair and join them
      hex_output = ' '.join(f'{byte:02x}' for byte in output_bytes)

      # Print results
      print("Ciphered Text (Hexadecimal): " + hex_output)
      print("Key: " + str(key))



def atbash(text):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  alphabet_upper = alphabet.upper()
  reversed_alphabet = "zyxwvutsrqponmlkjihgfedcba"
  reversed_alphabet_upper =reversed_alphabet.upper()
  ciphered_text = ""

  for char in text: 
    if char.islower(): 
      index = alphabet.index(char)
      ciphered_char = reversed_alphabet[index]
      ciphered_text += ciphered_char

    elif char.isupper():
      index = alphabet_upper.index(char)
      ciphered_char = reversed_alphabet_upper[index]
      ciphered_text += ciphered_char
    else: 
      ciphered_text += char
  print("Ciphered text: " + ciphered_text)



def caeser(text, shift):
  if shift == None:
    temp_shift = int(input("Kindly enter parameter shift: "))
    shift = temp_shift

  text.lower()
  ciphered_text = ""

  for char in text:
    if char.islower():
      ciphered_text += chr((ord(char) + shift - 97) % 26 + 97)
    else:
      ciphered_text += char

  print(f"Ciphered text: {ciphered_text}")  

  





if __name__ == "__main__":
  main()