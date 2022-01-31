# Yu-Gi-Oh! Master Duel 中文卡查

Yu-Gi-Oh! Master Duel translation script

* 自动切换，自动查卡，全面覆盖Deck、Duel、Solo、Replay模式。
* 高正确性，除非卡片数据本身有错。
* 超快识别速度，低于0.000001s。
* 极低占用，CPU占用忽略不计。
* 直接调用win32api，不使用第三方dll。
* 开源，你可以直接执行源代码并定制你自己的版本。
* 高兼容性，点开即用，支持各种语言，最低可支持win7。

![MDT](https://github.com/SkywalkerJi/mdt/raw/master/IMG/v0.2.1.png "MDT v0.2.1")

## Download

你可以在[Releases](https://github.com/SkywalkerJi/mdt/releases/latest)下载预打包的MDT版本。

如果是windows7用户请使用后缀win7的版本。

[中国大陆用户下载点](https://wwi.lanzouj.com/b0176jyjc) 密码:5j6f

你还可以在[Uncensor Patch](https://github.com/SkywalkerJi/mdt/releases/tag/v1.0.1-UncensorPatch)下载反和谐卡图补丁。

## Usage

目前MDT拥有两个版本，有GUI界面的版本（推荐）和纯命令行CLI界面。

**从预打包的GUI版本（v0.2.x）启动（适合大部分用户）**

1. 打开游戏。
2. 右键使用**管理员权限**运行`mdt.exe`。
3. 在组卡界面点击一张卡。
4. enjoy it。

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
cards_db = cards.json
; 翻译文件名
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

*v0.2.1版本*

[bilibili](https://www.bilibili.com/video/av636086411)   [Youtube](https://www.youtube.com/watch?v=TfHoNeEVqf4)

*卡图反和谐补丁*

[bilibili](https://www.bilibili.com/video/av765979539)   [Youtube](https://www.youtube.com/watch?v=ickw082Snwo)

<details>
   <summary>旧版演示</summary>

*v0.2.0版本*

[bilibili](https://www.bilibili.com/video/av466062188)   [Youtube](https://www.youtube.com/watch?v=Vav013Cx3BQ)

*v0.1.4版本*

[bilibili](https://www.bilibili.com/video/av850928534)   [Youtube](https://www.youtube.com/watch?v=mx0KaT3cRsQ)

*v0.1.2版本*

[bilibili](https://www.bilibili.com/video/av593463793)

</details>

## Contributing

有其他指针或功能欢迎提交[issue](https://github.com/SkywalkerJi/mdt/issues/new)或Pull Request。

## Contact us

如果你有错误报告、建议、想法，请随时通过以下方式联系开发者：

* [issue](https://github.com/SkywalkerJi/mdt/issues/new)
* [Telegram](https://t.me/KancolleRTA_bot)
* [Twitter](https://twitter.com/Skywalker_Ji)
* [NGA](https://bbs.nga.cn/read.php?tid=30415633)
* [Q群 710144213](https://jq.qq.com/?_wv=1027&k=uyFt3qi0)
* 或其他途径。

## Changelog

*v0.2.2*

* 修复OCG专有卡和dbsp卡包的英文卡名缺失问题。
* 添加右键菜单。
* UI锁定功能改为独立选项。
* 右键可恢复默认界面和检查更新页面。

<details>
   <summary>展开过往版本</summary>

*v0.2.1*

* 增加了日文卡名、英文卡名、卡片密码的显示。
* 优化了UI，比如效果文本可以随着窗口生成滚动条。
* 增加了透明度效果。
* 增加了字体大小设置。
* 点击中·日·英文卡名、卡密、卡片类型可以直接复制到系统剪贴板。
* 修复查询延迟，提高了默认轮询速度。由 @GenBill 修复
* 设置自动保存在配置文件中。
* 支持在solo模式入口查看租用卡组和AI对手卡组内容。由 @zealyahweh 贡献
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

</details>

## Donation

<ins>注意本项目并没有开放捐赠。</ins>但是依然感谢以下捐赠者。

* xay罘
* 国王的冕冠

请向你的朋友推荐本项目就好:)

## Related Efforts

* [Yu-Gi-Oh! Master Duel - Uncensor Patch](https://www.youtube.com/watch?v=hXGVXXHT6us) 反和谐卡图替换补丁
* [MasterDuelSimpleTranslateTool](https://github.com/PatchouliTC/MasterDuelSimpleTranslateTool) 基于图像指纹识别的CLI工具，提供了本项目的CLI版本UI基础。

## License

[GNU General Public License v3.0](https://github.com/SkywalkerJi/mdt/blob/master/LICENSE) 

## Disclaimers

<ins>This project is not affiliated with or sponsored by Konami or its licensors.</ins>

## Assets

Card texts come from [ygocdb.com](https://ygocdb.com) and [ygopro-database](https://github.com/mycard/ygopro-database)

Some multimedia content is NOT under GPLv3 License. Get in touch with Konami if you want to use it.