from fastapi import FastAPI
import components.authentication as auth

app = FastAPI()

@app.post('/auth/reg') #register user in database
def register():
    return auth.register()

@app.post('/auth/log') #create token after auth ; for user and provide
def login(data : dict):
    return {"token" : auth.login(data)}


@app.post('/auth/logout') #store data of log out time for monitoring purposes
def logout(data : dict):
    return auth.logout()

@app.post('/auth/info') # look for user data information
def userInfo(data : dict):
    return auth.userInfo(data)