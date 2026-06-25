import components.support as t

def register():
    return {"status" : "ok"}

def login(data : dict):
    token = t.encode_token(data)
    return {"token" : token, "status" : "ok"}

def logout():
    return {"status" : "ok"}

def userInfo(data : dict):
    return {"status" : "ok"}

def testing():
    return {"status" : "ok"}