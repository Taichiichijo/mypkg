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
##  取得方法
~~~
ros2 topic echo /greeting
~~~
## 実行例
~~~
data: Good morning
---
data: Howdy
---
data: Hey!
---
data: Good morning
---
data: Good morning
---
data: Hello
---
data: Howdy
---
data: Hey!
~~~
## トピック 
greeting : ノード間でデータをやりとりするための通信チャンネル
## ノード
greeting_node : 挨拶を送り続けるノード

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
