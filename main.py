from fastapi import FastAPI


app = FastAPI()

@app.get('/') #decorate
def index():
    return {'data':{'name': 'Remon'}} 


@app.get('/about')  
def about():
    return {'data':{'about page'}}