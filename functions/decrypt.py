def decrypt(text):
  encrypted = ""
  encrypted_tab = []
  for shift in range(1, 26):
    for char in text:
      if char.isalpha():
        ascii_code = ord(char)
        if(ascii_code <=90):
          ascii_code = (ascii_code - 65 - shift)%26 + 65
        else:
          ascii_code = (ascii_code - 97 - shift)%26 + 97
        char = chr(ascii_code)
      encrypted+=char
  encrypted_tab.append(encrypted)
  print(encrypted_tab)

  return encrypted
