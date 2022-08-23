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
    def Janky(self, arg):
        """
        Parameters:
         - arg

        """
        pass

    def voidMethod(self):
        pass

    def primitiveMethod(self):
        pass

    def structMethod(self):
        pass

    def methodWithDefaultArgs(self, something):
        """
        Parameters:
         - something

        """
        pass

    def onewayMethod(self):
        pass

    def declaredExceptionMethod(self, shouldThrow):
        """
        Parameters:
         - shouldThrow

        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def Janky(self, arg):
        """
        Parameters:
         - arg

        """
        self.send_Janky(arg)
        return self.recv_Janky()

    def send_Janky(self, arg):
        self._oprot.writeMessageBegin('Janky', TMessageType.CALL, self._seqid)
        args = Janky_args()
        args.arg = arg
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_Janky(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = Janky_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "Janky failed: unknown result")

    def voidMethod(self):
        self.send_voidMethod()
        self.recv_voidMethod()

    def send_voidMethod(self):
        self._oprot.writeMessageBegin('voidMethod', TMessageType.CALL, self._seqid)
        args = voidMethod_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_voidMethod(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = voidMethod_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return

    def primitiveMethod(self):
        self.send_primitiveMethod()
        return self.recv_primitiveMethod()

    def send_primitiveMethod(self):
        self._oprot.writeMessageBegin('primitiveMethod', TMessageType.CALL, self._seqid)
        args = primitiveMethod_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_primitiveMethod(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = primitiveMethod_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "primitiveMethod failed: unknown result")

    def structMethod(self):
        self.send_structMethod()
        return self.recv_structMethod()

    def send_structMethod(self):
        self._oprot.writeMessageBegin('structMethod', TMessageType.CALL, self._seqid)
        args = structMethod_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_structMethod(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = structMethod_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "structMethod failed: unknown result")

    def methodWithDefaultArgs(self, something):
        """
        Parameters:
         - something

        """
        self.send_methodWithDefaultArgs(something)
        self.recv_methodWithDefaultArgs()

    def send_methodWithDefaultArgs(self, something):
        self._oprot.writeMessageBegin('methodWithDefaultArgs', TMessageType.CALL, self._seqid)
        args = methodWithDefaultArgs_args()
        args.something = something
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_methodWithDefaultArgs(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = methodWithDefaultArgs_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return

    def onewayMethod(self):
        self.send_onewayMethod()

    def send_onewayMethod(self):
        self._oprot.writeMessageBegin('onewayMethod', TMessageType.ONEWAY, self._seqid)
        args = onewayMethod_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def declaredExceptionMethod(self, shouldThrow):
        """
        Parameters:
         - shouldThrow

        """
        self.send_declaredExceptionMethod(shouldThrow)
        return self.recv_declaredExceptionMethod()

    def send_declaredExceptionMethod(self, shouldThrow):
        self._oprot.writeMessageBegin('declaredExceptionMethod', TMessageType.CALL, self._seqid)
        args = declaredExceptionMethod_args()
        args.shouldThrow = shouldThrow
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_declaredExceptionMethod(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = declaredExceptionMethod_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.xwamap is not None:
            raise result.xwamap
        raise TApplicationException(TApplicationException.MISSING_RESULT, "declaredExceptionMethod failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["Janky"] = Processor.process_Janky
        self._processMap["voidMethod"] = Processor.process_voidMethod
        self._processMap["primitiveMethod"] = Processor.process_primitiveMethod
        self._processMap["structMethod"] = Processor.process_structMethod
        self._processMap["methodWithDefaultArgs"] = Processor.process_methodWithDefaultArgs
        self._processMap["onewayMethod"] = Processor.process_onewayMethod
        self._processMap["declaredExceptionMethod"] = Processor.process_declaredExceptionMethod
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

    def process_Janky(self, seqid, iprot, oprot):
        args = Janky_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Janky_result()
        try:
            result.success = self._handler.Janky(args.arg)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("Janky", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_voidMethod(self, seqid, iprot, oprot):
        args = voidMethod_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = voidMethod_result()
        try:
            self._handler.voidMethod()
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("voidMethod", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_primitiveMethod(self, seqid, iprot, oprot):
        args = primitiveMethod_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = primitiveMethod_result()
        try:
            result.success = self._handler.primitiveMethod()
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("primitiveMethod", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_structMethod(self, seqid, iprot, oprot):
        args = structMethod_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = structMethod_result()
        try:
            result.success = self._handler.structMethod()
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("structMethod", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_methodWithDefaultArgs(self, seqid, iprot, oprot):
        args = methodWithDefaultArgs_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = methodWithDefaultArgs_result()
        try:
            self._handler.methodWithDefaultArgs(args.something)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("methodWithDefaultArgs", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_onewayMethod(self, seqid, iprot, oprot):
        args = onewayMethod_args()
        args.read(iprot)
        iprot.readMessageEnd()
        try:
            self._handler.onewayMethod()
        except TTransport.TTransportException:
            raise
        except Exception:
            logging.exception('Exception in oneway handler')

    def process_declaredExceptionMethod(self, seqid, iprot, oprot):
        args = declaredExceptionMethod_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = declaredExceptionMethod_result()
        try:
            result.success = self._handler.declaredExceptionMethod(args.shouldThrow)
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
        oprot.writeMessageBegin("declaredExceptionMethod", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class Janky_args(TBase):
    """
    Attributes:
     - arg

    """


    def __init__(self, arg=None,):
        self.arg = arg

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Janky_args)
Janky_args.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'arg', None, None, ),  # 1
)


class Janky_result(TBase):
    """
    Attributes:
     - success

    """


    def __init__(self, success=None,):
        self.success = success

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Janky_result)
Janky_result.thrift_spec = (
    (0, TType.I32, 'success', None, None, ),  # 0
)


class voidMethod_args(TBase):


    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(voidMethod_args)
voidMethod_args.thrift_spec = (
)


class voidMethod_result(TBase):


    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(voidMethod_result)
voidMethod_result.thrift_spec = (
)


class primitiveMethod_args(TBase):


    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(primitiveMethod_args)
primitiveMethod_args.thrift_spec = (
)


class primitiveMethod_result(TBase):
    """
    Attributes:
     - success

    """


    def __init__(self, success=None,):
        self.success = success

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(primitiveMethod_result)
primitiveMethod_result.thrift_spec = (
    (0, TType.I32, 'success', None, None, ),  # 0
)


class structMethod_args(TBase):


    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(structMethod_args)
structMethod_args.thrift_spec = (
)


class structMethod_result(TBase):
    """
    Attributes:
     - success

    """


    def __init__(self, success=None,):
        self.success = success

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(structMethod_result)
structMethod_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [CompactProtoTestStruct, None], None, ),  # 0
)


class methodWithDefaultArgs_args(TBase):
    """
    Attributes:
     - something

    """


    def __init__(self, something=2,):
        self.something = something

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(methodWithDefaultArgs_args)
methodWithDefaultArgs_args.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'something', None, 2, ),  # 1
)


class methodWithDefaultArgs_result(TBase):


    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(methodWithDefaultArgs_result)
methodWithDefaultArgs_result.thrift_spec = (
)


class onewayMethod_args(TBase):


    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(onewayMethod_args)
onewayMethod_args.thrift_spec = (
)


class declaredExceptionMethod_args(TBase):
    """
    Attributes:
     - shouldThrow

    """


    def __init__(self, shouldThrow=None,):
        self.shouldThrow = shouldThrow

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(declaredExceptionMethod_args)
declaredExceptionMethod_args.thrift_spec = (
    None,  # 0
    (1, TType.BOOL, 'shouldThrow', None, None, ),  # 1
)


class declaredExceptionMethod_result(TBase):
    """
    Attributes:
     - success
     - xwamap

    """


    def __init__(self, success=None, xwamap=None,):
        self.success = success
        self.xwamap = xwamap

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(declaredExceptionMethod_result)
declaredExceptionMethod_result.thrift_spec = (
    (0, TType.BOOL, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'xwamap', [ExceptionWithAMap, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs
