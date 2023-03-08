score = int(input('输入你的成绩0-100'))

if score >= 90:
  grade = 'A'
elif score >= 80:
  grade = 'B'
elif score >= 70:
  grade = 'C'
elif score >= 60:
  grade = 'D'
else:
  grade = 'F'

print("你的成绩等级是"+grade)