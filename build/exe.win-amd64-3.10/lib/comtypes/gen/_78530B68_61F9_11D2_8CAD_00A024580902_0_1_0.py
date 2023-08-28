# -*- coding: mbcs -*-

from ctypes import *
from ctypes.wintypes import _FILETIME, _LARGE_INTEGER, _ULARGE_INTEGER
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import (
    _check_version, BSTR, CoClass, COMMETHOD, dispid, GUID,
    helpstring, IPersist, IUnknown
)
from ctypes import HRESULT
from comtypes.typeinfo import ULONG_PTR
from comtypes.automation import VARIANT
from comtypes.persist import IErrorLog, IPropertyBag

_lcid = 0  # change this if required
typelib_path = 'C:\\Windows\\System32\\qedit.dll'
WSTRING = c_wchar_p
LONG_PTR = c_longlong



class tagSTATSTG(Structure):
    pass


tagSTATSTG._fields_ = [
    ('pwcsName', WSTRING),
    ('Type', c_ulong),
    ('cbSize', _ULARGE_INTEGER),
    ('mtime', _FILETIME),
    ('ctime', _FILETIME),
    ('atime', _FILETIME),
    ('grfMode', c_ulong),
    ('grfLocksSupported', c_ulong),
    ('clsid', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('grfStateBits', c_ulong),
    ('reserved', c_ulong),
]

assert sizeof(tagSTATSTG) == 80, sizeof(tagSTATSTG)
assert alignment(tagSTATSTG) == 8, alignment(tagSTATSTG)


class IAMTimelineObj(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IAMTimelineObj Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{78530B77-61F9-11D2-8CAD-00A024580902}')
    _idlflags_ = []


class IPropertySetter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IPropertySetter Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{AE9472BD-B0C3-11D2-8D24-00A0C9441E20}')
    _idlflags_ = []


# values for enumeration '__MIDL___MIDL_itf_qedit_0000_0000_0007'
TIMELINE_MAJOR_TYPE_COMPOSITE = 1
TIMELINE_MAJOR_TYPE_TRACK = 2
TIMELINE_MAJOR_TYPE_SOURCE = 4
TIMELINE_MAJOR_TYPE_TRANSITION = 8
TIMELINE_MAJOR_TYPE_EFFECT = 16
TIMELINE_MAJOR_TYPE_GROUP = 128
__MIDL___MIDL_itf_qedit_0000_0000_0007 = c_int  # enum
TIMELINE_MAJOR_TYPE = __MIDL___MIDL_itf_qedit_0000_0000_0007


class IAMTimeline(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IAMTimeline Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{78530B74-61F9-11D2-8CAD-00A024580902}')
    _idlflags_ = []


class IAMTimelineGroup(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IAMTimelineGroup Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{9EED4F00-B8A6-11D2-8023-00C0DF10D434}')
    _idlflags_ = []


IAMTimelineObj._methods_ = [
    COMMETHOD(
        [helpstring('method GetStartStop')],
        HRESULT,
        'GetStartStop',
        ([], POINTER(c_longlong), 'pStart'),
        ([], POINTER(c_longlong), 'pStop')
    ),
    COMMETHOD(
        [helpstring('method GetStartStop2')],
        HRESULT,
        'GetStartStop2',
        ([], POINTER(c_double), 'pStart'),
        ([], POINTER(c_double), 'pStop')
    ),
    COMMETHOD(
        [helpstring('method FixTimes')],
        HRESULT,
        'FixTimes',
        ([], POINTER(c_longlong), 'pStart'),
        ([], POINTER(c_longlong), 'pStop')
    ),
    COMMETHOD(
        [helpstring('method FixTimes2')],
        HRESULT,
        'FixTimes2',
        ([], POINTER(c_double), 'pStart'),
        ([], POINTER(c_double), 'pStop')
    ),
    COMMETHOD(
        [helpstring('method SetStartStop')],
        HRESULT,
        'SetStartStop',
        ([], c_longlong, 'Start'),
        ([], c_longlong, 'Stop')
    ),
    COMMETHOD(
        [helpstring('method SetStartStop2')],
        HRESULT,
        'SetStartStop2',
        ([], c_double, 'Start'),
        ([], c_double, 'Stop')
    ),
    COMMETHOD(
        [helpstring('method GetPropertySetter')],
        HRESULT,
        'GetPropertySetter',
        (['out', 'retval'], POINTER(POINTER(IPropertySetter)), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method SetPropertySetter')],
        HRESULT,
        'SetPropertySetter',
        ([], POINTER(IPropertySetter), 'newVal')
    ),
    COMMETHOD(
        [helpstring('method GetSubObject')],
        HRESULT,
        'GetSubObject',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method SetSubObject')],
        HRESULT,
        'SetSubObject',
        ([], POINTER(IUnknown), 'newVal')
    ),
    COMMETHOD(
        [helpstring('method SetSubObjectGUID')],
        HRESULT,
        'SetSubObjectGUID',
        (
            [],
            comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID,
            'newVal',
        )
    ),
    COMMETHOD(
        [helpstring('method SetSubObjectGUIDByBSTR')],
        HRESULT,
        'SetSubObjectGUIDB',
        ([], BSTR, 'newVal')
    ),
    COMMETHOD(
        [helpstring('method GetSubObjectGUID')],
        HRESULT,
        'GetSubObjectGUID',
        (
            [],
            POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
            'pVal',
        )
    ),
    COMMETHOD(
        [helpstring('method GetSubObjectGUIDByBSTR')],
        HRESULT,
        'GetSubObjectGUIDB',
        (['out', 'retval'], POINTER(BSTR), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method GetSubObjectLoaded')],
        HRESULT,
        'GetSubObjectLoaded',
        ([], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method GetTimelineType')],
        HRESULT,
        'GetTimelineType',
        ([], POINTER(TIMELINE_MAJOR_TYPE), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method SetTimelineType')],
        HRESULT,
        'SetTimelineType',
        ([], TIMELINE_MAJOR_TYPE, 'newVal')
    ),
    COMMETHOD(
        [helpstring('method GetUserID')],
        HRESULT,
        'GetUserID',
        ([], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method SetUserID')],
        HRESULT,
        'SetUserID',
        ([], c_int, 'newVal')
    ),
    COMMETHOD(
        [helpstring('method GetGenID')],
        HRESULT,
        'GetGenID',
        ([], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method GetUserName')],
        HRESULT,
        'GetUserName',
        (['out', 'retval'], POINTER(BSTR), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method SetUserName')],
        HRESULT,
        'SetUserName',
        ([], BSTR, 'newVal')
    ),
    COMMETHOD(
        [helpstring('method GetUserData')],
        HRESULT,
        'GetUserData',
        ([], POINTER(c_ubyte), 'pData'),
        ([], POINTER(c_int), 'pSize')
    ),
    COMMETHOD(
        [helpstring('method SetUserData')],
        HRESULT,
        'SetUserData',
        ([], POINTER(c_ubyte), 'pData'),
        ([], c_int, 'Size')
    ),
    COMMETHOD(
        [helpstring('method GetMuted')],
        HRESULT,
        'GetMuted',
        ([], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method SetMuted')],
        HRESULT,
        'SetMuted',
        ([], c_int, 'newVal')
    ),
    COMMETHOD(
        [helpstring('method GetLocked')],
        HRESULT,
        'GetLocked',
        ([], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method SetLocked')],
        HRESULT,
        'SetLocked',
        ([], c_int, 'newVal')
    ),
    COMMETHOD(
        [helpstring('method GetDirtyRange')],
        HRESULT,
        'GetDirtyRange',
        ([], POINTER(c_longlong), 'pStart'),
        ([], POINTER(c_longlong), 'pStop')
    ),
    COMMETHOD(
        [helpstring('method GetDirtyRange')],
        HRESULT,
        'GetDirtyRange2',
        ([], POINTER(c_double), 'pStart'),
        ([], POINTER(c_double), 'pStop')
    ),
    COMMETHOD(
        [helpstring('method SetDirtyRange')],
        HRESULT,
        'SetDirtyRange',
        ([], c_longlong, 'Start'),
        ([], c_longlong, 'Stop')
    ),
    COMMETHOD(
        [helpstring('method SetDirtyRange')],
        HRESULT,
        'SetDirtyRange2',
        ([], c_double, 'Start'),
        ([], c_double, 'Stop')
    ),
    COMMETHOD([helpstring('method ClearDirty')], HRESULT, 'ClearDirty'),
    COMMETHOD([helpstring('method Remove')], HRESULT, 'Remove'),
    COMMETHOD([helpstring('method RemoveAll')], HRESULT, 'RemoveAll'),
    COMMETHOD(
        [],
        HRESULT,
        'GetTimelineNoRef',
        ([], POINTER(POINTER(IAMTimeline)), 'ppResult')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetGroupIBelongTo',
        (['out'], POINTER(POINTER(IAMTimelineGroup)), 'ppGroup')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetEmbedDepth',
        ([], POINTER(c_int), 'pVal')
    ),
]

################################################################
# code template for IAMTimelineObj implementation
# class IAMTimelineObj_Impl(object):
#     def GetStartStop(self, pStart, pStop):
#         'method GetStartStop'
#         #return 
#
#     def GetStartStop2(self, pStart, pStop):
#         'method GetStartStop2'
#         #return 
#
#     def FixTimes(self, pStart, pStop):
#         'method FixTimes'
#         #return 
#
#     def FixTimes2(self, pStart, pStop):
#         'method FixTimes2'
#         #return 
#
#     def SetStartStop(self, Start, Stop):
#         'method SetStartStop'
#         #return 
#
#     def SetStartStop2(self, Start, Stop):
#         'method SetStartStop2'
#         #return 
#
#     def GetPropertySetter(self):
#         'method GetPropertySetter'
#         #return pVal
#
#     def SetPropertySetter(self, newVal):
#         'method SetPropertySetter'
#         #return 
#
#     def GetSubObject(self):
#         'method GetSubObject'
#         #return pVal
#
#     def SetSubObject(self, newVal):
#         'method SetSubObject'
#         #return 
#
#     def SetSubObjectGUID(self, newVal):
#         'method SetSubObjectGUID'
#         #return 
#
#     def SetSubObjectGUIDB(self, newVal):
#         'method SetSubObjectGUIDByBSTR'
#         #return 
#
#     def GetSubObjectGUID(self, pVal):
#         'method GetSubObjectGUID'
#         #return 
#
#     def GetSubObjectGUIDB(self):
#         'method GetSubObjectGUIDByBSTR'
#         #return pVal
#
#     def GetSubObjectLoaded(self, pVal):
#         'method GetSubObjectLoaded'
#         #return 
#
#     def GetTimelineType(self, pVal):
#         'method GetTimelineType'
#         #return 
#
#     def SetTimelineType(self, newVal):
#         'method SetTimelineType'
#         #return 
#
#     def GetUserID(self, pVal):
#         'method GetUserID'
#         #return 
#
#     def SetUserID(self, newVal):
#         'method SetUserID'
#         #return 
#
#     def GetGenID(self, pVal):
#         'method GetGenID'
#         #return 
#
#     def GetUserName(self):
#         'method GetUserName'
#         #return pVal
#
#     def SetUserName(self, newVal):
#         'method SetUserName'
#         #return 
#
#     def GetUserData(self, pData, pSize):
#         'method GetUserData'
#         #return 
#
#     def SetUserData(self, pData, Size):
#         'method SetUserData'
#         #return 
#
#     def GetMuted(self, pVal):
#         'method GetMuted'
#         #return 
#
#     def SetMuted(self, newVal):
#         'method SetMuted'
#         #return 
#
#     def GetLocked(self, pVal):
#         'method GetLocked'
#         #return 
#
#     def SetLocked(self, newVal):
#         'method SetLocked'
#         #return 
#
#     def GetDirtyRange(self, pStart, pStop):
#         'method GetDirtyRange'
#         #return 
#
#     def GetDirtyRange2(self, pStart, pStop):
#         'method GetDirtyRange'
#         #return 
#
#     def SetDirtyRange(self, Start, Stop):
#         'method SetDirtyRange'
#         #return 
#
#     def SetDirtyRange2(self, Start, Stop):
#         'method SetDirtyRange'
#         #return 
#
#     def ClearDirty(self):
#         'method ClearDirty'
#         #return 
#
#     def Remove(self):
#         'method Remove'
#         #return 
#
#     def RemoveAll(self):
#         'method RemoveAll'
#         #return 
#
#     def GetTimelineNoRef(self, ppResult):
#         '-no docstring-'
#         #return 
#
#     def GetGroupIBelongTo(self):
#         '-no docstring-'
#         #return ppGroup
#
#     def GetEmbedDepth(self, pVal):
#         '-no docstring-'
#         #return 
#


class IAMSetErrorLog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IAMSetErrorLog Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{963566DA-BE21-4EAF-88E9-35704F8F52A1}')
    _idlflags_ = []


class IAMErrorLog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IAMErrorLog Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{E43E73A2-0EFA-11D3-9601-00A0C9441E20}')
    _idlflags_ = []


IAMSetErrorLog._methods_ = [
    COMMETHOD(
        ['propget', helpstring('property ErrorLog')],
        HRESULT,
        'ErrorLog',
        (['out', 'retval'], POINTER(POINTER(IAMErrorLog)), 'pVal')
    ),
    COMMETHOD(
        ['propput', helpstring('property ErrorLog')],
        HRESULT,
        'ErrorLog',
        (['in'], POINTER(IAMErrorLog), 'pVal')
    ),
]

################################################################
# code template for IAMSetErrorLog implementation
# class IAMSetErrorLog_Impl(object):
#     def _get(self):
#         'property ErrorLog'
#         #return pVal
#     def _set(self, pVal):
#         'property ErrorLog'
#     ErrorLog = property(_get, _set, doc = _set.__doc__)
#


class IEnumMediaTypes(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{89C31040-846B-11CE-97D3-00AA0055595A}')
    _idlflags_ = []

    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)


class _AMMediaType(Structure):
    pass


IEnumMediaTypes._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], c_ulong, 'cMediaTypes'),
        (['out'], POINTER(POINTER(_AMMediaType)), 'ppMediaTypes'),
        (['out'], POINTER(c_ulong), 'pcFetched')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], c_ulong, 'cMediaTypes')
    ),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumMediaTypes)), 'ppEnum')
    ),
]

################################################################
# code template for IEnumMediaTypes implementation
# class IEnumMediaTypes_Impl(object):
#     def Next(self, cMediaTypes):
#         '-no docstring-'
#         #return ppMediaTypes, pcFetched
#
#     def Skip(self, cMediaTypes):
#         '-no docstring-'
#         #return 
#
#     def Reset(self):
#         '-no docstring-'
#         #return 
#
#     def Clone(self):
#         '-no docstring-'
#         #return ppEnum
#


class IMediaSample(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A8689A-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []


IMediaSample._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetPointer',
        (['out'], POINTER(POINTER(c_ubyte)), 'ppBuffer')
    ),
    COMMETHOD([], c_int, 'GetSize'),
    COMMETHOD(
        [],
        HRESULT,
        'GetTime',
        (['out'], POINTER(c_longlong), 'pTimeStart'),
        (['out'], POINTER(c_longlong), 'pTimeEnd')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTime',
        (['in'], POINTER(c_longlong), 'pTimeStart'),
        (['in'], POINTER(c_longlong), 'pTimeEnd')
    ),
    COMMETHOD([], HRESULT, 'IsSyncPoint'),
    COMMETHOD(
        [],
        HRESULT,
        'SetSyncPoint',
        ([], c_int, 'bIsSyncPoint')
    ),
    COMMETHOD([], HRESULT, 'IsPreroll'),
    COMMETHOD(
        [],
        HRESULT,
        'SetPreroll',
        ([], c_int, 'bIsPreroll')
    ),
    COMMETHOD([], c_int, 'GetActualDataLength'),
    COMMETHOD(
        [],
        HRESULT,
        'SetActualDataLength',
        ([], c_int, '__MIDL__IMediaSample0000')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMediaType',
        (['out'], POINTER(POINTER(_AMMediaType)), 'ppMediaType')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetMediaType',
        (['in'], POINTER(_AMMediaType), 'pMediaType')
    ),
    COMMETHOD([], HRESULT, 'IsDiscontinuity'),
    COMMETHOD(
        [],
        HRESULT,
        'SetDiscontinuity',
        ([], c_int, 'bDiscontinuity')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMediaTime',
        (['out'], POINTER(c_longlong), 'pTimeStart'),
        (['out'], POINTER(c_longlong), 'pTimeEnd')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetMediaTime',
        (['in'], POINTER(c_longlong), 'pTimeStart'),
        (['in'], POINTER(c_longlong), 'pTimeEnd')
    ),
]

################################################################
# code template for IMediaSample implementation
# class IMediaSample_Impl(object):
#     def GetPointer(self):
#         '-no docstring-'
#         #return ppBuffer
#
#     def GetSize(self):
#         '-no docstring-'
#         #return 
#
#     def GetTime(self):
#         '-no docstring-'
#         #return pTimeStart, pTimeEnd
#
#     def SetTime(self, pTimeStart, pTimeEnd):
#         '-no docstring-'
#         #return 
#
#     def IsSyncPoint(self):
#         '-no docstring-'
#         #return 
#
#     def SetSyncPoint(self, bIsSyncPoint):
#         '-no docstring-'
#         #return 
#
#     def IsPreroll(self):
#         '-no docstring-'
#         #return 
#
#     def SetPreroll(self, bIsPreroll):
#         '-no docstring-'
#         #return 
#
#     def GetActualDataLength(self):
#         '-no docstring-'
#         #return 
#
#     def SetActualDataLength(self, __MIDL__IMediaSample0000):
#         '-no docstring-'
#         #return 
#
#     def GetMediaType(self):
#         '-no docstring-'
#         #return ppMediaType
#
#     def SetMediaType(self, pMediaType):
#         '-no docstring-'
#         #return 
#
#     def IsDiscontinuity(self):
#         '-no docstring-'
#         #return 
#
#     def SetDiscontinuity(self, bDiscontinuity):
#         '-no docstring-'
#         #return 
#
#     def GetMediaTime(self):
#         '-no docstring-'
#         #return pTimeStart, pTimeEnd
#
#     def SetMediaTime(self, pTimeStart, pTimeEnd):
#         '-no docstring-'
#         #return 
#


class IRenderEngine2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IRenderEngine2 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{6BEE3A82-66C9-11D2-918F-00C0DF10D434}')
    _idlflags_ = []


IRenderEngine2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetResizerGUID',
        (
            [],
            comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID,
            'ResizerGuid',
        )
    ),
]

