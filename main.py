# This is a sample fast api script.

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from apis import stock_api

app = FastAPI(openapi_prefix='./')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'],
                   allow_credentials=True)


@app.get('/health')
def heath_check():
    return {'success': True}


app.include_router(
    stock_api.router,
    prefix="/stock",
    tags=["Stock API", "(internal only)"],
    responses={404: {
        "message": "Not found"
    }})

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=3000)
