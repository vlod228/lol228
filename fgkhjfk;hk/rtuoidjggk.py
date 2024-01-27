#a = input().split()
#if len(a):
#    a.append(a.pop(0))
#print(a)

a = input().split()
try:
    a.append(a.pop(0))
except:
    print("У тебя в списке пусто")
finally:
    print(a)