################################################################
# code template for IRenderEngine2 implementation
# class IRenderEngine2_Impl(object):
#     def SetResizerGUID(self, ResizerGuid):
#         '-no docstring-'
#         #return 
#


class SmartRenderEngine(CoClass):
    _reg_clsid_ = GUID('{498B0949-BBE9-4072-98BE-6CCAEB79DC6F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


class IRenderEngine(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IRenderEngine Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{6BEE3A81-66C9-11D2-918F-00C0DF10D434}')
    _idlflags_ = []


class ISmartRenderEngine(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """ISmartRenderEngine Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{F03FA8CE-879A-4D59-9B2C-26BB1CF83461}')
    _idlflags_ = []


SmartRenderEngine._com_interfaces_ = [IRenderEngine, ISmartRenderEngine, IAMSetErrorLog]


class IFilterGraph(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A8689F-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []


class IGraphBuilder(IFilterGraph):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A9-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []


class IMediaFilter(IPersist):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86899-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []


class IBaseFilter(IMediaFilter):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86895-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []


class IEnumFilters(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86893-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []

    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)


class IPin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86891-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []


IFilterGraph._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AddFilter',
        (['in'], POINTER(IBaseFilter), 'pFilter'),
        (['in'], WSTRING, 'pName')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveFilter',
        (['in'], POINTER(IBaseFilter), 'pFilter')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumFilters',
        (['out'], POINTER(POINTER(IEnumFilters)), 'ppEnum')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FindFilterByName',
        (['in'], WSTRING, 'pName'),
        (['out'], POINTER(POINTER(IBaseFilter)), 'ppFilter')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ConnectDirect',
        (['in'], POINTER(IPin), 'ppinOut'),
        (['in'], POINTER(IPin), 'ppinIn'),
        (['in'], POINTER(_AMMediaType), 'pmt')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Reconnect',
        (['in'], POINTER(IPin), 'pPin')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Disconnect',
        (['in'], POINTER(IPin), 'pPin')
    ),
    COMMETHOD([], HRESULT, 'SetDefaultSyncSource'),
]

################################################################
# code template for IFilterGraph implementation
# class IFilterGraph_Impl(object):
#     def AddFilter(self, pFilter, pName):
#         '-no docstring-'
#         #return 
#
#     def RemoveFilter(self, pFilter):
#         '-no docstring-'
#         #return 
#
#     def EnumFilters(self):
#         '-no docstring-'
#         #return ppEnum
#
#     def FindFilterByName(self, pName):
#         '-no docstring-'
#         #return ppFilter
#
#     def ConnectDirect(self, ppinOut, ppinIn, pmt):
#         '-no docstring-'
#         #return 
#
#     def Reconnect(self, pPin):
#         '-no docstring-'
#         #return 
#
#     def Disconnect(self, pPin):
#         '-no docstring-'
#         #return 
#
#     def SetDefaultSyncSource(self):
#         '-no docstring-'
#         #return 
#

IGraphBuilder._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Connect',
        (['in'], POINTER(IPin), 'ppinOut'),
        (['in'], POINTER(IPin), 'ppinIn')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Render',
        (['in'], POINTER(IPin), 'ppinOut')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RenderFile',
        (['in'], WSTRING, 'lpcwstrFile'),
        (['in'], WSTRING, 'lpcwstrPlayList')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddSourceFilter',
        (['in'], WSTRING, 'lpcwstrFileName'),
        (['in'], WSTRING, 'lpcwstrFilterName'),
        (['out'], POINTER(POINTER(IBaseFilter)), 'ppFilter')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetLogFile',
        (['in'], ULONG_PTR, 'hFile')
    ),
    COMMETHOD([], HRESULT, 'Abort'),
    COMMETHOD([], HRESULT, 'ShouldOperationContinue'),
]

################################################################
# code template for IGraphBuilder implementation
# class IGraphBuilder_Impl(object):
#     def Connect(self, ppinOut, ppinIn):
#         '-no docstring-'
#         #return 
#
#     def Render(self, ppinOut):
#         '-no docstring-'
#         #return 
#
#     def RenderFile(self, lpcwstrFile, lpcwstrPlayList):
#         '-no docstring-'
#         #return 
#
#     def AddSourceFilter(self, lpcwstrFileName, lpcwstrFilterName):
#         '-no docstring-'
#         #return ppFilter
#
#     def SetLogFile(self, hFile):
#         '-no docstring-'
#         #return 
#
#     def Abort(self):
#         '-no docstring-'
#         #return 
#
#     def ShouldOperationContinue(self):
#         '-no docstring-'
#         #return 
#


class IAMTimelineVirtualTrack(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IAMTimelineVirtualTrack Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{A8ED5F80-C2C7-11D2-8D39-00A0C9441E20}')
    _idlflags_ = []


IAMTimelineVirtualTrack._methods_ = [
    COMMETHOD(
        [helpstring('method TrackGetPriority')],
        HRESULT,
        'TrackGetPriority',
        ([], POINTER(c_int), 'pPriority')
    ),
    COMMETHOD([helpstring('method SetTrackDirty')], HRESULT, 'SetTrackDirty'),
]

################################################################
# code template for IAMTimelineVirtualTrack implementation
# class IAMTimelineVirtualTrack_Impl(object):
#     def TrackGetPriority(self, pPriority):
#         'method TrackGetPriority'
#         #return 
#
#     def SetTrackDirty(self):
#         'method SetTrackDirty'
#         #return 
#


class IFindCompressorCB(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IFindCompressorCB Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{F03FA8DE-879A-4D59-9B2C-26BB1CF83461}')
    _idlflags_ = []


ISmartRenderEngine._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetGroupCompressor',
        ([], c_int, 'Group'),
        ([], POINTER(IBaseFilter), 'pCompressor')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetGroupCompressor',
        ([], c_int, 'Group'),
        ([], POINTER(POINTER(IBaseFilter)), 'pCompressor')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetFindCompressorCB',
        ([], POINTER(IFindCompressorCB), 'pCallback')
    ),
]

################################################################
# code template for ISmartRenderEngine implementation
# class ISmartRenderEngine_Impl(object):
#     def SetGroupCompressor(self, Group, pCompressor):
#         '-no docstring-'
#         #return 
#
#     def GetGroupCompressor(self, Group, pCompressor):
#         '-no docstring-'
#         #return 
#
#     def SetFindCompressorCB(self, pCallback):
#         '-no docstring-'
#         #return 
#
# values for enumeration '_FilterState'
State_Stopped = 0
State_Paused = 1
State_Running = 2
_FilterState = c_int  # enum


class IReferenceClock(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86897-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []


IMediaFilter._methods_ = [
    COMMETHOD([], HRESULT, 'Stop'),
    COMMETHOD([], HRESULT, 'Pause'),
    COMMETHOD(
        [],
        HRESULT,
        'Run',
        ([], c_longlong, 'tStart')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetState',
        (['in'], c_ulong, 'dwMilliSecsTimeout'),
        (['out'], POINTER(_FilterState), 'State')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSyncSource',
        (['in'], POINTER(IReferenceClock), 'pClock')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSyncSource',
        (['out'], POINTER(POINTER(IReferenceClock)), 'pClock')
    ),
]

################################################################
# code template for IMediaFilter implementation
# class IMediaFilter_Impl(object):
#     def Stop(self):
#         '-no docstring-'
#         #return 
#
#     def Pause(self):
#         '-no docstring-'
#         #return 
#
#     def Run(self, tStart):
#         '-no docstring-'
#         #return 
#
#     def GetState(self, dwMilliSecsTimeout):
#         '-no docstring-'
#         #return State
#
#     def SetSyncSource(self, pClock):
#         '-no docstring-'
#         #return 
#
#     def GetSyncSource(self):
#         '-no docstring-'
#         #return pClock
#


class IEnumPins(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86892-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []

    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)


class _FilterInfo(Structure):
    pass


IBaseFilter._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EnumPins',
        (['out'], POINTER(POINTER(IEnumPins)), 'ppEnum')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FindPin',
        (['in'], WSTRING, 'Id'),
        (['out'], POINTER(POINTER(IPin)), 'ppPin')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryFilterInfo',
        (['out'], POINTER(_FilterInfo), 'pInfo')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'JoinFilterGraph',
        (['in'], POINTER(IFilterGraph), 'pGraph'),
        (['in'], WSTRING, 'pName')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryVendorInfo',
        (['out'], POINTER(WSTRING), 'pVendorInfo')
    ),
]

################################################################
# code template for IBaseFilter implementation
# class IBaseFilter_Impl(object):
#     def EnumPins(self):
#         '-no docstring-'
#         #return ppEnum
#
#     def FindPin(self, Id):
#         '-no docstring-'
#         #return ppPin
#
#     def QueryFilterInfo(self):
#         '-no docstring-'
#         #return pInfo
#
#     def JoinFilterGraph(self, pGraph, pName):
#         '-no docstring-'
#         #return 
#
#     def QueryVendorInfo(self):
#         '-no docstring-'
#         #return pVendorInfo
#


class AMTimelineComp(CoClass):
    _reg_clsid_ = GUID('{74D2EC80-6233-11D2-8CAD-00A024580902}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


class IAMTimelineComp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IAMTimelineComp Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{EAE58536-622E-11D2-8CAD-00A024580902}')
    _idlflags_ = []


class IAMTimelineEffectable(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IAMTimelineEffectable Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{EAE58537-622E-11D2-8CAD-00A024580902}')
    _idlflags_ = []


class IAMTimelineTransable(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IAMTimelineTransable Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{378FA386-622E-11D2-8CAD-00A024580902}')
    _idlflags_ = []


AMTimelineComp._com_interfaces_ = [IAMTimelineComp, IAMTimelineObj, IAMTimelineEffectable, IAMTimelineTransable, IAMTimelineVirtualTrack]


class AudMixer(CoClass):
    _reg_clsid_ = GUID('{036A9790-C153-11D2-9EF7-006008039E37}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


AudMixer._com_interfaces_ = [IBaseFilter]


class __MIDL___MIDL_itf_qedit_0000_0000_0002(Structure):
    pass


DEXTER_PARAM = __MIDL___MIDL_itf_qedit_0000_0000_0002


class __MIDL___MIDL_itf_qedit_0000_0000_0003(Structure):
    pass


DEXTER_VALUE = __MIDL___MIDL_itf_qedit_0000_0000_0003

IPropertySetter._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'LoadXML',
        (['in'], POINTER(IUnknown), 'pxml')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PrintXML',
        (['out'], POINTER(c_ubyte), 'pszXML'),
        (['in'], c_int, 'cbXML'),
        (['out'], POINTER(c_int), 'pcbPrinted'),
        (['in'], c_int, 'indent')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CloneProps',
        (['out'], POINTER(POINTER(IPropertySetter)), 'ppSetter'),
        (['in'], c_longlong, 'rtStart'),
        (['in'], c_longlong, 'rtStop')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddProp',
        (['in'], DEXTER_PARAM, 'Param'),
        (['in'], POINTER(DEXTER_VALUE), 'paValue')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetProps',
        (['out'], POINTER(c_int), 'pcParams'),
        (['out'], POINTER(POINTER(DEXTER_PARAM)), 'paParam'),
        (['out'], POINTER(POINTER(DEXTER_VALUE)), 'paValue')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FreeProps',
        (['in'], c_int, 'cParams'),
        (['in'], POINTER(DEXTER_PARAM), 'paParam'),
        (['in'], POINTER(DEXTER_VALUE), 'paValue')
    ),
    COMMETHOD([], HRESULT, 'ClearProps'),
    COMMETHOD(
        [],
        HRESULT,
        'SaveToBlob',
        (['out'], POINTER(c_int), 'pcSize'),
        (['out'], POINTER(POINTER(c_ubyte)), 'ppb')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'LoadFromBlob',
        (['in'], c_int, 'cSize'),
        (['in'], POINTER(c_ubyte), 'pb')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetProps',
        (['in'], POINTER(IUnknown), 'pTarget'),
        (['in'], c_longlong, 'rtNow')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PrintXMLW',
        (['out'], POINTER(c_ushort), 'pszXML'),
        (['in'], c_int, 'cchXML'),
        (['out'], POINTER(c_int), 'pcchPrinted'),
        (['in'], c_int, 'indent')
    ),
]

################################################################
# code template for IPropertySetter implementation
# class IPropertySetter_Impl(object):
#     def LoadXML(self, pxml):
#         '-no docstring-'
#         #return 
#
#     def PrintXML(self, cbXML, indent):
#         '-no docstring-'
#         #return pszXML, pcbPrinted
#
#     def CloneProps(self, rtStart, rtStop):
#         '-no docstring-'
#         #return ppSetter
#
#     def AddProp(self, Param, paValue):
#         '-no docstring-'
#         #return 
#
#     def GetProps(self):
#         '-no docstring-'
#         #return pcParams, paParam, paValue
#
#     def FreeProps(self, cParams, paParam, paValue):
#         '-no docstring-'
#         #return 
#
#     def ClearProps(self):
#         '-no docstring-'
#         #return 
#
#     def SaveToBlob(self):
#         '-no docstring-'
#         #return pcSize, ppb
#
#     def LoadFromBlob(self, cSize, pb):
#         '-no docstring-'
#         #return 
#
#     def SetProps(self, pTarget, rtNow):
#         '-no docstring-'
#         #return 
#
#     def PrintXMLW(self, cchXML, indent):
#         '-no docstring-'
#         #return pszXML, pcchPrinted
#


class ColorSource(CoClass):
    _reg_clsid_ = GUID('{0CFDD070-581A-11D2-9EE6-006008039E37}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


ColorSource._com_interfaces_ = [IBaseFilter]

IAMTimelineComp._methods_ = [
    COMMETHOD(
        [helpstring('method VTrackInsBefore')],
        HRESULT,
        'VTrackInsBefore',
        ([], POINTER(IAMTimelineObj), 'pVirtualTrack'),
        ([], c_int, 'priority')
    ),
    COMMETHOD(
        [helpstring('method VTrackSwapPriorities')],
        HRESULT,
        'VTrackSwapPriorities',
        ([], c_int, 'VirtualTrackA'),
        ([], c_int, 'VirtualTrackB')
    ),
    COMMETHOD(
        [helpstring('method VTrackGetCount')],
        HRESULT,
        'VTrackGetCount',
        ([], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method GetVTrack')],
        HRESULT,
        'GetVTrack',
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppVirtualTrack'),
        ([], c_int, 'Which')
    ),
    COMMETHOD(
        [helpstring('method GetCountOfType')],
        HRESULT,
        'GetCountOfType',
        ([], POINTER(c_int), 'pVal'),
        ([], POINTER(c_int), 'pValWithComps'),
        ([], TIMELINE_MAJOR_TYPE, 'majortype')
    ),
    COMMETHOD(
        [helpstring('method GetRecursiveLayerOfType')],
        HRESULT,
        'GetRecursiveLayerOfType',
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppVirtualTrack'),
        ([], c_int, 'WhichLayer'),
        ([], TIMELINE_MAJOR_TYPE, 'Type')
    ),
    COMMETHOD(
        [helpstring('method GetRecursiveLayerOfTypeI (do not call)')],
        HRESULT,
        'GetRecursiveLayerOfTypeI',
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppVirtualTrack'),
        (['in', 'out'], POINTER(c_int), 'pWhichLayer'),
        ([], TIMELINE_MAJOR_TYPE, 'Type')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetNextVTrack',
        ([], POINTER(IAMTimelineObj), 'pVirtualTrack'),
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppNextVirtualTrack')
    ),
]

################################################################
# code template for IAMTimelineComp implementation
# class IAMTimelineComp_Impl(object):
#     def VTrackInsBefore(self, pVirtualTrack, priority):
#         'method VTrackInsBefore'
#         #return 
#
#     def VTrackSwapPriorities(self, VirtualTrackA, VirtualTrackB):
#         'method VTrackSwapPriorities'
#         #return 
#
#     def VTrackGetCount(self, pVal):
#         'method VTrackGetCount'
#         #return 
#
#     def GetVTrack(self, Which):
#         'method GetVTrack'
#         #return ppVirtualTrack
#
#     def GetCountOfType(self, pVal, pValWithComps, majortype):
#         'method GetCountOfType'
#         #return 
#
#     def GetRecursiveLayerOfType(self, WhichLayer, Type):
#         'method GetRecursiveLayerOfType'
#         #return ppVirtualTrack
#
#     def GetRecursiveLayerOfTypeI(self, Type):
#         'method GetRecursiveLayerOfTypeI (do not call)'
#         #return ppVirtualTrack, pWhichLayer
#
#     def GetNextVTrack(self, pVirtualTrack):
#         '-no docstring-'
#         #return ppNextVirtualTrack
#


class IAMTimelineSrc(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IAMTimelineSrc Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{78530B79-61F9-11D2-8CAD-00A024580902}')
    _idlflags_ = []


IAMTimelineGroup._methods_ = [
    COMMETHOD(
        [helpstring('method SetTimeline')],
        HRESULT,
        'SetTimeline',
        ([], POINTER(IAMTimeline), 'pTimeline')
    ),
    COMMETHOD(
        [helpstring('method GetTimeline')],
        HRESULT,
        'GetTimeline',
        (['out'], POINTER(POINTER(IAMTimeline)), 'ppTimeline')
    ),
    COMMETHOD(
        [helpstring('method GetPriority')],
        HRESULT,
        'GetPriority',
        ([], POINTER(c_int), 'pPriority')
    ),
    COMMETHOD(
        [helpstring('method GetMediaType')],
        HRESULT,
        'GetMediaType',
        (['out'], POINTER(_AMMediaType), '__MIDL__IAMTimelineGroup0000')
    ),
    COMMETHOD(
        [helpstring('method SetMediaType')],
        HRESULT,
        'SetMediaType',
        (['in'], POINTER(_AMMediaType), '__MIDL__IAMTimelineGroup0001')
    ),
    COMMETHOD(
        [helpstring('method SetOutputFPS')],
        HRESULT,
        'SetOutputFPS',
        ([], c_double, 'FPS')
    ),
    COMMETHOD(
        [helpstring('method GetOutputFPS')],
        HRESULT,
        'GetOutputFPS',
        ([], POINTER(c_double), 'pFPS')
    ),
    COMMETHOD(
        [helpstring('method SetGroupName')],
        HRESULT,
        'SetGroupName',
        ([], BSTR, 'pGroupName')
    ),
    COMMETHOD(
        [helpstring('method GetGroupName')],
        HRESULT,
        'GetGroupName',
        (['out', 'retval'], POINTER(BSTR), 'pGroupName')
    ),
    COMMETHOD(
        [helpstring('method SetPreviewMode')],
        HRESULT,
        'SetPreviewMode',
        ([], c_int, 'fPreview')
    ),
    COMMETHOD(
        [helpstring('method GetPreviewMode')],
        HRESULT,
        'GetPreviewMode',
        ([], POINTER(c_int), 'pfPreview')
    ),
    COMMETHOD(
        [helpstring('method SetMediaTypeForVB')],
        HRESULT,
        'SetMediaTypeForVB',
        (['in'], c_int, 'Val')
    ),
    COMMETHOD(
        [helpstring('method GetOutputBuffering')],
        HRESULT,
        'GetOutputBuffering',
        (['out'], POINTER(c_int), 'pnBuffer')
    ),
    COMMETHOD(
        [helpstring('method SetOutputBuffering')],
        HRESULT,
        'SetOutputBuffering',
        (['in'], c_int, 'nBuffer')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSmartRecompressFormat',
        ([], POINTER(c_int), 'pFormat')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSmartRecompressFormat',
        ([], POINTER(POINTER(c_int)), 'ppFormat')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsSmartRecompressFormatSet',
        ([], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsRecompressFormatDirty',
        ([], POINTER(c_int), 'pVal')
    ),
    COMMETHOD([], HRESULT, 'ClearRecompressFormatDirty'),
    COMMETHOD(
        [],
        HRESULT,
        'SetRecompFormatFromSource',
        ([], POINTER(IAMTimelineSrc), 'pSource')
    ),
]

################################################################
# code template for IAMTimelineGroup implementation
# class IAMTimelineGroup_Impl(object):
#     def SetTimeline(self, pTimeline):
#         'method SetTimeline'
#         #return 
#
#     def GetTimeline(self):
#         'method GetTimeline'
#         #return ppTimeline
#
#     def GetPriority(self, pPriority):
#         'method GetPriority'
#         #return 
#
#     def GetMediaType(self):
#         'method GetMediaType'
#         #return __MIDL__IAMTimelineGroup0000
#
#     def SetMediaType(self, __MIDL__IAMTimelineGroup0001):
#         'method SetMediaType'
#         #return 
#
#     def SetOutputFPS(self, FPS):
#         'method SetOutputFPS'
#         #return 
#
#     def GetOutputFPS(self, pFPS):
#         'method GetOutputFPS'
#         #return 
#
#     def SetGroupName(self, pGroupName):
#         'method SetGroupName'
#         #return 
#
#     def GetGroupName(self):
#         'method GetGroupName'
#         #return pGroupName
#
#     def SetPreviewMode(self, fPreview):
#         'method SetPreviewMode'
#         #return 
#
#     def GetPreviewMode(self, pfPreview):
#         'method GetPreviewMode'
#         #return 
#
#     def SetMediaTypeForVB(self, Val):
#         'method SetMediaTypeForVB'
#         #return 
#
#     def GetOutputBuffering(self):
#         'method GetOutputBuffering'
#         #return pnBuffer
#
#     def SetOutputBuffering(self, nBuffer):
#         'method SetOutputBuffering'
#         #return 
#
#     def SetSmartRecompressFormat(self, pFormat):
#         '-no docstring-'
#         #return 
#
#     def GetSmartRecompressFormat(self, ppFormat):
#         '-no docstring-'
#         #return 
#
#     def IsSmartRecompressFormatSet(self, pVal):
#         '-no docstring-'
#         #return 
#
#     def IsRecompressFormatDirty(self, pVal):
#         '-no docstring-'
#         #return 
#
#     def ClearRecompressFormatDirty(self):
#         '-no docstring-'
#         #return 
#
#     def SetRecompFormatFromSource(self, pSource):
#         '-no docstring-'
#         #return 
#

IFindCompressorCB._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCompressor',
        ([], POINTER(_AMMediaType), 'pType'),
        ([], POINTER(_AMMediaType), 'pCompType'),
        (['out'], POINTER(POINTER(IBaseFilter)), 'ppFilter')
    ),
]

################################################################
# code template for IFindCompressorCB implementation
# class IFindCompressorCB_Impl(object):
#     def GetCompressor(self, pType, pCompType):
#         '-no docstring-'
#         #return ppFilter
#


class DxtKey(CoClass):
    """DxtKey Class"""
    _reg_clsid_ = GUID('{C5B19592-145E-11D3-9F04-006008039E37}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


class IDXEffect(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IDXEffect Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{E31FB81B-1335-11D1-8189-0000F87557DB}')
    _idlflags_ = ['dual', 'oleautomation']


class IDxtKey(IDXEffect):
    """IDxtKey Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{3255DE56-38FB-4901-B980-94B438010D7B}')
    _idlflags_ = ['dual', 'oleautomation']


DxtKey._com_interfaces_ = [IDxtKey]


class Xml2Dex(CoClass):
    """Xml2Dex Class"""
    _reg_clsid_ = GUID('{18C628EE-962A-11D2-8D08-00A0C9441E20}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


class IXml2Dex(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IXml2Dex Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{18C628ED-962A-11D2-8D08-00A0C9441E20}')
    _idlflags_ = []


Xml2Dex._com_interfaces_ = [IXml2Dex]

_FilterInfo._fields_ = [
    ('achName', c_ushort * 128),
    ('pGraph', POINTER(IFilterGraph)),
]

assert sizeof(_FilterInfo) == 264, sizeof(_FilterInfo)
assert alignment(_FilterInfo) == 8, alignment(_FilterInfo)

IDXEffect._methods_ = [
    COMMETHOD(
        [dispid(10000), 'propget'],
        HRESULT,
        'Capabilities',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [dispid(10001), 'propget'],
        HRESULT,
        'Progress',
        (['out', 'retval'], POINTER(c_float), 'pVal')
    ),
    COMMETHOD(
        [dispid(10001), 'propput'],
        HRESULT,
        'Progress',
        (['in'], c_float, 'pVal')
    ),
    COMMETHOD(
        [dispid(10002), 'propget'],
        HRESULT,
        'StepResolution',
        (['out', 'retval'], POINTER(c_float), 'pVal')
    ),
    COMMETHOD(
        [dispid(10003), 'propget'],
        HRESULT,
        'Duration',
        (['out', 'retval'], POINTER(c_float), 'pVal')
    ),
    COMMETHOD(
        [dispid(10003), 'propput'],
        HRESULT,
        'Duration',
        (['in'], c_float, 'pVal')
    ),
]

################################################################
# code template for IDXEffect implementation
# class IDXEffect_Impl(object):
#     @property
#     def Capabilities(self):
#         '-no docstring-'
#         #return pVal
#
#     def _get(self):
#         '-no docstring-'
#         #return pVal
#     def _set(self, pVal):
#         '-no docstring-'
#     Progress = property(_get, _set, doc = _set.__doc__)
#
#     @property
#     def StepResolution(self):
#         '-no docstring-'
#         #return pVal
#
#     def _get(self):
#         '-no docstring-'
#         #return pVal
#     def _set(self, pVal):
#         '-no docstring-'
#     Duration = property(_get, _set, doc = _set.__doc__)
#

IDxtKey._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property KeyType'), 'propget'],
        HRESULT,
        'KeyType',
        (['out', 'retval'], POINTER(c_int), '__MIDL__IDxtKey0000')
    ),
    COMMETHOD(
        [dispid(1), helpstring('property KeyType'), 'propput'],
        HRESULT,
        'KeyType',
        (['in'], c_int, '__MIDL__IDxtKey0000')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property Hue'), 'propget'],
        HRESULT,
        'Hue',
        (['out', 'retval'], POINTER(c_int), '__MIDL__IDxtKey0002')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property Hue'), 'propput'],
        HRESULT,
        'Hue',
        (['in'], c_int, '__MIDL__IDxtKey0002')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property Luminance'), 'propget'],
        HRESULT,
        'Luminance',
        (['out', 'retval'], POINTER(c_int), '__MIDL__IDxtKey0004')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property Luminance'), 'propput'],
        HRESULT,
        'Luminance',
        (['in'], c_int, '__MIDL__IDxtKey0004')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property RGB'), 'propget'],
        HRESULT,
        'RGB',
        (['out', 'retval'], POINTER(c_ulong), '__MIDL__IDxtKey0006')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property RGB'), 'propput'],
        HRESULT,
        'RGB',
        (['in'], c_ulong, '__MIDL__IDxtKey0006')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property Similarity'), 'propget'],
        HRESULT,
        'Similarity',
        (['out', 'retval'], POINTER(c_int), '__MIDL__IDxtKey0008')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property Similarity'), 'propput'],
        HRESULT,
        'Similarity',
        (['in'], c_int, '__MIDL__IDxtKey0008')
    ),
    COMMETHOD(
        [dispid(6), helpstring('property Invert'), 'propget'],
        HRESULT,
        'Invert',
        (['out', 'retval'], POINTER(c_int), '__MIDL__IDxtKey0010')
    ),
    COMMETHOD(
        [dispid(6), helpstring('property Invert'), 'propput'],
        HRESULT,
        'Invert',
        (['in'], c_int, '__MIDL__IDxtKey0010')
    ),
]

################################################################
# code template for IDxtKey implementation
# class IDxtKey_Impl(object):
#     def _get(self):
#         'property KeyType'
#         #return __MIDL__IDxtKey0000
#     def _set(self, __MIDL__IDxtKey0000):
#         'property KeyType'
#     KeyType = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property Hue'
#         #return __MIDL__IDxtKey0002
#     def _set(self, __MIDL__IDxtKey0002):
#         'property Hue'
#     Hue = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property Luminance'
#         #return __MIDL__IDxtKey0004
#     def _set(self, __MIDL__IDxtKey0004):
#         'property Luminance'
#     Luminance = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property RGB'
#         #return __MIDL__IDxtKey0006
#     def _set(self, __MIDL__IDxtKey0006):
#         'property RGB'
#     RGB = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property Similarity'
#         #return __MIDL__IDxtKey0008
#     def _set(self, __MIDL__IDxtKey0008):
#         'property Similarity'
#     Similarity = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property Invert'
#         #return __MIDL__IDxtKey0010
#     def _set(self, __MIDL__IDxtKey0010):
#         'property Invert'
#     Invert = property(_get, _set, doc = _set.__doc__)
#


class IMediaLocator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IMediaLocator Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{288581E0-66CE-11D2-918F-00C0DF10D434}')
    _idlflags_ = []


IMediaLocator._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'FindMediaFile',
        ([], BSTR, 'Input'),
        ([], BSTR, 'FilterString'),
        ([], POINTER(BSTR), 'pOutput'),
        ([], c_int, 'Flags')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddFoundLocation',
        ([], BSTR, 'DirectoryName')
    ),
]

################################################################
# code template for IMediaLocator implementation
# class IMediaLocator_Impl(object):
#     def FindMediaFile(self, Input, FilterString, pOutput, Flags):
#         '-no docstring-'
#         #return 
#
#     def AddFoundLocation(self, DirectoryName):
#         '-no docstring-'
#         #return 
#

IAMErrorLog._methods_ = [
    COMMETHOD(
        [helpstring('method LogError')],
        HRESULT,
        'LogError',
        ([], c_int, 'Severity'),
        ([], BSTR, 'pErrorString'),
        ([], c_int, 'ErrorCode'),
        ([], c_int, 'hresult'),
        (['in'], POINTER(VARIANT), 'pExtraInfo')
    ),
]

################################################################
# code template for IAMErrorLog implementation
# class IAMErrorLog_Impl(object):
#     def LogError(self, Severity, pErrorString, ErrorCode, hresult, pExtraInfo):
#         'method LogError'
#         #return 
#

IReferenceClock._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetTime',
        (['out'], POINTER(c_longlong), 'pTime')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AdviseTime',
        (['in'], c_longlong, 'baseTime'),
        (['in'], c_longlong, 'streamTime'),
        (['in'], ULONG_PTR, 'hEvent'),
        (['out'], POINTER(ULONG_PTR), 'pdwAdviseCookie')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AdvisePeriodic',
        (['in'], c_longlong, 'startTime'),
        (['in'], c_longlong, 'periodTime'),
        (['in'], ULONG_PTR, 'hSemaphore'),
        (['out'], POINTER(ULONG_PTR), 'pdwAdviseCookie')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Unadvise',
        (['in'], ULONG_PTR, 'dwAdviseCookie')
    ),
]

