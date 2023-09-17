from .create import *
from .errors import *

@failure
def loadJSON(name, vjson = True):
   from json import load

   if vjson:
      name += ".json"

   with open(f"{name}", "r") as fi:
      arq = load(fi)
   j = CreateJSON(name, arq, p = False)
   return j