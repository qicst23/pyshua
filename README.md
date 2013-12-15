pyshua
======

Python 算法题练习

用法:
----
    python Judge.py library problem

例子:
----
    python Judge.py leetcode TwoSum

如何贡献:
--------
1. 收录题库

    - LeetCode (还有4题未录入, 分别为 LRU Cache, Copy List with Random Pointer, Populating Next Right Pointers in Each Node I && II)
    - PIE (未录入)
    - CC150 (未录入)
    - EPI (未录入)

    每一个题库对应problems路径下的一个文件夹，每一个题目对应相应题库下的一个Python文件。每一个题目都要至少实现以下四个函数:
        solve
        verify
        input
        output

    具体可参考problems/leetcode下我已经写好的那些题目。

2. 增加限时机制

    目前只能验证结果对错，并未对运行时间作出限制。

License:
--------
The MIT License (MIT)