################################################################
# code template for IReferenceClock implementation
# class IReferenceClock_Impl(object):
#     def GetTime(self):
#         '-no docstring-'
#         #return pTime
#
#     def AdviseTime(self, baseTime, streamTime, hEvent):
#         '-no docstring-'
#         #return pdwAdviseCookie
#
#     def AdvisePeriodic(self, startTime, periodTime, hSemaphore):
#         '-no docstring-'
#         #return pdwAdviseCookie
#
#     def Unadvise(self, dwAdviseCookie):
#         '-no docstring-'
#         #return 
#


class ISampleGrabberCB(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """ISampleGrabberCB Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{0579154A-2B53-4994-B0D0-E773148EFF85}')
    _idlflags_ = []


ISampleGrabberCB._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SampleCB',
        ([], c_double, 'SampleTime'),
        ([], POINTER(IMediaSample), 'pSample')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'BufferCB',
        ([], c_double, 'SampleTime'),
        ([], POINTER(c_ubyte), 'pBuffer'),
        ([], c_int, 'BufferLen')
    ),
]

################################################################
# code template for ISampleGrabberCB implementation
# class ISampleGrabberCB_Impl(object):
#     def SampleCB(self, SampleTime, pSample):
#         '-no docstring-'
#         #return 
#
#     def BufferCB(self, SampleTime, pBuffer, BufferLen):
#         '-no docstring-'
#         #return 
#


class AMTimelineObj(CoClass):
    """IAMTimelineObj Class"""
    _reg_clsid_ = GUID('{78530B78-61F9-11D2-8CAD-00A024580902}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


AMTimelineObj._com_interfaces_ = [IAMTimelineObj]

IXml2Dex._methods_ = [
    COMMETHOD(
        [helpstring('method CreateGraphFromFile')],
        HRESULT,
        'CreateGraphFromFile',
        (['out'], POINTER(POINTER(IUnknown)), 'ppGraph'),
        ([], POINTER(IUnknown), 'pTimeline'),
        ([], BSTR, 'Filename')
    ),
    COMMETHOD(
        [helpstring('method WriteGrfFile')],
        HRESULT,
        'WriteGrfFile',
        ([], POINTER(IUnknown), 'pGraph'),
        ([], BSTR, 'Filename')
    ),
    COMMETHOD(
        [helpstring('method WriteXMLFile')],
        HRESULT,
        'WriteXMLFile',
        ([], POINTER(IUnknown), 'pTimeline'),
        ([], BSTR, 'Filename')
    ),
    COMMETHOD(
        [helpstring('method ReadXMLFile')],
        HRESULT,
        'ReadXMLFile',
        ([], POINTER(IUnknown), 'pTimeline'),
        ([], BSTR, 'XMLName')
    ),
    COMMETHOD(
        [helpstring('method Delete')],
        HRESULT,
        'Delete',
        ([], POINTER(IUnknown), 'pTimeline'),
        ([], c_double, 'dStart'),
        ([], c_double, 'dEnd')
    ),
    COMMETHOD(
        [helpstring('method WriteXMLPart')],
        HRESULT,
        'WriteXMLPart',
        ([], POINTER(IUnknown), 'pTimeline'),
        ([], c_double, 'dStart'),
        ([], c_double, 'dEnd'),
        ([], BSTR, 'Filename')
    ),
    COMMETHOD(
        [helpstring('method PasteXMLFile')],
        HRESULT,
        'PasteXMLFile',
        ([], POINTER(IUnknown), 'pTimeline'),
        ([], c_double, 'dStart'),
        ([], BSTR, 'Filename')
    ),
    COMMETHOD(
        [helpstring('method CopyXML')],
        HRESULT,
        'CopyXML',
        ([], POINTER(IUnknown), 'pTimeline'),
        ([], c_double, 'dStart'),
        ([], c_double, 'dEnd')
    ),
    COMMETHOD(
        [helpstring('method PasteXML')],
        HRESULT,
        'PasteXML',
        ([], POINTER(IUnknown), 'pTimeline'),
        ([], c_double, 'dStart')
    ),
    COMMETHOD([helpstring('method Reset')], HRESULT, 'Reset'),
    COMMETHOD(
        [helpstring('method ReadXML')],
        HRESULT,
        'ReadXML',
        ([], POINTER(IUnknown), 'pTimeline'),
        ([], POINTER(IUnknown), 'pxml')
    ),
    COMMETHOD(
        [helpstring('method WriteXML')],
        HRESULT,
        'WriteXML',
        ([], POINTER(IUnknown), 'pTimeline'),
        ([], POINTER(BSTR), 'pbstrXML')
    ),
]

################################################################
# code template for IXml2Dex implementation
# class IXml2Dex_Impl(object):
#     def CreateGraphFromFile(self, pTimeline, Filename):
#         'method CreateGraphFromFile'
#         #return ppGraph
#
#     def WriteGrfFile(self, pGraph, Filename):
#         'method WriteGrfFile'
#         #return 
#
#     def WriteXMLFile(self, pTimeline, Filename):
#         'method WriteXMLFile'
#         #return 
#
#     def ReadXMLFile(self, pTimeline, XMLName):
#         'method ReadXMLFile'
#         #return 
#
#     def Delete(self, pTimeline, dStart, dEnd):
#         'method Delete'
#         #return 
#
#     def WriteXMLPart(self, pTimeline, dStart, dEnd, Filename):
#         'method WriteXMLPart'
#         #return 
#
#     def PasteXMLFile(self, pTimeline, dStart, Filename):
#         'method PasteXMLFile'
#         #return 
#
#     def CopyXML(self, pTimeline, dStart, dEnd):
#         'method CopyXML'
#         #return 
#
#     def PasteXML(self, pTimeline, dStart):
#         'method PasteXML'
#         #return 
#
#     def Reset(self):
#         'method Reset'
#         #return 
#
#     def ReadXML(self, pTimeline, pxml):
#         'method ReadXML'
#         #return 
#
#     def WriteXML(self, pTimeline, pbstrXML):
#         'method WriteXML'
#         #return 
#

__MIDL___MIDL_itf_qedit_0000_0000_0002._fields_ = [
    ('Name', BSTR),
    ('dispID', c_int),
    ('nValues', c_int),
]

assert sizeof(__MIDL___MIDL_itf_qedit_0000_0000_0002) == 16, sizeof(__MIDL___MIDL_itf_qedit_0000_0000_0002)
assert alignment(__MIDL___MIDL_itf_qedit_0000_0000_0002) == 8, alignment(__MIDL___MIDL_itf_qedit_0000_0000_0002)


class AMTimelineSrc(CoClass):
    """IAMTimelineSrc Class"""
    _reg_clsid_ = GUID('{78530B7A-61F9-11D2-8CAD-00A024580902}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


class IAMTimelineSplittable(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IAMTimelineSplittable Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{A0F840A0-D590-11D2-8D55-00A0C9441E20}')
    _idlflags_ = []


AMTimelineSrc._com_interfaces_ = [IAMTimelineSrc, IAMTimelineObj, IAMTimelineEffectable, IAMTimelineSplittable]


class SampleGrabber(CoClass):
    """MsGrab Class"""
    _reg_clsid_ = GUID('{C1F400A0-3F08-11D3-9F0B-006008039E37}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


class ISampleGrabber(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """ISampleGrabber Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{6B652FFF-11FE-4FCE-92AD-0266B5D7C78F}')
    _idlflags_ = []


SampleGrabber._com_interfaces_ = [ISampleGrabber]

IEnumFilters._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], c_ulong, 'cFilters'),
        (['out'], POINTER(POINTER(IBaseFilter)), 'ppFilter'),
        (['out'], POINTER(c_ulong), 'pcFetched')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], c_ulong, 'cFilters')
    ),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumFilters)), 'ppEnum')
    ),
]

