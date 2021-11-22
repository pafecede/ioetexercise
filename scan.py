class reader:
    data = []
    data1 = []

    def __init__(self, name,name1):
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
        f.close()
        fo = open(name1, "r")
        for x in fo:
            line = x.strip('ï»¿')
            name = line[0:line.find('=')]
            time = []
            days = line.strip(name + "=").split(",")
            self.data1.append(name)
            for y in days:
                time.append(y.strip('\n'))
            self.data1.append(time)
        fo.close()
