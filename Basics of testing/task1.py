#Task 1

#Pick your solution to one of the exercises in this module. Design tests for this solution and write tests using unittest library. 

def calculate_wage(rate:float,hour:float)->float:
  if hour<=40:
      return hour*rate
  else:
      return 40*rate+(hour-40)*1.5*rate

def test_calculate_wage_1():
    assert calculate_wage(10.0, 35.0)==350