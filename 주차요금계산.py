import math

def TimeToMinute(time):
    h,m = map(int, time.split(":"))
    return h*60+m

def solution(fees, records):
    answer = []
    basic_time, basic_fee, unit_time, unit_fee = fees
    rec = dict()
    
    for i in records:
        time, num, hist = i.split()
        num = int(num)
        
        if num in rec:
            rec[num].append([time,hist])
        else:
            rec[num] = [[time,hist]]
    # print(rec)    
    my_data = list(rec.items())
    my_data.sort(key=lambda x : x[0])
    print(my_data)
    for i in my_data:
        k = 0
        for j in i[1]:
            if j[1] == "OUT":
                k += TimeToMinute(j[0])
            elif j[1] == "IN":
                k -= TimeToMinute(j[0])
        if len(i[1])%2==1:
            k += TimeToMinute("23:59")
        if k <= basic_time:
            answer.append(basic_fee)
        else:
            answer.append(basic_fee+math.ceil((k-basic_time)/unit_time)*unit_fee)
    return answer
