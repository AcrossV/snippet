[referer](http://mingxinglai.com/cn/2012/09/tmux/)

>妈蛋，老是忘记这些快捷键，记录下来！

tmux 使用C/S模型构建，主要包括以下单元模块
- server 服务器。 输入tmux命令的同时就开启了一个服务器
- session 会话。 一个服务器可以包括多个会话
- window窗口。一个会话可以包含多个窗口
- pane面板，一个窗口可以包含过个面板

常用快捷键：

```
  C-b ? 显示帮助
  C-b 是命令前缀，以下全部省略
  C-o 调换窗口位置
  空格键 采用下一个窗口布局
  ! 把当前窗口变成新窗口
  " 横向切分窗口
  % 纵向切分窗口
  q 显示分割窗口的编号
  o 跳到下一个分割窗口
  上下左右，跳转窗口
  c 创建新窗口
  数字键 选择几号窗口
  n 选择下一个窗口
  | 切换到最后一个使用的窗口
  p 切换到上一个窗口
  w 以菜单形式选择窗口
  t 显示时钟
  ; 切换多最后一个使用的窗口
  x 关闭面板
  & 关闭面板
  s 以菜单方式显示和选择会话
  d 推出tmux，并保存当前会话，tmux在后台运行，可以通过tmux attach 进入到指定的会话
```
