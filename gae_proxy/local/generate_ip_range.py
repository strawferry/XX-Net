#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ip_utils

__author__ = 'moonshawdo@gamil.com'

# read ip range string
# order it
# merge over lapped
# Then reproduce good format file
# check it.

import re

ip_str_list = '''
1.179.248.0-1.179.248.255
4.3.2.0/24
8.6.48.0-8.6.55.255
8.8.4.0/24
8.8.8.0/24
8.22.56.0-8.22.63.255
8.34.208.0-8.34.223.255
8.35.192.0-8.35.207.255
12.216.80.0-12.216.80.255
24.156.131.0-24.156.131.255
41.206.96.0-41.206.96.255
60.199.175.18-60.199.175.187
61.19.1.30-61.19.1.109
61.219.131.84-61.219.131.251
62.116.207.0-62.116.207.63
62.197.198.193-62.197.198.251
63.211.200.72-63.211.200.79
64.15.112.0-64.15.117.255
64.15.119.0-64.15.126.255
64.18.0.0-64.18.15.255
64.41.221.192-64.41.221.207
64.68.64.64-64.68.64.127
64.68.80.0-64.68.95.255
64.154.178.208-64.154.178.223
64.233.160.0-64.233.191.255
66.102.0.0-66.102.15.255
66.249.64.0-66.249.95.255
70.32.128.0-70.32.159.255
70.90.219.48-70.90.219.55
70.90.219.72-70.90.219.79
72.14.192.0-72.14.255.255
74.125.0.0-74.125.255.255
78.37.100.0/24
80.64.175.0/24
80.228.65.128-80.228.65.191
81.175.29.128-81.175.29.191
84.235.77.0-84.235.77.255
85.182.250.0-85.182.250.255
86.127.118.128-86.127.118.191
93.94.217.0-93.94.217.31
93.94.218.0-93.94.218.31
93.183.211.192-93.183.211.255
94.40.70.0-94.40.70.63
94.200.103.64-94.200.103.71
95.54.196.0/24
106.162.192.148-106.162.192.187
106.162.198.84-106.162.198.123
106.162.216.20-106.162.216.123
108.59.80.0-108.59.95.255
108.170.192.0-108.170.255.255
108.177.0.0-108.177.127.255
111.168.255.20-111.168.255.187
113.197.105.0-113.197.105.255
114.4.41.0/24
118.174.24.0-118.174.27.255
121.78.74.68-121.78.74.123
123.205.250.0-123.205.250.255
123.205.251.68-123.205.251.123
139.175.107.88/24
142.250.0.0-142.251.255.255
162.216.148.0-162.216.151.255
166.90.148.64-166.90.148.79
172.217.0.0-172.217.255.255
172.253.0.0-172.253.255.255
173.194.0.0-173.194.255.255
178.45.251.84-178.45.251.123
178.60.128.1-178.60.128.
192.158.28.0-192.158.31.255
192.178.0.0-192.179.255.255
193.92.133.0-193.92.133.63
193.120.166.64-193.120.166.127
194.78.99.0-194.78.99.255
194.221.68.0-194.221.68.255
195.249.20.192-195.249.20.255
198.108.100.192-198.108.100.207
199.87.241.32-199.87.241.63
199.192.112.0-199.192.115.255
199.223.232.0-199.223.239.255
202.39.143.1-202.39.143.123
202.169.193.0/24
203.66.124.129-203.66.124.251
203.116.165.148-203.116.165.251
203.117.34.148-203.117.34.187
203.165.13.210-203.165.13.251
203.165.14.210-203.165.14.251
203.208.32.0-203.208.63.255
203.211.0.20-203.211.0.59
207.126.144.0-207.126.159.255
207.223.160.0-207.223.175.255
208.21.209.0-208.21.209.15
208.117.224.0-208.117.239.55
208.117.233.0/24
208.117.240.0-208.117.255.255
209.85.128.0-209.85.255.255
209.185.108.128-209.185.108.255
209.245.184.136-209.245.184.143
209.247.159.144-209.247.159.159
210.61.221.148-210.61.221.187
210.139.253.20-210.139.253.251
210.153.73.20-210.153.73.123
213.158.11.0/24
210.158.146.0/24
210.242.125.20-210.242.125.59
210.245.14.0/24
212.188.15.0-212.188.15.255
213.186.229.0-213.186.229.63
213.240.44.0-213.240.44.31
216.33.229.0/24
216.58.208.0/20
216.109.75.80-216.109.75.95
216.239.32.0-216.239.63.255
218.176.242.0-218.176.242.255
218.253.0.0/24
1.179.248-255.0-255
103.246.187.0-255
103.25.178.4-59
106.162.192.148-187
106.162.198.84-123
106.162.216.20-123
107.167.160-191.0-255
107.178.192-255.0-255
107.188.128-255.0-255
108.170.192-255.0-255
108.177.0-127.0-255
108.59.80-95.0-255
109.232.83.64-127
111.168.255.20-187
111.92.162.4-59
113.197.105-106.0-255
118.174.24-27.0-255
12.216.80.0-255
121.78.74.68-123
123.205.250-251.68-190
130.211.0-255.0-255
142.250-251.0-255.0-255
146.148.0-127.0-255
149.126.86.1-59
149.3.177.0-255
162.216.148-151.0-255
162.222.176-183.0-255
163.28.116.1-59
163.28.83.143-187
172.217.0-255.0-255
172.253.0-255.0-255
173.194.0-255.0-255
173.255.112-127.0-255
178.45.251.4-123
178.60.128.1-63
185.25.28-29.0-255
192.119.16-31.0-255
192.158.28-31.0-255
192.178-179.0-255.0-255
192.200.224-255.0-255
193.120.166.64-127
193.134.255.0-255
193.142.125.0-255
193.186.4.0-255
193.192.226.128-191
193.192.250.128-191
193.200.222.0-255
193.247.193.0-255
193.90.147.0-123
193.92.133.0-63
194.100.132.128-143
194.110.194.0-255
194.78.20.16-31
194.78.99.0-255
195.100.224.112-127
195.141.3.24-27
195.205.170.64-79
195.229.194.88-95
195.244.106.0-255
195.244.120.144-159
195.249.20.192-255
195.65.133.128-135
195.76.16.136-143
195.81.83.176-207
196.3.58-59.0-255
197.199.253-254.1-59
197.84.128.0-63
199.192.112-115.0-255
199.223.232-239.0-255
202.39.143.1-123
203.116.165.129-255
203.117.34-37.132-187
203.165.13-14.210-251
203.211.0.4-59
203.66.124.129-251
207.223.160-175.0-255
208.117.224-255.0-255
208.65.152-155.0-255
209.85.128-255.0-255
210.139.253.20-251
210.153.73.20-123
210.242.125.20-59
210.61.221.65-187
212.154.168.224-255
212.162.51.64-127
212.181.117.144-159
212.188.10.0-255
212.188.15.0-255
212.188.7.0-255
213.186.229.0-63
213.187.184.68-71
213.240.44.0-31
213.252.15.0-31
213.31.219.80-87
216.21.160-175.0-255
216.239.32-63.0-255
216.58.192-223.0-255
217.149.45.16-31
217.163.7.0-255
217.193.96.38
217.28.250.44-47
217.28.253.32-33
217.30.152.192-223
217.33.127.208-223
218.176.242.4-251
218.189.25.129-187
218.253.0.76-187
23.228.128-191.0-255
23.236.48-63.0-255
23.251.128-159.0-255
23.255.128-255.0-255
24.156.131.0-255
31.209.137.0-255
31.7.160.192-255
37.228.69.0-63
41.206.96.1-251
41.84.159.12-30
60.199.175.1-187
61.219.131.65-251
62.0.54.64-127
62.1.38.64-191
62.116.207.0-63
62.197.198.193-251
62.20.124.48-63
62.201.216.196-251
63.243.168.0-255
64.15.112-127.0-255
64.233.160-191.0-255
64.9.224-255.0-255
66.102.0-15.0-255
66.185.84.0-255
66.249.64-95.0-255
69.17.141.0-255
70.32.128-159.0-255
72.14.192-255.0-255
74.125.0-255.0-255
77.109.131.208-223
77.40.222.224-231
77.42.248-255.0-255
77.66.9.64-123
78.8.8.176-191
8.15.202.0-255
8.22.56.0-255
8.34.208-223.0-255
8.35.192-207.0-255
8.6.48-55.0-255
8.8.4.0-255
8.8.8.0-255
80.227.152.32-39
80.228.65.128-191
80.231.69.0-63
80.239.168.192-255
80.80.3.176-191
81.175.29.128-191
81.93.175.232-239
82.135.118.0-63
83.100.221.224-255
83.141.89.124-127
83.145.196.128-191
83.220.157.100-103
83.94.121.128-255
84.233.219.144-159
84.235.77.1-251
85.182.250.0-191
86.127.118.128-191
87.244.198.160-191
88.159.13.192-255
89.207.224-231.0-255
89.96.249.160-175
92.45.86.16-31
93.123.23.1-59
93.183.211.192-255
93.94.217-218.0-31
94.200.103.64-71
94.40.70.0-63
95.143.84.128-191
61.19.1-2.0-127
61.19.8.0-127
113.21.24.0-127
118.143.88.16-123
202.86.162.20-187
139.175.107.20-187
223.26.69.16-59
220.255.5-6.20-251
202.65.246.84-123
103.1.139.148-251
116.92.194.148-187
58.145.238.20-59
41.201.128.20-59
41.201.164.20-59
222.255.120.15-59
119.81.145.120-127
119.81.142.202
23.239.5.106
74.207.242.141
'''

