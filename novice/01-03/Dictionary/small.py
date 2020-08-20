tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print (tel)
print('________________________________')

print (tel ['jack'])
print('________________________________')

del tel['sape']
tel['irv'] = 4127
print (tel)
print('________________________________')

print (list(tel))
print (sorted(tel))
print('________________________________')

print ('guido' in tel)
print ('jack' not in tel)