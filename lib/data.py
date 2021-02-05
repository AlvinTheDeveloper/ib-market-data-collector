import datetime

def data_preperation(bar_count, symbol,time,historical_data_dict):
    input_data = []
    columns = None

    # if idx >= len(results)-3: # 3 bars
    #     print(data)
    #bars = bar_count - 1  # bars before current bar
    # for idx, data in enumerate(historical_data_dict[symbol]):
    #     if idx > bars - 1 and idx < len(historical_data_dict[symbol]) - 1:
            # arr=[d.values() for i=idx;i>=idx-5;i--]
            # idx-6
    data = dict()
    data['symbol']=symbol
    max_close = 0
    min_close = 0
    for i in range(1,bar_count+1):
        historical_datetime = (
                    datetime.datetime.fromtimestamp(time) - datetime.timedelta(minutes=i)).strftime(
            "%Y%m%d  %H:%M:00")
        if symbol in historical_data_dict and historical_datetime in historical_data_dict[symbol]:
            bar = historical_data_dict[symbol][historical_datetime]
            print(f'bar: {bar}')
            max_close = max([max_close,bar.close])
            min_close = max([min_close,bar.close])
            if i==1:
                data['open']=bar.open
                data['high']=bar.high
                data['low']=bar.low
                data['close']=bar.close
                data['volume']=bar.volume
            else:
                data[f't{i-1}_open'] = bar.open
                data[f't{i-1}_high'] = bar.high
                data[f't{i-1}_low'] = bar.low
                data[f't{i-1}_close'] = bar.close
                data[f't{i-1}_volume'] = bar.volume

            # data['next_close'] = historical_data[symbol][idx + 1]['close']
            # totally 7 bars before target bars
            # data['actual_percentage'] = historical_data[symbol][idx + 1]['close']

    input_data.append(list(data.values()))  # [1:] removes the symbol
    columns = list(data.keys())  # [1:] removes the symbol

            # print(f'bar_num: {bar_num} length: {bar_num}')
            # print(f'columns: {columns} length: {len(columns)}')
            # print(f'data: {list(data.values())} length: {list(data.values())}')

    return input_data,max_close,min_close, columns