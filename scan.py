import array as arr
class reader:
    data = []
    def __init__(self,name):
        f = open(name, "r")
        for x in f:
            line = x.strip('ï»¿')
            name = line[0:line.find('=')]
            time = []
            days = line.strip(name + "=").split(",")
            self.data.append(name)
            for y in days:
                time.append(y.strip('\n'))
            self.data.append(time)
