# Day 2 记录
## 函数
### 函数的定义：
函数是编程中一个非常重要的概念，它具有特定功能的代码块
可以在程序中多次被调用。
函数通过接受输入的值（作为参数），执行特定的操作，并返回输出（返回值）

### 为什么要使用函数

1. 代码可以重复使用
2. 提高代码的可读性
3. 简化复杂性：

可以把复杂的操作拆分成多个小步骤，每一个步骤用函数。

### 函数的组成

1. 定义函数 def (define)
2. 函数名（小写开头，见名知意，小驼峰，可以下划线）

def carBrand

def student_name

3. 参数（ ）：
4. 函数体 -> 要执行的代码块、记得缩紧
5. 返回值 return （return 后面接的什么就返回什么）

```python
# 函数举例

def super_calculator(a, b, c):
    d = a * b / c
    return d
```

```python
def greeting_bot(name):
    print("Hello " + name)
    return "大帅哥"

a = greeting_bot('杨家瑞')

print(a)
```

```python
#
# def greeting_bot(name):
#     print("Hello " + name)
#     return "大帅哥"
#
# a = greeting_bot('杨家瑞')
#
# print(a)

# 函数的参数（位置参数、关键子参数）

def bmi_calculator(height,weight, name, age):
    bmi_value = weight / height**2
    print(f'{name}的年龄是{age}，她/他的BMI值是{bmi_value}')
    return bmi_value


bmi_calculator(1.8, 100, age=6, name='杨家瑞')
bmi_calculator(1.8, 71, age=18, name='周子睿')
bmi_calculator(1.73, 70, age=30, name='hua')
```


## 文件存储

```python
with open('demo.txt','w', encoding='utf-8') as f:
    f.write('因为所以、科学道理')
    f.close()

with open('demo.txt','r',encoding='utf-8') as f:
    print(f.read())
```

### 挑战练习
```python
# 挑战练习，写一个ATM，txt 文件记录你们的卡余额，用户
# 用户可以选择 存款、取款、查看余额

# 先存钱
def savings():
    saving_value = int(input('请输入你要存入的数字>>>'))
    with open('bank.txt', 'r', encoding='utf-8') as f:
        actual_value = int(f.read())
    actual_value += saving_value
    with open('bank.txt', 'w', encoding='utf-8') as f:
        f.write(str(actual_value))

def balance():
    with open('bank.txt', 'r', encoding='utf-8') as f:
        actual_value = int(f.read())
        print(f'您当前的余额是>>>¥ {actual_value} 元')
        return actual_value

def wuwuwu():
    money = int(input('请输入你想要取走的金额>>>'))
    with open('bank.txt', 'r', encoding='utf-8') as f:
        actucal_value = int(f.read())
        if actucal_value < money:
            print('当前余额不足～请好好挣钱吧')
        else:
            actucal_value -= money
            print(f'取款成果，当前余额 ¥ {actucal_value} 元')
    with open('bank.txt', 'w', encoding='utf-8') as f:
        f.write(str(money))

bank_operation = {1: savings, 2: balance, 3: wuwuwu}

while True:
    print('1 ---> 存，2 ---> 余，3 ---> 取')
    user_choice = input('请输入你的选项>>>')
    if user_choice == '1':
        bank_operation.get(1)()
    elif user_choice == '2':
        bank_operation.get(2)()
    elif user_choice == '3':
        bank_operation.get(3)()
    else:
        print('Invalid Input')


```

## 类
面向对象编程 - OOP
在python里面，一切皆是对象
class
class Dog
class School

类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。

类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。

数据成员：类变量或者实例变量, 用于处理类及其实例对象的相关的数据。

方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。

局部变量：定义在方法中的变量，只作用于当前实例的类。

实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。

继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。