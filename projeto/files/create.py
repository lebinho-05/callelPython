from os import listdir

cfiles = listdir()

def create(self, name, code):
      with open(name, "w") as file:
         file.write(code)
      cfiles.append(name)

def createcsv(self, name, p, tp):
      if tp == list:
         with open(name, "w") as csv:
               for l in p:
                  for c in l:
                     if l.index(c) < (len(l) - 1):
                        csv.write(f"{c},")
                     else:
                        csv.write(f"{c}\n")
      else:
         with open(name, "w") as file:
            file.write(p)

      cfiles.append(name)