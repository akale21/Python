f=lambda a,b : a+b

result = f(5,6)

print(result)

nums = [3,5,6,2,6,8,6,94,79]

evens = list (filter(lambda n: n%2==0,nums))

doubles =list (map(lambda n: n*2,evens))

print(evens)
print(doubles)