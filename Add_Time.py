def transform(a):
    hours = a // 60
    mins = a % 60
    time_map = {
        # '1' : '1 AM',
        # '2' : '2 AM',
        # '3' : '3 AM',
        # '4' : '4 AM',
        # '5' : '5 AM',
        # '6' : '6 AM',
        # '7' : '7 AM',
        # '8' : '8 AM',
        # '9' : '9 AM',
        # '10' : '10 AM',
        # '11' : '11 AM',
        '12' : '12 PM',
        '13' : '1 PM',
        '14' : '2 PM',
        '15' : '3 PM',
        '16' : '4 PM',
        '17' : '5 PM',
        '18' : '6 PM',
        '19' : '7 PM',
        '20' : '8 PM',
        '21' : '9 PM',
        '22' : '10 PM',
        '23' : '11 PM',
        '24' : '12 AM',
        '0' : '12 AM'
    }
    part = 'AM'
    if hours >= 12 or hours == 0:
        temp = time_map.get(str(hours))
        hours = int(temp.split(' ')[0])
        part = temp.split(' ')[1]
    
    mins = str(mins).rjust(2,'0')
    return f'{hours}:{mins} {part}'

def add_time(start, duration, today=''):
    aDay = 24 * 60
    temp_time = start.split(' ')
    now_hours = int(temp_time[0].split(':')[0])
    now_min = int(temp_time[0].split(':')[1])
    
    if temp_time[1] == 'AM' or (temp_time[1] == 'PM' and now_hours == 12):
        timeToday = now_hours * 60 + now_min
    else:
        timeToday = 12 * 60 + (now_hours * 60 + now_min)

    timeWill = int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])

    sumTime = timeWill + timeToday

   

    data_map = {
        '' : 0,
        'monday' : 1,
        'tuesday' : 2,
        'wednesday' : 3,
        'thursday' : 4,
        'friday' : 5,
        'saturday' : 6,
        'sunday' : 7
    }

    countDay = sumTime // aDay
    countTime = sumTime % aDay
    c = 0
    temp = ''
    if today != '':
        for a,b in data_map.items():
            if a == today.lower():
                c = b
                break
        for i in range(countDay):
            if c < 7:
                c += 1
            else: 
                c = 1
        for a,b in data_map.items():
            if b == c:
                temp = ', ' + a.capitalize()
    if countDay == 0:
        return transform(countTime) + temp 
    elif countDay == 1:
        return transform(countTime) + temp + ' (next day)'
    else:
        return transform(countTime) + temp + f' ({countDay} days later)'

print(add_time('8:16 PM', '466:02', 'tuesday'))