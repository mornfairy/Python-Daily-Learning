# Python100_day1：

1、03分支结构

1.1、python分支结构使用if，elif和else关键字。

1.2、Python中没有用花括号来构造代码块而是**使用了缩进的方式来表示代码的层次结构**，换句话说**连续的代码如果又保持了相同的缩进那么它们属于同一个代码块**，相当于是一个执行的整体。**缩进**可以使用任意数量的空格，但**通常使用4个空格**。

1.3、在之前我们提到的Python之禅中有这么一句话“Flat is better than nested.”，之所以提倡代码“扁平化”是因为嵌套结构的嵌套层次多了之后会严重的影响代码的可读性，所以能使用扁平化的结构时就不要使用嵌套。

# Python100_day2:

1、05 构造程序逻辑

1.1、锻炼自己把用人类自然语言描述的算法（解决问题的方法和步骤）翻译成Python代码的能力，而这件事情必须通过大量的练习才能达成。思维转化！

1.2、水仙花数的例子体会下，两组程序的差别，代码的简洁程度。

# Python100_day3:

06函数的模块和使用

1、编程大师*Martin Fowler*先生曾经说过：“**代码有很多种坏味道，重复是最坏的一种！**”，要写出高质量的代码首先要解决的就是重复代码的问题。

2、在Python中可以使用`def`关键字来定义函数，和变量一样每个函数也有一个响亮的名字，而且命名规则跟变量的命名规则是一致的。在函数名后面的圆括号中可以放置传递给函数的参数，这一点和数学上的函数非常相似，程序中函数的==参数就相当于是数学上说的函数的自变量==，而函数执行完成后我们可以通过==`return`关键字来返回一个值，这相当于数学上说的函数的因变量==。

3、在了解了如何定义函数后，我们可以对上面的代码进行重构，所谓重构就是在不影响代码执行结果的前提下对代码的结构进行调整

