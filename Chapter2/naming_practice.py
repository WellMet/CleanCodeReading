class Poops:
    def __init__(self):
        self.poops_count = 0
        self.poops_state = "notPooping"
        pass

    def lole(self):
        return "poop"

    def poop(self, s, l , c):
        return Poop(s, l, c)
    
    def drop(self, poop):
        return f"Droping turd size {poop.size}, length {poop.length}, color {poop.color}"

    def droplots(self, number):
        for sumturd in range(number):
            self.drop(Poop())

        return


class Poop():
    def __init__(self, size=5, length=5, color="b"):
        self.size = size
        self.length = length
        self.color = color

