class Bitmap:
    def __init__(self,filepath):
        f = open(filepath, "rb")

        info = []
        for i in range(54):
            info.append(f.read(1))

        self.width = int.from_bytes(info[18], "little")
        self.height = int.from_bytes(info[22], "little")
        padding = ((self.width * 3) - (self.width * 3) % 4 + 4) - (self.width * 3) if self.width * 3 % 4 != 0 else 0

        pixels = f.read((self.width * self.height * 3) + (self.height * padding))
        f.close()
        
        temp = []
        for i in pixels:
            temp.append(i)
        
        x = 0
        self.pixels = [[[None for y in range(3)] for y in range(self.width)] for y in range(self.height)]
        for h in range(self.height-1,-1,-1):#self.height
            for w in range(self.width):
                for c in range(2,-1,-1):#3
                    self.pixels[h][w][c] = temp[x]
                    x += 1
            x += padding

#bmp = Bitmap('test.bmp')
#print(bmp.pixels)