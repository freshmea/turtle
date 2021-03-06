"""아래 나오는 문장과 코드를 직접 타이핑으로 작성하세요."""

empty_list = list() # 빈 리스트 객체를 만듬
print(len(empty_list)) # 0

fruits = ['banana', 'orange', 'mango', 'lemon']                     # 과일 리스트
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # 야채 리스트
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # 동물 제품 리스트
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # 기술 리스트
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] # 나라 리스트

# 각 리스트와 리스트의 길이 출력
print('과일:', fruits)
print('과일 갯수:', len(fruits))
print('야채:', vegetables)
print('야채 갯수:', len(vegetables))
print('동물 식품:',animal_products)
print('동물 식품 갯수:', len(animal_products))
print('인터넷 기술:', web_techs)
print('인터넷 기술 갯수:', len(web_techs))
print('국가:', countries)
print('국가 갯수:', len(countries))

# 리스트 변경


first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon

# 마지막 리스트
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# 인덱스로 리스트 접근하기

last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       # lemon
print(second_last)      # mango

# 리스트 슬라이싱

all_fruits = fruits[0:4] # 모든 리스트 받아 오기

# 같은 결과
all_fruits = fruits[0:]
orange_and_mango = fruits[1:3] # it does not include the end index
orange_mango_lemon = fruits[1:]


all_fruits = fruits[-4:] # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1] # it does not include the end index
orange_mango_lemon = fruits[-3:]



fruits[0] = 'Avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits)-1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

# checking items

does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# 리스트 추가 메소드 append

fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
print(fruits)

# 리스트 특정 위치에 집어 넣기 메소드 insert

fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
print(fruits)

# 항목을 지정해서 제거하는 메소드 remove

fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']

# 마지막 객체를 제거하고 얻어오는 메소드 pop

fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop()
print(fruits)       # ['orange', 'mango']

# del

del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]
print(fruits)       # ['orange', 'lemon']
del fruits
# print(fruits)       # This should give: NameError: name 'fruits' is not defined

# 리스트 안을 비우는 메소드 clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []

# 리스트를 복사하는 메소드 copy

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# 리스트를 더 해서 하나로 만드는 방법
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )

# 리스트를 더하는 메소드 extend
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )

# 갯수를 세는 메소드 count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# 위치가 어디인지 반환해 주는 메소드 index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))
# 거꾸로 정렬해 주는 메소드 Reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits.reverse())
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages.reverse())

# 정렬를 시키는 메소드 sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)