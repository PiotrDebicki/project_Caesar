def encrypt(text:str, shift:int):
  encrypted:str = ""
  while("\n" in text):
    text = text.replace("\n", " ")
  for char in text:
    if char.isalpha():
      ascii_code = ord(char)
      if(ascii_code <=90):
        ascii_code = (ascii_code - 65 + shift)%26 + 65
      else:
        ascii_code = (ascii_code - 97 + shift)%26 + 97
      encrypted += chr(ascii_code)
    else:
      encrypted+=char
  return encrypted