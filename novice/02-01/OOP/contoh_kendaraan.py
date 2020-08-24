class Kendaraan:
    #didalam class ada properti
    kecepatan = 0
    cc = 0

#constructor
    def __init__(self):
        #seperti properti tetapi bisa lebih complex
        self.roda = 0 
    
    def nyala(self):
        print('ngeeeng')

    def maju(self):
        if self.roda > 0:
            self.kecepatan = self.kecepatan + 10

    def mundur(self):
        pass

#inheritance (pewarisan)
class Motor(Kendaraan):
    pass

m1 = Motor()
m1.nyala()
m1.roda = 3
print(m1.roda)
