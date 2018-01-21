print('type your name and which year you were born')
name=input()
yborn=int(input())
year100=yborn+100
print('my dear ',name,', you`ll turn 100 in: ',year100)
print('how many more times do you want this massage above?')
x=int(input())
y=0
while y<x:
    print('my dear ',name,', you`ll turn 100 in: ',year100)
    y+=1

