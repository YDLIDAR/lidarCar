##X2lidarBot
###控制和显示
在雷达车和手柄已经匹配的情况下，雷达车和手柄可以通过EspNow互发消息，雷达车的雷达信息可以显示到手柄上，手柄也可以通过EspNow控制小车的移动。

- 普通控制模式：移动手柄摇杆，小车将实现前进后退和转向。
- 全向控制模式：按住手柄A键即手柄屏幕三个按钮中最左边的按钮，再移动摇杆可以实现左右的横移，但是前后的方向是反过来的。

###连接与匹配
在未连接状态或者有一方没连接另外一方的情况下，显示或者控制都有可能出现问题，这时候我们都需要做一个重新的连接。

- 雷达车按住C键不放按一下M5Core的电源键，等待屏幕重启完松开C键即可进入广播模式，所有从机都会收到主机发来的信号。
- 在雷达车进入广播模式的情况下，我们按住手柄C键不放再按一下手柄的电源键，等待手柄重启完成再松开C键即可在屏幕上查看到当前广播的主机。我们通过A/C键向上向下选择，然后按B键确定想要连接的主机的Mac地址，主机的Mac地址可以通过手机或者电脑查看附近的Wi-Fi，以lidar开头后面紧接着的就是主机的Mac地址。
- 确认完主机之后，主机即雷达车屏幕将收到从机的确认信号，同样通过ABC键选择和确定从机即手柄的地址。当按下B键确定之后，雷达车和手柄就完成了通信的配置，双方可以互发消息，实现雷达图显示和手柄控制。

###网页显示雷达图像
在雷达车启动完成之后，不需要雷达车和手柄完成匹配，便可以通过连接雷达车Wi-Fi，然后通过手机或者电脑浏览器访问192.168.4.1/map看到雷达图像信息。