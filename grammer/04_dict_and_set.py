# 04_dict_and_set
# 1. dictionary
# key, value로 이루어져있음
dict_a = {}
dict_b = dict()
#key가 중복이 불가능 하다.
dict_a = {'삼성':100,'역삼':50,'삼성':30}
print(dict_a)
print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())

print(dict_a['삼성'])
print(dict_a.get('삼성'))

#.get과 []접근 차이점
dict_a = {'삼성':100,'역삼':50,'삼성':30}
print(dict_a.get('선릉'))
#print(dict_a['선릉'])  #값을 가져올때 없을때 멈추어 주려고 할때 사용하면 좋다

# 2. set
# set는 순서가 없이 저장된다.
# 중복이 없다.
set_a = {1,2,3}
set_b = {3,6,9}
dict_b ={}
print(set_a - set_b)
print(set_a | set_b)
print(set_a & set_b)

list_a = [1,1,1,1,2]
print(list(set(list_a))[1])

string = "immutable"
list_a = ['immutable?','real?']
list_b = list_a
print(string[0])
print(list_a[0])
# string[0] = 'a'
list_a[0] = 'mutable'
print(list_a)
list_a = ['immutable?','real?']
list_b = list_a
print(list_a,list_b)
list_b[0] = 'mutable'
print(list_a,list_b)