4、函数是绝大多数编程语言中都支持的一个代码的"构建块"，但是Python中的函数与其他语言中的函数还是有很多不太相同的地方，其中一个显著的区别就是Python对函数参数的处理。在Python中，函数的参数可以有默认值，也支持使用可变参数，所以Python并不需要像其他语言一样支持[函数的重载](https://zh.wikipedia.org/wiki/函数重载)，因为我们在定义一个函数的时候可以让它有多种不同的使用方式

5、对于任何一种编程语言来说，给变量、函数这样的标识符起名字都是一个让人头疼的问题，因为我们会遇到命名冲突这种尴尬的情况。最简单的场景就是在同一个.py文件中定义了**两个同名函数**，由于Python没有函数重载的概念，那么**后面的定义会覆盖之前的定义**，也就意味着两个函数同名函数实际上只有一个是存在的。

6、Python中每个文件就代表了一个模块（module），我们在不同的模块中可以有同名的函数，在使用函数的时候我们**通过`import`关键字导入指定的模块**就可以区分到底要使用的是哪个模块中的`foo`函数

7、**将代码中重复出现的和相对独立的功能抽取成函数**后，我们可以**组合使用这些函数**来解决更为复杂的问题，这也是我们为什么要定义和使用函数的一个非常重要的原因

8、python中可以在函数内部重新定义函数,事实上，Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索

9、使用global关键字声明全局变量.在实际开发中，我们应该尽量减少对全局变量的使用，因为全局变量的作用域和影响过于广泛，可能会发生意料之外的修改和使用，除此之外全局变量比局部变量拥有更长的生命周期，可能导致对象占用的内存长时间无法被[垃圾回收](https://zh.wikipedia.org/wiki/垃圾回收_(計算機科學))

10、减少全局变量的使用就意味着我们应该尽量让变量的作用域在函数的内部，但是如果我们希望将一个局部变量的生命周期延长，使其在定义它的函数调用结束后依然可以使用它的值，这时候就需要使用[闭包](https://zh.wikipedia.org/wiki/闭包_(计算机科学))

11、==python函数套用的基本格式==：

```
def main():
    # Todo: Add your code here
    pass


if __name__ == '__main__':
    main()
```

12、所谓**字符串**，就是由零个或多个字符组成的有限序列，在Python程序中，如果我们把单个或多个字符用单引号或者双引号包围起来，就可以表示一个字符串。

13、可以在字符串中使用`\`（反斜杠）来表示转义，也就是说`\`后面的字符不再是它原来的意义，例如：`\n`不是代表反斜杠和字符n，而是表示换行；而`\t`也不是代表反斜杠和字符t，而是表示制表符。所以如果想在字符串中表示`'`要写成`\'`，同理想表示`\`要写成`\\`.如果不希望字符串中的`\`表示转义，我们可以通过在字符串的最前面加上字母`r`来加以说明。



14、Python为字符串类型提供了非常丰富的运算符，我们可以使用`+`运算符来实现字符串的拼接，可以使用`*`运算符来重复一个字符串的内容，可以使用`in`和`not in`来判断一个字符串是否包含另外一个字符串（成员运算），我们也可以用`[]`和`[:]`运算符从字符串取出某个字符或某些字符（切片运算）.

# Python100_day4:

1、字符串的格式化输出：

```
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
```

```
a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))
```

```
a, b = 5, 10
print(f'{a} * {b} = {a * b}')
```

Python 3.6以后，格式化字符串还有更为简洁的书写方式，就是在字符串前加上字母`f`

2、数值类型是标量类型，也就是说这种类型的对象没有可以访问的内部结构；而字符串类型是一种结构化的、非标量类型，所以才会有一系列的属性和方法

3、列表（`list`），也是一种结构化的、非标量类型，它是值的有序序列，每个值都可以通过索引进行标识，定义列表可以将列表的元素放在`[]`中，多个元素用`,`进行分隔，可以使用`for`循环对列表元素进行遍历，也可以使用`[]`或`[:]`运算符取出列表中的一个或多个元素。

4、Python中还有另外一种定义生成器的方式，就是通过`yield`关键字将一个普通函数改造成生成器函数。

5、Python中的元组与列表类似也是一种容器数据类型，可以用一个变量（对象）来存储多个数据，不同之处在于元组的元素不能修改。顾名思义，我们把多个元素组合到一起就形成了一个元组，所以它和列表一样可以保存多条数据。

6、元组在创建时间和占用的空间上面都优于列表。我们可以使用sys模块的getsizeof函数来检查存储同样的元素的元组和列表各自占用了多少内存空间，这个很容易做到。

7、字典是另一种可变容器模型，Python中的字典跟我们生活中使用的字典是一样一样的，它可以存储任意类型对象，与列表、集合不同的是，字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开。下面的代码演示了如何定义和使用字典。

# Python100_day5:

1、"把一组数据结构和处理它们的方法组成对象（object），把相同行为的对象归纳为类（class），通过类的封装（encapsulation）隐藏内部细节，通过继承（inheritance）实现类的特化（specialization）和泛化（generalization），通过多态（polymorphism）实现基于对象类型的动态分派。"

2、在Python中可以使用`class`关键字定义类，然后在类中通过之前学习过的函数来定义方法，这样就可以将对象的动态特征描述出来，代码如下所示。

3、写在类中的函数，我们通常称之为（对象的）方法，这些方法就是对象可以接收的消息。

4、在实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问（后面会讲到）。面向对象有三大支柱：封装、继承和多态。

# Python100_day6:

10.图形用户界面和游戏开发

1、基本上使用tkinter来开发GUI应用需要以下5个步骤：

             1. 导入tkinter模块中我们需要的东西
             2. 一个顶层窗口对象并用它来承载整个GUI应用。

3. 在顶层窗口对象上添加GUI组件。

​            4. 通过代码将这些GUI组件的功能组织起来。

​            5. 进入主事件循环(main loop)。

# Python100_day7:

1、在Python中，我们可以将那些在运行时可能会出现状况的代码放在`try`代码块中，在`try`代码块的后面可以跟上一个或多个`except`来捕获可能出现的异常状况。除了使用文件对象的`read`方法读取文件之外，还可以使用`for-in`循环逐行读取或者用`readlines`方法将文件按行读取到一个列表容器中

2、python中的列表和元组，列表用[]表示，元组的创建很简单，只要将一些值以逗号分隔就可以创建，也可以使用（）。二者的核心区别在于：列表可以修改，元组不可以修改。

3、如果希望把一个列表或者一个字典中的数据保存到文件中又该怎么做呢？答案是将数据以JSON格式进行保存。JSON是“JavaScript Object Notation”的缩写，它本来是JavaScript语言中创建对象的一种字面量语法，现在已经被广泛的应用于跨平台跨语言的数据交换，原因很简单，因为JSON也是纯文本，任何系统任何编程语言处理纯文本都是没有问题的。目前JSON基本上已经取代了XML作为异构系统间交换数据的事实标准。

4、

```
{
    "name": "骆昊",
    "age": 38,
    "qq": 957658,
    "friends": ["王大锤", "白元芳"],
    "cars": [
        {"brand": "BYD", "max_speed": 180},
        {"brand": "Audi", "max_speed": 280},
        {"brand": "Benz", "max_speed": 320}
    ]
}
```

可能大家已经注意到了，上面的JSON跟Python中的字典其实是一样一样的，事实上JSON的数据类型和Python的数据类型是很容易找到对应关系的，如下面两张表所示。

| JSON                | Python       |
| ------------------- | ------------ |
| object              | dict         |
| array               | list         |
| string              | str          |
| number (int / real) | int / float  |
| true / false        | True / False |
| null                | None         |

| Python                                 | JSON         |
| -------------------------------------- | ------------ |
| dict                                   | object       |
| list, tuple                            | array        |
| str                                    | string       |
| int, float, int- & float-derived Enums | number       |
| True / False                           | true / false |
| None                                   | null         |

5、json模块主要有四个比较重要的函数，分别是：

- `dump` - 将Python对象按照JSON格式序列化到文件中
- `dumps` - 将Python对象处理成JSON格式的字符串
- `load` - 将文件中的JSON数据反序列化成对象
- `loads` - 将字符串的内容反序列化成Python对象

6、“序列化（serialization）在计算机科学的数据处理中，是指将数据结构或对象状态转换为可以存储或传输的形式，这样在需要的时候能够恢复到原先的状态，而且通过序列化的数据重新获取字节时，可以利用这些字节来产生原始对象的副本（拷贝）。与这个过程相反的动作，即从一系列字节中提取数据结构的操作，就是反序列化（deserialization）”。

# Python100_day8:

1、是否采用多任务的第二个考虑是任务的类型，可以把任务分为计算密集型和I/O密集型。计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如对视频进行编码解码或者格式转换等等，这种任务全靠CPU的运算能力，虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低。计算密集型任务由于主要消耗CPU资源，这类任务用Python这样的脚本语言去执行效率通常很低，最能胜任这类任务的是C语言，我们之前提到了Python中有嵌入C/C++代码的机制。

2、除了计算密集型任务，其他的涉及到网络、存储介质I/O的任务都可以视为I/O密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待I/O操作完成（因为I/O的速度远远低于CPU和内存的速度）。对于I/O密集型任务，如果启动多任务，就可以减少I/O等待时间从而让CPU高效率的运转。有一大类的任务都属于I/O密集型任务，这其中包括了我们很快会涉及到的网络应用和Web应用。

3、构成我们今天使用的Internet的基础的是TCP/IP协议族，所谓协议族就是一系列的协议及其构成的通信模型，我们通常也把这套东西称为TCP/IP模型。与国际标准化组织发布的OSI/RM这个七层模型不同，TCP/IP是一个四层模型，也就是说，该模型将我们使用的网络从逻辑上分解为四个层次，自底向上依次是：网络接口层、网络层、传输层和应用层，如下图所示。

[![img](https://github.com/Sirwenhao/Python-100-Days/raw/master/Day01-15/res/TCP-IP-model.png)](https://github.com/Sirwenhao/Python-100-Days/blob/master/Day01-15/res/TCP-IP-model.png)

IP通常被翻译为网际协议，它服务于网络层，主要实现了寻址和路由的功能。接入网络的每一台主机都需要有自己的IP地址，IP地址就是主机在计算机网络上的身份标识。当然由于IPv4地址的匮乏，我们平常在家里、办公室以及其他可以接入网络的公共区域上网时获得的IP地址并不是全球唯一的IP地址，而是一个[局域网（LAN）](https://zh.wikipedia.org/zh-hans/局域网)中的内部IP地址，通过[网络地址转换（NAT）服务](https://zh.wikipedia.org/wiki/网络地址转换)我们也可以实现对网络的访问。计算机网络上有大量的被我们称为“[路由器](https://zh.wikipedia.org/wiki/路由器)”的网络中继设备，它们会存储转发我们发送到网络上的数据分组，让从源头发出的数据最终能够找到传送到目的地通路，这项功能就是所谓的路由。

TCP全称传输控制协议，它是基于IP提供的寻址和路由服务而建立起来的负责实现端到端可靠传输的协议，之所以将TCP称为可靠的传输协议是因为TCP向调用者承诺了三件事情：

1. 数据不传丢不传错（利用握手、校验和重传机制可以实现）。
2. 流量控制（通过滑动窗口匹配数据发送者和接收者之间的传输速度）。
3. 拥塞控制（通过RTT时间以及对滑动窗口的控制缓解网络拥堵）。

4、HTTP是超文本传输协议（Hyper-Text Transfer Proctol）的简称，维基百科上对HTTP的解释是：超文本传输协议是一种用于分布式、协作式和超媒体信息系统的应用层协议，它是[万维网](https://zh.wikipedia.org/wiki/全球資訊網)数据通信的基础，设计HTTP最初的目的是为了提供一种发布和接收[HTML](https://zh.wikipedia.org/wiki/HTML)页面的方法，通过HTTP或者[HTTPS](https://zh.wikipedia.org/wiki/超文本传输安全协议)（超文本传输安全协议）请求的资源由URI（[统一资源标识符](https://zh.wikipedia.org/wiki/統一資源標識符)）来标识。

5、**JSON**（**J**ava**S**cript **O**bject **N**otation）是一种轻量级的数据交换语言，该语言以易于让人阅读的文字（纯文本）为基础，用来传输由属性值或者序列性的值组成的数据对象。尽管JSON是最初只是Javascript中一种创建对象的字面量语法，但它在当下更是一种独立于语言的数据格式，很多编程语言都支持JSON格式数据的生成和解析，Python内置的json模块也提供了这方面的功能。由于JSON是纯文本，它和[XML](https://zh.wikipedia.org/wiki/XML)一样都适用于异构系统之间的数据交换，而相较于XML，JSON显得更加的轻便和优雅。

6、requests是一个基于HTTP协议来使用网络的第三库，其[官方网站](http://cn.python-requests.org/zh_CN/latest/)有这样的一句介绍它的话：“Requests是唯一的一个**非转基因**的Python HTTP库，人类可以安全享用。”简单的说，使用requests库可以非常方便的使用HTTP，避免安全缺陷、冗余代码以及“重复发明轮子”（行业黑话，通常用在软件工程领域表示重新创造一个已有的或是早已被优化過的基本方法）。前面的文章中我们已经使用过这个库，下面我们还是通过requests来实现一个访问网络数据接口并从中获取美女图片下载链接然后下载美女图片到本地的例子程序，程序中使用了[天行数据](https://www.tianapi.com/)提供的网络API。

# Python100_day9:

1、单斜杠：除法求商，不做下取整

==双斜杠：除法求商，下取整（floor）==

```python
>>> 3.2/2



1.6



>>> 3.2//2



1.0



>>> 
```

2、k最近邻分类

k-means聚类算法，通过给定k值，选用每种距离度量方式，在训练集中找出与之相对应距离的样本，然后基于所找出的样本进行预测。对于分类任务，可以将出现次数最多的样本的类别作为预测标签的结果。对于回归任务，可以将k个最近的值的平均值作为预测的结果，也可以根据距离的远近进行加权平均，距离近的样本权重大，距离大的权重小。

3、k最近邻算法中的k值选取尤为关键，

算法优缺点

优点：

1. 简单有效
2. 重新训练代价低
3. 适合类域交叉样本
4. 适合大样本分类

缺点：

1. 惰性学习
2. 输出的可解释性不强
3. 不擅长处理不均衡样本
4. 计算量比较大

# Python100_day10（python语言进阶）:

## 1、机器学习的分类

#### 1.1、监督学习：从给定的训练数据集中学习出一个函数，当给定新的数据时可以根据函数预测结果，训练集通常由人工标注。

#### 1.2、无监督学习：与监督学习对应，但是训练集无认为标注。

#### 1.3、强化学习：通过观察来执行什么样的操作会获取最好的回报，每个动作都会对环境有所影响，学习对象根据观察到的周围环境的变化做出判断。

#### 1.4、半监督学习：介于监督学习和无监督学习之间的一类学习方法。

#### 1.5、深度学习：利用深层神经网络模型抽象数据表示特征的一种方法。

## 2、Scikit-learn

### 2.1、Scikit-learn的基本功能

#分类：异常检测，图像识别。KNN，SVM

#聚类：图像分割，群体划分。K-Means，谱聚类

#回归：价格预测，趋势预测。线性回归，SVR

#降维：可视化。PCA，NMF









3、python生成式（推导式）用法：

\3. 字符串s1 ='ABC'，字符串 s2 = '123'，要求：生成序列 A1 A2 A3 B1 B2 B3 C1 C2 C3

\## 初学者思维：

![img](https://img-blog.csdnimg.cn/20181216190230878.png)

\## python老手思维：

![img](https://img-blog.csdnimg.cn/20181216190310692.png)

运行结果是相同的：

![img](https://img-blog.csdnimg.cn/20181216190344535.png)

4、7.  腾讯2018校招在线编程题：

![img](https://img-blog.csdnimg.cn/20181216192802569.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwNjI4MTA2,size_16,color_FFFFFF,t_70)

第一步：从终端接收一个输入的数：

num1 = int(input('输入3<num<1000的整数：'))
第二步：找出接收的数的范围以内的质数：

def zhishu(f):
    if f == 1:
        return False
    for j in range(2, f):
        res = f % j
        if res == 0:
            return False
    else:
        return True

list1 = [i for i in range(2, num1+1) if zhishu(i)]
第三步： 求出符合题目条件的质数对的数量：

       方法一：

N = 0
for n in list1:
    for k in list1:
        if n + k == num1 and n <= k:   ### 写到这时，马同学思维是解决重复，我想着怎样让不重复
            N += 1
print(N)
      方法二：

N = 0
for item in list1:       ### 老师的思维
    if 10-item in list1 and item <= 10-item:
        N += 1
print(N)

![preview](https://pic4.zhimg.com/v2-770ed4822c9cd941c3783fb6a9f93a7f_r.jpg)

![preview](https://pic2.zhimg.com/v2-ac6f3c6d30d1b4100107fd2fd21057ad_r.jpg)

![preview](https://pic3.zhimg.com/v2-807312e421bedaacc4fd68db19d6c906_r.jpg)

![preview](https://pic4.zhimg.com/v2-8e9fbbc6c446c76afa6a3578ed5e76ef_r.jpg)

![preview](https://pic1.zhimg.com/v2-1fa0c82cb2f1e2b386c82247c4dfeea8_r.jpg)

![preview](https://pic4.zhimg.com/v2-09bd6d065b1aed3b67838b9d29b00f23_r.jpg)

![preview](https://pic4.zhimg.com/v2-314f0915ab4ef18eec5aee5bb2502003_r.jpg)

![preview](https://pic1.zhimg.com/v2-e35e58027d941d5a8766859b56563c64_r.jpg)

![preview](https://pic2.zhimg.com/v2-a3fdcafa4182725e323ea8458e533ab9_r.jpg)

![preview](https://pic4.zhimg.com/v2-b3d6a9ba43fb48422bed499b6acd304f_r.jpg)

![preview](https://pic2.zhimg.com/v2-4dd3828ab2bbee7c8a8602ab69a07a51_r.jpg)

enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

### 语法

以下是 enumerate() 方法的语法:

```
enumerate(sequence, [start=0])
```

### 参数

- sequence -- 一个序列、迭代器或其他支持迭代对象。
- start -- 下标起始位置。

### 返回值

返回 enumerate(枚举) 对象。

------

## 实例

以下展示了使用 enumerate() 方法的实例：

![image-20210411204424417](C:\Users\WH\AppData\Roaming\Typora\typora-user-images\image-20210411204424417.png)

![image-20210411204437039](C:\Users\WH\AppData\Roaming\Typora\typora-user-images\image-20210411204437039.png)

# Python100_day11:

### 1、code sheep讲的github的高效检索

> 搜索名字里面含有关键词的就直接用：==in:name python== 就可以检索出名称中包含python的仓库，

> 要搜索star比较高的，可以用==stars:>3000==，即表示stars数大于3000才能被检索出来

> 然后检索readme的话，当然就用==in:readme==进行检索

> 可以使用描述和语言限定搜索：==In:description 爬虫 language：Python==

> 搜索最近更新的就用：==pushed：>2021-01-01==

2、`collections`模块

常用的工具类：

- `namedtuple`：命令元组，它是一个类工厂，接受类型的名称和属性列表来创建一个类。
- `deque`：双端队列，是列表的替代实现。Python中的列表底层是基于数组来实现的，而deque底层是双向链表，因此当你需要在头尾添加和删除元素是，deque会表现出更好的性能，渐近时间复杂度为$O(1)$。
- `Counter`：`dict`的子类，键是元素，值是元素的计数，它的`most_common()`方法可以帮助我们获取出现频率最高的元素。`Counter`和`dict`的继承关系我认为是值得商榷的，按照CARP原则，`Counter`跟`dict`的关系应该设计为关联关系更为合理。
- `OrderedDict`：`dict`的子类，它记录了键值对插入的顺序，看起来既有字典的行为，也有链表的行为。
- `defaultdict`：类似于字典类型，但是可以通过默认的工厂函数来获得键对应的默认值，相比字典中的`setdefault()`方法，这种做法更加高效。

# Python100_day12:

1、数据结构和算法：

- 算法：解决问题的方法和步骤
- 评价算法的好坏：渐近时间复杂度和渐近空间复杂度。
- 渐近时间复杂度的大O标记：
  - [![img](https://camo.githubusercontent.com/44ba5f6ba25b0fae0eaec4f1aeccac8ce1124791ef98ded00466e336dff8cf4d/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286329)](https://camo.githubusercontent.com/44ba5f6ba25b0fae0eaec4f1aeccac8ce1124791ef98ded00466e336dff8cf4d/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286329) - 常量时间复杂度 - 布隆过滤器 / 哈希存储
  - [![img](https://camo.githubusercontent.com/c84069cd18fc61eac8f4f1b899ba6ec878a4c21af64c04d8853fbb150d01a788/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286c6f675f326e29)](https://camo.githubusercontent.com/c84069cd18fc61eac8f4f1b899ba6ec878a4c21af64c04d8853fbb150d01a788/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286c6f675f326e29) - 对数时间复杂度 - 折半查找（二分查找）
  - [![img](https://camo.githubusercontent.com/9ad5f8dcd5bdae8b66205c7472fed2e90d2f569698b6ae5034993c434a4bd11a/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e29)](https://camo.githubusercontent.com/9ad5f8dcd5bdae8b66205c7472fed2e90d2f569698b6ae5034993c434a4bd11a/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e29) - 线性时间复杂度 - 顺序查找 / 计数排序
  - [![img](https://camo.githubusercontent.com/bf71fc4b5a6a518fad4d54001f7c7bee82dc1d97d7abbcc4c1d2277b93d0f67f/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e2a6c6f675f326e29)](https://camo.githubusercontent.com/bf71fc4b5a6a518fad4d54001f7c7bee82dc1d97d7abbcc4c1d2277b93d0f67f/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e2a6c6f675f326e29) - 对数线性时间复杂度 - 高级排序算法（归并排序、快速排序）
  - [![img](https://camo.githubusercontent.com/f3038618c31ec54aa23dcf811d5ed03dcd29eccb0fc4770bd396ae8ed52be161/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e5e3229)](https://camo.githubusercontent.com/f3038618c31ec54aa23dcf811d5ed03dcd29eccb0fc4770bd396ae8ed52be161/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e5e3229) - 平方时间复杂度 - 简单排序算法（选择排序、插入排序、冒泡排序）
  - [![img](https://camo.githubusercontent.com/baf1669c4a134e97391d6fc955a13f4ee6939fda151dc759d06d97e0f65b0415/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e5e3329)](https://camo.githubusercontent.com/baf1669c4a134e97391d6fc955a13f4ee6939fda151dc759d06d97e0f65b0415/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e5e3329) - 立方时间复杂度 - Floyd算法 / 矩阵乘法运算
  - [![img](https://camo.githubusercontent.com/22b2ff251b344e42a2cdfad014b1b5788dd9b1533e85d99033a6c9616bc7c27b/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f28325e6e29)](https://camo.githubusercontent.com/22b2ff251b344e42a2cdfad014b1b5788dd9b1533e85d99033a6c9616bc7c27b/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f28325e6e29) - 几何级数时间复杂度 - 汉诺塔
  - [![img](https://camo.githubusercontent.com/213fa8ee7fceaccee605072b5db903789bdbc4bd46b0b5a5ede19a50e2c2e270/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e2129)](https://camo.githubusercontent.com/213fa8ee7fceaccee605072b5db903789bdbc4bd46b0b5a5ede19a50e2c2e270/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f4f286e2129) - 阶乘时间复杂度 - 旅行经销商问题 - NPC

2、排序详解：

- 交换排序，选择排序，插入排序，都属于基本排序
- 交换排序：冒泡排序，快速排序
- 插入排序：希尔排序
- 堆排序：完全二叉树，平方二叉树

3、简单选择排序：

- 属于选择排序

- 两两比较大小，找出极值（极大值或者极小值）被放置在固定的位置，这个固定的位置一般参考值某一端

- 对比一般分为升序和降序两种
  + 降序
    + n个数从左至右，索引从0开始至n-1，两两依次比较，记录大值的索引，此轮将所有的书对比完毕将极大值索引和0索引的数值交换
    + 第二轮从1开始，找最大值，并将最大值和索引1位置交换
    + 其他值以此类推  

- 简单选择排序

  - 属于选择排序
  - 两两比较大小，找出极值（极大值或极小值）被放置在固定的位置，这个固定位置一般指的是某一端。
  - 结果分为升序和降序排列

- 降序

  - n个数从左至右，索引从0开始到n-1，两两依次比较，记录大值索引，此轮所有数比较完毕，将极大值和索引0数交换。
  - 如果极大值就是索引0，不交换。
  - 第二轮，从1开始比较，找到最大值，将它和索引1位置交换。
  - 如果它就在索引1位置则不交换。
  - 依次类推，每次左边就会固定下一个大数

  ![img](http://yuntu88.oss-cn-beijing.aliyuncs.com/fromlocal/gnuzsx@126.com/20200421/mFSHiDGwpj.png)

- 简单选择排序需要数据一轮轮比较，并在每一轮当中发现极值。

- 没有办法知道当前轮是否已经达到排序要求，但是可以知道极值是否在目标索引位置上。

- 遍历次数1,...n-1之和n(n-1)/2

- 时间复杂度O($$n^2$$)

- 减少了交换次数，提高了效率，性能略好于冒泡法

  ![img](https://www.runoob.com/wp-content/uploads/2019/03/selectionSort.gif)

# Python100_day13:

1、lambda是一个表达式，仅能在lambda的表达式中封装有限的逻辑进去，其主体是一个表达式，起到函数速写的作用。

2、python冒泡排序：

- 重复走访要排序的数列，每次比较两个元素，如果大小顺序错误，就将其互相交换。
- 算法名称的由来是指，最小的元素会经过多次的交换，最终逐渐上浮到数列的顶端。
- 相比于简单选择排序，其实冒泡排序相当于每次找到最大值并将其位置固定到数列的最后。
- 示意图如下：

![img](https://www.runoob.com/wp-content/uploads/2019/03/bubbleSort.gif)

3、lambda函数相关：

+ lambda的一般表现形式是关键字lambda后面跟上一个或者多个参数，之后是一个冒号，最后是一个表达式
+ 一般形式是：lambda *argument1，argument2，...，argumentN ：expression using arguments*
+ lambda是一个表达式，而不是语句
+ lambda的主体是一个单独的表达式，而不是一个代码块

4、python双向冒泡排序：

从名字就可以看出来，是双向的冒泡排序。
冒泡排序，每次都是从左往右，交换相邻的元素，从而达到循环一边可以把最大的元素放在右边。
而双向冒泡排序，在完成一次从左往右的冒泡排序后，再从右往左进行冒泡，从而把小的元素放在左边

![img](https://img-blog.csdnimg.cn/20191203173746758.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDA2MzAzMQ==,size_16,color_FFFFFF,t_70)

# Python100_day14:

1、enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

enumerate(sequence, [start=0])

- sequence -- 一个序列、迭代器或其他支持迭代对象。
- start -- 下标起始位置。

返回 enumerate(枚举) 对象。

以下展示了使用 enumerate() 方法的实例：

\>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter'] 

list(enumerate(seasons)) 

[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')] 

list(enumerate(seasons, start=1))       # 下标从 1 开始

 [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

2、python常用算法

- 穷举法：暴力破解法，对所有的可能进行尝试，直至找到结果。
- 贪婪法：不求最优解，只求当前满意解。
- 分治法：把一个复杂的大问题分成若干个相同或者相似的小问题，再把小问题分解为更小的问题，直至可以直接求解的程度。
- 回溯法：按照选优条件向前搜索，当当前的选择不能满足要求时，则退回到上一步。
- 动态规划：将待求解的问题分为若干个小问题，先求解并保存这些小问题，避免产生大量重复的运算

3、python运算符

#### Python算术运算符

以下假设变量： **a=10，b=20**：

| 运算符 | 描述                                            | 实例                                               |
| :----- | :---------------------------------------------- | :------------------------------------------------- |
| +      | 加 - 两个对象相加                               | a + b 输出结果 30                                  |
| -      | 减 - 得到负数或是一个数减去另一个数             | a - b 输出结果 -10                                 |
| *      | 乘 - 两个数相乘或是返回一个被重复若干次的字符串 | a * b 输出结果 200                                 |
| /      | 除 - x除以y                                     | b / a 输出结果 2                                   |
| %      | 取模 - 返回除法的余数                           | b % a 输出结果 0                                   |
| **     | 幂 - 返回x的y次幂                               | a**b 为10的20次方， 输出结果 100000000000000000000 |
| //     | ==取整除 - 返回商的整数部分（**向下取整**）==   | `>>> 9//2 4 >>> -9//2 -5`                          |

#### Python比较运算符

以下假设变量a为10，变量b为20：

| 运算符 | 描述                                                         | 实例                                     |
| :----- | :----------------------------------------------------------- | :--------------------------------------- |
| ==     | 等于 - 比较对象是否相等                                      | (a == b) 返回 False。                    |
| !=     | 不等于 - 比较两个对象是否不相等                              | (a != b) 返回 true.                      |
| <>     | 不等于 - 比较两个对象是否不相等。**python3 已废弃。**        | (a <> b) 返回 true。这个运算符类似 != 。 |
| >      | 大于 - 返回x是否大于y                                        | (a > b) 返回 False。                     |
| <      | 小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。 | (a < b) 返回 true。                      |
| >=     | 大于等于 - 返回x是否大于等于y。                              | (a >= b) 返回 False。                    |
| <=     | 小于等于 - 返回x是否小于等于y。                              | (a <= b) 返回 true。                     |

#### Python赋值运算符

以下假设变量a为10，变量b为20：

| 运算符 | 描述             | 实例                                  |
| :----- | :--------------- | :------------------------------------ |
| =      | 简单的赋值运算符 | c = a + b 将 a + b 的运算结果赋值为 c |
| +=     | 加法赋值运算符   | c += a 等效于 c = c + a               |
| -=     | 减法赋值运算符   | c -= a 等效于 c = c - a               |
| *=     | 乘法赋值运算符   | c *= a 等效于 c = c * a               |
| /=     | 除法赋值运算符   | c /= a 等效于 c = c / a               |
| %=     | 取模赋值运算符   | c %= a 等效于 c = c % a               |
| **=    | 幂赋值运算符     | c **= a 等效于 c = c ** a             |
| //=    | 取整除赋值运算符 | c //= a 等效于 c = c // a             |

#### Python运算符优先级

以下表格列出了从最高到最低优先级的所有运算符：

| 运算符                   | 描述                                                   |
| :----------------------- | :----------------------------------------------------- |
| **                       | 指数 (最高优先级)                                      |
| ~ + -                    | 按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@) |
| * / % //                 | 乘，除，取模和取整除                                   |
| + -                      | 加法减法                                               |
| >> <<                    | 右移，左移运算符                                       |
| &                        | 位 'AND'                                               |
| ^ \|                     | 位运算符                                               |
| <= < > >=                | 比较运算符                                             |
| <> == !=                 | 等于运算符                                             |
| = %= /= //= -= += *= **= | 赋值运算符                                             |
| is is not                | 身份运算符                                             |
| in not in                | 成员运算符                                             |
| not and or               | 逻辑运算符                                             |

# Python100_day15:

1、python中的类

对象 = 属性 + 方法

属性：静态的特征

方法：动态的动作

2、 例

```
# 小甲鱼python教程：类

class Turtle:  #python中的类名约定以大写字母开头
    """关于类的一个简单例子"""
    # 属性
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    # 方法
    def climb(self):
        print("我正在很努力的往前爬.....")

    def run(self):
        print("我正在飞快地向前爬......")

    def bite(self):
        print("咬死你")
```

3、面向对象编程的特征：1、封装，2、继承（子类自动共享父类之间数据和方法的机制），3、多态（不同对象对同一方法响应不同的举动）

```
#  多态

class A:
    def func(self):
        print("我是小A......")

class B:
    def fun(self):
        print("我是小B.......")

>>>a = A()
>>>b = B()
>>>a.fun()
我是小A...
>>>b.fun()
我是小B...
```

上述例子中都调用一个叫fun的函数，但是执行的动作却不相同，这就是多态。

# Python100_day16:

1、函数的使用方式

- 将函数视为“一等公民”
  - 函数可以赋值给变量
  - 函数可以作为函数的参数
  - 函数可以作为函数的返回值

- 高阶函数的用法（`filter`、`map`以及它们的替代品）

  ```
  items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
  items2 = [x ** 2 for x in range(1, 10) if x % 2]
  ```

- 位置参数、可变参数、关键字参数、命名关键字参数

- 参数的元信息（代码可读性问题）

- 匿名函数和内联函数的用法（`lambda`函数）

- 闭包和作用域问题

  - Python搜索变量的LEGB顺序（Local >>> Embedded >>> Global >>> Built-in）

  - `global`和`nonlocal`关键字的作用

    `global`：声明或定义全局变量（要么直接使用现有的全局作用域的变量，要么定义一个变量放到全局作用域）。

    `nonlocal`：声明使用嵌套作用域的变量（嵌套作用域必须存在该变量，否则报错）。

- 装饰器函数（使用装饰器和取消装饰器）

2、Python中的函数跟这个结构是一致的，每个函数都有自己的名字、自变量和因变量。我们通常把Python中函数的自变量称为函数的参数，而因变量称为函数的返回值。在Python中可以使用==`def`关键字==来定义函数，和变量一样每个函数也应该有一个漂亮的名字，命名规则跟变量的命名规则是一致的（赶紧想一想我们之前讲过的变量的命名规则）。在函数名后面的==圆括号中可以放置传递给函数的参数，就是我们刚才说到的函数的自变量==，而函数执行完成后我们会通过==`return`关键字来返回函数的执行结果==，就是我们刚才说的函数的因变量。一个函数要执行的代码块（要做的事情）也是通过缩进的方式来表示的，跟之前分支和循环结构的代码块是一样的。大家不要忘了`def`那一行的最后面还有一个`:`，之前提醒过大家，那是在英文输入法状态下输入的冒号。

3、参数的默认值

如果函数中没有`return`语句，那么函数默认返回代表空值的`None`。另外，在定义函数时，函数也可以没有自变量，但是函数名后面的圆括号是必须有的。

# Python100_day17:

1、今天其实很水，只是了解了一下python怎么按列读取数据就已经十点了。其实就是给txt文件中的两个列分别起了个名字，然后按照名字读取了。。。。。

祭出今天写的使用python实现SROCC、PLCC、KROCC、RMSE的程序，完全原创：#  使用python实现SROCC，PLCC，KROCC的计算

import pandas as pd
import numpy as np

#输入原始数据

从txt文件中读入数据

test1 = pd.read_table("data.txt")
a = test1["ScoreA"]
#print(a)
test2 = pd.read_table("data.txt")
b = test2["ScoreB"]
#print(b)


###### a = pd.Series([43.5014, 60.2509, 67.3574, 61.2848, 42.9953, 46.6351, 45.4776,
######                 43.0422, 38.5426, 29.0167, 69.2392, 65.7653, 55.0551, 54.7645])
###### b = pd.Series([0.7353, 0.7269, 0.7287, 0.7487, 0.7668, 0.8523, 0.8414, 0.8279,
######                0.7145, 0.8279, 0.7240, 0.7223, 0.7211, 0.7198])

计算SROCC

SROCC = a.corr(b, method = 'spearman')
print('SROCC = %.6f' %SROCC)

计算KROCC

KROCC = a.corr(b, method = 'kendall')
print('KROCC = %.6f' %KROCC)

计算PLCC

PLCC = a.corr(b, method = 'pearson')
print('PLCC = %.6f' %PLCC)

计算均方根误差RMSE

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

rmse_val = rmse(np.array(a), np.array(b))
print('RMSE = %.6f' %rmse_val)

# Python100_day18:

1、python路径读取以及拼接等问题：

import os

Path1 = 'home'
Path2 = 'develop'
Path3 = 'code'

Path10 = Path1 + Path2 + Path3
Path20 = os.path.join(Path1,Path2,Path3)
print ('Path10 = ',Path10)
print ('Path20 = ',Path20)

输出

 

Path10 = homedevelopcode
Path20 = home\develop\code
    >>>print("1:",os.path.join('aaaa','/bbbb','ccccc.txt'))

2、os.path.join()函数：连接两个或更多的路径名组件

       1.如果各组件名首字母不包含’/’，则函数会自动加上

　　　　2.第一个以”/”开头的参数开始拼接，之前的参数全部丢弃,当有多个时，从最后一个开始

　　　　3.如果最后一个组件为空，则生成的路径以一个’/’分隔符结尾

print("2:",os.path.join('/aaaa','/bbbb','/ccccc.txt')) #不良写法习惯

     >>>2: /ccccc.txt

print("22:",os.path.join('/aaaa/','bbbb/','ccccc.txt')) #通常可以这样写22: aaaa/bbb/ccccc.txt


3、path = 'I:\SCVD_frames\yuv_frames'
fileList = os.listdir(path)
for i in fileList:
    #print(i)
#print(fileList)
    Path1 = 'I:\SCVD_frames\yuv_frames'
    file_path = os.path.join(Path1, i)  #os.path.join()的用法
    #print(file_path)
    img_list = os.listdir(file_path)    #获取路径之后打开路径的方法os.listdir()
    img_list.sort(key = lambda x:int(x.split('.')[0]))   #此步骤略牛逼，可以把后缀去掉直接按照前面的数字顺序进行排序
    print(img_list)

# Python100_day19:

1、python中os.listdir()的用法：os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。它不包括 **.** 和 **..** 即使它在文件夹中。

2、**listdir()**方法语法格式如下：

```
os.listdir(path)
```

### 参数

- **path** -- 需要列出的目录路径

### 返回值

返回指定路径下的文件和文件夹列表。

3、若要编写的类是另一个线程类的特殊版本，可以使用继承。一个类继承另一个类时，它将自动获得另一个类的所有属性和方法，原有的类称为符类，新的类成为子类。创建子类实例时，python首先需要完成的任务是给父类的所有属性赋值，因此要通过子类方法`__init__`方法

子类方法：`__init__`方法负责对象的初始化，系统执行该方法前，其实该对象已经存在了，要不然初始化什么东西呢？

# Python100_day20:

1、argparse是一个Python模块：命令行选项、参数和子命令解析器。[`argparse`](https://docs.python.org/zh-cn/3/library/argparse.html#module-argparse) 模块可以让人轻松编写用户友好的命令行接口。程序定义它需要的参数，然后 [`argparse`](https://docs.python.org/zh-cn/3/library/argparse.html#module-argparse) 将弄清如何从 [`sys.argv`](https://docs.python.org/zh-cn/3/library/sys.html#sys.argv) 解析出那些参数。 [`argparse`](https://docs.python.org/zh-cn/3/library/argparse.html#module-argparse) 模块还会自动生成帮助和使用手册，并在用户给程序传入无效参数时报出错误信息。

使用流程：

1.创建解析器：parser = argparse.ArgumentParser(description='Process some integers.')

使用 [`argparse`](https://docs.python.org/zh-cn/3/library/argparse.html#module-argparse) 的第一步是创建一个 [`ArgumentParser`](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser) 对象。[`ArgumentParser`](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser) 对象包含将命令行解析成 Python 数据类型所需的全部信息。

2.添加参数：parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')

给一个 [`ArgumentParser`](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser) 添加程序参数信息是通过调用 [`add_argument()`](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser.add_argument) 方法完成的。

3.解析参数：>>> parser.parse_args(['--sum', '7', '-1', '42'])
Namespace(accumulate=<built-in function sum>, integers=[7, -1, 42])

[`ArgumentParser`](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser) 通过 [`parse_args()`](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser.parse_args) 方法解析参数。

add_argument() 方法：

ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])

name or flags - 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
action - 当参数在命令行中出现时使用的动作基本类型。
nargs - 命令行参数应当消耗的数目。
const - 被一些 action 和 nargs 选择所需求的常数。
default - 当参数未在命令行中出现时使用的值。
type - 命令行参数应当被转换成的类型。
choices - 可用的参数的容器。
required - 此命令行选项是否可省略 （仅选项可用）。
help - 一个此选项作用的简单描述。
metavar - 在使用方法消息中使用的参数值示例。
dest - 被添加到 parse_args() 所返回对象上的属性名。

4、Python中的函数跟这个结构是一致的，每个函数都有自己的名字、自变量和因变量。我们通常把Python中函数的自变量称为函数的参数，而因变量称为函数的返回值。在函数名后面的圆括号中可以放置传递给函数的参数，就是我们刚才说到的函数的自变量，而函数执行完成后我们会通过`return`关键字来返回函数的执行结果，就是我们刚才说的函数的因变量。如果函数中没有`return`语句，那么函数默认返回代表空值的`None`。另外，在定义函数时，函数也可以没有自变量，但是函数名后面的圆括号是必须有的。

5、因为Python语言中的函数可以通过星号表达式语法来支持可变参数。所谓可变参数指的是在调用函数时，可以向函数传入0个或任意多个参数。

6、Python中每个文件就代表了一个模块（module），我们在不同的模块中可以有同名的函数，在使用函数的时候我们通过`import`关键字导入指定的模块再使用**完全限定名**的调用方式就可以区分到底要使用的是哪个模块中的`foo`函数。如果我们如果从两个不同的模块中导入了同名的函数，后导入的函数会覆盖掉先前的导入。

# Python100_day21:

1、python中首字母大写，全部大写，全部小写分别用：.upper()，.lower()，.title()方法进行表示。如：

```
name = input('请输入名字: ')
print(name.upper())
print(name.lower())
print(name.title())
```

2、python中的对象和类型

python中一共支持五种对象类型：

- 字符串类型（string），简记为str。使用""或者''括起来的一系列字符

- 整数类型（integer），简记为int。

- 浮点数（float）

- 布尔类型（boolean），简记为bool

- 复数（complex）

  

  3、python为什么要区分不同的数据类型

  - 不同数据类型的运算规则不同

  - 不同类型对象在计算机内表示的方式不同

    

  4、为何区分整数与浮点数？

  - 浮点数的表示能力更强
  - 浮点数有精度损失
  - CPU有专门的浮点数运算部件

  5、python计算自动类型转换：

  - 若参与运算的两个对象的数据类型相同，则结果类型不变
  - 如参与运算的两个对象的类型不同，则按照以下的规则进行自动类型转换
    - bool -- int -- float -- complex

  

  6、python中的模块引入：

  - 指令：import module_name
  - 查看模块的内容dir(math)
  - 查看帮助help(math.sin)

7、python程序中：

$$(2**2)**3$$得到的结果为64

$$2**2**3$$得到的结果为256

8、python关系运算符，逻辑运算符等等

9、python中的enumerate()函数：enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。`enumerate()`是用来遍历一个可迭代容器中的元素，同时通过一个计数器变量记录当前元素所对应的索引值。

具体用法：enumerate(sequence, [start=0])

- sequence -- 一个序列、迭代器或其他支持迭代对象。
- start -- 下标起始位置。

10、下面以常见的序列，列表、元组、字符串为例简单说明enumerate()的使用方法。

- 列表

> s = [2,5,8,3,6,9] 
>
> for index, value in enumerate(s):    
>
> ​	  print index, value
>
> 结果：0 2     1 5     2 8     3 3     4 6     5 9

- 元组

> s = (2,5,8,3,6,9)
> for index, value in enumerate(s):
>     print index, value
>
> 0 2     1 5     2 8     3 3     4 6     5 9

- 字符串

> s = 'test' 
>
> for index, value in enumerate(s):    
>
> ​	 print index, value
>
> 0 t     1 e     2 s     3 t