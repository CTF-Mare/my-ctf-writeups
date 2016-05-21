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

![easy_crackme1](https://raw.github.com/CTF-Mare/my-ctf-writeups/2016/2016-05-21-PhrackCTF/screenshots/easycrackme1.png)

![easy_crackme2](https://raw.github.com/CTF-Mare/my-ctf-writeups/2016/2016-05-21-PhrackCTF/screenshots/easycrackme2.png)

逻辑很简单，照着抄一下扔进 python 里就好了。


