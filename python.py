for i in range(1,20):
    resalt='even'+str(i) if i%2==0 else "odd"+str(i)
    print(resalt)

for i in range(1,20):
    resalt='even' if i%2==0 else 'odd'
    print(f'{i} is {resalt}')