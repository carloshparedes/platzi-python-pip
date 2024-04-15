import store
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_list():
    return ["item1", "item2", "item3"]

@app.get("/contact")
def get_list():
    return [{"name" : "Platzi"}, "contact1", "contact2", "contact3"]


def run():
    store.get_categories()

if __name__ == "__main__":
    run()