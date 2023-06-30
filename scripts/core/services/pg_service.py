from fastapi import Request, APIRouter
# from fastapi import FastAPI, Request
from scripts.core.handlers.pg_handler import signup_3, delete_1, login_3, triplesharing, doublesharing, single, \
    welcome, \
    find_all_customers_details, customers_signup0, customers_signup1, customers_signup2, customers_signup3, \
    customers_login, customers_delete, room_update_page, pg_update_page
from scripts.constants.app_constant import pg

app_router = APIRouter()


@app_router.get(pg.singlesharing)
async def function(request: Request):
    try:
        return await signup_3(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.get(pg.delete)
async def function(request: Request):
    try:
        return await delete_1(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.get("/")
async def function(request: Request):
    try:
        return await login_3(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.get(pg.triplesharing)
async def function(request: Request):
    try:
        return await triplesharing(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.get(pg.doublesharing)
async def function(request: Request):
    try:
        return await doublesharing(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.get(pg.singlesharingwelocome)
async def function(request: Request):
    try:
        return await single(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.get(pg.welcome)
async def function(request: Request):
    try:
        return await welcome(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.get(pg.roomupdate)
async def emp_update(request: Request):
    try:
        return await room_update_page(request)
    except Exception as e:
        return {"Error:", str(e)}


@app_router.post(pg.customerdetails)
async def function(request: Request):
    try:
        return await find_all_customers_details(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.post("/customers_signup0")
async def function_demo(request: Request):
    try:
        return await customers_signup0(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.post(pg.triplesharingbooking)
async def function(request: Request):
    try:
        return await customers_signup1(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.post(pg.doublesharingbooking)
async def function(request: Request):
    try:
        return await customers_signup2(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.post(pg.singlesharingbooking)
async def function(request: Request):
    try:
        return await customers_signup3(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.post(pg.userlogin)
async def function(request: Request):
    try:
        return await customers_login(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.post(pg.roomupdate)
async def pg_update(request: Request):
    try:
        return await pg_update_page(request)
    except Exception as e:
        return {"Error:", str(e)}


@app_router.post(pg.delete)
async def function(request: Request):
    try:
        return await customers_delete(request)
    except Exception as e:
        return {"Error": str(e)}
