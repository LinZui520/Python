friends = ['Jack', 'Mask']
friends.insert(0, 'Alen')
friends[2] = 'Mark'
for i in friends:
    print(i)
friends.append('Mask')
print(friends, len(friends), type(friends))
friends.remove('Mask')
print(friends)
