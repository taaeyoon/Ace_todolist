# Ace_todolist

This is python CLI application.

## 목차

&nbsp;&nbsp;1. [Github repository rules](#repo_rules)<br/>
&nbsp;&nbsp;2. [Coding convention - for Ace team](#coding_convention)<br/>

## <div id = "repo_rules"> 1. Github reporitory rules </div>

### 1.1. 각자 작업은 fork한 저장소에서

repository를 만드신 분을 제외한 모든 분들은 fork한 저장소에서 작업을 합니다 

repository를 만드신 분은 master branch가 아닌 branch를 새로 만들어 작업을 해주시면 됩니다

### 1.2. 해결해야 할 일들은 issue를 발행 

#### 1.2.1. 해결해야할 항목이나 과제일 경우

assignee를 지정하여 발행합니다 (스스로를 지정해도 좋습니다) 

#### 1.2.2. 토의하고 싶은 경우

assignee를 모두 지정하여 발행합니다 

#### 1.2.3. 해결한 항목(과제) 이나 토의가 끝난 issue인 경우 

해당 issue를 close 합니다 


### 1.3. 발행한 issue를 해결할 때는 branch를 만들어서 해결 

발행한 issue를 해결해야하는 경우에는 branch를 만들어서 해결을 합니다 

* branch name : issue#번호


### 1.4. Github 저장소에 push 하기 전

#### 1.4.1. python 코딩을 한 경우 

각자의 컴퓨터에서 직접 코드를 실행한 후, 에러가 있는 지 없는 지 확인해봅니다

에러가 존재할 경우, 에러를 직접 해결합니다

#### 1.4.2. pull을 해주어 저장소를 최신 상태로 유지한 후에 push를 합니다 
### 1.5. pull request를 할 때

conflict가 일어나지 않는 한, 그대로 merge를 합니다


## <div id = "coding_convention"> 2. Python Coding Convention for Ace team </div>

### 2.1. Indentation

indentation은 space 4칸으로 한다

```python
# example
def sum (a,b):
    print(a+b)
```    

### 2.2. 함수 이름, 변수 이름 

* 알아볼 수 있게 적는다(즉, a,b,c,x,y,z 등 자신만의 기호로 적지 않는다)

* 이름 중간에 띄어쓰기가 필요할 경우 **_(underscore)**를 쓴다 

```python

# loop 횟수를 세는 counter 변수를 만들고 싶은 경우
# 아래와 같이 띄어쓰기가 필요한 곳에 _를 쓴다
loop_counter = 0 
```    

### 2.3. 한 줄에 적을 수 있는 글자 수 

한 줄에 최대 79자까지 적는다 

### 2.4. 괄호, 연산자 공백에 대해서 

* (),[],{} 등에서 의미 없는 공백은 두지 않기

* 연산자와 변수 사이는 공백을 둔다

* ,를 쓸 때도 공백을 둔다

```python
#example
print(a, b)

c = a + b
```

### 2.5. 주석 

* 각 파일에 대한 설명은 가장 처음에 주석으로 적어준다 

* 조건문이나 반복문에 대한 설명이 필요할 경우,최대한 간단하게 한 줄 정도로 주석을 적어둔다
