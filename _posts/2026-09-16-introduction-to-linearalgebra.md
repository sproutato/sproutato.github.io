---
title: "Introduction to Linearalgebra"
description: "study note of linear algebra, textbook : Introduction to Linear Algebra, 5th edition, by Gilbert Strang"
author: Sproutato
date: 2026-09-16 00:00:00 +0900
categories: [Linear Algebra]
tags: []
published: true
pin: false
math: true
mermaid: true
image:
  path: /assets/posts/2026-09-16-introduction-to-linearalgebra/cover.png
  lqip: data:image/webp;base64,UklGRpoAAABXRUJQVlA4WAoAAAAQAAAADwAABwAAQUxQSDIAAAARL0AmbZurmr57yyIiqE8oiG0bejIYEQTgqiDA9vqnsUSI6H+oAERp2HZ65qP/VIAWAFZQOCBCAAAA8AEAnQEqEAAIAAVAfCWkAALp8sF8rgRgAP7o9FDvMCkMde9PK7euH5M1m6VWoDXf2FkP3BqV0ZYbO6NA/VFIAAAA
  alt: "Cover image for Chapter 1: Introduction to Probability"
---

Projects: Linear Algebra (https://app.notion.com/p/Linear-Algebra-37e562ef2201808f94b6edcde2ac7502?pvs=21)

# Chapter 1

## 1.1 Vectors and Linear Combinations

## 1.2 Lengths and Dot Products

## 1.3 Matrices

# Chapter 2

## 2.1 Vectors and Linear Equations

- The central problem of linear algebra is to solve a system of equations. Those equations
are linear, which means that the unknowns are only multiplied by numbers-we never see
x times y.

### Linear Equation

- 선형대수의 중요 문제는 선형 방정식을 풀이하는 것이다.
- 선형 방정식이란 변수들이 오직 숫자들에 의해서만 곱해진 방정식을 말한다. 따라서 $x*y$ 등의 꼴은 볼 수 없다.
- 

![image.png](/assets/posts/2026-09-16-introduction-to-linearalgebra/image.png)

- 이 두 선형방정식을 행렬을 통해 표현하면 아래와 같다.

$$
\begin{bmatrix}
1 & -2 \\
3 & 2
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
=
\begin{bmatrix}
1 \\
11
\end{bmatrix}
$$

### Geometry of Linear Algebra

- 같은 행렬을 보더라도 다르게 해석할 수 있다.
- 

$$
\begin{bmatrix}
1 & -2 \\
3 & 2
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
=
\begin{bmatrix}
1 \\
11
\end{bmatrix}

\quad \quad \text{(1)}
$$

#### Row Picture

- 위 행렬을 두개의 직선 방정식으로 해석한다면. 아래와 같이 표현할 수 있다.
- 행관점에서의 해석은 두 직선의 교점을 보여준다.

![image.png](/assets/posts/2026-09-16-introduction-to-linearalgebra/image%201.png)

- 이때 $x,y$ 두 값은 두 직선이 만나는 좌표 값을 의미하게 된다.

#### Column Picture

- $(1)$번 행렬을 열 관점에서 보면 두 벡터의 선형 결합 형태로 해석할 수 있다.

$$
x\begin{bmatrix}1\\3\end{bmatrix}+y\begin{bmatrix}-2\\2\end{bmatrix}=\begin{bmatrix}1\\11\end{bmatrix}=b
$$

- 열 관점은 열벡터들을 결합하여 우항의 벡터를 만든다.
- 

![image.png](/assets/posts/2026-09-16-introduction-to-linearalgebra/image%202.png)

### Three Equations in Three Unknowns

- 3차원에서의 경우를 생각해보기
- 변수를 3개 갖는 3개의 선형 방정식은 다음과 같이 두가지 방식으로 표현 가능하다.

$$
\begin{aligned}x+2y+3z&=6\\2x+5y+2z&=4\\6x-3y+z&=2\end{aligned},
\qquad

A\mathbf{x}=\mathbf{b},\qquad
\begin{bmatrix}
1 & 2 & 3\\
2 & 5 & 2\\
6 & -3 & 1
\end{bmatrix}
\begin{bmatrix}
x\\
y\\
z
\end{bmatrix}
=
\begin{bmatrix}
6\\
4\\
2
\end{bmatrix}

$$

- Row Picture
    - 이를 행 관점에서 본다면 세가지 평면의 방정식의 해를 구하는 문제로 볼 수 있다.
    - 
    
    ![image.png](/assets/posts/2026-09-16-introduction-to-linearalgebra/image%203.png)
    
    - 1번, 2번 방정식이 만드는 두 평면의 교선과 3번째 방정식이 만드는 평면이 만나는 교점이  연립방정식의 해 $x,y,z$ 가 된다.$(0,0,2)$
    - 
- Column Picture
    - 이를 열 관점에서 본다면 3차원 공간에서의 세 벡터를 선형 결합하여 우측 $b$ 벡터를 만들 때 각 행벡터에 곱해지는 scalar 값이 무엇인지 구하는 문제가 된다.
    
    $$
    x\begin{bmatrix}1\\2\\6\end{bmatrix}+y\begin{bmatrix}2\\5\\-3\end{bmatrix}+z\begin{bmatrix}3\\2\\1\end{bmatrix}=\begin{bmatrix}6\\4\\2\end{bmatrix}=\mathbf{b}
    $$
    

![image.png](/assets/posts/2026-09-16-introduction-to-linearalgebra/image%204.png)

### The Matrix Form of the Equations

#### Coefficient Matrix

- 연립 방정식을 행렬을 사용하여 표현이 가능하다.이때 $A$를 “coefficient matrix”라 한다.

$$
\begin{aligned}x+2y+3z&=6\\2x+5y+2z&=4\\6x-3y+z&=2\end{aligned},
\qquad

A\mathbf{x}=\mathbf{b},\qquad
\begin{bmatrix}
1 & 2 & 3\\
2 & 5 & 2\\
6 & -3 & 1
\end{bmatrix}
\begin{bmatrix}
x\\
y\\
z
\end{bmatrix}
=
\begin{bmatrix}
6\\
4\\
2
\end{bmatrix}

$$

#### Multiplication by rows/columns

- 행렬의 곱을 풀이할 때 행 관점에서의 곱셈과 열 관점의 곱셈 두가지 방식으로 풀이할 수 있다.
- 

$$
\begin{aligned}

&A\mathbf{x}\text{ comes from dot products:}\\

&\qquad
A\mathbf{x}
=
\begin{bmatrix}
(\operatorname{row}1)\cdot\mathbf{x}\\
(\operatorname{row}2)\cdot\mathbf{x}\\
(\operatorname{row}3)\cdot\mathbf{x}
\end{bmatrix}
\\
\\

&A\mathbf{x}\text{ is a combination of column vectors:}
\\
&\qquad
A\mathbf{x}
=
x(\operatorname{column}1)
+y(\operatorname{column}2)
+z(\operatorname{column}3)

\end{aligned}
$$

## 2.2 The Idea of Elimination

- Elimination의 목표는 coefficient Matrix를 upper triangular꼴로 정리하여 방정식의 해를 쉽게 구하는 것이다.
- 

$$
\begin{cases}x-2y=1\\3x+2y=11\end{cases}
\quad
\xrightarrow{\,R_2\leftarrow R_2-3R_1\,}
\quad
\begin{cases}x-2y=1\\\qquad8y=8\end{cases}
$$

#### Upper/Lower Triangular matrix

$$
\begin{cases}x-2y=1\\\qquad8y=8\end{cases}
$$

- 위 연립 방정식을 행렬로 표현하면  아래와 같다.
- 

$$
Ux=

\begin{bmatrix}1 & -2\\0 & 8\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}1\\8\end{bmatrix}

