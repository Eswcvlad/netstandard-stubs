import typing, abc
from System.IO import BinaryReader, BinaryWriter
from System.Collections.Generic import IDictionary_2, IEnumerable_1
from System.Security.Principal import IIdentity, IPrincipal
from System import Predicate_1, Func_1, Func_2

class Claim:
    @typing.overload
    def __init__(self, reader: BinaryReader) -> None: ...
    @typing.overload
    def __init__(self, reader: BinaryReader, subject: ClaimsIdentity) -> None: ...
    @typing.overload
    def __init__(self, type: str, value: str) -> None: ...
    @typing.overload
    def __init__(self, type: str, value: str, valueType: str) -> None: ...
    @typing.overload
    def __init__(self, type: str, value: str, valueType: str, issuer: str) -> None: ...
    @typing.overload
    def __init__(self, type: str, value: str, valueType: str, issuer: str, originalIssuer: str) -> None: ...
    @typing.overload
    def __init__(self, type: str, value: str, valueType: str, issuer: str, originalIssuer: str, subject: ClaimsIdentity) -> None: ...
    @property
    def Issuer(self) -> str: ...
    @property
    def OriginalIssuer(self) -> str: ...
    @property
    def Properties(self) -> IDictionary_2[str, str]: ...
    @property
    def Subject(self) -> ClaimsIdentity: ...
    @property
    def Type(self) -> str: ...
    @property
    def Value(self) -> str: ...
    @property
    def ValueType(self) -> str: ...
    def ToString(self) -> str: ...
    def WriteTo(self, writer: BinaryWriter) -> None: ...
    # Skipped Clone due to it being static, abstract and generic.

    Clone : Clone_MethodGroup
    class Clone_MethodGroup:
        @typing.overload
        def __call__(self) -> Claim:...
        @typing.overload
        def __call__(self, identity: ClaimsIdentity) -> Claim:...



class ClaimsIdentity(IIdentity):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, authenticationType: str) -> None: ...
    @typing.overload
    def __init__(self, authenticationType: str, nameType: str, roleType: str) -> None: ...
    @typing.overload
    def __init__(self, claims: IEnumerable_1[Claim]) -> None: ...
    @typing.overload
    def __init__(self, claims: IEnumerable_1[Claim], authenticationType: str) -> None: ...
    @typing.overload
    def __init__(self, claims: IEnumerable_1[Claim], authenticationType: str, nameType: str, roleType: str) -> None: ...
    @typing.overload
    def __init__(self, identity: IIdentity) -> None: ...
    @typing.overload
    def __init__(self, identity: IIdentity, claims: IEnumerable_1[Claim]) -> None: ...
    @typing.overload
    def __init__(self, identity: IIdentity, claims: IEnumerable_1[Claim], authenticationType: str, nameType: str, roleType: str) -> None: ...
    @typing.overload
    def __init__(self, reader: BinaryReader) -> None: ...
    DefaultIssuer : str
    DefaultNameClaimType : str
    DefaultRoleClaimType : str
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
    def AddClaim(self, claim: Claim) -> None: ...
    def AddClaims(self, claims: IEnumerable_1[Claim]) -> None: ...
    def Clone(self) -> ClaimsIdentity: ...
    def RemoveClaim(self, claim: Claim) -> None: ...
    def TryRemoveClaim(self, claim: Claim) -> bool: ...
    def WriteTo(self, writer: BinaryWriter) -> None: ...
    # Skipped FindAll due to it being static, abstract and generic.

    FindAll : FindAll_MethodGroup
    class FindAll_MethodGroup:
        @typing.overload
        def __call__(self, match: Predicate_1[Claim]) -> IEnumerable_1[Claim]:...
        @typing.overload
        def __call__(self, type: str) -> IEnumerable_1[Claim]:...

    # Skipped FindFirst due to it being static, abstract and generic.

    FindFirst : FindFirst_MethodGroup
    class FindFirst_MethodGroup:
        @typing.overload
        def __call__(self, match: Predicate_1[Claim]) -> Claim:...
        @typing.overload
        def __call__(self, type: str) -> Claim:...

    # Skipped HasClaim due to it being static, abstract and generic.

    HasClaim : HasClaim_MethodGroup
    class HasClaim_MethodGroup:
        @typing.overload
        def __call__(self, match: Predicate_1[Claim]) -> bool:...
        @typing.overload
        def __call__(self, type: str, value: str) -> bool:...



