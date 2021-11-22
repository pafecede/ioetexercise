import time
import scan


class matching:
    matching = {}
    matching1 = {}

    def timeComparasion(self, time1, time2, time3, time4):
        hour1 = time.strptime(time1, '%H:%M')
        hour2 = time.strptime(time2, '%H:%M')
        hour3 = time.strptime(time3, '%H:%M')
        hour4 = time.strptime(time4, '%H:%M')
        if hour1 >= hour3 or hour4 <= hour2:
            return bool(1)
        else:
            return bool(0)

    def comparision(self, a, b):
        counter = 0
        for i in range(0, len(a)):
            day = a[i][0] + a[i][1]
            for j in range(0, len(b)):
                if b[j][0] + b[j][1] == day and self.timeComparasion(a[i][2:7], a[i][8:13], b[j][2:7], b[j][8:13]):
                    counter = counter + 1
        return counter

    def __init__(self, file, file1):
        self.matching = {}
        var = scan.reader(file, file1)
        lector = var.data
        lector1 = var.data1
        self.builder(lector, self.matching)
        self.builder(lector1, self.matching1)

    def builder(self, lector, result):
        for y in range(0, len(lector)):
            if y % 2 != 0 and y <= len(lector) - 1:
                for z in range(y, len(lector), 2):
                    if z != 1 and y != z and lector[y - 1] != lector[z - 1]:
                        result.update(
                            {lector[y - 1] + '-' + lector[z - 1]: self.comparision(lector[y], lector[z])})