################################################################
# code template for IEnumFilters implementation
# class IEnumFilters_Impl(object):
#     def Next(self, cFilters):
#         '-no docstring-'
#         #return ppFilter, pcFetched
#
#     def Skip(self, cFilters):
#         '-no docstring-'
#         #return 
#
#     def Reset(self):
#         '-no docstring-'
#         #return 
#
#     def Clone(self):
#         '-no docstring-'
#         #return ppEnum
#


class NullRenderer(CoClass):
    """NullRenderer Class"""
    _reg_clsid_ = GUID('{C1F400A4-3F08-11D3-9F0B-006008039E37}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


NullRenderer._com_interfaces_ = [IBaseFilter]

IAMTimelineEffectable._methods_ = [
    COMMETHOD(
        [helpstring('method EffectInsBefore')],
        HRESULT,
        'EffectInsBefore',
        ([], POINTER(IAMTimelineObj), 'pFX'),
        ([], c_int, 'priority')
    ),
    COMMETHOD(
        [helpstring('method EffectSwapPriorities')],
        HRESULT,
        'EffectSwapPriorities',
        ([], c_int, 'PriorityA'),
        ([], c_int, 'PriorityB')
    ),
    COMMETHOD(
        [helpstring('method EffectGetCount')],
        HRESULT,
        'EffectGetCount',
        ([], POINTER(c_int), 'pCount')
    ),
    COMMETHOD(
        [helpstring('method GetEffect')],
        HRESULT,
        'GetEffect',
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppFx'),
        ([], c_int, 'Which')
    ),
]

################################################################
# code template for IAMTimelineEffectable implementation
# class IAMTimelineEffectable_Impl(object):
#     def EffectInsBefore(self, pFX, priority):
#         'method EffectInsBefore'
#         #return 
#
#     def EffectSwapPriorities(self, PriorityA, PriorityB):
#         'method EffectSwapPriorities'
#         #return 
#
#     def EffectGetCount(self, pCount):
#         'method EffectGetCount'
#         #return 
#
#     def GetEffect(self, Which):
#         'method GetEffect'
#         #return ppFx
#


class DxtCompositor(CoClass):
    """DxtCompositor Class"""
    _reg_clsid_ = GUID('{BB44391D-6ABD-422F-9E2E-385C9DFF51FC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


class IDxtCompositor(IDXEffect):
    """IDxtCompositor Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{BB44391E-6ABD-422F-9E2E-385C9DFF51FC}')
    _idlflags_ = ['dual', 'oleautomation']


DxtCompositor._com_interfaces_ = [IDxtCompositor]


class MediaLocator(CoClass):
    """MediaLocator Class"""
    _reg_clsid_ = GUID('{CC1101F2-79DC-11D2-8CE6-00A0C9441E20}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


MediaLocator._com_interfaces_ = [IMediaLocator]

IDxtCompositor._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property OffsetX'), 'propget'],
        HRESULT,
        'OffsetX',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [dispid(1), helpstring('property OffsetX'), 'propput'],
        HRESULT,
        'OffsetX',
        (['in'], c_int, 'pVal')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property OffsetY'), 'propget'],
        HRESULT,
        'OffsetY',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property OffsetY'), 'propput'],
        HRESULT,
        'OffsetY',
        (['in'], c_int, 'pVal')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property Width'), 'propget'],
        HRESULT,
        'Width',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property Width'), 'propput'],
        HRESULT,
        'Width',
        (['in'], c_int, 'pVal')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property Height'), 'propget'],
        HRESULT,
        'Height',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property Height'), 'propput'],
        HRESULT,
        'Height',
        (['in'], c_int, 'pVal')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property SrcOffsetX'), 'propget'],
        HRESULT,
        'SrcOffsetX',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property SrcOffsetX'), 'propput'],
        HRESULT,
        'SrcOffsetX',
        (['in'], c_int, 'pVal')
    ),
    COMMETHOD(
        [dispid(6), helpstring('property SrcOffsetY'), 'propget'],
        HRESULT,
        'SrcOffsetY',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [dispid(6), helpstring('property SrcOffsetY'), 'propput'],
        HRESULT,
        'SrcOffsetY',
        (['in'], c_int, 'pVal')
    ),
    COMMETHOD(
        [dispid(7), helpstring('property SrcWidth'), 'propget'],
        HRESULT,
        'SrcWidth',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [dispid(7), helpstring('property SrcWidth'), 'propput'],
        HRESULT,
        'SrcWidth',
        (['in'], c_int, 'pVal')
    ),
    COMMETHOD(
        [dispid(8), helpstring('property SrcHeight'), 'propget'],
        HRESULT,
        'SrcHeight',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [dispid(8), helpstring('property SrcHeight'), 'propput'],
        HRESULT,
        'SrcHeight',
        (['in'], c_int, 'pVal')
    ),
]

################################################################
# code template for IDxtCompositor implementation
# class IDxtCompositor_Impl(object):
#     def _get(self):
#         'property OffsetX'
#         #return pVal
#     def _set(self, pVal):
#         'property OffsetX'
#     OffsetX = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property OffsetY'
#         #return pVal
#     def _set(self, pVal):
#         'property OffsetY'
#     OffsetY = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property Width'
#         #return pVal
#     def _set(self, pVal):
#         'property Width'
#     Width = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property Height'
#         #return pVal
#     def _set(self, pVal):
#         'property Height'
#     Height = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property SrcOffsetX'
#         #return pVal
#     def _set(self, pVal):
#         'property SrcOffsetX'
#     SrcOffsetX = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property SrcOffsetY'
#         #return pVal
#     def _set(self, pVal):
#         'property SrcOffsetY'
#     SrcOffsetY = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property SrcWidth'
#         #return pVal
#     def _set(self, pVal):
#         'property SrcWidth'
#     SrcWidth = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property SrcHeight'
#         #return pVal
#     def _set(self, pVal):
#         'property SrcHeight'
#     SrcHeight = property(_get, _set, doc = _set.__doc__)
#

__MIDL___MIDL_itf_qedit_0000_0000_0003._fields_ = [
    ('v', VARIANT),
    ('rt', c_longlong),
    ('dwInterp', c_ulong),
]

assert sizeof(__MIDL___MIDL_itf_qedit_0000_0000_0003) == 40, sizeof(__MIDL___MIDL_itf_qedit_0000_0000_0003)
assert alignment(__MIDL___MIDL_itf_qedit_0000_0000_0003) == 8, alignment(__MIDL___MIDL_itf_qedit_0000_0000_0003)


class AMTimelineGroup(CoClass):
    _reg_clsid_ = GUID('{F6D371E1-B8A6-11D2-8023-00C0DF10D434}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


AMTimelineGroup._com_interfaces_ = [IAMTimelineGroup, IAMTimelineComp, IAMTimelineObj]


class IPersistStream(IPersist):
    _case_insensitive_ = True
    _iid_ = GUID('{00000109-0000-0000-C000-000000000046}')
    _idlflags_ = []


class ISequentialStream(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0C733A30-2A1C-11CE-ADE5-00AA0044773D}')
    _idlflags_ = []


class IStream(ISequentialStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000C-0000-0000-C000-000000000046}')
    _idlflags_ = []


IPersistStream._methods_ = [
    COMMETHOD([], HRESULT, 'IsDirty'),
    COMMETHOD(
        [],
        HRESULT,
        'Load',
        (['in'], POINTER(IStream), 'pstm')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Save',
        (['in'], POINTER(IStream), 'pstm'),
        (['in'], c_int, 'fClearDirty')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSizeMax',
        (['out'], POINTER(_ULARGE_INTEGER), 'pcbSize')
    ),
]

################################################################
# code template for IPersistStream implementation
# class IPersistStream_Impl(object):
#     def IsDirty(self):
#         '-no docstring-'
#         #return 
#
#     def Load(self, pstm):
#         '-no docstring-'
#         #return 
#
#     def Save(self, pstm, fClearDirty):
#         '-no docstring-'
#         #return 
#
#     def GetSizeMax(self):
#         '-no docstring-'
#         #return pcbSize
#


class AMTimelineTrans(CoClass):
    _reg_clsid_ = GUID('{74D2EC81-6233-11D2-8CAD-00A024580902}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


class IAMTimelineTrans(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IAMTimelineTrans Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{BCE0C265-622D-11D2-8CAD-00A024580902}')
    _idlflags_ = []


AMTimelineTrans._com_interfaces_ = [IAMTimelineTrans, IAMTimelineObj, IAMTimelineSplittable]

IAMTimelineSplittable._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SplitAt',
        ([], c_longlong, 'Time')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SplitAt2',
        ([], c_double, 'Time')
    ),
]

################################################################
# code template for IAMTimelineSplittable implementation
# class IAMTimelineSplittable_Impl(object):
#     def SplitAt(self, Time):
#         '-no docstring-'
#         #return 
#
#     def SplitAt2(self, Time):
#         '-no docstring-'
#         #return 
#


class PropertySetter(CoClass):
    """Varying Property Holder"""
    _reg_clsid_ = GUID('{ADF95821-DED7-11D2-ACBE-0080C75E246E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


PropertySetter._com_interfaces_ = [IPropertySetter, IAMSetErrorLog]

IAMTimelineTrans._methods_ = [
    COMMETHOD(
        [helpstring('method GetCutPoint')],
        HRESULT,
        'GetCutPoint',
        ([], POINTER(c_longlong), 'pTLTime')
    ),
    COMMETHOD(
        [helpstring('method GetCutPoint2')],
        HRESULT,
        'GetCutPoint2',
        ([], POINTER(c_double), 'pTLTime')
    ),
    COMMETHOD(
        [helpstring('method SetCutPoint')],
        HRESULT,
        'SetCutPoint',
        ([], c_longlong, 'TLTime')
    ),
    COMMETHOD(
        [helpstring('method SetCutPoint2')],
        HRESULT,
        'SetCutPoint2',
        ([], c_double, 'TLTime')
    ),
    COMMETHOD(
        [helpstring('method GetSwapInputs')],
        HRESULT,
        'GetSwapInputs',
        ([], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method SetSwapInputs')],
        HRESULT,
        'SetSwapInputs',
        ([], c_int, 'pVal')
    ),
    COMMETHOD(
        [helpstring('method GetCutsOnly')],
        HRESULT,
        'GetCutsOnly',
        ([], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method SetCutsOnly')],
        HRESULT,
        'SetCutsOnly',
        ([], c_int, 'pVal')
    ),
]

################################################################
# code template for IAMTimelineTrans implementation
# class IAMTimelineTrans_Impl(object):
#     def GetCutPoint(self, pTLTime):
#         'method GetCutPoint'
#         #return 
#
#     def GetCutPoint2(self, pTLTime):
#         'method GetCutPoint2'
#         #return 
#
#     def SetCutPoint(self, TLTime):
#         'method SetCutPoint'
#         #return 
#
#     def SetCutPoint2(self, TLTime):
#         'method SetCutPoint2'
#         #return 
#
#     def GetSwapInputs(self, pVal):
#         'method GetSwapInputs'
#         #return 
#
#     def SetSwapInputs(self, pVal):
#         'method SetSwapInputs'
#         #return 
#
#     def GetCutsOnly(self, pVal):
#         'method GetCutsOnly'
#         #return 
#
#     def SetCutsOnly(self, pVal):
#         'method SetCutsOnly'
#         #return 
#

IEnumPins._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], c_ulong, 'cPins'),
        (['out'], POINTER(POINTER(IPin)), 'ppPins'),
        (['out'], POINTER(c_ulong), 'pcFetched')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], c_ulong, 'cPins')
    ),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumPins)), 'ppEnum')
    ),
]

################################################################
# code template for IEnumPins implementation
# class IEnumPins_Impl(object):
#     def Next(self, cPins):
#         '-no docstring-'
#         #return ppPins, pcFetched
#
#     def Skip(self, cPins):
#         '-no docstring-'
#         #return 
#
#     def Reset(self):
#         '-no docstring-'
#         #return 
#
#     def Clone(self):
#         '-no docstring-'
#         #return ppEnum
#


class MediaDet(CoClass):
    """MediaDet Class"""
    _reg_clsid_ = GUID('{65BD0711-24D2-4FF7-9324-ED2E5D3ABAFA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


class IMediaDet(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IMediaDet Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{65BD0710-24D2-4FF7-9324-ED2E5D3ABAFA}')
    _idlflags_ = []


MediaDet._com_interfaces_ = [IMediaDet]

IMediaDet._methods_ = [
    COMMETHOD(
        ['propget', helpstring('property Filter')],
        HRESULT,
        'Filter',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'pVal')
    ),
    COMMETHOD(
        ['propput', helpstring('property Filter')],
        HRESULT,
        'Filter',
        (['in'], POINTER(IUnknown), 'pVal')
    ),
    COMMETHOD(
        ['propget', helpstring('property OutputStreams')],
        HRESULT,
        'OutputStreams',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        ['propget', helpstring('property CurrentStream')],
        HRESULT,
        'CurrentStream',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        ['propput', helpstring('property CurrentStream')],
        HRESULT,
        'CurrentStream',
        (['in'], c_int, 'pVal')
    ),
    COMMETHOD(
        ['propget', helpstring('property StreamType')],
        HRESULT,
        'StreamType',
        (
            ['out', 'retval'],
            POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
            'pVal',
        )
    ),
    COMMETHOD(
        ['propget', helpstring('property StreamTypeB')],
        HRESULT,
        'StreamTypeB',
        (['out', 'retval'], POINTER(BSTR), 'pVal')
    ),
    COMMETHOD(
        ['propget', helpstring('property StreamLength')],
        HRESULT,
        'StreamLength',
        (['out', 'retval'], POINTER(c_double), 'pVal')
    ),
    COMMETHOD(
        ['propget', helpstring('property Filename')],
        HRESULT,
        'Filename',
        (['out', 'retval'], POINTER(BSTR), 'pVal')
    ),
    COMMETHOD(
        ['propput', helpstring('property Filename')],
        HRESULT,
        'Filename',
        (['in'], BSTR, 'pVal')
    ),
    COMMETHOD(
        [helpstring('method GetBitmapBits')],
        HRESULT,
        'GetBitmapBits',
        ([], c_double, 'streamTime'),
        ([], POINTER(c_int), 'pBufferSize'),
        ([], POINTER(c_ubyte), 'pBuffer'),
        ([], c_int, 'Width'),
        ([], c_int, 'Height')
    ),
    COMMETHOD(
        [helpstring('method WriteBitmapBits')],
        HRESULT,
        'WriteBitmapBits',
        ([], c_double, 'streamTime'),
        ([], c_int, 'Width'),
        ([], c_int, 'Height'),
        ([], BSTR, 'Filename')
    ),
    COMMETHOD(
        ['propget', helpstring('property StreamMediaType')],
        HRESULT,
        'StreamMediaType',
        (['out', 'retval'], POINTER(_AMMediaType), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method GetSampleGrabber')],
        HRESULT,
        'GetSampleGrabber',
        (['out'], POINTER(POINTER(ISampleGrabber)), 'ppVal')
    ),
    COMMETHOD(
        ['propget', helpstring('property FrameRate')],
        HRESULT,
        'FrameRate',
        (['out', 'retval'], POINTER(c_double), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method EnterBitmapGrabMode')],
        HRESULT,
        'EnterBitmapGrabMode',
        ([], c_double, 'SeekTime')
    ),
]

################################################################
# code template for IMediaDet implementation
# class IMediaDet_Impl(object):
#     def _get(self):
#         'property Filter'
#         #return pVal
#     def _set(self, pVal):
#         'property Filter'
#     Filter = property(_get, _set, doc = _set.__doc__)
#
#     @property
#     def OutputStreams(self):
#         'property OutputStreams'
#         #return pVal
#
#     def _get(self):
#         'property CurrentStream'
#         #return pVal
#     def _set(self, pVal):
#         'property CurrentStream'
#     CurrentStream = property(_get, _set, doc = _set.__doc__)
#
#     @property
#     def StreamType(self):
#         'property StreamType'
#         #return pVal
#
#     @property
#     def StreamTypeB(self):
#         'property StreamTypeB'
#         #return pVal
#
#     @property
#     def StreamLength(self):
#         'property StreamLength'
#         #return pVal
#
#     def _get(self):
#         'property Filename'
#         #return pVal
#     def _set(self, pVal):
#         'property Filename'
#     Filename = property(_get, _set, doc = _set.__doc__)
#
#     def GetBitmapBits(self, streamTime, pBufferSize, pBuffer, Width, Height):
#         'method GetBitmapBits'
#         #return 
#
#     def WriteBitmapBits(self, streamTime, Width, Height, Filename):
#         'method WriteBitmapBits'
#         #return 
#
#     @property
#     def StreamMediaType(self):
#         'property StreamMediaType'
#         #return pVal
#
#     def GetSampleGrabber(self):
#         'method GetSampleGrabber'
#         #return ppVal
#
#     @property
#     def FrameRate(self):
#         'property FrameRate'
#         #return pVal
#
#     def EnterBitmapGrabMode(self, SeekTime):
#         'method EnterBitmapGrabMode'
#         #return 
#


class AMTimelineTrack(CoClass):
    _reg_clsid_ = GUID('{8F6C3C50-897B-11D2-8CFB-00A0C9441E20}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


class IAMTimelineTrack(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IAMTimelineTrack Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{EAE58538-622E-11D2-8CAD-00A024580902}')
    _idlflags_ = []


AMTimelineTrack._com_interfaces_ = [IAMTimelineTrack, IAMTimelineObj, IAMTimelineEffectable, IAMTimelineTransable, IAMTimelineVirtualTrack, IAMTimelineSplittable]

IAMTimelineSrc._methods_ = [
    COMMETHOD(
        [helpstring('method GetMediaTimes')],
        HRESULT,
        'GetMediaTimes',
        ([], POINTER(c_longlong), 'pStart'),
        ([], POINTER(c_longlong), 'pStop')
    ),
    COMMETHOD(
        [helpstring('method GetMediaTimes2')],
        HRESULT,
        'GetMediaTimes2',
        ([], POINTER(c_double), 'pStart'),
        ([], POINTER(c_double), 'pStop')
    ),
    COMMETHOD(
        [helpstring('method ModifyStopTime')],
        HRESULT,
        'ModifyStopTime',
        ([], c_longlong, 'Stop')
    ),
    COMMETHOD(
        [helpstring('method ModifyStopTime2')],
        HRESULT,
        'ModifyStopTime2',
        ([], c_double, 'Stop')
    ),
    COMMETHOD(
        [helpstring('method FixMediaTimes')],
        HRESULT,
        'FixMediaTimes',
        ([], POINTER(c_longlong), 'pStart'),
        ([], POINTER(c_longlong), 'pStop')
    ),
    COMMETHOD(
        [helpstring('method FixMediaTimes2')],
        HRESULT,
        'FixMediaTimes2',
        ([], POINTER(c_double), 'pStart'),
        ([], POINTER(c_double), 'pStop')
    ),
    COMMETHOD(
        [helpstring('method SetMediaTimes')],
        HRESULT,
        'SetMediaTimes',
        ([], c_longlong, 'Start'),
        ([], c_longlong, 'Stop')
    ),
    COMMETHOD(
        [helpstring('method SetMediaTimes2')],
        HRESULT,
        'SetMediaTimes2',
        ([], c_double, 'Start'),
        ([], c_double, 'Stop')
    ),
    COMMETHOD(
        [helpstring('method SetMediaLength')],
        HRESULT,
        'SetMediaLength',
        ([], c_longlong, 'Length')
    ),
    COMMETHOD(
        [helpstring('method SetMediaLength2')],
        HRESULT,
        'SetMediaLength2',
        ([], c_double, 'Length')
    ),
    COMMETHOD(
        [helpstring('method GetMediaLength')],
        HRESULT,
        'GetMediaLength',
        ([], POINTER(c_longlong), 'pLength')
    ),
    COMMETHOD(
        [helpstring('method GetMediaLength2')],
        HRESULT,
        'GetMediaLength2',
        ([], POINTER(c_double), 'pLength')
    ),
    COMMETHOD(
        [helpstring('method GetMediaName')],
        HRESULT,
        'GetMediaName',
        (['out', 'retval'], POINTER(BSTR), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method SetMediaName')],
        HRESULT,
        'SetMediaName',
        ([], BSTR, 'newVal')
    ),
    COMMETHOD(
        [helpstring('method SpliceWithNext')],
        HRESULT,
        'SpliceWithNext',
        ([], POINTER(IAMTimelineObj), 'pNext')
    ),
    COMMETHOD(
        [helpstring('method GetStreamNumber')],
        HRESULT,
        'GetStreamNumber',
        ([], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method SetStreamNumber')],
        HRESULT,
        'SetStreamNumber',
        ([], c_int, 'Val')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsNormalRate',
        ([], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method GetDefaultFPS')],
        HRESULT,
        'GetDefaultFPS',
        ([], POINTER(c_double), 'pFPS')
    ),
    COMMETHOD(
        [helpstring('method SetDefaultFPS')],
        HRESULT,
        'SetDefaultFPS',
        ([], c_double, 'FPS')
    ),
    COMMETHOD(
        [helpstring('method GetStretchMode')],
        HRESULT,
        'GetStretchMode',
        ([], POINTER(c_int), 'pnStretchMode')
    ),
    COMMETHOD(
        [helpstring('method SetStretchMode')],
        HRESULT,
        'SetStretchMode',
        ([], c_int, 'nStretchMode')
    ),
]

################################################################
# code template for IAMTimelineSrc implementation
# class IAMTimelineSrc_Impl(object):
#     def GetMediaTimes(self, pStart, pStop):
#         'method GetMediaTimes'
#         #return 
#
#     def GetMediaTimes2(self, pStart, pStop):
#         'method GetMediaTimes2'
#         #return 
#
#     def ModifyStopTime(self, Stop):
#         'method ModifyStopTime'
#         #return 
#
#     def ModifyStopTime2(self, Stop):
#         'method ModifyStopTime2'
#         #return 
#
#     def FixMediaTimes(self, pStart, pStop):
#         'method FixMediaTimes'
#         #return 
#
#     def FixMediaTimes2(self, pStart, pStop):
#         'method FixMediaTimes2'
#         #return 
#
#     def SetMediaTimes(self, Start, Stop):
#         'method SetMediaTimes'
#         #return 
#
#     def SetMediaTimes2(self, Start, Stop):
#         'method SetMediaTimes2'
#         #return 
#
#     def SetMediaLength(self, Length):
#         'method SetMediaLength'
#         #return 
#
#     def SetMediaLength2(self, Length):
#         'method SetMediaLength2'
#         #return 
#
#     def GetMediaLength(self, pLength):
#         'method GetMediaLength'
#         #return 
#
#     def GetMediaLength2(self, pLength):
#         'method GetMediaLength2'
#         #return 
#
#     def GetMediaName(self):
#         'method GetMediaName'
#         #return pVal
#
#     def SetMediaName(self, newVal):
#         'method SetMediaName'
#         #return 
#
#     def SpliceWithNext(self, pNext):
#         'method SpliceWithNext'
#         #return 
#
#     def GetStreamNumber(self, pVal):
#         'method GetStreamNumber'
#         #return 
#
#     def SetStreamNumber(self, Val):
#         'method SetStreamNumber'
#         #return 
#
#     def IsNormalRate(self, pVal):
#         '-no docstring-'
#         #return 
#
#     def GetDefaultFPS(self, pFPS):
#         'method GetDefaultFPS'
#         #return 
#
#     def SetDefaultFPS(self, FPS):
#         'method SetDefaultFPS'
#         #return 
#
#     def GetStretchMode(self, pnStretchMode):
#         'method GetStretchMode'
#         #return 
#
#     def SetStretchMode(self, nStretchMode):
#         'method SetStretchMode'
#         #return 
#

IAMTimelineTrack._methods_ = [
    COMMETHOD(
        [helpstring('method SrcAdd')],
        HRESULT,
        'SrcAdd',
        ([], POINTER(IAMTimelineObj), 'pSource')
    ),
    COMMETHOD(
        [helpstring('method GetNextSrc')],
        HRESULT,
        'GetNextSrc',
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppSrc'),
        ([], POINTER(c_longlong), 'pInOut')
    ),
    COMMETHOD(
        [helpstring('method GetNextSrc2')],
        HRESULT,
        'GetNextSrc2',
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppSrc'),
        ([], POINTER(c_double), 'pInOut')
    ),
    COMMETHOD(
        [helpstring('method MoveEverythingBy')],
        HRESULT,
        'MoveEverythingBy',
        ([], c_longlong, 'Start'),
        ([], c_longlong, 'MoveBy')
    ),
    COMMETHOD(
        [helpstring('method MoveEverythingBy2')],
        HRESULT,
        'MoveEverythingBy2',
        ([], c_double, 'Start'),
        ([], c_double, 'MoveBy')
    ),
    COMMETHOD(
        [helpstring('method GetSourcesCount')],
        HRESULT,
        'GetSourcesCount',
        ([], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method AreYouBlank')],
        HRESULT,
        'AreYouBlank',
        ([], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [helpstring('method GetSrcAtTime')],
        HRESULT,
        'GetSrcAtTime',
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppSrc'),
        ([], c_longlong, 'Time'),
        ([], c_int, 'SearchDirection')
    ),
    COMMETHOD(
        [helpstring('method GetSrcAtTime2')],
        HRESULT,
        'GetSrcAtTime2',
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppSrc'),
        ([], c_double, 'Time'),
        ([], c_int, 'SearchDirection')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'InsertSpace',
        ([], c_longlong, 'rtStart'),
        ([], c_longlong, 'rtEnd')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'InsertSpace2',
        ([], c_double, 'rtStart'),
        ([], c_double, 'rtEnd')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ZeroBetween',
        ([], c_longlong, 'rtStart'),
        ([], c_longlong, 'rtEnd')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ZeroBetween2',
        ([], c_double, 'rtStart'),
        ([], c_double, 'rtEnd')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetNextSrcEx',
        ([], POINTER(IAMTimelineObj), 'pLast'),
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppNext')
    ),
]

################################################################
# code template for IAMTimelineTrack implementation
# class IAMTimelineTrack_Impl(object):
#     def SrcAdd(self, pSource):
#         'method SrcAdd'
#         #return 
#
#     def GetNextSrc(self, pInOut):
#         'method GetNextSrc'
#         #return ppSrc
#
#     def GetNextSrc2(self, pInOut):
#         'method GetNextSrc2'
#         #return ppSrc
#
#     def MoveEverythingBy(self, Start, MoveBy):
#         'method MoveEverythingBy'
#         #return 
#
#     def MoveEverythingBy2(self, Start, MoveBy):
#         'method MoveEverythingBy2'
#         #return 
#
#     def GetSourcesCount(self, pVal):
#         'method GetSourcesCount'
#         #return 
#
#     def AreYouBlank(self, pVal):
#         'method AreYouBlank'
#         #return 
#
#     def GetSrcAtTime(self, Time, SearchDirection):
#         'method GetSrcAtTime'
#         #return ppSrc
#
#     def GetSrcAtTime2(self, Time, SearchDirection):
#         'method GetSrcAtTime2'
#         #return ppSrc
#
#     def InsertSpace(self, rtStart, rtEnd):
#         '-no docstring-'
#         #return 
#
#     def InsertSpace2(self, rtStart, rtEnd):
#         '-no docstring-'
#         #return 
#
#     def ZeroBetween(self, rtStart, rtEnd):
#         '-no docstring-'
#         #return 
#
#     def ZeroBetween2(self, rtStart, rtEnd):
#         '-no docstring-'
#         #return 
#
#     def GetNextSrcEx(self, pLast):
#         '-no docstring-'
#         #return ppNext
#


class _PinInfo(Structure):
    pass


# values for enumeration '_PinDirection'
PINDIR_INPUT = 0
PINDIR_OUTPUT = 1
_PinDirection = c_int  # enum

IPin._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Connect',
        (['in'], POINTER(IPin), 'pReceivePin'),
        (['in'], POINTER(_AMMediaType), 'pmt')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReceiveConnection',
        (['in'], POINTER(IPin), 'pConnector'),
        (['in'], POINTER(_AMMediaType), 'pmt')
    ),
    COMMETHOD([], HRESULT, 'Disconnect'),
    COMMETHOD(
        [],
        HRESULT,
        'ConnectedTo',
        (['out'], POINTER(POINTER(IPin)), 'pPin')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ConnectionMediaType',
        (['out'], POINTER(_AMMediaType), 'pmt')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryPinInfo',
        (['out'], POINTER(_PinInfo), 'pInfo')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryDirection',
        (['out'], POINTER(_PinDirection), 'pPinDir')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryId',
        (['out'], POINTER(WSTRING), 'Id')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryAccept',
        (['in'], POINTER(_AMMediaType), 'pmt')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumMediaTypes',
        (['out'], POINTER(POINTER(IEnumMediaTypes)), 'ppEnum')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryInternalConnections',
        (['out'], POINTER(POINTER(IPin)), 'apPin'),
        (['in', 'out'], POINTER(c_ulong), 'nPin')
    ),
    COMMETHOD([], HRESULT, 'EndOfStream'),
    COMMETHOD([], HRESULT, 'BeginFlush'),
    COMMETHOD([], HRESULT, 'EndFlush'),
    COMMETHOD(
        [],
        HRESULT,
        'NewSegment',
        (['in'], c_longlong, 'tStart'),
        (['in'], c_longlong, 'tStop'),
        (['in'], c_double, 'dRate')
    ),
]

################################################################
# code template for IPin implementation
# class IPin_Impl(object):
#     def Connect(self, pReceivePin, pmt):
#         '-no docstring-'
#         #return 
#
#     def ReceiveConnection(self, pConnector, pmt):
#         '-no docstring-'
#         #return 
#
#     def Disconnect(self):
#         '-no docstring-'
#         #return 
#
#     def ConnectedTo(self):
#         '-no docstring-'
#         #return pPin
#
#     def ConnectionMediaType(self):
#         '-no docstring-'
#         #return pmt
#
#     def QueryPinInfo(self):
#         '-no docstring-'
#         #return pInfo
#
#     def QueryDirection(self):
#         '-no docstring-'
#         #return pPinDir
#
#     def QueryId(self):
#         '-no docstring-'
#         #return Id
#
#     def QueryAccept(self, pmt):
#         '-no docstring-'
#         #return 
#
#     def EnumMediaTypes(self):
#         '-no docstring-'
#         #return ppEnum
#
#     def QueryInternalConnections(self):
#         '-no docstring-'
#         #return apPin, nPin
#
#     def EndOfStream(self):
#         '-no docstring-'
#         #return 
#
#     def BeginFlush(self):
#         '-no docstring-'
#         #return 
#
#     def EndFlush(self):
#         '-no docstring-'
#         #return 
#
#     def NewSegment(self, tStart, tStop, dRate):
#         '-no docstring-'
#         #return 
#

ISequentialStream._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'RemoteRead',
        (['out'], POINTER(c_ubyte), 'pv'),
        (['in'], c_ulong, 'cb'),
        (['out'], POINTER(c_ulong), 'pcbRead')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoteWrite',
        (['in'], POINTER(c_ubyte), 'pv'),
        (['in'], c_ulong, 'cb'),
        (['out'], POINTER(c_ulong), 'pcbWritten')
    ),
]

################################################################
# code template for ISequentialStream implementation
# class ISequentialStream_Impl(object):
#     def RemoteRead(self, cb):
#         '-no docstring-'
#         #return pv, pcbRead
#
#     def RemoteWrite(self, pv, cb):
#         '-no docstring-'
#         #return pcbWritten
#

IStream._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'RemoteSeek',
        (['in'], _LARGE_INTEGER, 'dlibMove'),
        (['in'], c_ulong, 'dwOrigin'),
        (['out'], POINTER(_ULARGE_INTEGER), 'plibNewPosition')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSize',
        (['in'], _ULARGE_INTEGER, 'libNewSize')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoteCopyTo',
        (['in'], POINTER(IStream), 'pstm'),
        (['in'], _ULARGE_INTEGER, 'cb'),
        (['out'], POINTER(_ULARGE_INTEGER), 'pcbRead'),
        (['out'], POINTER(_ULARGE_INTEGER), 'pcbWritten')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Commit',
        (['in'], c_ulong, 'grfCommitFlags')
    ),
    COMMETHOD([], HRESULT, 'Revert'),
    COMMETHOD(
        [],
        HRESULT,
        'LockRegion',
        (['in'], _ULARGE_INTEGER, 'libOffset'),
        (['in'], _ULARGE_INTEGER, 'cb'),
        (['in'], c_ulong, 'dwLockType')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnlockRegion',
        (['in'], _ULARGE_INTEGER, 'libOffset'),
        (['in'], _ULARGE_INTEGER, 'cb'),
        (['in'], c_ulong, 'dwLockType')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Stat',
        (['out'], POINTER(tagSTATSTG), 'pstatstg'),
        (['in'], c_ulong, 'grfStatFlag')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IStream)), 'ppstm')
    ),
]

################################################################
# code template for IStream implementation
# class IStream_Impl(object):
#     def RemoteSeek(self, dlibMove, dwOrigin):
#         '-no docstring-'
#         #return plibNewPosition
#
#     def SetSize(self, libNewSize):
#         '-no docstring-'
#         #return 
#
#     def RemoteCopyTo(self, pstm, cb):
#         '-no docstring-'
#         #return pcbRead, pcbWritten
#
#     def Commit(self, grfCommitFlags):
#         '-no docstring-'
#         #return 
#
#     def Revert(self):
#         '-no docstring-'
#         #return 
#
#     def LockRegion(self, libOffset, cb, dwLockType):
#         '-no docstring-'
#         #return 
#
#     def UnlockRegion(self, libOffset, cb, dwLockType):
#         '-no docstring-'
#         #return 
#
#     def Stat(self, grfStatFlag):
#         '-no docstring-'
#         #return pstatstg
#
#     def Clone(self):
#         '-no docstring-'
#         #return ppstm
#


class AMTimelineEffect(CoClass):
    _reg_clsid_ = GUID('{74D2EC82-6233-11D2-8CAD-00A024580902}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


class IAMTimelineEffect(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IAMTimelineEffect Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{BCE0C264-622D-11D2-8CAD-00A024580902}')
    _idlflags_ = []


AMTimelineEffect._com_interfaces_ = [IAMTimelineEffect, IAMTimelineObj, IAMTimelineSplittable, IPropertyBag]

_AMMediaType._fields_ = [
    ('majortype', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('subtype', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('bFixedSizeSamples', c_int),
    ('bTemporalCompression', c_int),
    ('lSampleSize', c_ulong),
    ('formattype', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('pUnk', POINTER(IUnknown)),
    ('cbFormat', c_ulong),
    ('pbFormat', POINTER(c_ubyte)),
]

assert sizeof(_AMMediaType) == 88, sizeof(_AMMediaType)
assert alignment(_AMMediaType) == 8, alignment(_AMMediaType)

IAMTimelineEffect._methods_ = [
    COMMETHOD(
        [helpstring('method EffectGetPriority')],
        HRESULT,
        'EffectGetPriority',
        ([], POINTER(c_int), 'pVal')
    ),
]

################################################################
# code template for IAMTimelineEffect implementation
# class IAMTimelineEffect_Impl(object):
#     def EffectGetPriority(self, pVal):
#         'method EffectGetPriority'
#         #return 
#


class AMTimeline(CoClass):
    """AMTimeline Class"""
    _reg_clsid_ = GUID('{78530B75-61F9-11D2-8CAD-00A024580902}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


AMTimeline._com_interfaces_ = [IAMTimeline, IPersistStream, IAMSetErrorLog]


class IDxtAlphaSetter(IDXEffect):
    """IDxtAlphaSetter Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{4EE9EAD9-DA4D-43D0-9383-06B90C08B12B}')
    _idlflags_ = ['dual', 'oleautomation']


IDxtAlphaSetter._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property Alpha'), 'propget'],
        HRESULT,
        'Alpha',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [dispid(1), helpstring('property Alpha'), 'propput'],
        HRESULT,
        'Alpha',
        (['in'], c_int, 'pVal')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property AlphaRamp'), 'propget'],
        HRESULT,
        'AlphaRamp',
        (['out', 'retval'], POINTER(c_double), 'pVal')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property AlphaRamp'), 'propput'],
        HRESULT,
        'AlphaRamp',
        (['in'], c_double, 'pVal')
    ),
]

