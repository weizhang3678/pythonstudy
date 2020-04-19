# 0x：hex
# 0b：bin
# 0O：octal

# arithmetic operators: + - * / % // **(right to left)
# compared or relational operators: >= <= == !=
# assignment operator: =
# compound assignment operators: += -= *= /= %= **=(right to left)
# logical operator: and or not, T and T is T; T and F is F;  T or T is T; T or F is T;
# not (a and b) is not a or not b
# not (a or b) is not a and not b

# int()
# float()
# str()
# bool(): 0 0.0 are false, others are true
# 1230 = 1.23E3

currency = input('What kind of currency do you have?(C: Canada dollar; R: RMB; A: American dollars)')
money = float(input('How much do you have?'))
target_currency = input('What kind of currency do you want to exchange?(C: Canadian dollar; R:RMB; A:American dollars)')
c_r_rate = 5
a_r_rate = 7
a_c_rate = 1.4
if currency == target_currency:
    print("You don't need to change.")
if currency == 'C' and target_currency == 'R':
    print('You can exchange RMB ', money * c_r_rate)
elif currency == 'R' and target_currency == 'C':
    print("You can exchange Canadian dollars", money / c_r_rate)
elif currency == 'R' and target_currency == 'A':
    print("You can exchange American dollars", money / a_r_rate)
elif currency == 'A' and target_currency == 'R':
    print("You can exchange RMB", money * a_r_rate)
elif currency == 'C' and target_currency == 'A':
    print("You can exchange American dollars", money / a_c_rate)
elif currency == 'A' and target_currency == 'C':
    print("You can exchange Canadian dollars", money * a_c_rate)