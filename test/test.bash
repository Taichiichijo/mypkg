#!/bin/bash
# SPDX-FileCopyrightTest: 2024 Taichi Ichijo
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg talk_listen.launch.py | tee - /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Listen: 10' || echo "Pattern 'Listen: 10' not found in logs"
