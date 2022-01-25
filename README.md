# Yu-Gi-Oh! Master Duel 中文卡查

Yu-Gi-Oh! Master Duel translation script

* 高正确性，除非卡图数据本身有错。
* 超快识别率，低于0.000001s。
* 极低占用，CPU占用忽略不计。
* 直接使用win32api，不使用第三方dll。
* 开源，你可以直接执行源代码。
* 高兼容性，点开即用。

## Download

你可以在[Releases](https://github.com/SkywalkerJi/mdt/releases/latest)下载预打包的版本。

如果是windows7用户请使用后缀win7的版本。

## Usage

1. 打开游戏后
2. 使用管理员权限运行mdt.exe，根据提示使用快捷键。

| 快捷键 | 功能                  |
| ------ | --------------------- |
| ctrl+s | 切换检测卡组/决斗模式 |
| ctrl+p | 暂停检测              |
| ctrl+q | 退出程序              |

3. 可在config.ini文件中进行功能配置。以下是一份样例，可以直接复制粘贴。

   如果要进行窗口置顶设置，尤其要注意窗口名（lp_window_name）选项。使用默认配置文件时可以把软件放在C:\mdt 目录下即可。
```
[config] 
; 基本设置
cards_db = cards.json
; 翻译文件名
pause_hotkey = ctrl+p
; 暂停快捷键
exit_hotkey = ctrl+q
; 退出快捷键
switch_hotkey = ctrl+s
; 切换模式快捷键
window_on_top = 1
; 是否开启窗口置顶 1开启 0关闭
lp_window_name = C:\mdt\mdt.exe
; 开启窗口置顶时需要提供窗口名，一般是软件安装路径
; 参考路径格式 C:\mdt\mdt.exe
; 直接运行py源代码时一般为 C:\WINDOWS\py.exe
window_pos_x = 400
window_pos_y = 400
window_pos_cx = 400
window_pos_cy = 400
; 这四个参数是控制窗口置顶时默认的窗口大小，分别代表窗口左侧坐标，窗口顶部坐标，窗口宽度，窗口高度。取值为整数。
```

4.视频演示

[v0.1.2版本](https://www.bilibili.com/video/av593463793)

## Contributing

有其他指针可以提交[issue](https://github.com/SkywalkerJi/mdt/issues/new)或PR。

你也可以通过[Twitter](https://twitter.com/Skywalker_Ji)或[NGA](https://bbs.nga.cn/read.php?tid=30415633)进行反馈

## Related Efforts

* [MasterDuelSimpleTranslateTool](https://github.com/PatchouliTC/MasterDuelSimpleTranslateTool) 基于图像指纹识别的CLI工具，提供了本项目的CLI-UI基础。

## License

GPLv3

## Disclaimers

<ins>This project is not affiliated with or sponsored by Konami or its licensors.</ins>

## Assets

Card texts come from [ygocdb.com](https://ygocdb.com)
