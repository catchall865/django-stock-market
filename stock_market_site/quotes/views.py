from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stock
from .forms import StockForm

def home(request):
    import requests
    import json 

    BASE_URL = 'http://http://api.marketstack.com/v1/tickers/'
    MY_KEY = 'a13b15c59033cc1a9aed4a6d4c3d8618'
    
    params = {
        'access_key': MY_KEY,
        'limit': '1'
    }

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_result = requests.get(f'http://api.marketstack.com/v1/tickers/{ticker}/eod', params)

        try:
            api = json.loads(api_result.content)
            print(api)
        except Exception as e:
            api = 'Error'
        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': 'Enter a ticker symbol above'})


def add_stock(request):
    import requests
    import json

    BASE_URL = 'http://http://api.marketstack.com/v1/tickers/aapl/eod'
    MY_KEY = 'a13b15c59033cc1a9aed4a6d4c3d8618'

    params = {
        'access_key': MY_KEY,
        'limit': '1'
    }

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Stock has been added'))
            return redirect('add_stock')
        else:
            messages.error(request, 'Looks like your ticker symbol was incorrect. Please try again.')
            return redirect(add_stock)
    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_result = requests.get(f'http://api.marketstack.com/v1/tickers/{str(ticker_item)}/eod', params)
            try:
                api = json.loads(api_result.content)
                output.append(api)
            except Exception as e:
                api = 'Error'

        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ('Stock has been deleted.'))
    return redirect(delete_stock)

def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker})


# Create your views here.