def PRINT(strlog):
    print (strlog)

def merge_ip_range():
    ip_range_list = []

    ip_lines_list = re.split("\r|\n", ip_str_list)
    for iplines in ip_lines_list:
        if len(iplines) == 0 or iplines[0] == '#':
            #print "non:", iplines
            continue

        ips = re.split(",|\|", iplines)
        for line in ips:
            if len(line) == 0 or line[0] == '#':
                #print "non line:", line
                continue
            begin, end = ip_utils.split_ip(line)
            if ip_utils.check_ip_valid(begin) == 0 or ip_utils.check_ip_valid(end) == 0:
                PRINT("ip format is error,line:%s, begin: %s,end: %s" % (line, begin, end))
                continue
            nbegin = ip_utils.ip_string_to_num(begin)
            nend = ip_utils.ip_string_to_num(end)
            ip_range_list.append([nbegin,nend])
            #print begin, end


    ip_range_list.sort()

    # merge range
    ip_range_list_2 = []
    range_num = len(ip_range_list)

    last_begin = ip_range_list[0][0]
    last_end = ip_range_list[0][1]
    for i in range(1,range_num - 1):
        ip_range = ip_range_list[i]

        begin = ip_range[0]
        end = ip_range[1]

        #print "now:",ip_utils.ip_num_to_string(begin), ip_utils.ip_num_to_string(end)

        if begin > last_end + 2:
            #print "add:",ip_utils.ip_num_to_string(begin), ip_utils.ip_num_to_string(end)
            ip_range_list_2.append([last_begin, last_end])
            last_begin = begin
            last_end = end
        else:
            print "merge:", ip_utils.ip_num_to_string(last_begin), ip_utils.ip_num_to_string(last_end), ip_utils.ip_num_to_string(begin), ip_utils.ip_num_to_string(end)
            if end > last_end:
                last_end = end

    ip_range_list_2.append([last_begin, last_end])


    for ip_range in ip_range_list_2:
        begin = ip_range[0]
        end = ip_range[1]
        print ip_utils.ip_num_to_string(begin), ip_utils.ip_num_to_string(end)

    # write out
    fd = open("ip_range.txt", "w")
    for ip_range in ip_range_list_2:
        begin = ip_range[0]
        end = ip_range[1]
        #print ip_utils.ip_num_to_string(begin), ip_utils.ip_num_to_string(end)
        fd.write(ip_utils.ip_num_to_string(begin)+ "-" + ip_utils.ip_num_to_string(end)+"\n")

    fd.close()

merge_ip_range()

def test_load():

    fd = open("ip_range.txt", "r")
    if not fd:
        print "open ip_range.txt fail."
        exit()

    amount = 0
    for line in fd.readlines():
        if len(line) == 0 or line[0] == '#':
            continue
        begin, end = ip_utils.split_ip(line)

        nbegin = ip_utils.ip_string_to_num(begin)
        nend = ip_utils.ip_string_to_num(end)

        num = nend - nbegin
        amount += num
        print ip_utils.ip_num_to_string(nbegin), ip_utils.ip_num_to_string(nend), num

    fd.close()
    print "amount:", amount

#
test_load()







