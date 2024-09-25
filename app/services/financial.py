from app.services.consume_api import get_financial_data
import pandas as pd

def fetch_financial_data(symbol: str, interval: str) -> pd.DataFrame:
    # Lógica para obtener los datos financieros de la API
    financial_data = get_financial_data(symbol, interval)
    return financial_data