class ClaimsPrincipal(IPrincipal):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, identities: IEnumerable_1[ClaimsIdentity]) -> None: ...
    @typing.overload
    def __init__(self, identity: IIdentity) -> None: ...
    @typing.overload
    def __init__(self, principal: IPrincipal) -> None: ...
    @typing.overload
    def __init__(self, reader: BinaryReader) -> None: ...
    @property
    def Claims(self) -> IEnumerable_1[Claim]: ...
    @classmethod
    @property
    def ClaimsPrincipalSelector(cls) -> Func_1[ClaimsPrincipal]: ...
    @classmethod
    @ClaimsPrincipalSelector.setter
    def ClaimsPrincipalSelector(cls, value: Func_1[ClaimsPrincipal]) -> Func_1[ClaimsPrincipal]: ...
    @classmethod
    @property
    def Current(cls) -> ClaimsPrincipal: ...
    @property
    def Identities(self) -> IEnumerable_1[ClaimsIdentity]: ...
    @property
    def Identity(self) -> IIdentity: ...
    @classmethod
    @property
    def PrimaryIdentitySelector(cls) -> Func_2[IEnumerable_1[ClaimsIdentity], ClaimsIdentity]: ...
    @classmethod
    @PrimaryIdentitySelector.setter
    def PrimaryIdentitySelector(cls, value: Func_2[IEnumerable_1[ClaimsIdentity], ClaimsIdentity]) -> Func_2[IEnumerable_1[ClaimsIdentity], ClaimsIdentity]: ...
    def AddIdentities(self, identities: IEnumerable_1[ClaimsIdentity]) -> None: ...
    def AddIdentity(self, identity: ClaimsIdentity) -> None: ...
    def Clone(self) -> ClaimsPrincipal: ...
    def IsInRole(self, role: str) -> bool: ...
    def WriteTo(self, writer: BinaryWriter) -> None: ...
    # Skipped FindAll due to it being static, abstract and generic.

    FindAll : FindAll_MethodGroup
    class FindAll_MethodGroup:
        @typing.overload
        def __call__(self, match: Predicate_1[Claim]) -> IEnumerable_1[Claim]:...
        @typing.overload
        def __call__(self, type: str) -> IEnumerable_1[Claim]:...

    # Skipped FindFirst due to it being static, abstract and generic.

    FindFirst : FindFirst_MethodGroup
    class FindFirst_MethodGroup:
        @typing.overload
        def __call__(self, match: Predicate_1[Claim]) -> Claim:...
        @typing.overload
        def __call__(self, type: str) -> Claim:...

    # Skipped HasClaim due to it being static, abstract and generic.

    HasClaim : HasClaim_MethodGroup
    class HasClaim_MethodGroup:
        @typing.overload
        def __call__(self, match: Predicate_1[Claim]) -> bool:...
        @typing.overload
        def __call__(self, type: str, value: str) -> bool:...



class ClaimTypes(abc.ABC):
    Actor : str
    Anonymous : str
    Authentication : str
    AuthenticationInstant : str
    AuthenticationMethod : str
    AuthorizationDecision : str
    CookiePath : str
    Country : str
    DateOfBirth : str
    DenyOnlyPrimaryGroupSid : str
    DenyOnlyPrimarySid : str
    DenyOnlySid : str
    DenyOnlyWindowsDeviceGroup : str
    Dns : str
    Dsa : str
    Email : str
    Expiration : str
    Expired : str
    Gender : str
    GivenName : str
    GroupSid : str
    Hash : str
    HomePhone : str
    IsPersistent : str
    Locality : str
    MobilePhone : str
    Name : str
    NameIdentifier : str
    OtherPhone : str
    PostalCode : str
    PrimaryGroupSid : str
    PrimarySid : str
    Role : str
    Rsa : str
    SerialNumber : str
    Sid : str
    Spn : str
    StateOrProvince : str
    StreetAddress : str
    Surname : str
    System : str
    Thumbprint : str
    Upn : str
    Uri : str
    UserData : str
    Version : str
    Webpage : str
    WindowsAccountName : str
    WindowsDeviceClaim : str
    WindowsDeviceGroup : str
    WindowsFqbnVersion : str
    WindowsSubAuthority : str
    WindowsUserClaim : str
    X500DistinguishedName : str


class ClaimValueTypes(abc.ABC):
    Base64Binary : str
    Base64Octet : str
    Boolean : str
    Date : str
    DateTime : str
    DaytimeDuration : str
    DnsName : str
    Double : str
    DsaKeyValue : str
    Email : str
    Fqbn : str
    HexBinary : str
    Integer : str
    Integer32 : str
    Integer64 : str
    KeyInfo : str
    Rfc822Name : str
    Rsa : str
    RsaKeyValue : str
    Sid : str
    String : str
    Time : str
    UInteger32 : str
    UInteger64 : str
    UpnName : str
    X500Name : str
    YearMonthDuration : str