################################################################
# code template for IDxtAlphaSetter implementation
# class IDxtAlphaSetter_Impl(object):
#     def _get(self):
#         'property Alpha'
#         #return pVal
#     def _set(self, pVal):
#         'property Alpha'
#     Alpha = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property AlphaRamp'
#         #return pVal
#     def _set(self, pVal):
#         'property AlphaRamp'
#     AlphaRamp = property(_get, _set, doc = _set.__doc__)
#


class Library(object):
    """Dexter 1.0 Type Library"""
    name = 'DexterLib'
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


_PinInfo._fields_ = [
    ('pFilter', POINTER(IBaseFilter)),
    ('dir', _PinDirection),
    ('achName', c_ushort * 128),
]

assert sizeof(_PinInfo) == 272, sizeof(_PinInfo)
assert alignment(_PinInfo) == 8, alignment(_PinInfo)


class DxtAlphaSetter(CoClass):
    """DxtAlphaSetter Class"""
    _reg_clsid_ = GUID('{506D89AE-909A-44F7-9444-ABD575896E35}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


DxtAlphaSetter._com_interfaces_ = [IDxtAlphaSetter]


class RenderEngine(CoClass):
    _reg_clsid_ = GUID('{64D8A8E0-80A2-11D2-8CF3-00A0C9441E20}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


RenderEngine._com_interfaces_ = [IRenderEngine, IRenderEngine2, IAMSetErrorLog]


class IResize(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """IResize Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{4ADA63A0-72D5-11D2-952A-0060081840BC}')
    _idlflags_ = []


IResize._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'get_Size',
        (['out'], POINTER(c_int), 'piHeight'),
        (['out'], POINTER(c_int), 'piWidth'),
        (['out'], POINTER(c_int), 'pFlag')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_InputSize',
        (['out'], POINTER(c_int), 'piHeight'),
        (['out'], POINTER(c_int), 'piWidth')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Size',
        (['in'], c_int, 'Height'),
        (['in'], c_int, 'Width'),
        (['in'], c_int, 'Flag')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_MediaType',
        (['out'], POINTER(_AMMediaType), 'pmt')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_MediaType',
        (['in'], POINTER(_AMMediaType), 'pmt')
    ),
]

################################################################
# code template for IResize implementation
# class IResize_Impl(object):
#     def get_Size(self):
#         '-no docstring-'
#         #return piHeight, piWidth, pFlag
#
#     def get_InputSize(self):
#         '-no docstring-'
#         #return piHeight, piWidth
#
#     def put_Size(self, Height, Width, Flag):
#         '-no docstring-'
#         #return 
#
#     def get_MediaType(self):
#         '-no docstring-'
#         #return pmt
#
#     def put_MediaType(self, pmt):
#         '-no docstring-'
#         #return 
#


class IGrfCache(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IGrfCache Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{AE9472BE-B0C3-11D2-8D24-00A0C9441E20}')
    _idlflags_ = []


IGrfCache._methods_ = [
    COMMETHOD(
        [helpstring('method AddFilter')],
        HRESULT,
        'AddFilter',
        ([], POINTER(IGrfCache), 'ChainedCache'),
        ([], c_longlong, 'Id'),
        ([], POINTER(IBaseFilter), 'pFilter'),
        ([], WSTRING, 'pName')
    ),
    COMMETHOD(
        [helpstring('method ConnectPins')],
        HRESULT,
        'ConnectPins',
        ([], POINTER(IGrfCache), 'ChainedCache'),
        ([], c_longlong, 'PinID1'),
        ([], POINTER(IPin), 'pPin1'),
        ([], c_longlong, 'PinID2'),
        ([], POINTER(IPin), 'pPin2')
    ),
    COMMETHOD(
        [helpstring('method SetGraph')],
        HRESULT,
        'SetGraph',
        ([], POINTER(IGraphBuilder), 'pGraph')
    ),
    COMMETHOD(
        [helpstring('method DoConnectionsNow')],
        HRESULT,
        'DoConnectionsNow',
    ),
]

################################################################
# code template for IGrfCache implementation
# class IGrfCache_Impl(object):
#     def AddFilter(self, ChainedCache, Id, pFilter, pName):
#         'method AddFilter'
#         #return 
#
#     def ConnectPins(self, ChainedCache, PinID1, pPin1, PinID2, pPin2):
#         'method ConnectPins'
#         #return 
#
#     def SetGraph(self, pGraph):
#         'method SetGraph'
#         #return 
#
#     def DoConnectionsNow(self):
#         'method DoConnectionsNow'
#         #return 
#


class IDxtJpeg(IDXEffect):
    """IDxtJpeg Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{DE75D011-7A65-11D2-8CEA-00A0C9441E20}')
    _idlflags_ = ['dual', 'oleautomation']


IDxtJpeg._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property MaskNum'), 'propget'],
        HRESULT,
        'MaskNum',
        (['out', 'retval'], POINTER(c_int), '__MIDL__IDxtJpeg0000')
    ),
    COMMETHOD(
        [dispid(1), helpstring('property MaskNum'), 'propput'],
        HRESULT,
        'MaskNum',
        (['in'], c_int, '__MIDL__IDxtJpeg0000')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property MaskName'), 'propget'],
        HRESULT,
        'MaskName',
        (['out', 'retval'], POINTER(BSTR), 'pVal')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property MaskName'), 'propput'],
        HRESULT,
        'MaskName',
        (['in'], BSTR, 'pVal')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property ScaleX'), 'propget'],
        HRESULT,
        'ScaleX',
        (['out', 'retval'], POINTER(c_double), '__MIDL__IDxtJpeg0002')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property ScaleX'), 'propput'],
        HRESULT,
        'ScaleX',
        (['in'], c_double, '__MIDL__IDxtJpeg0002')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property ScaleY'), 'propget'],
        HRESULT,
        'ScaleY',
        (['out', 'retval'], POINTER(c_double), '__MIDL__IDxtJpeg0004')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property ScaleY'), 'propput'],
        HRESULT,
        'ScaleY',
        (['in'], c_double, '__MIDL__IDxtJpeg0004')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property OffsetX'), 'propget'],
        HRESULT,
        'OffsetX',
        (['out', 'retval'], POINTER(c_int), '__MIDL__IDxtJpeg0006')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property OffsetX'), 'propput'],
        HRESULT,
        'OffsetX',
        (['in'], c_int, '__MIDL__IDxtJpeg0006')
    ),
    COMMETHOD(
        [dispid(6), helpstring('property OffsetY'), 'propget'],
        HRESULT,
        'OffsetY',
        (['out', 'retval'], POINTER(c_int), '__MIDL__IDxtJpeg0008')
    ),
    COMMETHOD(
        [dispid(6), helpstring('property OffsetY'), 'propput'],
        HRESULT,
        'OffsetY',
        (['in'], c_int, '__MIDL__IDxtJpeg0008')
    ),
    COMMETHOD(
        [dispid(7), helpstring('property ReplicateX'), 'propget'],
        HRESULT,
        'ReplicateX',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [dispid(7), helpstring('property ReplicateX'), 'propput'],
        HRESULT,
        'ReplicateX',
        (['in'], c_int, 'pVal')
    ),
    COMMETHOD(
        [dispid(8), helpstring('property ReplicateY'), 'propget'],
        HRESULT,
        'ReplicateY',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [dispid(8), helpstring('property ReplicateY'), 'propput'],
        HRESULT,
        'ReplicateY',
        (['in'], c_int, 'pVal')
    ),
    COMMETHOD(
        [dispid(9), helpstring('property BorderColor'), 'propget'],
        HRESULT,
        'BorderColor',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [dispid(9), helpstring('property BorderColor'), 'propput'],
        HRESULT,
        'BorderColor',
        (['in'], c_int, 'pVal')
    ),
    COMMETHOD(
        [dispid(10), helpstring('property BorderWidth'), 'propget'],
        HRESULT,
        'BorderWidth',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [dispid(10), helpstring('property BorderWidth'), 'propput'],
        HRESULT,
        'BorderWidth',
        (['in'], c_int, 'pVal')
    ),
    COMMETHOD(
        [dispid(11), helpstring('property BorderSoftness'), 'propget'],
        HRESULT,
        'BorderSoftness',
        (['out', 'retval'], POINTER(c_int), 'pVal')
    ),
    COMMETHOD(
        [dispid(11), helpstring('property BorderSoftness'), 'propput'],
        HRESULT,
        'BorderSoftness',
        (['in'], c_int, 'pVal')
    ),
    COMMETHOD([dispid(1610809366)], HRESULT, 'ApplyChanges'),
    COMMETHOD([dispid(1610809367)], HRESULT, 'LoadDefSettings'),
]

################################################################
# code template for IDxtJpeg implementation
# class IDxtJpeg_Impl(object):
#     def _get(self):
#         'property MaskNum'
#         #return __MIDL__IDxtJpeg0000
#     def _set(self, __MIDL__IDxtJpeg0000):
#         'property MaskNum'
#     MaskNum = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property MaskName'
#         #return pVal
#     def _set(self, pVal):
#         'property MaskName'
#     MaskName = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property ScaleX'
#         #return __MIDL__IDxtJpeg0002
#     def _set(self, __MIDL__IDxtJpeg0002):
#         'property ScaleX'
#     ScaleX = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property ScaleY'
#         #return __MIDL__IDxtJpeg0004
#     def _set(self, __MIDL__IDxtJpeg0004):
#         'property ScaleY'
#     ScaleY = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property OffsetX'
#         #return __MIDL__IDxtJpeg0006
#     def _set(self, __MIDL__IDxtJpeg0006):
#         'property OffsetX'
#     OffsetX = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property OffsetY'
#         #return __MIDL__IDxtJpeg0008
#     def _set(self, __MIDL__IDxtJpeg0008):
#         'property OffsetY'
#     OffsetY = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property ReplicateX'
#         #return pVal
#     def _set(self, pVal):
#         'property ReplicateX'
#     ReplicateX = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property ReplicateY'
#         #return pVal
#     def _set(self, pVal):
#         'property ReplicateY'
#     ReplicateY = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property BorderColor'
#         #return pVal
#     def _set(self, pVal):
#         'property BorderColor'
#     BorderColor = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property BorderWidth'
#         #return pVal
#     def _set(self, pVal):
#         'property BorderWidth'
#     BorderWidth = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property BorderSoftness'
#         #return pVal
#     def _set(self, pVal):
#         'property BorderSoftness'
#     BorderSoftness = property(_get, _set, doc = _set.__doc__)
#
#     def ApplyChanges(self):
#         '-no docstring-'
#         #return 
#
#     def LoadDefSettings(self):
#         '-no docstring-'
#         #return 
#

ISampleGrabber._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetOneShot',
        ([], c_int, 'OneShot')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetMediaType',
        ([], POINTER(_AMMediaType), 'pType')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetConnectedMediaType',
        ([], POINTER(_AMMediaType), 'pType')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetBufferSamples',
        ([], c_int, 'BufferThem')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentBuffer',
        (['in', 'out'], POINTER(c_int), 'pBufferSize'),
        (['out'], POINTER(c_int), 'pBuffer')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentSample',
        (['out', 'retval'], POINTER(POINTER(IMediaSample)), 'ppSample')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetCallback',
        ([], POINTER(ISampleGrabberCB), 'pCallback'),
        ([], c_int, 'WhichMethodToCallback')
    ),
]

