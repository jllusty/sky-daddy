#
# Autogenerated by Thrift Compiler (0.16.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:dynamic
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol.TBase import TBase, TFrozenBase, TExceptionBase, TFrozenExceptionBase, TTransport
all_structs = []


class Iface(object):
    def methodThatThrowsAnException(self):
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def methodThatThrowsAnException(self):
        self.send_methodThatThrowsAnException()
        self.recv_methodThatThrowsAnException()

    def send_methodThatThrowsAnException(self):
        self._oprot.writeMessageBegin('methodThatThrowsAnException', TMessageType.CALL, self._seqid)
        args = methodThatThrowsAnException_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_methodThatThrowsAnException(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = methodThatThrowsAnException_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.xwamap is not None:
            raise result.xwamap
        return


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["methodThatThrowsAnException"] = Processor.process_methodThatThrowsAnException
        self._on_message_begin = None

    def on_message_begin(self, func):
        self._on_message_begin = func

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if self._on_message_begin:
            self._on_message_begin(name, type, seqid)
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_methodThatThrowsAnException(self, seqid, iprot, oprot):
        args = methodThatThrowsAnException_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = methodThatThrowsAnException_result()
        try:
            self._handler.methodThatThrowsAnException()
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ExceptionWithAMap as xwamap:
            msg_type = TMessageType.REPLY
            result.xwamap = xwamap
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("methodThatThrowsAnException", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class methodThatThrowsAnException_args(TBase):


    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(methodThatThrowsAnException_args)
methodThatThrowsAnException_args.thrift_spec = (
)


class methodThatThrowsAnException_result(TBase):
    """
    Attributes:
     - xwamap

    """


    def __init__(self, xwamap=None,):
        self.xwamap = xwamap

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(methodThatThrowsAnException_result)
methodThatThrowsAnException_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'xwamap', [ExceptionWithAMap, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs
