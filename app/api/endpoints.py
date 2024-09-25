from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.financial import fetch_financial_data
from app.services.notebook import lineal_regresion


router = APIRouter()

@router.post("/result_lineal_regresion/")
async def result_lineal_regresion():
    try:
        symbol = 'IBM'
        interval = '5min'
        # Llamar al servicio para obtener los datos financieros
        financial_data = fetch_financial_data(symbol, interval)
        # data = financial_data.to_dict(orient="records")
        lin_reg_rmse, lin_reg_preds = lineal_regresion(financial_data)
        return JSONResponse(
            status_code=200,
            content={"result": {"lin_reg_rmse": lin_reg_rmse, "lin_reg_preds": lin_reg_preds.tolist()}}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"success": False, "error": str(e)}
        )