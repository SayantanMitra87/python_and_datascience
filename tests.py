from __future__ import division
# from collections import counter
# from collections import defaultdict

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = []
while len(num) > 0:
    nums.append(num.pop())

nums_len = len(nums)
set_nums = set(nums)
# set_nums_len = len(set_nums)
back_to_list = list(set_nums)

print "        nums: %r" % nums
print "    set_nums: %r" % set_nums
print "back_to_list: %r" % back_to_list

