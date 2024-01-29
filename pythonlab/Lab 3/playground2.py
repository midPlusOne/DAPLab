class Time:

    def __init__(self, hour=0, minute=0, second=0) -> None:
        self.hour = hour #9     1
        self.minute = minute #45        35
        self.second = second

    def __str__(self) -> str:
        return "%.2d : %.2d : %.2d" % (self.hour, self.minute, self.second)
        #used to convert time to human readable format

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
                #35100 + 5700 = 40800
        return int_to_time(seconds) #return 11 : 20 : 00 to print(start + duration)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
                #minutes(9,45) = 585     
                #minutes(1,35) =  95
        seconds = minutes * 60 + self.second
                #seconds(9,45) = 35100       
                #seconds(1,35) = 5700 
        return seconds #return(9,45) = 35100
                        #return(1,35) = 5700

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
            #minutes = 40800 / 60 = 680 => quotient
            #time.second = 40800 % 60 = 0 => remainder
    time.hour, time.minute = divmod(minutes, 60)
            #time.hour = 680 / 60 = 11 => quotient
            #time.minute = 680 % 60 = 20 => remainder
    return time #return 11 : 20 : 00 to __add__(self,other)

start = Time(9, 45)
print("Start time:", start)

duration = Time(1, 35)
print("Duration:", duration)

end_time = start + duration
print("End time:", end_time)
