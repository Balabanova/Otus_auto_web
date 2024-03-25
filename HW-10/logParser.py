import json
import re
import os
import sys

result_json = {}
path_to_files = []
path_to_file_or_dir = ''
result_json_file_name = ''
pars_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*(\[.*\])\s+"([A-Z]*).*"\s+\d{3}\s+[\d, -]*\s+"(.*)"\s+".*"\s+(\d*)$'

try:
    path_to_file_or_dir = sys.argv[1]
except:
    print("Give me the path to log in start string")

if os.path.isfile(path_to_file_or_dir):
    path_to_files.append(path_to_file_or_dir)
elif os.path.isdir(path_to_file_or_dir):
    for f in os.listdir(path_to_file_or_dir):
        if '.log' in f:
            path_to_files.append(os.path.join(path_to_file_or_dir, f))

for path in path_to_files:
    with open(path, 'r') as logFile:
        find_parameters = []
        ip_counter = {}
        total_requests = 0
        duration_dict = {"duration": 0}
        list_of_duration_dict =[duration_dict, duration_dict, duration_dict]
        stat_dict = {
            "GET": 0,
            "POST": 0,
            "HEAD": 0,
            "PUT": 0,
            "OPTIONS": 0,
            "DELETE": 0
        }

        for raw in logFile:
            total_requests +=1
            find_parameters = re.search(pars_pattern, raw)

            try:
                ip_counter[find_parameters.group(1)] += 1
            except:
                ip_counter[find_parameters.group(1)] = 1

            if int(find_parameters.group(5)) > list_of_duration_dict[2]["duration"]:
                duration_dict = {
                    "ip": find_parameters.group(1),
                    "date": find_parameters.group(2),
                    "method": find_parameters.group(3),
                    "url": find_parameters.group(4),
                    "duration": int(find_parameters.group(5))
                }
                list_of_duration_dict.append(duration_dict)
                list_of_duration_dict = sorted(list_of_duration_dict, key=lambda d: d['duration'], reverse=True)
                list_of_duration_dict.pop(3)

            stat_dict[find_parameters.group(3)] += 1

        sorted_list_ip = sorted(ip_counter.items(), key=lambda x: x[1], reverse=True)
        d = {}
        for x in list(sorted_list_ip)[0:3]:
            d[x[0]] = x[1]
        result_json = {
            "top_ips": d,
            "top_longest": list_of_duration_dict,
            "total_stat": stat_dict,
            "total_requests": total_requests
        }

    print('\n' + os.path.basename(path) + '\n')
    print(json.dumps(result_json, indent=2))

    with open(f"{os.path.basename(path).split('.')[0]}_{'result.json'}", 'w') as outJson:
        json.dump(result_json, outJson, indent=2)