################################################################
# code template for ISampleGrabber implementation
# class ISampleGrabber_Impl(object):
#     def SetOneShot(self, OneShot):
#         '-no docstring-'
#         #return 
#
#     def SetMediaType(self, pType):
#         '-no docstring-'
#         #return 
#
#     def GetConnectedMediaType(self, pType):
#         '-no docstring-'
#         #return 
#
#     def SetBufferSamples(self, BufferThem):
#         '-no docstring-'
#         #return 
#
#     def GetCurrentBuffer(self):
#         '-no docstring-'
#         #return pBufferSize, pBuffer
#
#     def GetCurrentSample(self):
#         '-no docstring-'
#         #return ppSample
#
#     def SetCallback(self, pCallback, WhichMethodToCallback):
#         '-no docstring-'
#         #return 
#

IAMTimelineTransable._methods_ = [
    COMMETHOD(
        [helpstring('method TransAdd')],
        HRESULT,
        'TransAdd',
        ([], POINTER(IAMTimelineObj), 'pTrans')
    ),
    COMMETHOD(
        [helpstring('method TransGetCount')],
        HRESULT,
        'TransGetCount',
        ([], POINTER(c_int), 'pCount')
    ),
    COMMETHOD(
        [helpstring('method GetNextTrans')],
        HRESULT,
        'GetNextTrans',
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppTrans'),
        ([], POINTER(c_longlong), 'pInOut')
    ),
    COMMETHOD(
        [helpstring('method GetNextTrans2')],
        HRESULT,
        'GetNextTrans2',
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppTrans'),
        ([], POINTER(c_double), 'pInOut')
    ),
    COMMETHOD(
        [helpstring('method GetTransAtTime')],
        HRESULT,
        'GetTransAtTime',
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppObj'),
        ([], c_longlong, 'Time'),
        ([], c_int, 'SearchDirection')
    ),
    COMMETHOD(
        [helpstring('method GetTransAtTime2')],
        HRESULT,
        'GetTransAtTime2',
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppObj'),
        ([], c_double, 'Time'),
        ([], c_int, 'SearchDirection')
    ),
]

