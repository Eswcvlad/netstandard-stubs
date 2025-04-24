import typing
from System import TimeSpan, DateTime

class HttpCacheAgeControl(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : HttpCacheAgeControl # 0
    MinFresh : HttpCacheAgeControl # 1
    MaxAge : HttpCacheAgeControl # 2
    MaxAgeAndMinFresh : HttpCacheAgeControl # 3
    MaxStale : HttpCacheAgeControl # 4
    MaxAgeAndMaxStale : HttpCacheAgeControl # 6


class HttpRequestCacheLevel(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Default : HttpRequestCacheLevel # 0
    BypassCache : HttpRequestCacheLevel # 1
    CacheOnly : HttpRequestCacheLevel # 2
    CacheIfAvailable : HttpRequestCacheLevel # 3
    Revalidate : HttpRequestCacheLevel # 4
    Reload : HttpRequestCacheLevel # 5
    NoCacheNoStore : HttpRequestCacheLevel # 6
    CacheOrNextCacheOnly : HttpRequestCacheLevel # 7
    Refresh : HttpRequestCacheLevel # 8


class HttpRequestCachePolicy(RequestCachePolicy):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, cacheAgeControl: HttpCacheAgeControl, ageOrFreshOrStale: TimeSpan) -> None: ...
    @typing.overload
    def __init__(self, cacheAgeControl: HttpCacheAgeControl, maxAge: TimeSpan, freshOrStale: TimeSpan) -> None: ...
    @typing.overload
    def __init__(self, cacheAgeControl: HttpCacheAgeControl, maxAge: TimeSpan, freshOrStale: TimeSpan, cacheSyncDate: DateTime) -> None: ...
    @typing.overload
    def __init__(self, cacheSyncDate: DateTime) -> None: ...
    @typing.overload
    def __init__(self, level: HttpRequestCacheLevel) -> None: ...
    @property
    def CacheSyncDate(self) -> DateTime: ...
    @property
    def Level(self) -> HttpRequestCacheLevel: ...
    @property
    def Level(self) -> RequestCacheLevel: ...
    @property
    def MaxAge(self) -> TimeSpan: ...
    @property
    def MaxStale(self) -> TimeSpan: ...
    @property
    def MinFresh(self) -> TimeSpan: ...
    def ToString(self) -> str: ...


class RequestCacheLevel(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Default : RequestCacheLevel # 0
    BypassCache : RequestCacheLevel # 1
    CacheOnly : RequestCacheLevel # 2
    CacheIfAvailable : RequestCacheLevel # 3
    Revalidate : RequestCacheLevel # 4
    Reload : RequestCacheLevel # 5
    NoCacheNoStore : RequestCacheLevel # 6


class RequestCachePolicy:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, level: RequestCacheLevel) -> None: ...
    @property
    def Level(self) -> RequestCacheLevel: ...
    def ToString(self) -> str: ...

