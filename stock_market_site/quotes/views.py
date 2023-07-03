from django.shortcuts import render


def home(request):
    import requests
    import json 

    BASE_URL = 'http://http://api.marketstack.com/v1/tickers/aapl/eod'
    MY_KEY = 'a13b15c59033cc1a9aed4a6d4c3d8618'
    
    params = {
        'access_key': MY_KEY,
        'limit': '10'
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



    



def about(request):
    return render(request, 'about.html', {})

# Create your views here.
