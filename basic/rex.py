# -*-coding:UTF-8-*-

import re

# 手机号替换注意点：
# 1. 并非连续11位数字的就替换，时间戳常常包含11位数字
# 2. json中的数字打码后需要更换成字符串类型
# 3. 手机号结尾的情况可能会被忽略掉
# 4. 因为正则中常出现反斜线(\)，所以使用 r 类型的字符串是必要的

# re.sub 的用法几乎是php中的preg_replace 完全相同

s = '{"mobile":13552933414, "phone":18677678909}'
p_mobile_in_json = re.compile(r':(1\d{2})\d{4}(\d{4})([^0-9])', re.MULTILINE)

print(re.sub(p_mobile_in_json, r':"\1****\2"\3', s))

# 如果不是明显的json格式，直接打码
s = 'mobile: 13552933414, phone: 18677678909'
p_mobile = re.compile(r'(1\d{2})\d{4}(\d{4})([^0-9]|\s|$)', re.MULTILINE)

print(re.sub(p_mobile, r'\1****\2\3', s))
