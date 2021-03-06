### 在GitHub中添加 ssh Key
- 问题描述：
我从GitHub上找到一个感兴趣的Python项目，想clone到本地研究一下，但是在PyCharm上
用ssh克隆的时候用Git从项目checkout的时候提示无法建立连接，无法正常clone下来，项目
连接是`git@github.com:Lunarstaff/12306.git`
![](../../resources/image/pycharm-ssh-github-无法建立连接.png)

>目前猜测是我邮件账号出问题了，收不到 GitHub的验证邮件。

- 结论：最终也不知道是什么原因
     - 首先，我第二天中午用手机再次尝试github的邮箱验证，手机上163邮箱可以收到GitHub发的验证邮件了，所以GitHub账号验证通过了。
     - 晚上，从本地的git仓库往GitHub上推的时候仍然提示无法建立连接
     - 我在Pycharm上重新登录了我的GitHub账号后再次Push，成功了。
     所以具体什么原因也不清楚，后续再次操作的时候注意吧。有必得了再整理过来。


- 问题描述：
从GitHub通过ssh克隆到本地仓，但是如果本地修改commit后想要push到GitHub上，在Pycharm上总是提示：
```
23:09	Push failed
		Connection reset by 52.74.223.119 port 22
		Could not read from remote repository.
		Please make sure you have the correct access rights
		and the repository exists.
```
百度后找到[解决方法](https://www.cnblogs.com/Diamond-sjh/p/11352156.html "博客园 Diamond蚊子")
> 在防火墙高级设置中，新建入站规则，允许本地特定端口"22"通过TCP连接，设置完成后再次Push就成功了：
```
23:13	Push successful: Pushed 2 commits to origin/master
```

然而，上面的方法只push成功了一次，要再次push的时候又报上面那个错了。难道ssh克隆的每次push都要重新给GitHub添加sshKey？

我还是用https重新克隆下来吧！~~~

---

微信公众号上找到一个图，大致是GitHub和Git的概要图:  
![](../../resources/image/git-概要图.jpg)