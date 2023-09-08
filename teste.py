import files as f

fileCsv = f.CreateCSV("dados", 
"""
nome,idade
Callebe,9
"""
, tp = str)

fileJson = f.CreateJSON("meu json", """
{
    "nome": "Callebe"
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

get = fileJson.get()
print(get["nome"])

print(fileJson.get()["nome"])

print(f.files)