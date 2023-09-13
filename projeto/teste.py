import files as f
from json import load

f.files = []

fileCsv = f.CreateCSV("dados", 
"nome,idade\nCallebe,9"
, tp = str)

fileJson = f.CreateJSON("meu json", """
{
    "pessoa1":{
        "nome":"Callebe",
        "idade": 9
    }
}
""")

fileJson2 = f.CreateJSON("meu json", """
{
    "teste": "conteúdo da chave teste"
}
""")

fileExper = f.CreateOther("meu exper.exper", "print('oi')")

fileHtml = f.CreateHTML("index", "<html>oi</html>")

fileHtml.show()
fileHtml.clear()
fileHtml.save()
fileHtml.show()

fileCsv.show()

get = fileJson.get
print(get["pessoa1"]["nome"])

print(fileJson.get["pessoa1"]["nome"])

print(f.CreateJSON.cont)

print(f.files)