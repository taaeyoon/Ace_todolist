# Python Coding Convention - Ace team 

## 1. Indentation

indentation은 space 4칸으로 한다

```python
# example
def sum (a,b):
    print(a+b)
```    

## 2. 함수 이름, 변수 이름 

* 알아볼 수 있게 적는다(즉, a,b,c,x,y,z 등 자신만의 기호로 적지 않는다)

* 이름 중간에 띄어쓰기가 필요할 경우 **_(underscore)**를 쓴다 

```python

# loop 횟수를 세는 counter 변수를 만들고 싶은 경우
# 아래와 같이 띄어쓰기가 필요한 곳에 _를 쓴다
loop_counter = 0 
```    

## 3. 한 줄에 적을 수 있는 글자 수 

한 줄에 최대 79자까지 적는다 

## 4. 괄호, 연산자 공백에 대해서 

* (),[],{} 등에서 의미 없는 공백은 두지 않기

* 연산자와 변수 사이는 공백을 둔다

* ,를 쓸 때도 공백을 둔다

```python
#example
print(a, b)

c = a + b
```

## 5. 주석 

* 각 파일에 대한 설명은 가장 처음에 주석으로 적어준다 

* 조건문이나 반복문에 대한 설명이 필요할 경우,최대한 간단하게 한 줄 정도로 주석을 적어둔다