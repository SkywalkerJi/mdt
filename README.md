# Yu-Gi-Oh! Master Duel 中文卡查 MDT

Yu-Gi-Oh! Master Duel Translation Script

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/SkywalkerJi/mdt)](https://github.com/SkywalkerJi/mdt/releases/latest) [![GitHub all releases](https://img.shields.io/github/downloads/SkywalkerJi/mdt/total)](https://github.com/SkywalkerJi/mdt#download) [![GitHub forks](https://img.shields.io/github/forks/SkywalkerJi/mdt)](https://github.com/SkywalkerJi/mdt/network) [![GitHub stars](https://img.shields.io/github/stars/SkywalkerJi/mdt)](https://github.com/SkywalkerJi/mdt/stargazers) [![GitHub license](https://img.shields.io/github/license/SkywalkerJi/mdt)](https://github.com/SkywalkerJi/mdt/blob/master/LICENSE) ![Chinese translation](https://img.shields.io/badge/%E4%B8%AD%E6%96%87%E7%BF%BB%E8%AF%91-100%25-green) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/SkywalkerJi/mdt/GitHub%20Actions%20Build%20and%20Deploy) [![Steam Game Ver](https://img.shields.io/badge/Steam-1.1.2-informational)](https://store.steampowered.com/app/1449850/YuGiOh_Master_Duel/)

* 自动切换，自动查卡，全面覆盖Deck、Duel、Solo、Replay、Shop模式。
* 高正确性，除非卡片数据本身有错。
* 超快识别速度，低于0.000001s。
* 极低占用，CPU占用忽略不计。
* 直接调用win32api，不使用第三方dll。
* 开源，你可以直接执行源代码并定制你自己的版本。
* i18n，支持简体中文和繁体中文。
* 高兼容性，点开即用，支持各种游戏内语言，最低可支持win7。
* 支持内存检测和图像指纹两种识别模式。
* 一键导入导出游戏卡组，支持`.ydk`格式。
* 可一键直达网页卡查和官方数据库，MDT也有 [Secret Pack查询工具](https://ygo.xn--uesr8qr0rdwk.cn/)。
* 支持全屏置顶、无边框、半透明。
* 支持对重要UR，主流断点进行警示。
* 支持自定义语音、BGM、召唤词。

![MDT](https://github.com/SkywalkerJi/mdt/raw/master/IMG/v0.2.12.png "MDT v0.2.12")

## Download

你可以在 [![GitHub release (latest by date)](https://img.shields.io/github/v/release/SkywalkerJi/mdt)](https://github.com/SkywalkerJi/mdt/releases/latest) 下载预打包的MDT版本。

如果是Windows7系统请下载后缀`_win7`的版本，如果想使用CLI请下载`_CLI`的版本。

中国大陆用户可在 [蓝奏云](https://wwi.lanzouj.com/b0176jyjc) 密码:5j6f 或者 [Microsoft OneDrive](https://1drv.ms/u/s!Apo8OlF1smGK6nS7sXukI9Bt9xOd?e=bbzDea) 分流下载。

你可以通过 [YGO.御坂美琴.CN](https://ygo.xn--uesr8qr0rdwk.cn/) 访问MDT网页工具。

你还可以在 [Uncensored GFX](https://www.nexusmods.com/yugiohmasterduel/mods/1) 下载反和谐卡图补丁。

## Usage

目前MDT拥有两个版本，有GUI界面的版本（推荐）和纯命令行CLI界面。此外MDT也提供网页工具。

**从预打包的GUI版本（v0.2.x）启动（适合大部分用户）**

1. 打开游戏。
2. 右键使用**管理员权限**运行`mdt.exe`。
3. 在组卡界面点击一张卡。
4. 右键可打开更多功能。繁体中文用户右键切换语言。
5. 右键设置中可以切换内存或图像识别模式。图像识别模式下可以进行商店和抽卡页面汉化。

**使用网页工具 [MDT-web](https://ygo.xn--uesr8qr0rdwk.cn/)**

1. 打开 [MDT-web](https://ygo.xn--uesr8qr0rdwk.cn/)
2. 目前可模糊检索全部154个Secret Pack包内容。同样支持一键卡查，一键复制。
3. 支持转换YGOpro卡组格式为日英双语，点击可复制到游戏中。

<details>
   <summary>使用预打包的CLI版本</summary>

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

4. 如果要进行CLI窗口置顶设置，要注意config.ini文件中窗口名（`lp_window_name`）选项。使用默认配置文件时可以把软件放在C:\mdt 目录下即可进行窗口置顶。可查看下一节，配置文件说明。
</details>

<details>
   <summary>功能配置文件说明</summary>

1. 可在`config.ini`文件中进行功能配置。以下是一份带有注释的样例。

   cli组为CLI版本设置项，gui组为GUI版本设置项。

   编辑ini时注意注释行开头必须是`; `
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
show_types = 1
; 卡片类型 1开启 0取消
show_en_name = 1
; 英文卡名 1开启 0取消
show_jp_name = 1
; 日文卡名 1开启 0取消
show_card_id = 1
; 卡密显示 1开启 0取消
show_notice = 1
; 显示提示 1开启 0取消
no_scrollbar = 1
; 隐藏滚动条 1隐藏 0显示
cv_mode = 0
; 识别模式 1图像 0内存
play_diy_bgm = 1
; 播放自定义BGM 1开启 0关闭
```

2. 自定义BGM。（v0.2.13后支持）

   在选中一张卡牌时，自动播放BGM或召唤词。样例为青眼亚白龙。可以在设置中开启。
```
自定义BGM配置文件位于`/data/bgm.json`。
json格式

{
    "12253": {
        "cn_name": "青眼亚白龙",
        "file": "Blue_audio.wav"
    },
    "666666666666": {
        "cn_name": "样例",
        "file": "wav音频文件"
    }
}

数字为cid值，可以在选中卡片后点击英文或日文名跳转官方数据库，在网址url中找到 cid=某个数字 。
中文名只做标识用。
音频文件目前只支持wav格式，其他音频格式（MP3，aac等）请转码为wav格式。
```

3. 自定义卡表
```
自定义卡表文件也位于`/data/`目录下。
sr.json SR优先级卡表
ur.json UR优先级卡表
breakpoint.json 断点卡表
格式类似自定义BGM
```
| TIER值 | 含义     |
| ------ | -------- |
| 1 | 非常重要UR |
| 2 | 重要UR |
| 3| 重要SR |
| 99|无效断点 |
| 98| 除外断点 |
| 97| 破坏断点 |

对卡表进行PR前，推荐开启issue。

</details>

<details>
   <summary>从源代码执行</summary>

```
pip install -r requirements.txt
python mdt_gui.py
python mdt_cli.py
```

</details>

**视频演示**

*v0.2.12版本*

[![Video Views](https://bilistats.lonelyion.com/views?uid=2012479&style=social&label=BiliBili&format=short)](https://www.bilibili.com/video/av681943783)  [![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UC3kA_NGfQFHMMn-kja8GTFA?style=social&label=YouTube)](https://www.youtube.com/watch?v=lsfBUmYeQRw)

*MDT-web*

[![Video Views](https://bilistats.lonelyion.com/views?uid=2012479&style=social&label=BiliBili&format=short)](https://www.bilibili.com/video/av551332211)  [![YouTube Video Views](https://img.shields.io/youtube/views/AnzWFG2RZr0?style=social&label=YouTube)](https://www.youtube.com/watch?v=AnzWFG2RZr0)

*卡图反和谐补丁*

[![Video Views](https://bilistats.lonelyion.com/views?uid=2012479&style=social&label=BiliBili&format=short)](https://www.bilibili.com/video/av765979539)   [![YouTube Video Views](https://img.shields.io/youtube/views/ickw082Snwo?style=social&label=YouTube)](https://www.youtube.com/watch?v=ickw082Snwo)

<details>
   <summary>旧版演示</summary>

*v0.2.11版本*

[![Video Views](https://bilistats.lonelyion.com/views?uid=2012479&style=social&label=BiliBili&format=short)](https://www.bilibili.com/video/av211976664)  [![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UC3kA_NGfQFHMMn-kja8GTFA?style=social&label=YouTube)](https://www.youtube.com/watch?v=7u684z4KVIQ)


*v0.2.10版本*

[![Video Views](https://bilistats.lonelyion.com/views?uid=2012479&style=social&label=BiliBili&format=short)](https://www.bilibili.com/video/av766762394)  [![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UC3kA_NGfQFHMMn-kja8GTFA?style=social&label=YouTube)](https://www.youtube.com/watch?v=oWNtD6Ko0yo)

*v0.2.9版本*

[![Video Views](https://bilistats.lonelyion.com/views?uid=2012479&style=social&label=BiliBili&format=short)](https://www.bilibili.com/video/av809137781)  [![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UC3kA_NGfQFHMMn-kja8GTFA?style=social&label=YouTube)](https://www.youtube.com/watch?v=uyDORr6GIbM)

*v0.2.5版本*

[![Video Views](https://bilistats.lonelyion.com/views?uid=2012479&style=social&label=BiliBili&format=short)](https://www.bilibili.com/video/av636233915)  [![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UC3kA_NGfQFHMMn-kja8GTFA?style=social&label=YouTube)](https://www.youtube.com/watch?v=ITXjWSsmEmc)

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

源代码是公开的，不可能加入病毒，如果实在不放心可以直接执行源代码。MDT在GitHub统计已经[![GitHub all releases](https://img.shields.io/github/downloads/SkywalkerJi/mdt/total)](https://github.com/SkywalkerJi/mdt#download)，有足够多的人进行了源代码审查，没有出现过安全问题。

目前MDT以功能开发为主，现阶段对抗杀毒软件需要大量的精力而且毫无必要。因此不打算主动解决此问题，请直接添加信任。
</details>

<details>
   <summary>Q2：管理员权限开启后依然无法检测？点击后exe消失？提示没有权限？被杀毒软件拦截隔离？</summary>

先确认你是从本页所列途径下载的版本。

然后在你使用的杀毒软件以及Windows自带的安全系统里添加信任。参见Q1。

不同的杀毒软件的安全策略不同，给出的隔离清除方式也不同，因此会导致各种奇怪的问题无法一一叙述。如果尝试后依然无法解决，请提交[issue](https://github.com/SkywalkerJi/mdt/issues/new)。
</details>

<details>
   <summary>Q3：是否可以排位？是否会封号？</summary>

不会。我第一赛季是白金1结算。

MDT以玩家数据安全为己任，不会在有风险情况下进行检测，目前Master duel游戏无法侦察MDT的读取行为，不需要担心。未来有机会可以加入CV引擎进行辅助，目前来说没有必要。

另外这个游戏没有反作弊，从经济角度考虑一个99%依赖服务端的游戏根本没必要进行检测，参考游戏王duel link。

如果你实在担心的话可以在设置中切换使用图像识别模式。
</details>

<details>
   <summary>Q4：CLI版本是否还会进行后续开发？</summary>

CLI版本在MDT v0.2.3版本进行拆分，拆分后对CLI版本只做基础可用性维护，原则上不再添加新功能。但欢迎PR。

</details>

<details>
   <summary>Q5：使用MDT时需要注意什么？</summary>

请遵循[GPLv3协议](https://github.com/SkywalkerJi/mdt/blob/master/LICENSE)。

如果你参与我们的社区，请遵循[贡献者契约行为准则](https://github.com/SkywalkerJi/mdt/blob/master/CODE_OF_CONDUCT.md)。

如果你喜欢MDT，请分享给你的朋友。

</details>

<details>
   <summary>Q6：以前能使用，现在无法使用？切换不同账号后无法使用？我确定开启条件正确，但是一直显示“等待检测”？</summary>

先在游戏的开始页面（game start 那个页面），确认左上角的游戏版本号和readme中支持的游戏版本号一致。如果不一致请更新MDT或更新游戏。

确认其他条件正确，比如：使用管理员权限开启，已经完整解压全部文件，右键exe属性中解除锁定，在安全软件中添加信任，点击一张卡等。

如果条件都正确，请尝试更改steam存档缓存文件后缀。一般在游戏安装位置，目录地址类似`SteamLibrary\steamapps\common\Yu-Gi-Oh! Master Duel\LocalData`。里面有一个形如`93b16f2`的文件夹。先备份一下，然后在这个文件夹后面加几个1，`93b16f21111111111111111`。再开游戏和mdt试一下。

</details>

<details>
   <summary>Q7：如何调整无边框模式下的窗口大小？</summary>

先在边框模式下调整大小。然后右键保存窗口位置。再在设置中切换为无边框。

</details>

<details>
   <summary>Q8：为何MDT之前一直不支持商店和抽卡页面汉化？现在又可以支持？</summary>

之前通过内存读取的方式暂时无法在抽卡页面获得稳定指针地址，如果要实施检测需要对游戏进行注入，风险较高。所以一直在考虑中没有实施。

在v0.2.12版本后，引入了图像指纹识别，mdt在图像模式下可以通过窗口截图对游戏进行非侵入式检测，所以可以对抽卡和商店界面进行汉化支持。

如果有更好的基于内存的识别模式，还是一样欢迎提交 issue 或 PR。

</details>


## Contributing

有其他指针或功能欢迎提交 [issue](https://github.com/SkywalkerJi/mdt/issues/new) 或 Pull Request。

## Contact us

如果你有错误报告、建议、想法，请随时通过以下方式联系开发者：

* [issue](https://github.com/SkywalkerJi/mdt/issues/new)
* [![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UC3kA_NGfQFHMMn-kja8GTFA?style=social)](https://www.youtube.com/channel/UC3kA_NGfQFHMMn-kja8GTFA?sub_confirmation=1)
* [Telegram](https://t.me/ygomasterduel)
* [![Twitter Follow](https://img.shields.io/twitter/follow/Skywalker_Ji?style=social&label=Follow)](https://twitter.com/Skywalker_Ji)
* [NGA](https://bbs.nga.cn/read.php?tid=30415633)
* [巴哈姆特](https://forum.gamer.com.tw/C.php?bsn=725&snA=54550&tnum=1)
* [Q群 710144213](https://jq.qq.com/?_wv=1027&k=uyFt3qi0)
* [![Followers](https://bilistats.lonelyion.com/followers?uid=2012479&style=social&format=short&label=BiliBili%20关注)](https://space.bilibili.com/2012479)
* 或其他途径。

报告故障时请附上全屏截图、Windows系统版本、MDT版本号和游戏版本号，方便快速定位。

## Changelog

*v0.2.20*
* 修复导出卡组时主卡组为0的bug。

*v0.2.19*
* 对游戏steam版本1.1.2进行支持。

<details>
   <summary>展开过往版本</summary>
*v0.2.18*
* 修复卡组导出功能。

*v0.2.17*
* 图像模式更新6月10日新卡hash。by wtof1996
* 修复识别线程失效问题。by chunibyo
* 将效果框置为只读。by funnyvalentine2363
* 去除了失效的卡组导出功能。

*v0.2.16*
* 对游戏steam版本V1.1.1进行支持。

*v0.2.15*
* 添加ydk卡组自动导入功能。感谢@chunibyo-wly 的贡献。 

*v0.2.14 beta*
* 支持4月新卡图像识别。感谢@wtof1996 的贡献。

*v0.2.13*
* 自定义BGM支持，在选中一张卡牌时，自动播放BGM或召唤词。样例为青眼亚白龙。可以在设置中开启。
* 分词处理。
* 图像模式兼容对手卡组页面。
* 调整断点表。
* 调整UR优先级。基于 NTUCGM 3/3版本。
* 修复图像模式下部分网页卡查跳转失效问题。

*v0.2.12*
* 加入图像指纹识别。感谢 md_hover@wangyi041228 的贡献。
* 在图像模式下，支持商店页面和抽卡界面汉化识别。
* 可以在右键设置中进行模式切换。
* 一个漂亮的ico，感谢bootstrap。

*v0.2.11*
* 考虑无障碍视觉，取消了上一版本中的红蓝颜色区分，改为文字显示。
* 修改断点提示底色，提高文字可读性。
* 添加重要SR提示，对352张重要SR进行分解提示，分级基于 NTUCGM。
* 设置中可选是否启用提示信息（包括重要UR，重要SR，主流断点提示）。 
* 提示框可一键跳转 masterduelmeta.com，可查询当前卡牌实时使用统计。
* 添加对影依融合、No.75的断点提示。
* MDT-web 添加 YGOpro 卡组格式转换功能，可点击将日文、英文卡名复制到 master duel进行卡组导入，支持手机。

*v0.2.10*
* 支持配置隐藏滚动条。
* 添加重要UR提示，数据基于 NTUCGM。重要UR的卡密颜色会变更：红色为可以定义环境的强力卡片，是T1主流套牌的核心部件，不建议分解。绿色为部分卡组的构筑主力，如果要分解请务必确认。白色为普通UR，可考虑分解。
* 添加主流卡组断点提示。主流卡组核心断点会进行警告，卡密背景底色变为橙色。目前支持：黄金国，龙辉巧，闪刀姬，幻影骑士团，电脑堺，恩底弥翁，召唤师，龙女仆，魔救，雷龙，英雄，调皮宝贝，源数，割草，抒情歌鸲，魔偶甜点，龙link。
* 提示卡表可在data文件夹中自定义。或开启issue提交，我将在确定卡表后在下个版本中进行添加。

*v0.2.9*
* 对游戏steam版本V1.0.2进行支持。

*v0.2.8*
* 添加反和谐补丁mod发布地址。
* 调整卡片类型显示位置。

*v0.2.7*
* 修复网页卡查设置不保存的bug。
* 优化繁中翻译。
* 增加一个[Secret Pack查询工具](https://ygo.xn--uesr8qr0rdwk.cn/)。

*v0.2.6*
* 修复点击关闭后进程未结束的bug。
* 修复不在deck界面时点击导出卡组会发生崩溃的bug。
* 现在可以单独勾选英、日文卡名、卡密显示。
* 修改文本“保存卡组”为“导出卡组”，避免混淆。

*v0.2.5*
* 支持masterduel卡组一键导出！由 @zealyahweh 贡献。可同时生成ygopro卡组`.ydk`格式和文本格式。
* 拆分英日文卡名和卡类型显示选项，现在可以分别勾选“原始卡名”和“卡片类型”。
* 主题配色改为暗色。
* 添加无边框模式，可更好融入游戏。
* 窗口整体可拖拽。
* 右键添加关闭选项。
* 鼠标悬停时添加右键提示。

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

* [md_hover](https://github.com/wangyi041228/md_hover) 提供了本项目的图像指纹识别功能。
* [Uncensored GFX](https://www.nexusmods.com/yugiohmasterduel/mods/1) 反和谐卡图替换补丁
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
