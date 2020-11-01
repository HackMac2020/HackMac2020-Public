# Writeup

If you visit /robots.txt you can see one disallowed entry for /.git.bak

Visiting /.git.bak shows us a list of what looks like the contest of a .git folder

We can then download this folder to our system with `wget` via
```wget -r https://chal.hackmac.xyz:30107/.git.bak```

Moving this file into a new directory and renaming it to `.git` we can then look at the git commit history of the repo which looks like this:
```
commit 109fc3962b3018377a85714e678a19c03dead5da (HEAD -> master)
Author: jordanbertasso <36979824+jordanbertasso@users.noreply.github.com>
Date:   Tue Oct 13 22:01:22 2020 +1100

    annoy

commit 7f993834071dfc1a45f4d8227c8d187c17fe0c9a
Author: jordanbertasso <36979824+jordanbertasso@users.noreply.github.com>
Date:   Tue Oct 13 22:01:03 2020 +1100

    initial
```

We can see that there were two commits, `initial` and `annoy`.
Let's checkout `initial` and see what we can find
```
❯ git checkout 7f993834071dfc1a45f4d8227c8d187c17fe0c9a
D	hello_world.py
Note: switching to '7f993834071dfc1a45f4d8227c8d187c17fe0c9a'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 7f99383 initial
```

Let's look at the files we have
```
❯ ls -la
total 16
drwxr-xr-x   4 jbertasso  wheel   128 15 Oct 20:18 .
drwxrwxrwt  71 root       wheel  2272 15 Oct 20:15 ..
-rw-r--r--   1 jbertasso  wheel  6148 15 Oct 20:18 .DS_Store
drwxr-xr-x  12 jbertasso  wheel   384 15 Oct 20:18 .git
```

We see a .DS_Store file, hinted at by the theme of the challenge. You can [read more about the contents of these files here](https://ponderthebits.com/2017/01/mac-dumpster-diving-identifying-deleted-file-references-in-the-trash-ds_store-files-part-1/). They are used as a sort of local database for file system changes on macos, allowing you to undo modifications and such.

Let's see what we have inside
```
❯ xxd .DS_Store
...

00000200: 0000 0000 0000 0000 0000 0003 0000 0015  ................
00000210: 0068 0061 0063 006b 006d 0061 0063 007b  .h.a.c.k.m.a.c.{
00000220: 0064 0065 006c 0065 0074 005f 0064 0073  .d.e.l.e.t._.d.s
00000230: 0074 006f 0072 0065 007d 496c 6f63 626c  .t.o.r.e.}Ilocbl
00000240: 6f62 0000 0010 0000 003b 0000 0028 ffff  ob.......;...(..
00000250: ffff ffff 0000 0000 0015 0068 0061 0063  ...........h.a.c
00000260: 006b 006d 0061 0063 007b 0064 0065 006c  .k.m.a.c.{.d.e.l
00000270: 0065 0074 005f 0064 0073 0074 006f 0072  .e.t._.d.s.t.o.r
00000280: 0065 007d 7074 624c 7573 7472 0000 0024  .e.}ptbLustr...$
00000290: 0053 0079 0073 0074 0065 006d 002f 0056  .S.y.s.t.e.m./.V
000002a0: 006f 006c 0075 006d 0065 0073 002f 0044  .o.l.u.m.e.s./.D
000002b0: 0061 0074 0061 002f 0070 0072 0069 0076  .a.t.a./.p.r.i.v
000002c0: 0061 0074 0065 002f 0074 006d 0070 002f  .a.t.e./.t.m.p./
000002d0: 0074 006d 0070 002f 0000 0015 0068 0061  .t.m.p./.....h.a
000002e0: 0063 006b 006d 0061 0063 007b 0064 0065  .c.k.m.a.c.{.d.e
000002f0: 006c 0065 0074 005f 0064 0073 0074 006f  .l.e.t._.d.s.t.o
00000300: 0072 0065 007d 7074 624e 7573 7472 0000  .r.e.}ptbNustr..
00000310: 0015 0068 0061 0063 006b 006d 0061 0063  ...h.a.c.k.m.a.c
00000320: 007b 0064 0065 006c 0065 0074 005f 0064  .{.d.e.l.e.t._.d
00000330: 0073 0074 006f 0072 0065 007d 0000 0000  .s.t.o.r.e.}....
00000340: 0000 0000 0000 0000 0000 0000 0000 0000  ................
...
```

And we can see the flag which was the name of a previously deleted file!
```
hackmac{delet_dstore}
```