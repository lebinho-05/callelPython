files = []

class CreateCSV:
    cont = 0

    def __create(self, name, p, tp):
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

      files.append(name)

    def __init__(self, name: str, p: list, tp = list) -> None:
        import pandas as pd
        self.cont += 1
        self.name = name +   ".csv"
        self.p = p
        if self.name in files:
           if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
              self.__create(self.name, self.p, tp)
        else:
            self.__create(self.name, self.p, tp)
         
        self.tabela = pd.read_csv(self.name)
   
    def clear(self):
      self.p = ''
   
    def save(self):
       with open(self.name, "w") as file:
          file.write(self.code)

    def show(self):
       print(self.tabela)
   
    def utilities(self):
       return self.tabela

class CreateJSON:
   cont = 0

   def __create(self, name, code):
      with open(name, "w") as file:
         file.write(code)
      files.append(name)
   
   def __init__(self, name: str, code: str) -> None:
      self.name = name +   ".json"
      self.code = code

      if self.name in files:
           if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
              self.__create(self.name, self.code)
      else:
         self.__create(self.name, self.code)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)
   
   def get(self):
      from json import load
      with open(self.name, "r") as file:
         fiJson = load(file)
      return fiJson

class CreateOther:
   cont = 0

   def __create(self, name, code):
      with open(name, "w") as fi:
         fi.write(code)
      files.append(name)

   def __init__(self, name, code):
      self.cont += 1
      self.name = name; self.code = code
      if self.name in files:
           if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
              self.__create(self.name, self.code)
      else:
         self.__create(self.name, self.code)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)

class CreateHTML:
   cont = 0

   def __create(self, name, code):
      with open(name, "w") as file:
         file.write(code)
      files.append(name)
   
   def __init__(self, name: str, code: str) -> None:
      self.name = name +   ".html"
      self.code = code

      if self.name in files:
           if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
              self.__create(self.name, self.code)
      else:
         self.__create(self.name, self.code)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)

class CreateCSS:
   cont = 0

   def __create(self, name, code):
      with open(name, "w") as file:
         file.write(code)
      files.append(name)
   
   def __init__(self, name: str, code: str) -> None:
      self.name = name +   ".css"
      self.code = code

      if self.name in files:
           if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
              self.__create(self.name, self.code)
      else:
         self.__create(self.name, self.code)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)

   def show(self):
       print(self.code)

class CreateJS:
   cont = 0

   def __create(self, name, code):
      with open(name, "w") as file:
         file.write(code)
      files.append(name)
   
   def __init__(self, name: str, code: str) -> None:
      self.name = name +   ".js"
      self.code = code

      if self.name in files:
           if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
              self.__create(self.name, self.code)
      else:
         self.__create(self.name, self.code)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)

class CreateJava:
   cont = 0

   def __create(self, name, code):
      with open(name, "w") as file:
         file.write(code)
      files.append(name)
   
   def __init__(self, name: str, code: str) -> None:
      self.name = name +   ".java"
      self.code = code

      if self.name in files:
           if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
              self.__create(self.name, self.code)
      else:
         self.__create(self.name, self.code)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)

class CreateC:
   cont = 0

   def __create(self, name, code):
      with open(name, "w") as file:
         file.write(code)
      files.append(name)
   
   def __init__(self, name: str, code: str) -> None:
      self.name = name +   ".c"
      self.code = code

      if self.name in files:
           if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
              self.__create(self.name, self.code)
      else:
         self.__create(self.name, self.code)

   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)

class CreateCMM:
   cont = 0

   def __create(self, name, code):
      with open(name, "w") as file:
         file.write(code)
      files.append(name)
   
   def __init__(self, name: str, code: str) -> None:
      self.name = name +   ".c++"
      self.code = code

      if self.name in files:
           if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
              self.__create(self.name, self.code)
      else:
         self.__create(self.name, self.code)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)

class CreateCSharp:
   cont = 0

   def __create(self, name, code):
      with open(name, "w") as file:
         file.write(code)
      files.append(name)
   
   def __init__(self, name: str, code: str) -> None:
      self.name = name +   ".cs"
      self.code = code

      if self.name in files:
           if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
              self.__create(self.name, self.code)
      else:
         self.__create(self.name, self.code)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)

class CreatePython:
   cont = 0

   def __create(self, name, code):
      with open(name, "w") as file:
         file.write(code)
      files.append(name)
   
   def __init__(self, name: str, code: str) -> None:
      self.name = name +   ".py"
      self.code = code

      if self.name in files:
           if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
              self.__create(self.name, self.code)
      else:
         self.__create(self.name, self.code)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)

class CreateTXT:
   cont = 0

   def __create(self, name, code):
      with open(name, "w") as file:
         file.write(code)
      files.append(name)
   
   def __init__(self, name: str, code: str) -> None:
      self.name = name +   ".txt"
      self.code = code

      if self.name in files:
           if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
              self.__create(self.name, self.code)
      else:
         self.__create(self.name, self.code)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)