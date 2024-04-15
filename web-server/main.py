import store
from fastapi import FastAPI

app = FastAPI()



def run():
    store.get_categories()

if __name__ == "__main__":
    run()