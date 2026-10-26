def grades():
  marks=list(map(int,input("Enter your marks: ").split()))
  total=0
  for x in marks:
      if x<0 or x>100:
          raise ValueError(f" {x} is a Invalid mark")
      total+=x

  avg = total / len(marks)
  if avg >= 90:
      print("Grade: A+")
  elif avg >= 80:
      print("Grade: A")
  elif avg >= 70:
      print("Grade: B+")
  elif avg >= 60:
      print("Grade: B")
  else:
      print("Grade: F")

try:
    grades()
except ValueError as error:
    print(error)