#Time Conversion

time = input()

if time[ : 2] == '12' and time[-2 : ] == 'AM':
      print('00' + time[2 : -2])
elif time[ : 2] == '12' and time[-2 : ] == 'PM':
      print(time[0 : -2])
elif time[-2 : ] == 'AM':
      print(time[0 : -2])
elif time[-2 : ] == 'PM':
      print(str(int(time[ : 2]) + 12) + time[2 : -2])

