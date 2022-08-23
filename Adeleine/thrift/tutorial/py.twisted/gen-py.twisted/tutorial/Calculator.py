#
# Autogenerated by Thrift Compiler (0.16.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:twisted
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import shared.SharedService
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from zope.interface import Interface, implementer
from twisted.internet import defer
from thrift.transport import TTwisted
all_structs = []


class Iface(shared.SharedService.Iface):
    """
    Ahh, now onto the cool part, defining a service. Services just need a name
    and can optionally inherit from another service using the extends keyword.

    """
    def ping():
        """
        A method definition looks like C code. It has a return type, arguments,
        and optionally a list of exceptions that it may throw. Note that argument
        lists and exception lists are specified using the exact same syntax as
        field lists in struct or exception definitions.

        """
        pass

    def add(num1, num2):
        """
        Parameters:
         - num1
         - num2

        """
        pass

    def calculate(logid, w):
        """
        Parameters:
         - logid
         - w

        """
        pass

    def zip():
        """
        This method has a oneway modifier. That means the client only makes
        a request and does not listen for any response at all. Oneway methods
        must be void.

        """
        pass


@implementer(Iface)
class Client(shared.SharedService.Client):

    """
    Ahh, now onto the cool part, defining a service. Services just need a name
    and can optionally inherit from another service using the extends keyword.

    """
    def __init__(self, transport, oprot_factory):
        shared.SharedService.Client.__init__(self, transport, oprot_factory)

    def ping(self):
        """
        A method definition looks like C code. It has a return type, arguments,
        and optionally a list of exceptions that it may throw. Note that argument
        lists and exception lists are specified using the exact same syntax as
        field lists in struct or exception definitions.

        """
        seqid = self._seqid = self._seqid + 1
        self._reqs[seqid] = defer.Deferred()

        d = defer.maybeDeferred(self.send_ping)
        d.addCallbacks(
            callback=self.cb_send_ping,
            callbackArgs=(seqid,),
            errback=self.eb_send_ping,
            errbackArgs=(seqid,))
        return d

    def cb_send_ping(self, _, seqid):
        return self._reqs[seqid]

    def eb_send_ping(self, f, seqid):
        d = self._reqs.pop(seqid)
        d.errback(f)
        return d

    def send_ping(self):
        oprot = self._oprot_factory.getProtocol(self._transport)
        oprot.writeMessageBegin('ping', TMessageType.CALL, self._seqid)
        args = ping_args()
        args.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def recv_ping(self, iprot, mtype, rseqid):
        d = self._reqs.pop(rseqid)
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            return d.errback(x)
        result = ping_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return d.callback(None)

    def add(self, num1, num2):
        """
        Parameters:
         - num1
         - num2

        """
        seqid = self._seqid = self._seqid + 1
        self._reqs[seqid] = defer.Deferred()

        d = defer.maybeDeferred(self.send_add, num1, num2)
        d.addCallbacks(
            callback=self.cb_send_add,
            callbackArgs=(seqid,),
            errback=self.eb_send_add,
            errbackArgs=(seqid,))
        return d

    def cb_send_add(self, _, seqid):
        return self._reqs[seqid]

    def eb_send_add(self, f, seqid):
        d = self._reqs.pop(seqid)
        d.errback(f)
        return d

    def send_add(self, num1, num2):
        oprot = self._oprot_factory.getProtocol(self._transport)
        oprot.writeMessageBegin('add', TMessageType.CALL, self._seqid)
        args = add_args()
        args.num1 = num1
        args.num2 = num2
        args.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def recv_add(self, iprot, mtype, rseqid):
        d = self._reqs.pop(rseqid)
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            return d.errback(x)
        result = add_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return d.callback(result.success)
        return d.errback(TApplicationException(TApplicationException.MISSING_RESULT, "add failed: unknown result"))

    def calculate(self, logid, w):
        """
        Parameters:
         - logid
         - w

        """
        seqid = self._seqid = self._seqid + 1
        self._reqs[seqid] = defer.Deferred()

        d = defer.maybeDeferred(self.send_calculate, logid, w)
        d.addCallbacks(
            callback=self.cb_send_calculate,
            callbackArgs=(seqid,),
            errback=self.eb_send_calculate,
            errbackArgs=(seqid,))
        return d

    def cb_send_calculate(self, _, seqid):
        return self._reqs[seqid]

    def eb_send_calculate(self, f, seqid):
        d = self._reqs.pop(seqid)
        d.errback(f)
        return d

    def send_calculate(self, logid, w):
        oprot = self._oprot_factory.getProtocol(self._transport)
        oprot.writeMessageBegin('calculate', TMessageType.CALL, self._seqid)
        args = calculate_args()
        args.logid = logid
        args.w = w
        args.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def recv_calculate(self, iprot, mtype, rseqid):
        d = self._reqs.pop(rseqid)
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            return d.errback(x)
        result = calculate_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return d.callback(result.success)
        if result.ouch is not None:
            return d.errback(result.ouch)
        return d.errback(TApplicationException(TApplicationException.MISSING_RESULT, "calculate failed: unknown result"))

    def zip(self):
        """
        This method has a oneway modifier. That means the client only makes
        a request and does not listen for any response at all. Oneway methods
        must be void.

        """
        seqid = self._seqid = self._seqid + 1
        self._reqs[seqid] = defer.Deferred()

        d = defer.maybeDeferred(self.send_zip)
        d.addCallbacks(
            callback=self.cb_send_zip,
            callbackArgs=(seqid,),
            errback=self.eb_send_zip,
            errbackArgs=(seqid,))
        return d

    def cb_send_zip(self, _, seqid):
        d = self._reqs.pop(seqid)
        d.callback(None)
        return d

    def eb_send_zip(self, f, seqid):
        d = self._reqs.pop(seqid)
        d.errback(f)
        return d

    def send_zip(self):
        oprot = self._oprot_factory.getProtocol(self._transport)
        oprot.writeMessageBegin('zip', TMessageType.ONEWAY, self._seqid)
        args = zip_args()
        args.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()


