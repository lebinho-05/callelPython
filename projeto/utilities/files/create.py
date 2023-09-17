from .__init__ import files

def create(self, name, code, apn):
      with open(name, "w") as file:
         file.write(code)
      
      if apn:
         files.append(name)

class CreateCSV:
    cont = 0

    def __create(self, name, p, tp, apn):
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

      if apn:
         files.append(name)

    def __init__(self, name: str, p: list, tp = list, apn = True) -> None:
        import pandas as pd
        self.cont += 1
        self.tp = tp
        self.name = name +   ".csv"
        self.p = p
        if self.name in files:
           if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
              self.__create(self.name, self.p, self.tp)
        else:
            self.__create(self.name, self.p, self.tp)
         
        self.tabela = pd.read_csv(self.name)
   
    def clear(self):
      self.p = ''
   
    def save(self):
       with open(self.name, "w") as file:
          file.write(self.code)

    def show(self):
       print(self.tabela)

    def saveto(self, name_file):
       name_file += ".csv"
       self.__create(name_file, self.p, self.tp)

class CreateJSON:
   cont = 0

   __create = create
   
   def __init__(self, name: str, code: str, p = True, apn = True) -> None:
      from json import load
      self.load = load
      self.name = name +   ".json"
      self.code = code

      if self.name in files:
           if p:
            if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
               self.__create(self.name, self.code, apn)
      else:
         self.__create(self.name, self.code, apn)
      
      with open(self.name) as fiJson:
         self.arq = self.load(fiJson)
            
      
      
      class get:
         nonlocal self
         def __getitem__(i, item):
            return self.arq[item]
      
      class set:
         nonlocal self
         def __setitem__(i, ):...
      
      self.get = get()
      self.set = set()
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)
   
   def saveto(self, name_file):
       name_file += ".json"
       self.__create(name_file, self.code)

   def replace(self, r, n): ...

class CreateOther:
   cont = 0

   def __create(self, name, code):
      with open(name, "w") as fi:
         fi.write(code)
      files.append(name)

   def __init__(self, name, code, apn = True, p = True):
      self.cont += 1
      self.name = name; self.code = code
      if p:
         if self.name in files:
            if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
               self.__create(self.name, self.code, apn)
      else:
         self.__create(self.name, self.code, apn)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)
   
   def saveto(self, name_file):
       self.__create(name_file, self.code)

class CreateHTML:
   cont = 0

   __create = create
   
   def __init__(self, name: str, code: str, apn = True, p = True) -> None:
      self.name = name +   ".html"
      self.code = code

      if p:
         if self.name in files:
            if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
               self.__create(self.name, self.code, apn)
      else:
         self.__create(self.name, self.code, apn)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)
   
   def saveto(self, name_file):
       name_file += ".html"
       self.__create(name_file, self.code)

class CreateCSS:
   cont = 0

   __create = create
   
   def __init__(self, name: str, code: str, apn = True, p = True) -> None:
      self.name = name +   ".css"
      self.code = code

      if p:
         if self.name in files:
            if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
               self.__create(self.name, self.code, apn)
      else:
         self.__create(self.name, self.code, apn)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)

   def show(self):
       print(self.code)

   def saveto(self, name_file):
       name_file += ".css"
       self.__create(name_file, self.code)

class CreateJS:
   cont = 0

   __create = create
   
   def __init__(self, name: str, code: str, apn = True, p = True) -> None:
      self.name = name +   ".js"
      self.code = code

      if p:
         if self.name in files:
            if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
               self.__create(self.name, self.code, apn)
      else:
         self.__create(self.name, self.code, apn)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)
   
   def saveto(self, name_file):
       name_file += ".js"
       self.__create(name_file, self.code)

class CreateJava:
   cont = 0

   __create = create
   
   def __init__(self, name: str, code: str, apn = True, p = True) -> None:
      self.name = name +   ".java"
      self.code = code

      if p:
         if self.name in files:
            if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
               self.__create(self.name, self.code, apn)
      else:
         self.__create(self.name, self.code, apn)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)
   
   def saveto(self, name_file):
       name_file += ".java"
       self.__create(name_file, self.code)

class CreateC:
   cont = 0

   __create = create
   
   def __init__(self, name: str, code: str, apn = True, p = True) -> None:
      self.name = name +   ".c"
      self.code = code

      if p:
         if self.name in files:
            if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
               self.__create(self.name, self.code, apn)
      else:
         self.__create(self.name, self.code, apn)

   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)
      
   def saveto(self, name_file):
       name_file += ".c"
       self.__create(name_file, self.code)

class CreateCMM:
   cont = 0

   __create = create
   
   def __init__(self, name: str, code: str, apn = True, p = True) -> None:
      self.name = name +   ".c++"
      self.code = code

      if p:
         if self.name in files:
            if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
               self.__create(self.name, self.code, apn)
      else:
         self.__create(self.name, self.code, apn)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)
   
   def saveto(self, name_file):
       name_file += ".c++"
       self.__create(name_file, self.code)

class CreateCSharp:
   cont = 0

   __create = create
   
   def __init__(self, name: str, code: str, apn = True, p = True) -> None:
      self.name = name +   ".cs"
      self.code = code

      if p:
         if self.name in files:
            if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
               self.__create(self.name, self.code, apn)
      else:
         self.__create(self.name, self.code, apn)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)
   
   def saveto(self, name_file):
       name_file += ".cs"
       self.__create(name_file, self.code)

class CreatePython:
   cont = 0

   __create = create
   
   def __init__(self, name: str, code: str, apn = True, p = True) -> None:
      self.name = name +   ".py"
      self.code = code

      if p:
         if self.name in files:
            if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
               self.__create(self.name, self.code, apn)
      else:
         self.__create(self.name, self.code, apn)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)
   
   def saveto(self, name_file):
       name_file += ".py"
       self.__create(name_file, self.code)

class CreateTXT:
   cont = 0

   __create = create
   
   def __init__(self, name: str, code: str, apn = True, p = True) -> None:
      self.name = name +   ".txt"
      self.code = code

      if p:
         if self.name in files:
            if (input(f"O arquivo {self.name} já existe. Deseja substituilo?").upper())[0] == "S":
               self.__create(self.name, self.code, apn)
      else:
         self.__create(self.name, self.code, apn)
   
   def clear(self):
      self.code = ''
   
   def save(self):
      with open(self.name, "w") as file:
         file.write(self.code)
   
   def show(self):
       print(self.code)
   
   def saveto(self, name_file):
       name_file += ".txt"
       self.__create(name_file, self.code)