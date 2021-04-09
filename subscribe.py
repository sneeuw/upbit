from pyupbit import WebSocketManager


def goes_up_change_rate(prev_data, rt_data):
    if prev_data['change'] == 'RISE' and rt_data['change'] == 'RISE':
        if prev_data['change_price'] < rt_data['change_price']:
            print(rt_data['code'], rt_data['trade_price'], rt_data['change_price'] - prev_data['change_price'])


def run(ticker):
    wm = WebSocketManager("ticker", [ticker])
    prev_data = {'change': '-'}
    while True:
        data = wm.get()
        goes_up_change_rate(prev_data, data)
        prev_data = data
    wm.terminate()


if __name__ == "__main__":
    for ticker in ["KRW-XRP", "KRW-BTC", "KRW-PCI"]:
        run(ticker)
