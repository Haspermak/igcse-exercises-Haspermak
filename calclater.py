onenum = input("input the first number")
calc = input("input either a 1 for +, a 2 for -, a 3 for /, or a 4 for *")
twonum = input("input the second number")
num1 = int(onenum)
num2 = int(twonum)
if calc == "1":
    answer = num1+num2
elif calc == "2":
    answer = num1-num2
elif calc == "3":
    answer = num1/num2
elif calc == "4":
    answer = num1*num2

print(f"here's your answer {answer}")



