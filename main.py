from fastapi import FastAPI, HTTPException
from crypt import crypt_context
from database import connect_to_mysql,create_user

#initializing FastAPI
app = FastAPI()

#declare encryption 


#Database Connection
conn = connect_to_mysql()
cursor = conn.cursor()

@app.post("/add/")
async def add_user(name: str, password: str, email: str):
    encrypt_pass = crypt_context.encrypt(password)
    user_id = create_user(name, encrypt_pass, email)
    if user_id:
        return {"id": user_id, "name": name, "password": password, "email": email}
    else:
        raise HTTPException(status_code=400, detail="User not created")
    
@app.post("/verify/")
async def verify_user(email: str):
    user = verify_user(email)
    return user



