def main():
    #write your code below this line
    result = average(4, 3, 6, 1)
    print("Average: " + str(result))

def sum(number1, number2, number3, number4):
  return number1 + number2 + number3 + number4

def average(number1, number2, number3, number4):
  return sum(number1, number2, number3, number4) / 4

if __name__ == '__main__':
    main()
