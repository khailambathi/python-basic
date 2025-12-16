log_dict = {}
with open("log.txt") as file:
    for log in file:
        log_array = log.split(" ")
        log_dict[log_array[4]] = log_dict.get(log_array[4], 0) + 1 

print("Status Code Reports")

for status, count in sorted(log_dict.items()):
    plural = "s" if count > 1 else ""
    print(f"{status}: {count} Request{plural}")
