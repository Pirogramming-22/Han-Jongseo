import random

def brGame():
  num = 0

  random_number = random.randint(1, 3)

  for i in range(random_number):
    num += 1
    print("computer : ", num)

  while True:
    try:
      random_number = random.randint(1, 3)
      input_count = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : "))

      if input_count not in [1, 2, 3]:
        print("1,2,3 중 하나를 입력하세요")
        continue

      for i in range(input_count):
        num += 1
        if num == 31:
          print("player : ", num)
          print("computer win!")
          return
        print("player : ", num)

      for i in range(random_number):
        num += 1
        if num == 31:
          print("computer : ", num)
          print("player win!")
          return
        print("computer : ", num)

    except ValueError:
      print("정수를 입력하세요")
      continue

brGame()