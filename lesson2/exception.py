def get_summ(num_one,num_two):
    if (num_one == int(num_one) and num_two == int(num_two)):
        print(num_one + num_two)
    else:
        print("hell")
try: 
    one = int(input('Write sth pls '))
    two = int(input('Write sth else '))
except ValueError:
    print('I just cant tackle it')
get_summ(one,two)


# import ephem
# venus = ephem.Venus('2000/09/10')
# const = ephem.constellation(venus)
# print(const)