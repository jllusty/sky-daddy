#
# Autogenerated by Thrift Compiler (0.16.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:dynamic,slots
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
    def echoTree(self, tree):
        """
        Parameters:
         - tree

        """
        pass

    def echoList(self, lst):
        """
        Parameters:
         - lst

        """
        pass

    def echoCoRec(self, item):
        """
        Parameters:
         - item

        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def echoTree(self, tree):
        """
        Parameters:
         - tree

        """
        self.send_echoTree(tree)
        return self.recv_echoTree()

    def send_echoTree(self, tree):
        self._oprot.writeMessageBegin('echoTree', TMessageType.CALL, self._seqid)
        args = echoTree_args()
        args.tree = tree
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_echoTree(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = echoTree_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "echoTree failed: unknown result")

    def echoList(self, lst):
        """
        Parameters:
         - lst

        """
        self.send_echoList(lst)
        return self.recv_echoList()

    def send_echoList(self, lst):
        self._oprot.writeMessageBegin('echoList', TMessageType.CALL, self._seqid)
        args = echoList_args()
        args.lst = lst
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_echoList(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = echoList_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "echoList failed: unknown result")

    def echoCoRec(self, item):
        """
        Parameters:
         - item

        """
        self.send_echoCoRec(item)
        return self.recv_echoCoRec()

    def send_echoCoRec(self, item):
        self._oprot.writeMessageBegin('echoCoRec', TMessageType.CALL, self._seqid)
        args = echoCoRec_args()
        args.item = item
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_echoCoRec(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = echoCoRec_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "echoCoRec failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["echoTree"] = Processor.process_echoTree
        self._processMap["echoList"] = Processor.process_echoList
        self._processMap["echoCoRec"] = Processor.process_echoCoRec
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

    def process_echoTree(self, seqid, iprot, oprot):
        args = echoTree_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = echoTree_result()
        try:
            result.success = self._handler.echoTree(args.tree)
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
        oprot.writeMessageBegin("echoTree", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_echoList(self, seqid, iprot, oprot):
        args = echoList_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = echoList_result()
        try:
            result.success = self._handler.echoList(args.lst)
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
        oprot.writeMessageBegin("echoList", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_echoCoRec(self, seqid, iprot, oprot):
        args = echoCoRec_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = echoCoRec_result()
        try:
            result.success = self._handler.echoCoRec(args.item)
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
        oprot.writeMessageBegin("echoCoRec", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class echoTree_args(TBase):
    """
    Attributes:
     - tree

    """

    __slots__ = (
        'tree',
    )


    def __init__(self, tree=None,):
        self.tree = tree
all_structs.append(echoTree_args)
echoTree_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'tree', [RecTree, None], None, ),  # 1
)


class echoTree_result(TBase):
    """
    Attributes:
     - success

    """

    __slots__ = (
        'success',
    )


    def __init__(self, success=None,):
        self.success = success
all_structs.append(echoTree_result)
echoTree_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [RecTree, None], None, ),  # 0
)


class echoList_args(TBase):
    """
    Attributes:
     - lst

    """

    __slots__ = (
        'lst',
    )


    def __init__(self, lst=None,):
        self.lst = lst
all_structs.append(echoList_args)
echoList_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'lst', [RecList, None], None, ),  # 1
)


class echoList_result(TBase):
    """
    Attributes:
     - success

    """

    __slots__ = (
        'success',
    )


    def __init__(self, success=None,):
        self.success = success
all_structs.append(echoList_result)
echoList_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [RecList, None], None, ),  # 0
)


class echoCoRec_args(TBase):
    """
    Attributes:
     - item

    """

    __slots__ = (
        'item',
    )


    def __init__(self, item=None,):
        self.item = item
all_structs.append(echoCoRec_args)
echoCoRec_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'item', [CoRec, None], None, ),  # 1
)


class echoCoRec_result(TBase):
    """
    Attributes:
     - success

    """

    __slots__ = (
        'success',
    )


    def __init__(self, success=None,):
        self.success = success
all_structs.append(echoCoRec_result)
echoCoRec_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [CoRec, None], None, ),  # 0
)
fix_spec(all_structs)
del all_structs
