string = "msdjdgf(^&%*(Aroha Technologies&^$^&*^CHJdjg"

def string_format(text):
  letter_list = []
  for letter in text:
    if letter.isalpha():
      letter_list.append(letter)
    else:
      letter_list.append(" ")
  letter_list = "".join(letter_list)
  words = letter_list.split()
  word_list = []
  for word in words:
    if word.istitle():
      word_list.append(word)
  return " ".join(word_list)
  letter_list = None
  word_list = None
  
print string_format(string)