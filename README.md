# Yu-Gi-Oh! Master Duel 中文卡查 MDT

Yu-Gi-Oh! Master Duel Translation Script

* 自动切换，自动查卡，全面覆盖Deck、Duel、Solo、Replay模式。
* 高正确性，除非卡片数据本身有错。
* 超快识别速度，低于0.000001s。
* 极低占用，CPU占用忽略不计。
* 直接调用win32api，不使用第三方dll。
* 开源，你可以直接执行源代码并定制你自己的版本。
* i18n，支持简体中文和繁体中文。
* 高兼容性，点开即用，支持各种游戏内语言，最低可支持win7。
* 一键导出Master Duel游戏卡组，兼容ygopro格式。
* 可一键直达网页卡查和官方数据库。
* 支持全屏置顶、无边框、半透明。

![MDT](https://github.com/SkywalkerJi/mdt/raw/master/IMG/v0.2.5.png "MDT v0.2.5")

## Download

你可以在[Releases](https://github.com/SkywalkerJi/mdt/releases/latest)下载预打包的MDT版本。

如果是Windows7系统请下载后缀`_win7`的版本，如果想使用CLI请下载`_CLI`的版本。

中国大陆用户可在[此处下载](https://wwi.lanzouj.com/b0176jyjc) 密码:5j6f

你还可以在[Uncensor Patch](https://github.com/SkywalkerJi/mdt/releases/tag/v1.0.1-UncensorPatch)下载反和谐卡图补丁。


## Usage

目前MDT拥有两个版本，有GUI界面的版本（推荐）和纯命令行CLI界面。

**从预打包的GUI版本（v0.2.x）启动（适合大部分用户）**

1. 打开游戏。
2. 右键使用**管理员权限**运行`mdt.exe`。
3. 在组卡界面点击一张卡。
4. 右键可打开更多功能。繁体中文用户右键切换语言。

**使用预打包的CLI版本**

<details>
   <summary>点击CLI使用说明</summary>

命令行界面这是MDT v0.1.x版本的默认UI，在v0.2.3开始进行了拆分。

并不是每次release都会更新CLI，所以你可能要往前找一下后缀`_cli`的打包。

1. 打开游戏。
2. 右键使用**管理员权限**运行`mdt.exe`。
3. 根据提示使用快捷键。

| 快捷键 | 功能     |
| ------ | -------- |
| ctrl+s | 开启检测 |
| ctrl+p | 暂停检测 |
| ctrl+q | 退出程序 |

4. 可在`config.ini`文件中进行功能配置。以下是一份样例，可以直接复制粘贴。
   如果要进行CLI窗口置顶设置，尤其要注意窗口名（`lp_window_name`）选项。使用默认配置文件时可以把软件放在C:\mdt 目录下即可进行窗口置顶。注意ini时注意注释行开头必须是`; `
```
[cli] 
; CLI基本设置
pause_hotkey = ctrl+p
; 暂停快捷键
exit_hotkey = ctrl+q
; 退出快捷键
switch_hotkey = ctrl+s
; 切换模式快捷键
window_on_top = 0
; 是否开启CLI窗口置顶 1置顶 0取消
lp_window_name = C:\mdt\mdt.exe
; 开启窗口置顶时需要提供窗口名，一般是软件安装路径
window_pos_x = 400
window_pos_y = 400
window_pos_cx = 400
window_pos_cy = 400
; 这四个参数是控制CLI窗口置顶时默认的窗口大小。
show_all_info = 1
; 如果你想要只显示中文卡名+卡密+效果，可以把这一项改成0。

[gui]
font_size = 12
; 字体大小 整数
window_alpha = 0.96
; 透明度 
keep_on_top = 1
; gui窗口置顶 1置顶 0取消
ui_lock = 0
; gui窗口ui锁定 1锁定 0取消
web_search = 1
; 1开启网页卡查 0关闭
x_loc = 960
y_loc = 540
; gui窗口位置
x_len = 400
y_len = 600
; gui窗口大小
locale = zh-CN
; zh-CN简体，zh-TW繁体
borderless = 1
; 无边框 1开启 0取消
show_names = 1
; 英日文卡名卡密 1开启 0取消
show_types = 1
; 卡片类型 1开启 0取消
```
</details>

**从源代码执行**

<details>
   <summary>点击展开</summary>

```
pip install -r requirements.txt
python mdt_gui.py
python mdt_cli.py
```

</details>

**视频演示**

*v0.2.5版本*

[bilibili](https://www.bilibili.com/video/av636233915)   [Youtube](https://www.youtube.com/watch?v=ITXjWSsmEmc)

*卡图反和谐补丁*

[bilibili](https://www.bilibili.com/video/av765979539)   [Youtube](https://www.youtube.com/watch?v=ickw082Snwo)

<details>
   <summary>旧版演示</summary>

*v0.2.3版本*

[bilibili](https://www.bilibili.com/video/av978731073)   [Youtube](https://www.youtube.com/watch?v=YUNeiOCAd6M)

*v0.2.1版本*

[bilibili](https://www.bilibili.com/video/av636086411)   [Youtube](https://www.youtube.com/watch?v=TfHoNeEVqf4)

*v0.2.0版本*

[bilibili](https://www.bilibili.com/video/av466062188)   [Youtube](https://www.youtube.com/watch?v=Vav013Cx3BQ)

*v0.1.4版本*

[bilibili](https://www.bilibili.com/video/av850928534)   [Youtube](https://www.youtube.com/watch?v=mx0KaT3cRsQ)

*v0.1.2版本*

[bilibili](https://www.bilibili.com/video/av593463793)

</details>

## Q＆A

<details>
   <summary>Q1：杀毒软件报告MDT有病毒？如何解决？</summary>
  
确认你是从本页所列途径下载的版本那就是误报。

源代码是公开的，不可能加入病毒，如果实在不放心可以直接执行源代码。

目前MDT以功能开发为主，不打算主动解决此问题，请直接添加信任。
</details>

<details>
   <summary>Q2：管理员权限开启后依然无法检测？点击后exe消失？提示没有权限？被杀毒软件拦截隔离？</summary>

先确认你是从本页所列途径下载的版本。

然后在你使用的杀毒软件以及Windows自带的安全系统里添加信任。
</details>

<details>
   <summary>Q3：是否可以排位？是否会封号？</summary>

不会。我第一赛季是白金1结算。

另外这个游戏没有反作弊，从经济角度考虑一个99%依赖服务端的游戏根本必要进行检测，参考游戏王duel link。

</details>

<details>
   <summary>Q4：CLI版本是否还会进行后续开发？</summary>

CLI版本在MDT v0.2.3版本进行拆分，拆分后对CLI版本只做基础可用性维护，原则上不再添加新功能。但欢迎PR。

</details>

<details>
   <summary>Q5：使用MDT时需要注意什么？</summary>

请遵循[GPLv3协议](https://github.com/SkywalkerJi/mdt/blob/master/LICENSE)。

如果你参与我们的社区，请遵循[贡献者契约行为准则](https://github.com/SkywalkerJi/mdt/blob/master/CODE_OF_CONDUCT.md)。

</details>

## Contributing

有其他指针或功能欢迎提交[issue](https://github.com/SkywalkerJi/mdt/issues/new)或Pull Request。

## Contact us

如果你有错误报告、建议、想法，请随时通过以下方式联系开发者：

* [issue](https://github.com/SkywalkerJi/mdt/issues/new)
* [NGA](https://bbs.nga.cn/read.php?tid=30415633)
* [巴哈姆特](https://forum.gamer.com.tw/C.php?bsn=725&snA=54550&tnum=1)
* [Q群 710144213](https://jq.qq.com/?_wv=1027&k=uyFt3qi0)
* [Telegram](https://t.me/ygomasterduel)
* [Twitter](https://twitter.com/Skywalker_Ji)
* 或其他途径。

## Changelog

*v0.2.5*
* 支持masterduel卡组一键导出！由 @zealyahweh 贡献。可同时生成ygopro卡组`.ydk`格式和文本格式。
* 拆分英日文卡名和卡类型显示选项，现在可以分别勾选“原始卡名”和“卡片类型”。
* 主题配色改为暗色。
* 添加无边框模式，可更好融入游戏。
* 窗口整体可拖拽。
* 右键添加关闭选项。
* 鼠标悬停时添加右键提示。

<details>
   <summary>展开过往版本</summary>

*v0.2.4*
* 添加对繁体中文的i18n支持。右键可以切换语言。UI文本由 @ranke96 贡献，卡片翻译来自 @stillfiy0529 。
* 针对重启游戏后无法检测的问题，可以右键重启检测。
* 未查询到卡片的状态下不再唤起网页卡查。

*v0.2.3*
* 拆分GUI版本和CLI版本。
* 添加详情显示选项。关闭后只显示中文卡名+效果描述。
* 添加网页卡查跳转选项，开启后点击中文卡名会跳转百鸽（ygocdb.com)，英文和日文卡名会跳转K社官方数据库,点击卡密会跳转ourocg。
* 打开时Windows将主动询问管理员权限。
* 移动设置选项，右键可以打开设置窗口。
* 可横向扩展效果描述框。
* 可记录窗口位置、尺寸。
* 将"效果"改为"描述"，避免部分通常怪兽造成误解。

*v0.2.2*

* 修复OCG专有卡和dbsp卡包的英文卡名缺失问题。
* 添加右键菜单。
* UI锁定功能改为独立选项。
* 右键可恢复默认界面和检查更新页面。

*v0.2.1*

* 增加了日文卡名、英文卡名、卡片密码的显示。
* 优化了UI，比如效果文本可以随着窗口生成滚动条。
* 增加了透明度效果。
* 增加了字体大小设置。
* 点击中·日·英文卡名、卡密、卡片类型可以直接复制到系统剪贴板。
* 修复查询延迟，提高了默认轮询速度。由 @GenBill 修复。
* 设置自动保存在配置文件中。
* 支持在solo模式入口查看租用卡组和AI对手卡组内容。由 @zealyahweh 贡献。
* 修复回放模式查看对手卡组。由 @zealyahweh 贡献
* 修复一个崩溃问题。

*v0.2.0*

现在有一个初步的GUI界面。

目前版本依然保留CLI界面。

*v0.1.6*

自动切换模式，现在不用手动切换卡组或者决斗模式。

支持回放模式中查询对手卡组。

由 @zealyahweh 贡献

*v0.1.5*

添加UAC判断，非管理员权限运行会执行重开。由 @RyoLee 贡献。

添加一个配置项，可选精简卡查内容。

*v0.1.4*

新增配置文件。可自定义快捷键，窗口置顶等。

置顶功能不再限制目录。

修复灵摆效果不显示的bug。

修复一个崩溃bug。

*v0.1.3*

增加窗口置顶功能

修复部分崩溃问题

*v0.1.2*

处理窗口闪烁。

*v0.1.1*

提供win7兼容版本。

</details>

## Donation

<ins>注意本项目并没有开放捐赠。</ins>但是依然感谢以下捐赠者。

* xay罘
* 国王的冕冠

请多多分享本项目就好:)

## Related Efforts

* [Yu-Gi-Oh! Master Duel - Uncensor Patch](https://www.youtube.com/watch?v=hXGVXXHT6us) 反和谐卡图替换补丁
* [MasterDuelSimpleTranslateTool](https://github.com/PatchouliTC/MasterDuelSimpleTranslateTool) 基于图像指纹识别的翻译工具，提供了本项目的CLI版本UI基础。

## License

[GNU General Public License v3.0](https://github.com/SkywalkerJi/mdt/blob/master/LICENSE) 

## Code of conduct

[Contributor Covenant Code of Conduct](https://github.com/SkywalkerJi/mdt/blob/master/CODE_OF_CONDUCT.md)

## Disclaimers

<ins>This project is not affiliated with or sponsored by Konami or its licensors.</ins>

## Assets

Card texts come from [ygocdb.com](https://ygocdb.com) and [ygopro-database](https://github.com/mycard/ygopro-database)

Some multimedia content is NOT under GPLv3 License. Get in touch with Konami if you want to use it.