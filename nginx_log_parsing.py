'''
Read log file extact the below details :

1. Print (host, request-count) tuples for the top-10 frequent hosts
2. Print (HTTP-status-code, count) tuples, sorted by count
3. Print the hour with the highest request count, along with the count
4. Print the hour with the highest total number of bytes served, along with the total
5. Print the first & last path name components of top-10 most frequently accessed resources
6. Print the mean and mode of the distribution of number of GET params

 Write test cases to test your implementation

 '''

import re
import collections

regex = r'^(?P<host>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) - - ' \
        r'\[(?P<date>.*)\] ' \
        r'"(?P<request>.*?)" ' \
        r'(?P<status>\d*) ' \
        r'(?P<size>\d*) ' \
        r'"(?P<referer>.*?)" ' \
        r'"(?P<user_agent>.*?)".*$'

host_count = {} # key=host and value=request_count
status_count = {}
hour_count = {}
hour_size = {}
request_count = {}
size = 0
count = 0
file = open('access.log', 'r')
for line in file.readlines():
    matches = re.finditer(regex,line)
    for line in matches:
        if line.group('host') in host_count:
            host_count[line.group('host')] +=1
        else:
            host_count[line.group('host')] = 1

        if line.group('status') in status_count:
            status_count[line.group('status')] += 1
        else:
             status_count[line.group('status')] = 1

        if line.group('date').split(':')[1] in hour_count:
            hour_count[line.group('date').split(':')[1]] +=1
            size = int(line.group('size')) + size
            hour_size[line.group('date').split(':')[1]] = size
            # print(line.group('date').split(':')[1], ":::", size)
        else:
            hour_count[line.group('date').split(':')[1]] =1
            # resources_count[(line.group('request').split(' ')[1].split('/')[1])] = 1
            size = 0

        if line.group('request').split(' ')[1].split('/')[1] in request_count:
            request_count[(line.group('request').split(' ')[1].split('/')[1])] += 1
        else:
            request_count[(line.group('request').split(' ')[1].split('/')[1])] = 1

        if line.group('request')[0:3] == 'GET':
            count = count + 1

    hosts = collections.Counter(host_count)
    host_top10 = hosts.most_common(10)

    reuest = collections.Counter(request_count)
    request_top10 = reuest.most_common(10)

print("\nTop-10 frequent hosts:",host_top10)
print("\nHTTP-status-code, count:\n")
for stats, count in sorted(status_count.items(), key=lambda item: item[1]):
    print(stats, count)

print("\nHour with highest requests: - ",max(hour_count, key=hour_count.get),"hour",
      "Total requests: ", hour_count[max(hour_count, key=hour_count.get)])

print("\nHighest total number of bytes served in ", max(hour_size), "with total size::", hour_size[max(hour_size)])

print("\nPath name components of top-10 most frequently accessed resources ::",request_top10)

print("\nCount of GET requests: ", count)