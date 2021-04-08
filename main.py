import pyupbit
"""
# ticker
tickers = pyupbit.get_tickers()
print(len(tickers))

tickers = pyupbit.get_tickers(fiat="KRW")
print(len(tickers))
print(tickers)

# 현재가 조회
price = pyupbit.get_current_price(tickers)
print(price)


# 과거 데이터 조회
# 시가(open), 고가(high), 저가(low), 종가(close), 거래량(volume)
for ticker in tickers[:2]:
    df = pyupbit.get_ohlcv(ticker, interval="minute")   # 월/주/일/분봉 중 하나, 일봉 디폴트
    # df = pyupbit.get_ohlcv(ticker, count=5) # 5일치
    print(ticker)
    print(df)


# 호가 조회
for ticker in tickers[:2]:
    orderbook = pyupbit.get_orderbook(ticker)
    print(orderbook)
    try:
        bids_asks = orderbook[0]['orderbook_units']

        for bid_ask in bids_asks:
            print(bid_ask)
    except Exception:
        print(f'{ticker} JSONDecodeError')
        pass



# 잔고 조회
print('잔고 조회')
access_key = "Hf5NbkaVteJNya5S7031RfhfXlMbzza1Ei0rGSYx"
secret_key = "h8LoUry0mdDnDv3xrxtK3WdXbBlVxfL9xCcNKeuf"

upbit = pyupbit.Upbit(access_key, secret_key)
print(upbit.get_balances())


"""

"""

import websockets
import asyncio
import json

async def upbit_ws_client():
    uri = "wss://api.upbit.com/websocket/v1"

    async with websockets.connect(uri) as websocket:
        subscribe_fmt = [
            {"ticket":"test"},
            {
                "type": "ticker",
                "codes":["KRW-BTC"],
                "isOnlyRealtime": True
            },
            {"format":"SIMPLE"}
        ]
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)    # 구독 신청

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            print(data)


async def main():
    await upbit_ws_client()

asyncio.run(main())



"""

