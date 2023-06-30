from fastapi import Request
# from scripts.core.db.mongo_db import collection, double_share, triple_share
from schemas.models import user, Roombooking
from scripts.logging.logging import logging
from fastapi.templating import Jinja2Templates
from scripts.core.db.mongo_utility import mongo

templates = Jinja2Templates(directory="templates")


async def signup_3(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


async def delete_1(request: Request):
    return templates.TemplateResponse("deleteuser.html", {"request": request})


async def login_3(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


async def single(request: Request):
    return templates.TemplateResponse("singlesharing.html", {"request": request})


async def doublesharing(request: Request):
    return templates.TemplateResponse("doublesharing.html", {"request": request})


async def triplesharing(request: Request):
    return templates.TemplateResponse("triplesharing.html", {"request": request})


async def welcome(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})


async def room_update_page(request: Request):
    return templates.TemplateResponse("update.html", {"request": request})


async def find_all_customers_details(request: Request):
    data = await request.form()
    logging.debug('signup')
    temp = user(
        username=data["username"],
        password=data["password"],
        email=data["email"],
        phone_no=data["phone_no"],
    )
    insert = mongo.for_insert_one("Srijan_766", temp)
    if insert:
        return {"message": "Data found Successfully"}
    else:
        return {"error": "data not fount"}


async def customers_signup0(request: Request):
    data = await request.form()
    logging.debug('signup')
    temp = user(
        username=data["username"],
        password=data["password"],
        email=data["email"],
        phone_no=data["phone_no"],
    )
    result = mongo.for_insert_one("Srijan_766", temp)
    if result:
        return {"message": "Sign up page created successfully"}
    else:
        return {"none"}


async def customers_signup1(request: Request):
    data = await request.form()
    logging.debug('triplesharing')
    temp = Roombooking(
        name=data["name"],
        place=data["place"],
        number=data["number"],
    )
    result = mongo.for_insert_one("Srijan_766", temp)
    if result:
        return {"message": "triple sharing room booked successfully"}
    else:
        return {"message": "none"}


async def customers_signup2(request: Request):
    data = await request.form()
    logging.debug('doublesharing')
    temp = Roombooking(
        name=data["name"],
        place=data["place"],
        number=data["number"],
    )
    result = mongo.for_insert_one("srijan2", temp)
    if result:
        return {"message": "double sharing room booked successfully"}
    else:
        return {"none"}


async def customers_signup3(request: Request):
    data = await request.form()
    logging.debug('singlesharing')
    temp = Roombooking(
        name=data["name"],
        place=data["place"],
        number=data["number"],
    )
    result = mongo.for_insert_one("Srijan_766", temp)
    if result:
        return {"message": "single sharing room booked successfully"}
    else:
        return {"none"}


async def customers_login(request: Request):
    data = await request.form()
    logging.debug('login')
    username = data["username"]
    password = data["password"]
    find = {"username": username, "password": password}
    temp = mongo.for_find_one("Srijan_766", find)
    if temp:
        return templates.TemplateResponse("welcomepage.html", {"request": request})
    else:
        return {"error": "Login failed,username or password is wrong!!"}


async def pg_update_page(request: Request):
    update = await request.form()
    user = update.get("username")
    new_roomtype = update.get("new_roomtype")
    update = {"username": user}
    set = {"$set": {"roomtype": new_roomtype}}
    result = mongo.for_update_one("Srijan_766", update, set)
    if result:
        logging.debug("updated information done")
        return {"Updated"}
    else:
        return {"not updated"}


async def customers_delete(request: Request):
    data = await request.form()
    username = data["username"]
    password = data["password"],
    find = {"username": username, "password": password}
    temp = mongo.for_find_one("Srijan_766", find)
    if temp:
        delete = {"username": username}
        mongo.for_delete_one("Srijan_766", delete)
        return {"message: successfully deleted "}
    else:
        return {"message: not deleted"}