################################################################
# code template for IAMTimelineTransable implementation
# class IAMTimelineTransable_Impl(object):
#     def TransAdd(self, pTrans):
#         'method TransAdd'
#         #return 
#
#     def TransGetCount(self, pCount):
#         'method TransGetCount'
#         #return 
#
#     def GetNextTrans(self, pInOut):
#         'method GetNextTrans'
#         #return ppTrans
#
#     def GetNextTrans2(self, pInOut):
#         'method GetNextTrans2'
#         #return ppTrans
#
#     def GetTransAtTime(self, Time, SearchDirection):
#         'method GetTransAtTime'
#         #return ppObj
#
#     def GetTransAtTime2(self, Time, SearchDirection):
#         'method GetTransAtTime2'
#         #return ppObj
#

IRenderEngine._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetTimelineObject',
        ([], POINTER(IAMTimeline), 'pTimeline')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTimelineObject',
        (['out'], POINTER(POINTER(IAMTimeline)), 'ppTimeline')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFilterGraph',
        (['out'], POINTER(POINTER(IGraphBuilder)), 'ppFG')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetFilterGraph',
        ([], POINTER(IGraphBuilder), 'pFG')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetInterestRange',
        ([], c_longlong, 'Start'),
        ([], c_longlong, 'Stop')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetInterestRange2',
        ([], c_double, 'Start'),
        ([], c_double, 'Stop')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetRenderRange',
        ([], c_longlong, 'Start'),
        ([], c_longlong, 'Stop')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetRenderRange2',
        ([], c_double, 'Start'),
        ([], c_double, 'Stop')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetGroupOutputPin',
        ([], c_int, 'Group'),
        (['out'], POINTER(POINTER(IPin)), 'ppRenderPin')
    ),
    COMMETHOD([], HRESULT, 'ScrapIt'),
    COMMETHOD([], HRESULT, 'RenderOutputPins'),
    COMMETHOD(
        [],
        HRESULT,
        'GetVendorString',
        (['out', 'retval'], POINTER(BSTR), 'pVendorID')
    ),
    COMMETHOD([], HRESULT, 'ConnectFrontEnd'),
    COMMETHOD(
        [],
        HRESULT,
        'SetSourceConnectCallback',
        ([], POINTER(IGrfCache), 'pCallback')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDynamicReconnectLevel',
        ([], c_int, 'Level')
    ),
    COMMETHOD([], HRESULT, 'DoSmartRecompression'),
    COMMETHOD([], HRESULT, 'UseInSmartRecompressionGraph'),
    COMMETHOD(
        [],
        HRESULT,
        'SetSourceNameValidation',
        ([], BSTR, 'FilterString'),
        ([], POINTER(IMediaLocator), 'pOverride'),
        ([], c_int, 'Flags')
    ),
    COMMETHOD([], HRESULT, 'Commit'),
    COMMETHOD([], HRESULT, 'Decommit'),
    COMMETHOD(
        [],
        HRESULT,
        'GetCaps',
        ([], c_int, 'Index'),
        ([], POINTER(c_int), 'pReturn')
    ),
]

