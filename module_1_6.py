my_dict = {'Alex': 1991, 'Stas': 2001}
print(my_dict)
print(my_dict['Stas'])
my_dict['Dima']=2002
print(my_dict['Dima'])
my_dict.update({'Lena': 1989, 'Petya': 2004})
a= my_dict.pop('Petya')
print(a)
print(my_dict)

my_set = {1,2,3,'ok',True, 1,2,2,3,'ok',(1,2,3),(1,2,3)}
print(my_set)
my_set.add(8)
my_set.add('test')
my_set.discard((1,2,3))
print(my_set)