,\qquad (U\text{: Upper triangular matrix})
\\

$$

- 이때, 행렬 $U$는 대각선(원소가 1,8)을 기준으로 아래 원소의 값들이 모두 $0$이다. 이러한 삼각행렬을 상삼각행렬(upper triangular matrix)라고 한다.
- 반대의 경우 ( 대각선을 기준으로 윗 부분의 원소들이 ‘0’인 행렬)을 “하삼각행렬(Lower triangular matrix)라고 한다.
- 

$$
L=\begin{bmatrix}2 & 0 & 0\\-1 & 3 & 0\\4 & 5 & 1\end{bmatrix}, \qquad (L \text{: Lower triangular matrix})
$$

#### Back substitution

- Elimination 에서 Upper triangular matrix를 만드는 이유이다.
- 마지막 방정식이 $8y = 8$ 꼴이기 때문에 쉽게 나머지 해를 구할 수 있다.

$$
Ux=

\begin{bmatrix}1 & -2\\0 & 8\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}1\\8\end{bmatrix}

,\qquad (U\text{: Upper triangular matrix})
\\

$$

### To Eliminate x

- Subtract a multiple of equation 1 from equation 2.

$$
\begin{cases}4x-8y=4\\3x+2y=11\end{cases}\quad\xrightarrow{\substack{\frac{3}{4}R_1\\ R_2\leftarrow R_2-\frac{3}{4}R_1}}\quad\begin{cases}4x-&8y=4\\
&8y=8

