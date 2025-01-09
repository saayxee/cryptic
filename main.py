def main():
  text = input('Please enter your sentence here: ')
  if (len(text) < 1):
    print("Error - no text entered")
  else :
    print("\nEncryption/cipher modes available:")
    print("  1. Caeser Cipher")
    # print("  2. Atbash Cipher")
    # print("  3. Vigen Cipher")
    try:
      choice = int(input("\nKindly enter your numerical choice here: "))
      if (choice == 1):
        shift = None
        caeser(text, shift)
      else: 
        print("Invalid input. Please enter a valid number.")
    except ValueError:
      print("Invalid input. Please enter a valid number.")
  



def caeser(text, shift):
  if shift == None:
    tempShift = int(input("Kindly enter parameter shift: "))
    shift = tempShift

  text.lower()
  encrypted_text = ""

  for char in text:
    if char.islower():
      encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
    else:
      encrypted_text += char

  print(f"Ciphered/Encrypted text: {encrypted_text}")  

  





if __name__ == "__main__":
  main()