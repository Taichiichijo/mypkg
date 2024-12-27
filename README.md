# mypkg
宿題
# greetingコマンド
[![test](https://github.com/Taichiichijo/mypkg/actions/workflows/test.yml/badge.svg)]
(https://github.com/Taichiichijo/mypkg/actions/workflows/test.yml/)

talkerとlistenerであいさつを交わす

## 実行方法
~~~
ros2 launch mypkg talk_listen.launch.py
~~~

## 実行例
~~~
[talker-1] [INFO] [1735275893.946049236] [talker]: Talker says: Hello
[listener-2] [INFO] [1735275893.954848275] [listener]: Listener received: Hello
[listener-2] [INFO] [1735275893.955478703] [listener]: Listener responds: Good to hear from you!
[talker-1] [INFO] [1735275895.936374444] [talker]: Talker says: Hi there!
[listener-2] [INFO] [1735275895.939177966] [listener]: Listener received: Hi there!
[listener-2] [INFO] [1735275895.940442516] [listener]: Listener responds: Hi there!
~~~

talkerがランダムで挨拶をlistenerに送り、挨拶を受け取ったlistenerがランダムに挨拶をする

## 必要なソフトウェア
- python
  
- ROS2
## テスト環境