\end{cases}
$$

![image.png](/assets/posts/2026-09-16-introduction-to-linearalgebra/image%205.png)

- 왼쪽 연립방정식을 오른쪽 연립방정식 꼴로 바꾸기 위해
- $\frac{3}{4}$을 첫번째 방정식 $R_1$에 곱하여 두번째 방정식에서 빼준다.$newR_2 = R_2 - \frac{3}{4}R_1$

#### Pivot

- first nonzero in the row that does the elimination $(pivot_1 = 4)$
- 제거를 수행하는 행에서 $0$이 아닌 첫번째 값을 말한다.
- 위 경우에서 $Pivot$은 elimination을 하는 첫번째 행의 첫번째 상수 $4$가 $pivot$이다.
- 우측 연립방정식에서 Pivot은 각각 4,8이다.
- Pivot은 elimination연산 이후 대각선에 위치하게 된다.
- 연립방정식의 해를 구하기 위해서는 변수의 개수 이상의 Pivot이 필요.

#### Multiplier

- (entry to eliminate) divided by (pivot) = ¾, $(\text{multiplier } l= \frac{3}{4})$
- 제거의 대상이 되는 행의 계수($x$의 계수 $3$)를 pivot으로 나눈 값이다.

### Breakdown of Elimination

- Example 1 : Permanent failure with no solution
    - 
    
    $$
    \begin{cases}
    
    x-2y=1
    \\3x-6y=11
    
    \end{cases}
    \quad
    
    \xrightarrow{\,R_2\leftarrow R_2-3R_1\,}
    
    \quad\begin{cases}
    x-2y=1\\
    0y=8&
    \end{cases}
    $$
    
    - 구해야 하는 변수는 $x,y$두개이나 Pivot은 $1$ 하나이기 때문에 해가 존재하지 않는다.
    
    ![image.png](/assets/posts/2026-09-16-introduction-to-linearalgebra/image%206.png)
    
    - Row picture :
        - 두 평행한 직선이므로, 해가 존재하지 않음
    - Column picture :
        - 두 벡터가 같은 방향을 향하는 상황에서 우변 $(1,11)$은 두 벡터 위에 존재하지 않는다.
        - 어떠한 선형 결합을 통해서도 우변을 만들 수 없으므로 해가 존재하지 않는다.
        
- Example 2 : Failure with infinitely many solutions
    - 
    
    $$
    \begin{cases}x-2y=1\\3x-6y=3\end{cases}\quad\xrightarrow{\,R_2\leftarrow R_2-3R_1\,}\quad\begin{cases}x-2y=1\\
    \qquad0y=0\end{cases}\qquad\text{only one pivot.}
    $$
    
    - 모든 $y$가 $0y = 0$을 만족한다.  무한한 $y$값에 따라 무한한 $x$값이 존재한다.
    - 
    
    ![image.png](/assets/posts/2026-09-16-introduction-to-linearalgebra/image%207.png)
    
    - Row picture :
        - 제공된 두 방정식이 사실 동일한 방정식이다. 때문에 해당 직선위에 존재하는 모든 점들이 두 방정식을 만족한다.
    - Column picture :
        - 우변 벡터 $b(1,3)$를 포함한 세 벡터가 같은 방향을 향하고 있으므로 두 열벡터를 사용해 우변벡터를 만들 수 있는 조합이 무한히 존재한다.
    
