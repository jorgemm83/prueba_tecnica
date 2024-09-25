from fastapi.responses import JSONResponse

def success_response(data, status_code=200):
    return JSONResponse(
        status_code=status_code,
        content={"result": data}
    )

def error_response(error_message, status_code=500):
    return JSONResponse(
        status_code=status_code,
        content={"success": False, "error": error_message}
    )
