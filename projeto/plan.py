class plan:
    cont = 0

    def __init__(self, p):
        self.cont += 1
        self.name = f"plan{self.cont}.csv"
        with open(self.name, "w") as pl:
            for l in p:
                for i in l:
                    if l.index(i) == (len(l) - 1):
                        pl.write(f"{i}\n")
                    else:
                        pl.write(f"{i},")

p1 = plan([
    ["nome", "idade", "peso", "altura"],
    ["Callebe", "8", "36", "1.45"]
])