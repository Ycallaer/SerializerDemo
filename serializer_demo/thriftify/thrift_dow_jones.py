from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport

from dow_jones_index_thrift.ttypes import DowJonesIndex, DowJonesOutput

class DowJonesThrift():
    def __init__(self):
        DowJonesOutput=[]

    def create_thrift_message(self,row):
        msg = DowJonesIndex()
        msg.quarter = row['quarter']
        msg.stock = row['stock']
        msg.date = row['date']
        msg.open = row['open']
        msg.high = row['high']
        msg.low = row['low']
        msg.quarter = row['quarter']
        msg.quarter = row['quarter']
        msg.quarter = row['quarter']

        print("go")
    def serialize_message(self, thrift_msg):
        thrift_out = TTransport.TMemoryBuffer()
        protocol_out = TBinaryProtocol.TBinaryProtocol(thrift_out)
        thrift_msg.write(protocol_out)
        return thrift_out.getvalue()