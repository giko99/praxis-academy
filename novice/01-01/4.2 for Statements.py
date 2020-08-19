words = ['cat', 'window', 'defenestrate']
for w in words:
    print (w, len(w))

#strategy : Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

#strategy: Create a new collection
active_users = {}
for user, status in users.item():
    if status == 'active':
        active_users[user] = status