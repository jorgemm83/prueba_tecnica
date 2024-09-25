from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.financial import fetch_financial_data

router = APIRouter()

@router.post("/result_model/")
async def result_model():
    try:
        symbol = 'IBM'
        interval = '5min'
        # Llamar al servicio para obtener los datos financieros
        financial_data = fetch_financial_data(symbol, interval)
        data = financial_data.to_dict(orient="records")
        
        return JSONResponse(
            status_code=200,
            content={"result": data}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"success": False, "error": str(e)}
        )
