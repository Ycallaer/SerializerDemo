from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport

from dow_jones_index_thrift.ttypes import DowJonesIndex, DowJonesResult, DowJonesOutput

class DowJonesThrift():
    def __init__(self):
        self.thrift_result=None
        #First level
        self.thrift_result=DowJonesOutput()
        #second level
        self.result=DowJonesResult()
        self.result.dowjonesresponse = []

    def create_thrift_message(self,row):
        msg = DowJonesIndex()
        msg.quarter = row['quarter']
        msg.stock = row['stock']
        msg.date = row['date']
        msg.open = row['open']
        msg.high = row['high']
        msg.low = row['low']
        msg.close = row['close']
        msg.volume = row['volume']
        msg.percent_change_price = row['percent_change_price']
        msg.percent_change_volume_over_last_wk = row['percent_change_volume_over_last_wk']
        msg.previous_weeks_volume = row['previous_weeks_volume']
        msg.next_weeks_open = row['next_weeks_open']
        msg.next_weeks_close = row['next_weeks_close']
        msg.percent_change_next_weeks_price = row['percent_change_next_weeks_price']
        msg.days_to_next_dividend = row['days_to_next_dividend']
        msg.percent_return_next_dividend = row['percent_return_next_dividend']

        print("message constructed")
        self.result.dowjonesresponse.append(msg)

    def serialize_message(self):
        thrift_out = TTransport.TMemoryBuffer()
        protocol_out = TBinaryProtocol.TBinaryProtocol(thrift_out)
        self.thrift_result.write(protocol_out)
        return thrift_out.getvalue()