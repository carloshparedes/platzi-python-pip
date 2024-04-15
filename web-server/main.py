import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return ["item1", "item2", "item3"]

@app.get("/contact", response_class=HTMLResponse)
def get_list():
    return '''
    <html>
        <head>
            <title>Platzi</title>
        </head>
        <body>
            <h1>Platzi</h1>
            <p>Contáctanos</p>
        </body>'''
[{"name" : "Platzi"}, "contact1", "contact2", "contact3"]


def run():
    store.get_categories()

if __name__ == "__main__":
    run()