import json
inputt = '[ { "name" : "Gamda", "id" : "GGD", "email" : "nope"} , { "name" : "kanao" , "id" :"DFSD" , "email" : "nope"}]'
info = json.loads(inputt)
print(info , type(info))
