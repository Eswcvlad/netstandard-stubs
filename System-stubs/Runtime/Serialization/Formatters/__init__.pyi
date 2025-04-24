import typing
from System import Array_1

class FormatterAssemblyStyle(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Simple : FormatterAssemblyStyle # 0
    Full : FormatterAssemblyStyle # 1


class FormatterTypeStyle(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    TypesWhenNeeded : FormatterTypeStyle # 0
    TypesAlways : FormatterTypeStyle # 1
    XsdString : FormatterTypeStyle # 2


class IFieldInfo(typing.Protocol):
    @property
    def FieldNames(self) -> Array_1[str]: ...
    @FieldNames.setter
    def FieldNames(self, value: Array_1[str]) -> Array_1[str]: ...
    @property
    def FieldTypes(self) -> Array_1[typing.Type[typing.Any]]: ...
    @FieldTypes.setter
    def FieldTypes(self, value: Array_1[typing.Type[typing.Any]]) -> Array_1[typing.Type[typing.Any]]: ...


class TypeFilterLevel(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Low : TypeFilterLevel # 2
    Full : TypeFilterLevel # 3

