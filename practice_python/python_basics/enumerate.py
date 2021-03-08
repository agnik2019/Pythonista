names = ['Agnik','Nabil','Towkir','Troyee']

# index = 0
# for name in names:
#     print(index,name)
#     index += 1

for index,name in enumerate(names):
    print(index,name)


names = ['Peter Perker','Hritik','SRK','Bruce Wayne']
heroes = ['Spiderman','Krish',"Raone",'Batman']

# for index,name in enumerate(names):
#     hero = heroes[index]
#     print(f'{name} is actually a {hero}')
for name, hero in zip(names, heroes):
     print(f'{name} is actually a {hero}')