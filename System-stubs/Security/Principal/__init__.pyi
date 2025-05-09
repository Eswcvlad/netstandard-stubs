import typing, abc
from System.Security.Claims import ClaimsIdentity, Claim, ClaimsPrincipal
from System.Collections.Generic import IEnumerable_1
from System import Array_1

class GenericIdentity(ClaimsIdentity):
    @typing.overload
    def __init__(self, name: str) -> None: ...
    @typing.overload
    def __init__(self, name: str, type: str) -> None: ...
    @property
    def Actor(self) -> ClaimsIdentity: ...
    @Actor.setter
    def Actor(self, value: ClaimsIdentity) -> ClaimsIdentity: ...
    @property
    def AuthenticationType(self) -> str: ...
    @property
    def BootstrapContext(self) -> typing.Any: ...
    @BootstrapContext.setter
    def BootstrapContext(self, value: typing.Any) -> typing.Any: ...
    @property
    def Claims(self) -> IEnumerable_1[Claim]: ...
    @property
    def IsAuthenticated(self) -> bool: ...
    @property
    def Label(self) -> str: ...
    @Label.setter
    def Label(self, value: str) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def NameClaimType(self) -> str: ...
    @property
    def RoleClaimType(self) -> str: ...
    def Clone(self) -> ClaimsIdentity: ...


class GenericPrincipal(ClaimsPrincipal):
    def __init__(self, identity: IIdentity, roles: Array_1[str]) -> None: ...
    @property
    def Claims(self) -> IEnumerable_1[Claim]: ...
    @property
    def Identities(self) -> IEnumerable_1[ClaimsIdentity]: ...
    @property
    def Identity(self) -> IIdentity: ...
    def IsInRole(self, role: str) -> bool: ...


class IdentityReference(abc.ABC):
    @property
    def Value(self) -> str: ...
    @abc.abstractmethod
    def Equals(self, o: typing.Any) -> bool: ...
    @abc.abstractmethod
    def GetHashCode(self) -> int: ...
    @abc.abstractmethod
    def IsValidTargetType(self, targetType: typing.Type[typing.Any]) -> bool: ...
    def __eq__(self, left: IdentityReference, right: IdentityReference) -> bool: ...
    def __ne__(self, left: IdentityReference, right: IdentityReference) -> bool: ...
    @abc.abstractmethod
    def ToString(self) -> str: ...
    @abc.abstractmethod
    def Translate(self, targetType: typing.Type[typing.Any]) -> IdentityReference: ...


class IIdentity(typing.Protocol):
    @property
    def AuthenticationType(self) -> str: ...
    @property
    def IsAuthenticated(self) -> bool: ...
    @property
    def Name(self) -> str: ...


class IPrincipal(typing.Protocol):
    @property
    def Identity(self) -> IIdentity: ...
    @abc.abstractmethod
    def IsInRole(self, role: str) -> bool: ...


class PrincipalPolicy(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    UnauthenticatedPrincipal : PrincipalPolicy # 0
    NoPrincipal : PrincipalPolicy # 1
    WindowsPrincipal : PrincipalPolicy # 2


class TokenImpersonationLevel(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : TokenImpersonationLevel # 0
    Anonymous : TokenImpersonationLevel # 1
    Identification : TokenImpersonationLevel # 2
    Impersonation : TokenImpersonationLevel # 3
    Delegation : TokenImpersonationLevel # 4

