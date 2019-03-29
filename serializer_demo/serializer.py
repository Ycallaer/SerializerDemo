import pandas
from serializer_demo.thriftify.thrift_dow_jones import DowJonesThrift
from serializer_demo.timer_function.timer_decorator import timing
from serializer_demo.protobuf.proto_dow_jones import DownJonesProto


@timing
def main_pickle(pd_df):
    pd_df.to_pickle(path='resources/dow_jones_index.pickle')


@timing
def main_thrift(pd_df):

    thriftify = DowJonesThrift()
    pd_df.apply(thriftify.create_thrift_message,axis=1)
    result = thriftify.serialize_message()


@timing
def main_protobuf(pd_df):
    protobuf = DownJonesProto()
    pd_df.apply(protobuf.create_proto_msg, axis=1)
    result = protobuf.create_result()


if __name__=="__main__":
    dow_jones_data = pandas.read_csv(filepath_or_buffer="resources/dow_jones_index.data", sep=',')
    print(main_thrift(dow_jones_data))
    print(main_pickle(dow_jones_data))
    print(main_protobuf(dow_jones_data))