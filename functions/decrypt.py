from multiprocessing import Process

valid_words, encrypted, propability, global_text = "", "", 0, "test"

def decrypt(text):
  global valid_words, encrypted, propability, global_text

  global_text = text
  with open('./words_dictionary.json') as word_file:
    valid_words = word_file.read()
  encrypted = ""
  propability = 0
  processes = []
  for shift in range(1, 26):
    proc = Process(target=decrypting_process(shift))
    processes.append(proc)
    proc.start()
    if(propability>0.85):
      break
  for proc in processes:
    proc.join()
  return encrypted

def decrypting_process(shift):
  global propability, encrypted, global_text
  word = ""
  actuall_encrypted = ""
  actuall_words_counter = 0
  actuall_decoded_words = 0
  for char in global_text:
    if char.isalpha():
      ascii_code = ord(char)
      if(ascii_code <=90):
        ascii_code = (ascii_code - 65 - shift)%26 + 65
      else:
        ascii_code = (ascii_code - 97 - shift)%26 + 97
      char = chr(ascii_code)
      word+=char
    else:
      if not word == "":
        actuall_words_counter += 1
        if word.lower() in valid_words:
          actuall_decoded_words+=1
        actuall_encrypted +=word
        word = ""
      actuall_encrypted+=char
    if(actuall_decoded_words>30 and actuall_decoded_words/actuall_words_counter <0.3):
      break
  try:
    actuall_propability = actuall_decoded_words/actuall_words_counter
    if(actuall_propability>propability):
      propability = actuall_propability
      encrypted = actuall_encrypted
  except ZeroDivisionError:
    pass