- Example 3 : Temporary failure (zero in pivot)
    - 이 경우에는 열을 교환하여 풀이가 가능하다.
    - $0$은 Pivot이 될 수 없다. 첫번째 방정식이 $x$를 포함하는 항이 없을 때 행을 치환하여 풀 수 있다.
    - 
    
    $$
    \begin{cases}0x+2y=4\\3x-2y=5\end{cases}\quad\xrightarrow{\,R_1\leftrightarrow R_2\,}\quad\begin{cases}3x-2y=5\\
    \qquad2y=4\end{cases}
    $$
    
- 예시 1과 2는  특이 방정식이다 ( Pivot이 오직 한개만 존재). 즉 해가 존재하지 않거나 특정지을 수 없다.
- 반면 예시 3의 경우 비특이 방정식이다. 즉 해를 특정지을 수 있다.

### Three Equations in Three Unknowns

### Elimination from A to U

- 

$$
\begin{cases}2x+4y-2z=2\\4x+9y-3z=8\\-2x-3y+7z=10\end{cases}
$$

- 위 연립방정식을 행렬로 표현하여 가우스 소거를 진행하면
- 
    
    $$
    \begin{aligned}
    
    \begin{bmatrix}
    2&4&-2\\4&9&-3\\-2&-3&7
    \end{bmatrix}
    
    \begin{bmatrix}
    x\\y\\z
    \end{bmatrix}
    
    &=
    \begin{bmatrix}
    2\\8\\10
    \end{bmatrix}\\[8pt]
    \\
    \xrightarrow{
    \substack{
    R_2\leftarrow R_2-2R_1\\\\
    R_3\leftarrow R_3+R_1
    }
    }
    
    \begin{bmatrix}
    2&4&-2\\
    0&1&1\\
    0&1&5
    \end{bmatrix}
    
    \begin{bmatrix}
    x\\y\\z
    \end{bmatrix}
    &=
    \begin{bmatrix}
    2\\4\\12
    \end{bmatrix}\\[8pt]
    \\
    \xrightarrow{\,
    R_3\leftarrow R_3-R_2\,}
    \underbrace{
    \begin{bmatrix}
    2&4&-2\\
    0&1&1\\
    0&0&4
    \end{bmatrix}}_{U}
    
    \begin{bmatrix}
    x\\y\\z
    \end{bmatrix}
    
    &=
    \underbrace{
    \begin{bmatrix}
    2\\4\\8
    \end{bmatrix}}_{\mathbf{c}}
    
    \end{aligned}
    $$
    
    - 위와 같이 $Ax=b$  가 $Ux=c$ 꼴로 바뀌고 Pivot 3개를 얻을 수 있다.
    - $p_{pivot} = (2,1,4)$
    - $x,y,z = (-1,2,2)$
- Row Picture
    
    $$
    \begin{cases}
    2x+4y-2z=2\\
    0x+y-z=4\\
    0x-0y+4z=8
    \end{cases}
    $$
    
    - 기존 연립방정식을 통해 그려지는 평면 3개는 모두 $x,y,z$에 의해 그려지는 그래프이다. (The original planes are sloping)
    - 하지만 $Ux=c$ 꼴로 변환한 후에 $Ux$에 의해 그려지는 평면을 보면 기울어진 평면 1개, $x$축과 평행한 평면 1개, $x,y$평면에 평행한 평면 1개 로 비교적 간단하게 변한 것을 알 수 있다.
    - 
    
    ![image.png](/assets/posts/2026-09-16-introduction-to-linearalgebra/image%208.png)
    
    ![image.png](/assets/posts/2026-09-16-introduction-to-linearalgebra/image%209.png)
    
- Column Picture
    - 열 관점에서 보면 한 벡터 $(b)$를 만드는  $A$행렬의 열벡터들의 결합을 보여준다.
    - 
    - 
        
        $$
        A\mathbf{x}=(-1)\begin{bmatrix}2\\4\\-2\end{bmatrix}+2\begin{bmatrix}4\\9\\-3\end{bmatrix}+2\begin{bmatrix}-2\\-3\\7\end{bmatrix}=\begin{bmatrix}2\\8\\10\end{bmatrix}=\mathbf{b}
        $$
        
        ![image.png](/assets/posts/2026-09-16-introduction-to-linearalgebra/image%2010.png)
        

