import pandas
from serializer_demo.thriftify.thrift_dow_jones import DowJonesThrift

def main():
    dow_jones_data=pandas.read_csv(filepath_or_buffer="resources/dow_jones_index.data", sep=',')
    thriftify = DowJonesThrift()
    dow_jones_data.apply(thriftify.create_thrift_message,axis=1)

    result = thriftify.serialize_message()

    print(result)

if __name__=="__main__":
    main()