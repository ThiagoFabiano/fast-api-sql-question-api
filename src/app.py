from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database.vanna_client import MyVanna

app = FastAPI()
vn = MyVanna(config={'print_prompt': False, 'print_sql': False})

vn.connect_to_postgres(
    host="localhost",  
    dbname="vanna_test",  
    user="postgres",  
    password="postgres",  
    port="5432"  
)

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(question: Question):
    try:
        sql_gerado = vn.generate_sql(question.question)
        resultado = vn.run_sql(sql_gerado)
        return {"result": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))