################################################################
# code template for IRenderEngine implementation
# class IRenderEngine_Impl(object):
#     def SetTimelineObject(self, pTimeline):
#         '-no docstring-'
#         #return 
#
#     def GetTimelineObject(self):
#         '-no docstring-'
#         #return ppTimeline
#
#     def GetFilterGraph(self):
#         '-no docstring-'
#         #return ppFG
#
#     def SetFilterGraph(self, pFG):
#         '-no docstring-'
#         #return 
#
#     def SetInterestRange(self, Start, Stop):
#         '-no docstring-'
#         #return 
#
#     def SetInterestRange2(self, Start, Stop):
#         '-no docstring-'
#         #return 
#
#     def SetRenderRange(self, Start, Stop):
#         '-no docstring-'
#         #return 
#
#     def SetRenderRange2(self, Start, Stop):
#         '-no docstring-'
#         #return 
#
#     def GetGroupOutputPin(self, Group):
#         '-no docstring-'
#         #return ppRenderPin
#
#     def ScrapIt(self):
#         '-no docstring-'
#         #return 
#
#     def RenderOutputPins(self):
#         '-no docstring-'
#         #return 
#
#     def GetVendorString(self):
#         '-no docstring-'
#         #return pVendorID
#
#     def ConnectFrontEnd(self):
#         '-no docstring-'
#         #return 
#
#     def SetSourceConnectCallback(self, pCallback):
#         '-no docstring-'
#         #return 
#
#     def SetDynamicReconnectLevel(self, Level):
#         '-no docstring-'
#         #return 
#
#     def DoSmartRecompression(self):
#         '-no docstring-'
#         #return 
#
#     def UseInSmartRecompressionGraph(self):
#         '-no docstring-'
#         #return 
#
#     def SetSourceNameValidation(self, FilterString, pOverride, Flags):
#         '-no docstring-'
#         #return 
#
#     def Commit(self):
#         '-no docstring-'
#         #return 
#
#     def Decommit(self):
#         '-no docstring-'
#         #return 
#
#     def GetCaps(self, Index, pReturn):
#         '-no docstring-'
#         #return 
#


class DxtJpeg(CoClass):
    """SMPTE wipe DXT"""
    _reg_clsid_ = GUID('{DE75D012-7A65-11D2-8CEA-00A0C9441E20}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{78530B68-61F9-11D2-8CAD-00A024580902}', 1, 0)


DxtJpeg._com_interfaces_ = [IDxtJpeg]

IAMTimeline._methods_ = [
    COMMETHOD(
        [helpstring('method CreateEmptyNode')],
        HRESULT,
        'CreateEmptyNode',
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppObj'),
        ([], TIMELINE_MAJOR_TYPE, 'Type')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddGroup',
        ([], POINTER(IAMTimelineObj), 'pGroup')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemGroupFromList',
        ([], POINTER(IAMTimelineObj), 'pGroup')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetGroup',
        (['out'], POINTER(POINTER(IAMTimelineObj)), 'ppGroup'),
        ([], c_int, 'WhichGroup')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetGroupCount',
        ([], POINTER(c_int), 'pCount')
    ),
    COMMETHOD([], HRESULT, 'ClearAllGroups'),
    COMMETHOD(
        [],
        HRESULT,
        'GetInsertMode',
        ([], POINTER(c_int), 'pMode')
    ),
    COMMETHOD(
        [helpstring('method SetInsertMode')],
        HRESULT,
        'SetInsertMode',
        ([], c_int, 'Mode')
    ),
    COMMETHOD(
        [helpstring('method EnableTransitions')],
        HRESULT,
        'EnableTransitions',
        ([], c_int, 'fEnabled')
    ),
    COMMETHOD(
        [helpstring('method TransitionsEnabled')],
        HRESULT,
        'TransitionsEnabled',
        ([], POINTER(c_int), 'pfEnabled')
    ),
    COMMETHOD(
        [helpstring('method EnableEffects')],
        HRESULT,
        'EnableEffects',
        ([], c_int, 'fEnabled')
    ),
    COMMETHOD(
        [helpstring('method EffectsEnabled')],
        HRESULT,
        'EffectsEnabled',
        ([], POINTER(c_int), 'pfEnabled')
    ),
    COMMETHOD(
        [helpstring('method SetInterestRange')],
        HRESULT,
        'SetInterestRange',
        ([], c_longlong, 'Start'),
        ([], c_longlong, 'Stop')
    ),
    COMMETHOD(
        [helpstring('method GetDuration')],
        HRESULT,
        'GetDuration',
        ([], POINTER(c_longlong), 'pDuration')
    ),
    COMMETHOD(
        [helpstring('method GetDuration2')],
        HRESULT,
        'GetDuration2',
        ([], POINTER(c_double), 'pDuration')
    ),
    COMMETHOD(
        [helpstring('method SetDefaultFPS')],
        HRESULT,
        'SetDefaultFPS',
        ([], c_double, 'FPS')
    ),
    COMMETHOD(
        [helpstring('method GetDefaultFPS')],
        HRESULT,
        'GetDefaultFPS',
        ([], POINTER(c_double), 'pFPS')
    ),
    COMMETHOD(
        [helpstring('method IsDirty')],
        HRESULT,
        'IsDirty',
        ([], POINTER(c_int), 'pDirty')
    ),
    COMMETHOD(
        [helpstring('method GetDirtyRange')],
        HRESULT,
        'GetDirtyRange',
        ([], POINTER(c_longlong), 'pStart'),
        ([], POINTER(c_longlong), 'pStop')
    ),
    COMMETHOD(
        [helpstring('method GetCountOfType')],
        HRESULT,
        'GetCountOfType',
        ([], c_int, 'Group'),
        ([], POINTER(c_int), 'pVal'),
        ([], POINTER(c_int), 'pValWithComps'),
        ([], TIMELINE_MAJOR_TYPE, 'majortype')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ValidateSourceNames',
        ([], c_int, 'ValidateFlags'),
        ([], POINTER(IMediaLocator), 'pOverride'),
        ([], LONG_PTR, 'NotifyEventHandle')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDefaultTransition',
        (
            [],
            POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
            'pGuid',
        )
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultTransition',
        (
            [],
            POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
            'pGuid',
        )
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDefaultEffect',
        (
            [],
            POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
            'pGuid',
        )
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultEffect',
        (
            [],
            POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
            'pGuid',
        )
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDefaultTransitionB',
        ([], BSTR, 'pGuid')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultTransitionB',
        (['out', 'retval'], POINTER(BSTR), 'pGuid')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDefaultEffectB',
        ([], BSTR, 'pGuid')
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultEffectB',
        (['out', 'retval'], POINTER(BSTR), 'pGuid')
    ),
]

################################################################
# code template for IAMTimeline implementation
# class IAMTimeline_Impl(object):
#     def CreateEmptyNode(self, Type):
#         'method CreateEmptyNode'
#         #return ppObj
#
#     def AddGroup(self, pGroup):
#         '-no docstring-'
#         #return 
#
#     def RemGroupFromList(self, pGroup):
#         '-no docstring-'
#         #return 
#
#     def GetGroup(self, WhichGroup):
#         '-no docstring-'
#         #return ppGroup
#
#     def GetGroupCount(self, pCount):
#         '-no docstring-'
#         #return 
#
#     def ClearAllGroups(self):
#         '-no docstring-'
#         #return 
#
#     def GetInsertMode(self, pMode):
#         '-no docstring-'
#         #return 
#
#     def SetInsertMode(self, Mode):
#         'method SetInsertMode'
#         #return 
#
#     def EnableTransitions(self, fEnabled):
#         'method EnableTransitions'
#         #return 
#
#     def TransitionsEnabled(self, pfEnabled):
#         'method TransitionsEnabled'
#         #return 
#
#     def EnableEffects(self, fEnabled):
#         'method EnableEffects'
#         #return 
#
#     def EffectsEnabled(self, pfEnabled):
#         'method EffectsEnabled'
#         #return 
#
#     def SetInterestRange(self, Start, Stop):
#         'method SetInterestRange'
#         #return 
#
#     def GetDuration(self, pDuration):
#         'method GetDuration'
#         #return 
#
#     def GetDuration2(self, pDuration):
#         'method GetDuration2'
#         #return 
#
#     def SetDefaultFPS(self, FPS):
#         'method SetDefaultFPS'
#         #return 
#
#     def GetDefaultFPS(self, pFPS):
#         'method GetDefaultFPS'
#         #return 
#
#     def IsDirty(self, pDirty):
#         'method IsDirty'
#         #return 
#
#     def GetDirtyRange(self, pStart, pStop):
#         'method GetDirtyRange'
#         #return 
#
#     def GetCountOfType(self, Group, pVal, pValWithComps, majortype):
#         'method GetCountOfType'
#         #return 
#
#     def ValidateSourceNames(self, ValidateFlags, pOverride, NotifyEventHandle):
#         '-no docstring-'
#         #return 
#
#     def SetDefaultTransition(self, pGuid):
#         '-no docstring-'
#         #return 
#
#     def GetDefaultTransition(self, pGuid):
#         '-no docstring-'
#         #return 
#
#     def SetDefaultEffect(self, pGuid):
#         '-no docstring-'
#         #return 
#
#     def GetDefaultEffect(self, pGuid):
#         '-no docstring-'
#         #return 
#
#     def SetDefaultTransitionB(self, pGuid):
#         '-no docstring-'
#         #return 
#
#     def GetDefaultTransitionB(self):
#         '-no docstring-'
#         #return pGuid
#
#     def SetDefaultEffectB(self, pGuid):
#         '-no docstring-'
#         #return 
#
#     def GetDefaultEffectB(self):
#         '-no docstring-'
#         #return pGuid
#

__all__ = [
    'DEXTER_VALUE', '__MIDL___MIDL_itf_qedit_0000_0000_0002',
    'IEnumFilters', 'IAMTimelineGroup', 'State_Stopped',
    'RenderEngine', 'ISmartRenderEngine', 'AMTimelineGroup',
    'IStream', 'IMediaSample', '_FilterInfo', 'DEXTER_PARAM',
    'IMediaFilter', 'IAMTimelineEffectable', 'IDxtKey',
    'TIMELINE_MAJOR_TYPE_EFFECT', 'PINDIR_OUTPUT', 'AudMixer',
    'IAMTimelineTransable', 'IEnumMediaTypes', 'AMTimelineTrack',
    '_FilterState', 'AMTimelineEffect', 'ISampleGrabber', 'IGrfCache',
    'TIMELINE_MAJOR_TYPE', 'NullRenderer', '_AMMediaType',
    'IPropertySetter', 'State_Paused', 'AMTimelineComp',
    'IAMTimelineSplittable', 'Xml2Dex', 'ISequentialStream',
    'IAMTimeline', 'IAMErrorLog', 'IRenderEngine2', 'IBaseFilter',
    'IAMTimelineVirtualTrack', 'MediaDet', 'SampleGrabber',
    'SmartRenderEngine', 'IFindCompressorCB', 'IReferenceClock',
    'IEnumPins', 'TIMELINE_MAJOR_TYPE_GROUP', 'DxtJpeg',
    'IAMTimelineSrc', 'IDXEffect', 'State_Running',
    'TIMELINE_MAJOR_TYPE_COMPOSITE', 'DxtCompositor', 'IRenderEngine',
    'MediaLocator', 'LONG_PTR', 'AMTimelineSrc', 'IAMSetErrorLog',
    'IAMTimelineTrack', '__MIDL___MIDL_itf_qedit_0000_0000_0003',
    'IFilterGraph', 'IAMTimelineEffect', 'IPin', 'IAMTimelineObj',
    'AMTimelineTrans', '_PinDirection', 'DxtKey', 'IGraphBuilder',
    'IXml2Dex', 'DxtAlphaSetter', 'AMTimeline', 'ISampleGrabberCB',
    'IDxtJpeg', 'IResize', 'IAMTimelineComp', 'IAMTimelineTrans',
    'ColorSource', '__MIDL___MIDL_itf_qedit_0000_0000_0007',
    'IPersistStream', 'AMTimelineObj', 'IDxtCompositor',
    'TIMELINE_MAJOR_TYPE_TRANSITION', '_PinInfo', 'IMediaLocator',
    'tagSTATSTG', 'TIMELINE_MAJOR_TYPE_SOURCE', 'IMediaDet',
    'PropertySetter', 'TIMELINE_MAJOR_TYPE_TRACK', 'PINDIR_INPUT',
    'IDxtAlphaSetter'
]

_check_version('1.2.0', 1662606574.078540)

