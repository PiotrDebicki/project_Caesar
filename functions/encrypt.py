def encrypt(text:str, shift:int):
  encrypted:str = ""
  for char in text:
    if char.isalpha():
      ascii_code = ord(char)
      if(ascii_code <=90):
        ascii_code = (ascii_code - 64 + shift)%26 + 64
      else:
        ascii_code = (ascii_code - 96 + shift)%26 + 96
      encrypted += chr(ascii_code)
    else:
      encrypted+=char
  return encrypted