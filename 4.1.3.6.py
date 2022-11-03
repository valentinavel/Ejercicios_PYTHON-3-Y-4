def is_Year_Leap (año) :
  if año % 4 != 0:
    return False
  elif año % 100 != 0:
    return True 
  elif año % 400 != 0:
    return False 
  else:
    return True 

test_Data = [1900, 2000, 2016, 1987]
test_Results = [False, True, True, False]
for i in range(len(test_Data)):
  yr = test_Data[i]
  print(yr,"->",end="")
  result = is_Year_Leap(yr)
  if result == test_Results[i]:
    print("OK")
  else:
    print("Failed")
