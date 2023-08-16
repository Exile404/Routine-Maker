
from Backend.mystery import Routine
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/process")
async def process_data(request: Request):
    form_data = await request.form()
    user_inputs = [form_data.get(f"input{i}") for i in range(1, 5)]
    print(user_inputs)
    send = []
    for i in user_inputs:
        if i != 'N/A':
            send.append(i)
    send.sort()
    with Routine() as Bot:
        Bot.land_first_page()
        result= Bot.get_info(send)

    return templates.TemplateResponse("results.html", {"request": request, "result": result})

