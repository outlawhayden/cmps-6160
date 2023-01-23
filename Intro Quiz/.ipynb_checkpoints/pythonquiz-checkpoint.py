

def my_function(a):
  result = 0
  for i in range(len(a)):
    for j in range(i):
      result += i*j
  return result


answer = my_function([10,20,30])
print(answer)