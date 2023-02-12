while True:
        
        print("Здравствуйте, попробуем сыграть в игру? 'Игра Крестики-нолики на двух игроков' ")
        a = int(input("Нажмите 1 (продолжить играть) или 0 (не продолжать и выйти из игры)"))
        if a == 1:
         
            break
        elif a == 0:
            exit()
        else:
            continue

print("+" * 5, "Cейчас  Вас ждет игра 'Игра Крестики-нолики на двух игроков' ",  "+" * 5)
print("*" * 43, " Удачи ", "*" * 43)

myboard = list(range(1,10))

def mydraw(myboard):
   print(" " * 41, "—" * 13, " " * 25)
   for i in range(3):
      print(" " * 41, "|", myboard[0+i*3], "|", myboard[1+i*3], "|", myboard[2+i*3], "|", " " * 25)
      print(" " * 41, "—" * 13, " " * 25)

def myinput(mytoken):
   valid = False
   while not valid:
      myanswer = input("Постваьте знак " +(mytoken)+ " на место любой свободной цифры от 1 до 9")
      try:
         myanswer = int(myanswer)
      except:
         print("Нужно Вводить только цифры от (1-9)")
         continue
      if myanswer >= 1 and myanswer <= 9:
         if(str(myboard[myanswer-1]) not in "XO"):
            myboard[myanswer-1] = mytoken
            valid = True
         else:
            print("В эту клетку ставить нельзя. она занята!")
      else:
        print("Нужно ввести число от (1-9)")

def check_mygame(myboard):
   mygame_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in mygame_coord:
       if myboard[each[0]] == myboard[each[1]] == myboard[each[2]]:
          return myboard[each[0]]
          print("Победа")
   return False

def main(myboard):
    mydraw(myboard)
    counter = 0
    mygame = False
    while not mygame:
        
        if counter % 2 == 0:
           myinput("X")
        else:
           myinput("O")
        counter += 1
        mydraw(myboard)
        if counter > 4:
            tmp = check_mygame(myboard)
            if tmp:
                if tmp:
                    print("Поздравляем", tmp , "Выиграл!")
                    mygame = True
                    break
        if counter == 9:
            print("Ничья!")
            break
        
main(myboard)
   
print("Спасибо что сыграли в игру:,  (Виталий Шамис группа  PWS- 1010)")
myprint = input("Чтобы вывести еще раз результат игры на доске, набирите цифру 1, в другом случае выйдите из игры")
if myprint == "1":
    main(myboard)
    
else:
    print("Спасибо, досвидания")
    exit()