## 2.3 Elimination Using Matrices

### > Review

- 앞선 챕터 1 에서는 벡터의 개념과 기본적인 연산을 다루었다.
- 챕터 2.1 에서는 행렬을 행관점, 열관점에서 해석하는 법을 다루었다.
- 챕터 2.2 에서는 Elimination의 아이디어를 다루었고, 그 과정에서 아래 개념을 배웠다.
    - 삼각행렬
    - back substitution
    - pivot
    - multiflier
    - breakdown of Elimination ( 해를 구할 수 없거나 무수히 많은 경우)

### > Goal

- Our goal is to see that matrices do something.
- $E$ acts on a vector $b$ or a matrix $A$ to produce a new vector $Eb$ or a new matrix $EA$.

#### - Elimination matrices

- $E_{ij}$ :  Multiply the $j^{th}$ equation by $l_{ij}$ and subtract from the $i^{th}$equation. (This eliminates
$x_j$ from equation $i$.)
- We need a lot of these simple matrices $E_{ij}$, one for every nonzero to be eliminated below the main diagonal.
- Fortunately, They can combine into one overall matrix $E$ that takes all steps at once
- The neatest way is to combine all their inverses $( E_{ij}^{-1} )$into one overall matrix $L =  E^{-1}$

### > The Matrix Form of One Elimination Step

#### -Elimination matrix

- 가우스 소거를 사용하여 Elimination을 진행했었다.
- 이때 행렬 $$ $A$ 를 상삼각행렬 꼴로 바꾸어 Back substitution을 사용하여 해(vector $x$) 를 구하였다.
- 이때 $A$의 행끼리 multiflier $l_{ij}$를 곱하고 빼기 연산을 통해 ($b$도 함께) $A$를 $U(upper triangular matrix)$ 꼴로 바꾸었다.
- 이 연산을 행렬의 곱으로 표현할 수 있는데 ( $E_{ij}Ax = E_{ij}b$  )
- 이때 Elimination matrix $E_{ij}$에는  각 연산에 사용된 multiflier $l_{ij}$의 정보가 들어있다.
- $E_{1 2}E_{13} \cdots E_{ij}Ax = EAx$ 이다.
    - 행렬 $E_{ij}$를 하나의 함수로 볼 때,  행렬  $E$ $E$$E_{1 2}E_{13} \cdots E_{ij}$들의 합성함수와 같다.
    - 행렬의 이러한 특성을 ( 여러 행렬의 곱이 하나의 행렬로 합해질 수 있는 것) 행렬의 결합법칙이라고 한다.
- 이때 행렬 $E$를 소거행렬이라고 한다.
- $EAx=Ux=Eb$ 이다. ($EA = U$)이때 모든 변에 $E^{-1}(=L)$을 곱해주면(역행렬이 존재할 때)
- 아래 꼴로 정리함으로써  multiflier의 정보를 함께 표기할 수 있다.

$$
E^{-1}EAx=E^{-1}Ux=E^{-1}Eb \\[6pt]
Ax=LUx=b 

$$

#### -Elementary matrix

- 기본행렬
- 단위 행렬 (Identity matrix)에 기본행연산을 오직 한 번만 적용하여 얻은 행렬을 말한다.
- 소거 행렬이 기본행 연산을 위한 단위 행렬들을 하나로 합성한 것과 같다.

#### -Identity matrix

- 항등행렬
- 주대각선(main diagonal)의 원소들이 모두 $1$이며 나머지 원소들은 $0$인 정방 행렬(square matrix) 을 말한다.

### > Matrix Multiplication

#### - associative law

- 결합법칙
- $E_{1 2}E_{13} \cdots E_{ij}Ax = EAx$ 이다.
- 행렬 $E_{ij}$를 하나의 함수로 볼 때,  행렬  $E$ 는 $E_{1 2}E_{13} \cdots E_{ij}$들의 합성함수와 같다.
- 행렬의 이러한 특성을 ( 여러 행렬의 곱이 하나의 행렬로 합해질 수 있는 것) 행렬의 결합법칙이라고 한다.
- 이때 행렬 $E$를 소거행렬이라고 한다.

