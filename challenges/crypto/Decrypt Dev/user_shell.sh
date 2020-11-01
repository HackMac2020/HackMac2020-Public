#!/bin/bash 

nsjail \
--really_quiet \
--user ctf \
--group ctf \
-R /lib \
-R /lib64 \
-R /bin \
-R /usr \
-T /dev -R /dev/urandom -R /dev/null \
-T /tmp \
-R /home/ctf/:/chal \
-D /chal \
--disable_proc \
--time_limit 300 \
--rlimit_cpu 10 \
--cgroup_pids_max 16 \
--cgroup_mem_max 67108864 \
-- /bin/bash -i