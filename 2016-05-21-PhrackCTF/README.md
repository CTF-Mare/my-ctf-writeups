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