#### -commulative law

- 교환법칙
- 함수 합성은 일반적으로 교환법칙을 만족하지 않는다.
- 예를 들어
    
$$
f,g : \mathbb{R} \to \mathbb{R}, \quad f(x) = x+1, \quad g(x) = 2x
$$
    
- 이고
    
    $$
    \begin{aligned}
    (f \circ g)(x) &= 2x+1\\[6pt]
    (g \circ f)(x) &= 2x+2
    \end{aligned}
    $$
    
- 이므로
    
    $$
    f \circ g \neq g \circ f
    $$
    
- 행렬 곱도 선형변환의 합성을 표현하므로 일반적으로 교환법칙을 만족하지 않는다.
    
    $$
    AB \neq BA
    $$
    

### > The Matrix $P_{ij}$ for a Row Exchange

#### -permutation matrix

- 치환 행렬
- 항등행렬의 행 또는 열을 임의의 순서로 재배열한 행렬
- 행 혹은 열의 순서를 바꾸는 역할을 함

### > The Augmented Matrix

- 확대행렬 $[ v_1,v_2|b]$꼴
- 연립 일차방정식 $Ax=b$에서 계수행렬 $A$와 우변 벡터 $b$를 하나로 붙여서 표현한 행렬
- 확대행렬의 각 행은 하나의 방정식
- 소거를 통해 방정식의 해를 찾을 때 불필요한 기호를 없애고 간단히 표기하기위한 방법

## 2.4 Rules for Matrix Operations

## 2.5 Inverse Matrices

## 2.6 Elimination = Factorization: \(A = LU\)

## 2.7 Transposes and Permutations

# Chapter 3

## 3.1 Spaces of Vectors

## 3.2 The Nullspace of \(A\): Solving \(Ax = 0\) and \(Rx = 0\)

## 3.3 The Complete Solution to \(Ax = b\)

## 3.4 Independence, Basis and Dimension

## 3.5 Dimensions of the Four Subspaces

# Chapter 4

## 4.1 Orthogonality of the Four Subspaces

## 4.2 Projections

## 4.3 Least Squares Approximations

## 4.4 Orthonormal Bases and Gram-Schmidt

# Chapter 5

## 5.1 The Properties of Determinants

## 5.2 Permutations and Cofactors

## 5.3 Cramer's Rule, Inverses, and Volumes

# Chapter 6

## 6.1 Introduction to Eigenvalues

## 6.2 Diagonalizing a Matrix

## 6.3 Systems of Differential Equations

## 6.4 Symmetric Matrices

## 6.5 Positive Definite Matrices

# Chapter 7

## 7.1 Image Processing by Linear Algebra

## 7.2 Bases and Matrices in the SVD

## 7.3 Principal Component Analysis (PCA by the SVD)

## 7.4 The Geometry of the SVD

# Chapter 8

## 8.1 The Idea of a Linear Transformation

## 8.2 The Matrix of a Linear Transformation

## 8.3 The Search for a Good Basis

# Chapter 9

## 9.1 Complex Numbers

## 9.2 Hermitian and Unitary Matrices

## 9.3 The Fast Fourier Transform

# Chapter 10

## 10.1 Graphs and Networks

## 10.2 Matrices in Engineering

## 10.3 Markov Matrices, Population, and Economics

## 10.4 Linear Programming

## 10.5 Fourier Series: Linear Algebra for Function

## 10.6 Computer Graphics

## 10.7 Linear Algebra for Cryptography

# Chapter 11

## 11.1 Gaussian Elimination in Practice

## 11.2 Norms and Condition Numbers

## 11.3 Iterative Methods and Preconditioners

# Chapter 12

## 12.1 Mean, Variance, and Probability

## 12.2 Covariance Matrices and Joint Probabilities

## 12.3 Multivariate Gaussian and Weighted Least Squares

![image.png](/assets/posts/2026-09-16-introduction-to-linearalgebra/image%2011.png)