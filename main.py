import uvicorn
from fastapi import FastAPI
from scripts.core.services.pg_service import app_router
# import configparser

app = FastAPI()
app.include_router(app_router)


# config = configparser.ConfigParser()
# client = config.read(r"C:\Users\srijan.tirunagari\PycharmProjects\project structure[srijan's pg]\configuration\mongo.txt")
# path1 = config.get('MongoDB', 'client')
# path2 = config.get('MongoDB', 'db')
# path3 = config.get('MongoDB', 'collection')
# path4 = config.get('MongoDB', 'double_share')
# path5 = config.get('MongoDB', 'triple_share')
# print(path1)
# print(path2)
# print(path3)
# print(path4)
# print(path5)

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000)
