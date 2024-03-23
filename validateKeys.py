from flask import  request, jsonify
def validateKeysPost(chain,msg,request):#funcion que valida que esas llave existan llaves
    if not all(key in request.json for key in chain):
        return jsonify({msg}), 400
    else:
        return False
    
    