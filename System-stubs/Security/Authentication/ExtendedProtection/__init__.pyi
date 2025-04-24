import typing
from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System.Runtime.Serialization import ISerializable
from System.Collections import ICollection, ReadOnlyCollectionBase, IEnumerable
from System.ComponentModel import TypeConverter, ITypeDescriptorContext
from System.Globalization import CultureInfo

class ChannelBinding(SafeHandleZeroOrMinusOneIsInvalid):
    @property
    def IsClosed(self) -> bool: ...
    @property
    def IsInvalid(self) -> bool: ...
    @property
    def Size(self) -> int: ...


class ChannelBindingKind(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Unknown : ChannelBindingKind # 0
    Unique : ChannelBindingKind # 25
    Endpoint : ChannelBindingKind # 26


class ExtendedProtectionPolicy(ISerializable):
    @typing.overload
    def __init__(self, policyEnforcement: PolicyEnforcement) -> None: ...
    @typing.overload
    def __init__(self, policyEnforcement: PolicyEnforcement, customChannelBinding: ChannelBinding) -> None: ...
    @typing.overload
    def __init__(self, policyEnforcement: PolicyEnforcement, protectionScenario: ProtectionScenario, customServiceNames: ServiceNameCollection) -> None: ...
    @typing.overload
    def __init__(self, policyEnforcement: PolicyEnforcement, protectionScenario: ProtectionScenario, customServiceNames: ICollection) -> None: ...
    @property
    def CustomChannelBinding(self) -> ChannelBinding: ...
    @property
    def CustomServiceNames(self) -> ServiceNameCollection: ...
    @classmethod
    @property
    def OSSupportsExtendedProtection(cls) -> bool: ...
    @property
    def PolicyEnforcement(self) -> PolicyEnforcement: ...
    @property
    def ProtectionScenario(self) -> ProtectionScenario: ...
    def ToString(self) -> str: ...


class ExtendedProtectionPolicyTypeConverter(TypeConverter):
    def __init__(self) -> None: ...
    # Skipped CanConvertTo due to it being static, abstract and generic.

    CanConvertTo : CanConvertTo_MethodGroup
    class CanConvertTo_MethodGroup:
        @typing.overload
        def __call__(self, destinationType: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, destinationType: typing.Type[typing.Any]) -> bool:...

    # Skipped ConvertTo due to it being static, abstract and generic.

    ConvertTo : ConvertTo_MethodGroup
    class ConvertTo_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any, destinationType: typing.Type[typing.Any]) -> typing.Any:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, culture: CultureInfo, value: typing.Any, destinationType: typing.Type[typing.Any]) -> typing.Any:...



class PolicyEnforcement(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Never : PolicyEnforcement # 0
    WhenSupported : PolicyEnforcement # 1
    Always : PolicyEnforcement # 2


class ProtectionScenario(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    TransportSelected : ProtectionScenario # 0
    TrustedProxy : ProtectionScenario # 1


class ServiceNameCollection(ReadOnlyCollectionBase):
    def __init__(self, items: ICollection) -> None: ...
    @property
    def Count(self) -> int: ...
    def Contains(self, searchServiceName: str) -> bool: ...
    # Skipped Merge due to it being static, abstract and generic.

    Merge : Merge_MethodGroup
    class Merge_MethodGroup:
        @typing.overload
        def __call__(self, serviceName: str) -> ServiceNameCollection:...
        @typing.overload
        def __call__(self, serviceNames: IEnumerable) -> ServiceNameCollection:...


