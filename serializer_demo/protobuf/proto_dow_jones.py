import serializer_demo.protobuf.dowjones_pb2 as djproto

class DownJonesProto():

    def __init__(self):
        self.result = djproto.DowJonesResult()
        self.messages= []

    def create_proto_msg(self, row):
        msg = djproto.DowJonesIndex()
        msg.quarter = row['quarter']
        msg.stock = row['stock']
        msg.date = row['date']
        msg.open = row['open']
        msg.high = row['high']
        msg.low = row['low']
        msg.close = row['close']
        msg.volume = row['volume']
        msg.percent_change_price = str(row['percent_change_price'])
        msg.percent_change_volume_over_last_wk = str(row['percent_change_volume_over_last_wk'])
        msg.previous_weeks_volume = str(row['previous_weeks_volume'])
        msg.next_weeks_open = str(row['next_weeks_open'])
        msg.next_weeks_close = str(row['next_weeks_close'])
        msg.percent_change_next_weeks_price = row['percent_change_next_weeks_price']
        msg.days_to_next_dividend = row['days_to_next_dividend']
        msg.percent_return_next_dividend = row['percent_return_next_dividend']

        self.messages.append(msg)

    def create_result(self):
        self.result.downjonesresponse.extend(self.messages)
        return self.result.SerializeToString()
