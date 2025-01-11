#!/bin/bash
# SPDX-FileCopyrightTest: 2024 Taichi Ichijo
# SPDX-License-Identifier: BSD-3-Clause

# ROS 2 ワークスペースのディレクトリ
dir=~
[ "$1" != "" ] && dir="$1"

# ワークスペースに移動してビルド
cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# ノードをバックグラウンドで起動し、プロセスIDを保存
ros2 run mypkg greeting &  # ノードを実行
node_pid=$!

# ノードが起動するまで少し待つ
sleep 3

# トピックの出力をキャプチャ
timeout 25 ros2 topic echo /greeting > /tmp/greeting.log

# ノードを終了する
kill $node_pid 2>/dev/null

# トピックにメッセージが出力されているか確認
if grep -q "Hello" /tmp/greeting.log || grep -q "Hi there!" /tmp/greeting.log; then
    echo "成功: GreetingNode は正常に動作しています。"
else
    echo "失敗: メッセージが見つかりません。"
fi

# ログファイルの削除
rm -f /tmp/greeting.log
