# mypkg
宿題
# greetingコマンド
[![test](https://github.com/Taichiichijo/mypkg/actions/workflows/test.yml/badge.svg)]
(https://github.com/Taichiichijo/mypkg/actions/workflows/test.yml/)

## 概要
このパッケージは、ROS2のパブリッシャとしてランダムに挨拶をする。

## 実行方法
~~~
$ ros2 launch mypkg talk_listen.launch
~~~
結果
~~~
[talker-1] [INFO] [1735275893.946049236] [talker]: Talker says: Hello
[listener-2] [INFO] [1735275893.954848275] [listener]: Listener received: Hello
[listener-2] [INFO] [1735275893.955478703] [listener]: Listener responds: Good to hear from you!
[talker-1] [INFO] [1735275895.936374444] [talker]: Talker says: Hi there!
[listener-2] [INFO] [1735275895.939177966] [listener]: Listener received: Hi there!
[listener-2] [INFO] [1735275895.940442516] [listener]: Listener responds: Hi there!
~~~

talkerがランダムで挨拶をlistenerに送り、挨拶を受け取ったlistenerがランダムに挨拶をする
## トピック
greeting : ノード間でデータをやりとりするための通信チャンネル
## ノード
talker : 定期的に挨拶を送信し続ける

listener : 受け取った挨拶に対してランダムに挨拶をかえす。

## 必要なソフトウェア
- python3
  
- ROS2 バージョン : hunble
## テスト環境
- ubuntu-22.04

## ライセンスや著作権
 - このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可される

 - このパッケージのコードは、下記のスライド　(CC-BY-SA 4.0 by Ryuichi Ueda)のものを、本人の許可を得て自身の著作としたものです。
    - [https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson8.html)
    - [https://ryuichiueda.github.io/slides_marp/robosys2024/lesson9.html](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson9.html)
    - [https://ryuichiueda.github.io/slides_marp/robosys2024/lesson10.html](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson10.html)
    - [https://ryuichiueda.github.io/slides_marp/robosys2024/lesson11.html](https://ryuichiueda.github.io/slides_marp/robosys2024/lesson11.html)
 　　

 - 2024 Taichi Ichijo