@implementer(Iface)
class Processor(shared.SharedService.Processor, TProcessor):
    def __init__(self, handler):
        shared.SharedService.Processor.__init__(self, Iface(handler))
        self._processMap["ping"] = Processor.process_ping
        self._processMap["add"] = Processor.process_add
        self._processMap["calculate"] = Processor.process_calculate
        self._processMap["zip"] = Processor.process_zip
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
            return defer.succeed(None)
        else:
            return self._processMap[name](self, seqid, iprot, oprot)

    def process_ping(self, seqid, iprot, oprot):
        args = ping_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ping_result()
        d = defer.maybeDeferred(self._handler.ping, )
        d.addCallback(self.write_results_success_ping, result, seqid, oprot)
        d.addErrback(self.write_results_exception_ping, result, seqid, oprot)
        return d

    def write_results_success_ping(self, success, result, seqid, oprot):
        oprot.writeMessageBegin("ping", TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def write_results_exception_ping(self, error, result, seqid, oprot):
        msg_type = TMessageType.REPLY
        try:
            error.raiseException()
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
        oprot.writeMessageBegin("ping", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_add(self, seqid, iprot, oprot):
        args = add_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = add_result()
        d = defer.maybeDeferred(self._handler.add, args.num1, args.num2)
        d.addCallback(self.write_results_success_add, result, seqid, oprot)
        d.addErrback(self.write_results_exception_add, result, seqid, oprot)
        return d

    def write_results_success_add(self, success, result, seqid, oprot):
        result.success = success
        oprot.writeMessageBegin("add", TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def write_results_exception_add(self, error, result, seqid, oprot):
        msg_type = TMessageType.REPLY
        try:
            error.raiseException()
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
        oprot.writeMessageBegin("add", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_calculate(self, seqid, iprot, oprot):
        args = calculate_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = calculate_result()
        d = defer.maybeDeferred(self._handler.calculate, args.logid, args.w)
        d.addCallback(self.write_results_success_calculate, result, seqid, oprot)
        d.addErrback(self.write_results_exception_calculate, result, seqid, oprot)
        return d

    def write_results_success_calculate(self, success, result, seqid, oprot):
        result.success = success
        oprot.writeMessageBegin("calculate", TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def write_results_exception_calculate(self, error, result, seqid, oprot):
        msg_type = TMessageType.REPLY
        try:
            error.raiseException()
        except InvalidOperation as ouch:
            result.ouch = ouch
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
        oprot.writeMessageBegin("calculate", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_zip(self, seqid, iprot, oprot):
        args = zip_args()
        args.read(iprot)
        iprot.readMessageEnd()
        d = defer.maybeDeferred(self._handler.zip, )
        d.addErrback(self.handle_exception_zip, seqid)
        return d

    def handle_exception_zip(self, error, seqid):
        try:
            error.raiseException()
        except TTransport.TTransportException:
            raise
        except Exception:
            logging.exception('Exception in oneway handler')

# HELPER FUNCTIONS AND STRUCTURES


class ping_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ping_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(ping_args)
ping_args.thrift_spec = (
)


class ping_result(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ping_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(ping_result)
ping_result.thrift_spec = (
)


class add_args(object):
    """
    Attributes:
     - num1
     - num2

    """


    def __init__(self, num1=None, num2=None,):
        self.num1 = num1
        self.num2 = num2

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.num1 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.num2 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('add_args')
        if self.num1 is not None:
            oprot.writeFieldBegin('num1', TType.I32, 1)
            oprot.writeI32(self.num1)
            oprot.writeFieldEnd()
        if self.num2 is not None:
            oprot.writeFieldBegin('num2', TType.I32, 2)
            oprot.writeI32(self.num2)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(add_args)
add_args.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'num1', None, None, ),  # 1
    (2, TType.I32, 'num2', None, None, ),  # 2
)


class add_result(object):
    """
    Attributes:
     - success

    """


    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('add_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(add_result)
add_result.thrift_spec = (
    (0, TType.I32, 'success', None, None, ),  # 0
)


class calculate_args(object):
    """
    Attributes:
     - logid
     - w

    """


    def __init__(self, logid=None, w=None,):
        self.logid = logid
        self.w = w

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.logid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.w = Work()
                    self.w.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('calculate_args')
        if self.logid is not None:
            oprot.writeFieldBegin('logid', TType.I32, 1)
            oprot.writeI32(self.logid)
            oprot.writeFieldEnd()
        if self.w is not None:
            oprot.writeFieldBegin('w', TType.STRUCT, 2)
            self.w.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(calculate_args)
calculate_args.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'logid', None, None, ),  # 1
    (2, TType.STRUCT, 'w', [Work, None], None, ),  # 2
)


class calculate_result(object):
    """
    Attributes:
     - success
     - ouch

    """


    def __init__(self, success=None, ouch=None,):
        self.success = success
        self.ouch = ouch

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.ouch = InvalidOperation.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('calculate_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.ouch is not None:
            oprot.writeFieldBegin('ouch', TType.STRUCT, 1)
            self.ouch.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(calculate_result)
calculate_result.thrift_spec = (
    (0, TType.I32, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'ouch', [InvalidOperation, None], None, ),  # 1
)


class zip_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('zip_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(zip_args)
zip_args.thrift_spec = (
)
fix_spec(all_structs)
del all_structs
