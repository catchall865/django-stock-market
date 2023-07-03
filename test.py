api = {
  'pagination': {
    'limit': 1,
    'offset': 0,
    'count': 1,
    'total': 250
  },
  'data': {
    'name': 'Apple Inc',
    'symbol': 'AAPL',
    'country': None,
    'has_intraday': False,
    'has_eod': True,
    'eod': [
      {
        'open': 191.63,
        'high': 194.48,
        'low': 191.26,
        'close': 193.97,
        'volume': 85069600.0,
        'adj_high': 194.48,
        'adj_low': 191.26,
        'adj_close': 193.97,
        'adj_open': 191.63,
        'adj_volume': 85213216.0,
        'split_factor': 1.0,
        'dividend': 0.0,
        'symbol': 'AAPL',
        'exchange': 'XNAS',
        'date': '2023-06-30T00:00:00+0000'
      }
    ]
  }
}

closing = api['data']['eod'][0]['close']

print(closing)

