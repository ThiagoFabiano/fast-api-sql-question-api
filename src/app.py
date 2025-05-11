from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.database.vanna_client import MyVanna, get_schema
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Configura o cliente Vanna com informações da API do .env
api_key = os.getenv("API_KEY")
model_name = os.getenv("MODEL_NAME")

vn = MyVanna(config={
    'print_prompt': False, 
    'print_sql': False,
    'api_key': api_key,
    'model_name': model_name
})

# Conecta ao banco usando os componentes individuais do .env
vn.connect_to_postgres(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

schema = get_schema(vn.db_url)

vn.train(ddl=schema)
vn.train(documentation="O script SQL define um banco de dados relacional para um sistema de pedidos. A tabela categories armazena os tipos de produtos, enquanto products registra os produtos com preços, estoque e categoria associada. A tabela customers guarda informações dos clientes. A tabela orders registra os pedidos feitos por clientes, e order_items detalha os produtos incluídos em cada pedido, com quantidade e preço. O script também inclui alguns dados de exemplo em cada tabela.")

## PQ
vn.train(sql="""SELECT 
    c.name AS cliente,
    o.order_date AS data_pedido,
    p.name AS produto,
    oi.quantity AS quantidade,
    oi.price AS preco_unitario,
    (oi.quantity * oi.price) AS total_item
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p ON oi.product_id = p.id
    ORDER BY o.id, oi.id;""")

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