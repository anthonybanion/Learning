name = 'Anthony'
last_name = 'Bañon'
age = 25

# Print uses space separator by default
print(name, last_name, age)  

# Print uses sep separator
print(name, last_name, age, sep = '...')  


#1 Concatenate strings
full_name = name + ' ' + last_name + ' has ' + str(age) + ' years old'
print(full_name)

#2 Format strings
full_name = f'{name} {last_name} has {age} years old'
print(full_name)

#3 Format strings with format()
full_name = '{0} {1} has {2} years old'.format(name, last_name, age)
print(full_name)


#4 Join strings
full_name = ' '.join([name, last_name, 'has', str(age), 'years old'])
print(full_name)

#5 Format strings with % operator and tuple
full_name = '%s %s has %d years old' % (name, last_name, age)
print(full_name)


#6 Format strings with % operator and dictionary
full_name = '%(name)s %(last_name)s has %(age)d years old' % {'name': name, 'last_name': last_name, 'age': age}
print(full_name)
