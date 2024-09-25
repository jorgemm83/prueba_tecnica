from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.metrics import mean_squared_error

def remove_outliers(data, columns):
    for col in columns:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]
    return data

 
def lineal_regresion(data):
    # Convertir el índice a formato de fecha
    data['date'] = pd.to_datetime(data.index)
    data = data.reset_index(drop=True) #Resets the index and drops the old index
    data = data.sort_values('date') #Sorts the values by date
    data = data[['date', 'open', 'high', 'low', 'close', 'volume']] #Reorders the columns so 'date' is first
    data.head()
    
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(data[['open', 'high', 'low', 'close', 'volume']])
    # Crear un nuevo DataFrame con las características escaladas
    df_scaled = pd.DataFrame(scaled_features, columns=['open', 'high', 'low', 'close', 'volume'])
    df_scaled['date'] = data['date']  # Mantener la columna de fecha intacta
    
     # Generación de nuevas características
    data['price_range'] = data['high'] - data['low']  # Rango de precios
    data['daily_change_pct'] = (data['close'] / data['open'] - 1) * 100  # Cambio porcentual diario
    
    df_cleaned = remove_outliers(data, ['open', 'high', 'low', 'close'])
    
    df=df_cleaned
    X = df[['open', 'high', 'low', 'volume','price_range','daily_change_pct']]
    y = df['close']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    
    # Regresión Lineal
    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)

    # Predicciones
    lin_reg_preds = lin_reg.predict(X_test)

    # Evaluación
    lin_reg_rmse = np.sqrt(mean_squared_error(y_test, lin_reg_preds))
    print(f'Linear Regression RMSE: {lin_reg_rmse}')
    return lin_reg_rmse, lin_reg_preds
