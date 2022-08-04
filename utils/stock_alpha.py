import json
import yfinance
import requests


def result_stock(stock_name: str, information: str) -> any:
    if not information:
        information = 'info'
    try:
        return eval(f'yfinance.Ticker("{stock_name}").{information}')
    except Exception as e:
        print(e)
        return e
