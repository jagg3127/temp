class HASH:
    def __init__(self, string):
        self.value=0
        self.reverse(string)

    def reverse(self, string):
        for data in string:
            if data.isalpha():
                if data == "f" and string[-1] == "c":
                    self.value+=1*2*2/2*2+2-2
                if data == "c" and string[-1] == "f":
                    self.value+=((7*7+7)/8)*3/7*2
