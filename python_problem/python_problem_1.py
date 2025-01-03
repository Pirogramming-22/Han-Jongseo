def brGame():
  num = 0
  player_flag = True

  while True:
    try:
      input_count = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))

      if input_count not in [1, 2, 3]:
        print("1,2,3 중 하나를 입력하세요")
        continue

      if player_flag:
        for i in range(input_count):
          num += 1
          if num == 31:
            print("playerA win!")
            return
          print("playerA : ", num)
        player_flag = not player_flag
        continue
      
      if not player_flag:
        for i in range(input_count):
          num += 1
          if num == 31:
            print("playerB win!")
            return
          print("playerB : ", num)
        player_flag = not player_flag
        continue

    except ValueError:
      print("정수를 입력하세요")
      continue

brGame()