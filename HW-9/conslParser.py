import re
import subprocess
import datetime

pattern = r'(\S*)\s*(\d*)\s*(\d*.\d*)\s*(\d*.\d)\s*(\d*)\s*(\d*)\s*(\S*)\s*(\S*)\s*(\S*)\s*(\d*:\d*)\s*(.*)$'

process = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
res_list = []
list_group = []
for raw in process.stdout.split("\n"):
    patt_group = re.search(pattern, raw)
    if patt_group:
        list_group = [patt_group.group(1), patt_group.group(2), patt_group.group(3), patt_group.group(4),
                      patt_group.group(5), patt_group.group(6), patt_group.group(7), patt_group.group(8),
                      patt_group.group(9), patt_group.group(10), patt_group.group(11)]
        res_list.append(list_group)

users = []
mem_sum = 0
cpu_sum = 0
mem_max = 0
cpu_max = 0
mem_max_process = ""
cpu_max_process = ""

for line in res_list:
    users.append(line[0])
    mem_sum += round(float(line[3]), 1)
    cpu_sum += round(float(line[2]), 1)
    if float(line[3]) > mem_max:
        mem_max = float(line[3])
        mem_max_process = line[10][:20]
    if float(line[2]) > cpu_max:
        cpu_max = float(line[2])
        cpu_max_process = line[10][:20]

users_processes = dict((x, users.count(x)) for x in set(users))

print("Отчёт о состоянии системы:")
print(f"Пользователи системы: {', '.join(set(users))}")
print(f"Процессов запущено: {len(res_list)}\n")
print(f"Пользовательских процессов:")
for key, value in users_processes.items():
    print(f"{key}: {value}")
print(f"\nВсего памяти используется: {round(mem_sum, 1)}%")
print(f"Всего CPU используется: {round(cpu_sum, 1)}%")
print(f"Больше всего памяти использует: {mem_max_process}")
print(f"Больше всего CPU использует: {cpu_max_process}")

datetime_now = datetime.datetime.now()
file_name = datetime_now.strftime('%m-%d-%y-%H-%M') + "-scan.txt"
with open(file_name, "w", encoding='utf-8') as f:
    f.write("Отчёт о состоянии системы:\n")
    f.write(f"Пользователи системы: {', '.join(set(users))}\n")
    f.write(f"Процессов запущено: {len(res_list)}\n\n")
    f.write(f"Пользовательских процессов: \n")
    for key, value in users_processes.items():
        f.write(f"{key}: {value} \n")
    f.write(f"\nВсего памяти используется: {round(mem_sum, 1)}%\n")
    f.write(f"Всего CPU используется: {round(cpu_sum, 1)}%\n")
    f.write(f"Больше всего памяти использует: {mem_max_process}\n")
    f.write(f"Больше всего CPU использует: {cpu_max_process}\n")
