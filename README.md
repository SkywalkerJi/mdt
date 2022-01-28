# Yu-Gi-Oh! Master Duel 中文卡查

Yu-Gi-Oh! Master Duel translation script

* 自动切换，自动查卡。
* 高正确性，除非卡图数据本身有错。
* 超快识别率，低于0.000001s。
* 极低占用，CPU占用忽略不计。
* 直接调用win32api，不使用第三方dll。
* 开源，你可以直接执行源代码。
* 高兼容性，点开即用。

![MDT](https://github.com/SkywalkerJi/mdt/raw/master/IMG/gui.png "MDT GUI")

## Download

你可以在[Releases](https://github.com/SkywalkerJi/mdt/releases/latest)下载预打包的MDT版本。

如果是windows7用户请使用后缀win7的版本。

中国大陆下载点[lanzou](https://wwi.lanzouj.com/b0176jyjc) 密码:5j6f

你还可以在[Uncensor Patch](https://github.com/SkywalkerJi/mdt/releases/tag/v1.0.1-UncensorPatch)下载反和谐卡图补丁。

## Usage

**从预打包的GUI版本（v0.2.x）启动（适合大部分用户）**

1. 打开游戏。
2. 使用**管理员权限**运行mdt.exe。
3. 在组卡界面点击一张卡。

**使用预打包的CLI版本**

1. MDT同时自带一个命令行界面。这是MDT v0.1.X版本的默认UI。
2. 打开游戏。使用管理员权限运行mdt.exe。
3. 根据提示使用快捷键。

| 快捷键 | 功能     |
| ------ | -------- |
| ctrl+s | 开启检测 |
| ctrl+p | 暂停检测 |
| ctrl+q | 退出程序 |

4. 可在config.ini文件中进行功能配置。以下是一份样例，可以直接复制粘贴。
   如果要进行CLI窗口置顶设置，尤其要注意窗口名（lp_window_name）选项。使用默认配置文件时可以把软件放在C:\mdt 目录下即可进行窗口置顶。
```
[config] 
; CLI基本设置
cards_db = cards.json
; 翻译文件名
pause_hotkey = ctrl+p
; 暂停快捷键
exit_hotkey = ctrl+q
; 退出快捷键
switch_hotkey = ctrl+s
; 切换模式快捷键
window_on_top = 0
; 是否开启CLI窗口置顶 1开启 0关闭 注意与GUI窗口无关，GUI默认置顶
lp_window_name = C:\mdt\mdt.exe
; 开启窗口置顶时需要提供窗口名，一般是软件安装路径
; 参考路径格式 C:\mdt\mdt.exe
; 直接运行py源代码时一般为 C:\WINDOWS\py.exe
window_pos_x = 400
window_pos_y = 400
window_pos_cx = 400
window_pos_cy = 400
; 这四个参数是控制CLI窗口置顶时默认的窗口大小，分别代表窗口左侧坐标，窗口顶部坐标，窗口宽度，窗口高度。取值为正整数。
sleep_time = 1
; 控制轮询间隔，如果你觉得太快可以把这个值改大。一般不用动。
show_all_info = 1
; 如果你想要只显示中文卡名+卡密+效果，可以把这一项改成0。
```

**视频演示**

*v0.2.0版本*

[bilibili](https://www.bilibili.com/video/av466062188)   [Youtube](https://www.youtube.com/watch?v=Vav013Cx3BQ)

*卡图反和谐补丁*

[bilibili](https://www.bilibili.com/video/av765979539)   [Youtube](https://www.youtube.com/watch?v=ickw082Snwo)

*v0.1.4版本*

[bilibili](https://www.bilibili.com/video/av850928534)   [Youtube](https://www.youtube.com/watch?v=mx0KaT3cRsQ)

*v0.1.2版本*

[bilibili](https://www.bilibili.com/video/av593463793)

## Contributing

有其他指针可以提交[issue](https://github.com/SkywalkerJi/mdt/issues/new)或PR。

你也可以通过[Twitter](https://twitter.com/Skywalker_Ji)或[NGA](https://bbs.nga.cn/read.php?tid=30415633)进行反馈

或者你可以加入Q群：710144213

## Changelog

*v0.2.0*

现在有一个初步的GUI界面。

目前版本依然保留CLI界面。

*v0.1.6*

自动切换模式，现在不用手动切换卡组或者决斗模式。

支持回放模式中查询对手卡组。

由 @zealyahweh 贡献

*v0.1.5*

添加UAC判断，非管理员权限运行会执行重开。由 @RyoLee 贡献

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

## Related Efforts

* [MasterDuelSimpleTranslateTool](https://github.com/PatchouliTC/MasterDuelSimpleTranslateTool) 基于图像指纹识别的CLI工具，提供了本项目的CLI-UI基础。
* [Yu-Gi-Oh! Master Duel - Uncensor Patch](https://www.youtube.com/watch?v=hXGVXXHT6us) 反和谐卡图替换补丁

## License

GPLv3

## Disclaimers

<ins>This project is not affiliated with or sponsored by Konami or its licensors.</ins>

## Assets

Card texts come from [ygocdb.com](https://ygocdb.com)

Some multimedia content is NOT under GPLv3 License. Get in touch with Konami if you want to use it.