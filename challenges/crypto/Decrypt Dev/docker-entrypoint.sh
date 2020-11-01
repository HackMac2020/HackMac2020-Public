#!/bin/bash

mkdir /sys/fs/cgroup/{cpu,memory,pids}/NSJAIL
chown -R ctf /sys/fs/cgroup/{cpu,memory,pids}/NSJAIL

/usr/sbin/sshd -D