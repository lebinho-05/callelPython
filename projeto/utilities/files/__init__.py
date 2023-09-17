r"""files é uma biblioteca python feita para criar arquivos
exemplo:
   import files

   fileCSV = files.CreateCSV("meu csv",
   [
      ["nome", "idade"],
      ["fulano de tal", 13]
   ]
   )

   # também pode se usar strings

   fileCSV2 = files.CreateCSV("meu csv 2", "nome,idader\nfulano de tal,13", tp = str)
"""

from .create import *
from .load import *
from os import listdir

files = listdir()
VERSION = "1.0"