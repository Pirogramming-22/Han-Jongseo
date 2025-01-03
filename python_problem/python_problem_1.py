num = 0
input_count = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
if type(input_count) != int:
  print("정수를 입력하세요")
elif input_count != 1 or input_count != 2 or input_count != 3:
  print("1,2,3 중 하나를 입력하세요")