immutable_var = (2024, 'октябрь', 11, True)
print(immutable_var)
print('False ','immutable_var[0]=2023, картеж не поддерживает изменение по элементам' )
immutable_var1= ([2024,11],'ноябрь', True)
print(immutable_var1)
immutable_var1[0][0]=2025
immutable_var1[0][1]=12
print(immutable_var1)
print('True', 'возможно изменить только если картеж хранит внутри список')
immutable_list= list(immutable_var)
print(immutable_list)
immutable_list[0]=2023
immutable_list[1]='ноябрь'
immutable_list[2]=10
immutable_list[3]=False
print(immutable_list)


