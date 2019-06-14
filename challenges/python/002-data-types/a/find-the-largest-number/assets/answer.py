def largest_number(number_1, number_2):
  if (type(number_1) == int or type(number_1) == float) and (type(number_2) == int or type(number_2)== float):
    return number_1 if number_1 > number_2 else number_2
  else:
     print ("Make sure both arugments are numbers")
     return
  pass
