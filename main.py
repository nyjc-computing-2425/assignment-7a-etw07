# Write a function to convert numbers to text numerals
NUM_WORD = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

def text_numeral(num):
  """takes in a positive integer less than 100 and returns a string representing it in text format"""
  modif_num = num
  used_keys = []
  keys = list(NUM_WORD.keys())[::-1]
  for x in keys:
    if modif_num == 0:
      break
    elif x <= modif_num:
      multi = modif_num//x
      used_keys.append([x,multi])
      modif_num -= x*multi
  output = ""
  for i in range(len(used_keys)):
    new_key = used_keys[i][0]*used_keys[i][1]
    output += NUM_WORD[new_key]
    if i != len(used_keys)-1:
      output += " "
  return output 
  pass
