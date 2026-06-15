# CAPM Workshop — Costo de Capital con Python

Estimación del costo de capital usando el modelo CAPM con datos reales de la Fed y Yahoo Finance.
Diseñado como workshop universitario de 4 módulos.

## Key Takeaways

1. **El costo de capital de Tesla es 20.69%** los accionistas exigen ese retorno mínimo por el riesgo que asumen.
2. **El WACC de Tesla (20.50%) es casi igual al Ke** Tesla se financia 99% con capital accionario, por lo que la deuda tiene un impacto mínimo.
3. **Todo reproducible con Python** — sin Excel, sin Bloomberg, con datos reales.

## Estructura
```bash
notebooks/
├── 01_tasa_libre_riesgo.ipynb # Módulo 1: Rf desde FRED
├── 02_prima_riesgo_mercado.ipynb # Módulo 2: Prima de riesgo del S&P 500
├── 03_beta.ipynb # Módulo 3: Beta por regresión
└── 04_capm_costo_capital.ipynb # Módulo 4: CAPM y WACC de Tesla
src/
├── db_client.py # Conexión a DB de FRED
└── yahoo_client.py # Descarga de precios
```
## Fuentes de datos
- **FRED API** — GS10 (tasa libre de riesgo)
- **Yahoo Finance** — S&P 500 y precios de acciones
## Stack
- Python 3.11
- pandas, matplotlib, scipy, yfinance, sqlalchemy
## Referencias
- Damodaran, A. — *Damodaran on Valuation*