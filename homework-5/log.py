filename_in = 'access.log'
filename_out = 'res_py.txt'
f_in = open(filename_in, 'r')
f_out = open(filename_out, "w")

## Общее количество запросов

n = sum(1 for line in f_in)
f_out.write("Общее количество запросов:\n")
f_out.write(str(n))

f_in.seek(0)

##Общее количество запросов по типам

request = {'GET' : 0, 'HEAD' :0 , 'POST' : 0, 'PUT' : 0}

for i in range(n):
    line = f_in.readline().split()[5:6][0].strip("\"")
    if (len(line) > 6):
        continue
    request[str(line)] += 1

f_out.write("\n\nОбщее количество запросов по типам:\n")
for key,value in request.items():
    f_out.write(str(value) + ' ' + str(key) + '\n')

f_in.seek(0)

##Топ 10 самых частых запросов

url_dict = {}
sorted_url = {}

for i in range(n):
    line = f_in.readline().split()[6:7][0]
    flag = 1
    for key, value in url_dict.items():
        if (line == key):
            value += 1
            url_dict[line] += 1
            flag = 0
    if (flag):
        url_dict[line] = 1

sorted(url_dict, key=url_dict.get, reverse=True)

sorted_keys = sorted(url_dict, key=url_dict.get, reverse=True)  

for w in sorted_keys:
    sorted_url[w] = url_dict[w]

f_out.write("\nТоп 10 самых частых запросов:")
count = 0
for key, value in sorted_url.items():
    f_out.write("\n" + str(value) + " " + str(key))
    count += 1
    if (count == 10):
        break

f_in.seek(0)

##Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой

mistake_4 = {}

arr_rc = []
arr_ip = []
arr_size = []
arr_url = []

for i in range (n):
    line = f_in.readline().split()
    if (int(line[8:9][0]) < 400 or int(line[8:9][0]) >= 500):
        continue

    arr_rc.append(int(line[8:9][0]))
    arr_size.append(int(line[9:10][0]))
    arr_ip.append(line[0:1][0])
    arr_url.append(line[6:7][0])

arr_res = zip(arr_rc, arr_size, arr_ip, arr_url)
sorted_arr_res = sorted(arr_res, key = lambda arr_res: arr_res[1], reverse=True)

f_out.write("\n\nТоп 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой:")
for i in range(5):
    f_out.write("\n" + str(sorted_arr_res[i]))

f_in.seek(0)

##Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой
    
ip_dict = {}
sorted_ip = {}
for i in range (n):
    line = f_in.readline().split()
    if (int(line[8:9][0]) < 500 or int(line[8:9][0]) >= 600):
        continue
    flag = 1

    for key, value in ip_dict.items():
        if (line[0:1][0] == key):
            value += 1
            ip_dict[line[0:1][0]] += 1
            flag = 0
    if (flag):
        ip_dict[line[0:1][0]] = 1

sorted(ip_dict, key=ip_dict.get, reverse=True)
sorted_keys = sorted(ip_dict, key=ip_dict.get, reverse=True)  

for w in sorted_keys:
    sorted_ip[w] = ip_dict[w]

f_out.write("\n\nТоп 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой:")
count = 0
for key, value in sorted_ip.items():
    f_out.write("\n" + str(value) + " " + str(key))
    count += 1
    if (count == 5):
        break

f_in.close
f_out.close