import sys 

def get_log_with_filter(filename, from_time, to_time):
    log_filter = []
    with open(filename) as file:
        for log in file:
            log_array = log.split()
            if from_time != "" and to_time != "":
                if log_array[1] < from_time or log_array[1] > to_time:
                    continue 
            log_filter.append(log_array)
    return log_filter 

def get_log(from_time, to_time):
    log_data = get_log_with_filter("log.txt", from_time, to_time) 

    req = {}
    latency = {}
    for log in log_data:
        req[log[4]] = req.get(log[4], 0) + 1
        latency[log[2] + " " + log[3]] = int(log[5].strip('ms'))

    return req, latency 

def print_log(request, latency):
    
    seen_status = 0
    for status, count in sorted(request.items()):
        code = int(status[0])
        if seen_status != code:
            seen_status = code 
            print('\n')
            if code == 2:
                print('Success (2xx/3xx):')
            elif code == 4:
                print('Client Errors (4xx):')
            elif code == 5:
                print('Server Errors (5xx):')
        plural = "s" if count > 1 else ""
        print(f"{status}: {count} request{plural}")

    n = 5
    print(f'\n\nSlowest {n} requests:')
    for api, lat in sorted(latency.items(), key=lambda item: item[1], reverse=True):
        if n == 0:
            break 

        print(f"{lat}ms - {api}")
        n -= 1

def main():
    from_time, to_time = "", ""
    if len(sys.argv) > 1:
        from_time, to_time = sys.argv[1], sys.argv[2]
        
    if from_time and to_time:
        print(f'Time Range: {from_time} to_time {to_time}')
    else:
        print('Time Range: all time') 

    req, lat = get_log(from_time, to_time)
    print_log(req, lat)

if __name__ == "__main__":
    main()

