#
# Autogenerated by Thrift Compiler (0.16.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:old_style
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
from .ttypes import *
DOUBLE_ASSIGNED_TO_INT_CONSTANT_TEST = float(1)
DOUBLE_ASSIGNED_TO_NEGATIVE_INT_CONSTANT_TEST = float(-100)
DOUBLE_ASSIGNED_TO_LARGEST_INT_CONSTANT_TEST = float(9223372036854775807)
DOUBLE_ASSIGNED_TO_SMALLEST_INT_CONSTANT_TEST = float(-9223372036854775807)
DOUBLE_ASSIGNED_TO_DOUBLE_WITH_MANY_DECIMALS_TEST = 3.1415926535900001
DOUBLE_ASSIGNED_TO_FRACTIONAL_DOUBLE_TEST = 1000000.0999999999767169
DOUBLE_ASSIGNED_TO_NEGATIVE_FRACTIONAL_DOUBLE_TEST = -1000000.0999999999767169
DOUBLE_ASSIGNED_TO_LARGE_DOUBLE_TEST = 169999999999999993883079578865998174333346074304075874502773119193537729178160565864330091787584707988572262467983188919169916105593357174268369962062473635296474636515660464935663040684957844303524367815028553272712298986386310828644513212353921123253311675499856875650512437415429217994623324794855339589632.0000000000000000
DOUBLE_ASSIGNED_TO_LARGE_FRACTIONAL_DOUBLE_TEST = 9223372036854775808.0000000000000000
DOUBLE_ASSIGNED_TO_SMALL_DOUBLE_TEST = -169999999999999993883079578865998174333346074304075874502773119193537729178160565864330091787584707988572262467983188919169916105593357174268369962062473635296474636515660464935663040684957844303524367815028553272712298986386310828644513212353921123253311675499856875650512437415429217994623324794855339589632.0000000000000000
DOUBLE_ASSIGNED_TO_NEGATIVE_BUT_LARGE_FRACTIONAL_DOUBLE_TEST = -9223372036854775808.0000000000000000
DOUBLE_LIST_TEST = [
    float(1),
    float(-100),
    float(100),
    float(9223372036854775807),
    float(-9223372036854775807),
    3.1415926535900001,
    1000000.0999999999767169,
    -1000000.0999999999767169,
    169999999999999993883079578865998174333346074304075874502773119193537729178160565864330091787584707988572262467983188919169916105593357174268369962062473635296474636515660464935663040684957844303524367815028553272712298986386310828644513212353921123253311675499856875650512437415429217994623324794855339589632.0000000000000000,
    -169999999999999993883079578865998174333346074304075874502773119193537729178160565864330091787584707988572262467983188919169916105593357174268369962062473635296474636515660464935663040684957844303524367815028553272712298986386310828644513212353921123253311675499856875650512437415429217994623324794855339589632.0000000000000000,
    9223372036854775808.0000000000000000,
    -9223372036854775808.0000000000000000,
]
