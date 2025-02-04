# Chapter 4: Primitive Types

## 打基础
* Python的bit operation (只操作integer,在作用于integer之前，将integer转换为binary，然后逐个bit操作，最后返回的结果是decimal十进制）  
#
	&  与
	|  或
	~  非
	^  异或
	>> bit右移
	<< bit左移
	X&(X-1)  Drop X最右侧的1
	X&~(X-1) Isolate X最右侧的1。结果为00001000，只有该1所在位置为1.
	X|(X-1)  将X最右侧的1右边的0全部填为1
	0x为16进制的前缀，A~F表示10~15，例子：0xFFFF
* 计算机内部用正数的补（非）来表示负数。 ~a = -(a+1). 比如 ~8 = -9.所以面对一个负数的二进制形式，欲求其具体数值，可以先求非，然后得到其代表的正数x，由此得知改负数为-(x+1)
* 64位的计算机，有64个位置来表示数字。第一位是表示符号的，0为正数，1为负数。因此64位计算机，最大的integer为2^63-1,最小的integer为-(2^63).

#
	random.randrange(start,end,step) 随机从range(start,end,step)抽取一个整数
    random.randint(start,end)        随机从start与end之间抽取一个整数，包含end
	random.random() 随机产生[0,1)内一个数
	random.shuffle(A) 对sequence A进行随机shuffle
    random.choice(A)  从sequence A中随机抽取一个元素
    random.choices(A,k=10) 从sequence A中随机抽取10次元素，有放回

### 4.1 parity.py
当需要对大量数字bit operation进行处理时，可以有2种思想提升效率：(打基础里提到的**commutativity and associativity**)  
1. Processing multiple bits at a time  
2. Caching results in an array-based lookup table.

### 4.2 swap_bits.py
1.bit_mask 000100001000  
2.Use bit mask with XOR to swap bits
 
### 4.3 reverse_bits.py
Cache ide

### 4.4 close_int_same_weight.py
01 10. 

### 4.5 primitive_multiply.py
#
	def add(a,b): 神了！  
	 return a if b==0 else add(a^b,(a&b)<<1)

### 4.6 primitive_divide.py
实现x//y 从高往下降的y^power使算法从0(N^2)提升到0(N)

### 4.7 power\_x_y.py
对y进行分解:  
比如x^21,y=21,则y=16+4+1. x^1,x^4,x^16之间可以联系起来**后面的可以利用前面**，所以算法复杂度为0(N),N为index of Y's MSB.


### 4.8 reverse_digits.py
### 4.9 is_palindrome_number.py
判断几位数N **math.floor(math.log2(X))+1**;对十进制，把log2换成log(X,10)即可  
掐头去尾

### 4.10 uniform_random.py
用0/1 RNG去产生给定范围内均匀分布的随机数

### 4.11 rectangle_intersection.py
考虑反面情况
滑块思想

    

