import typing
from System import SystemException, Exception
from System.Collections import IDictionary
from System.Reflection import MethodBase

class AuthenticationException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class CipherAlgorithmType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : CipherAlgorithmType # 0
    Null : CipherAlgorithmType # 24576
    Des : CipherAlgorithmType # 26113
    Rc2 : CipherAlgorithmType # 26114
    TripleDes : CipherAlgorithmType # 26115
    Aes128 : CipherAlgorithmType # 26126
    Aes192 : CipherAlgorithmType # 26127
    Aes256 : CipherAlgorithmType # 26128
    Aes : CipherAlgorithmType # 26129
    Rc4 : CipherAlgorithmType # 26625


class ExchangeAlgorithmType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : ExchangeAlgorithmType # 0
    RsaSign : ExchangeAlgorithmType # 9216
    RsaKeyX : ExchangeAlgorithmType # 41984
    DiffieHellman : ExchangeAlgorithmType # 43522


class HashAlgorithmType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : HashAlgorithmType # 0
    Md5 : HashAlgorithmType # 32771
    Sha1 : HashAlgorithmType # 32772
    Sha256 : HashAlgorithmType # 32780
    Sha384 : HashAlgorithmType # 32781
    Sha512 : HashAlgorithmType # 32782


class InvalidCredentialException(AuthenticationException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class SslProtocols(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : SslProtocols # 0
    Ssl2 : SslProtocols # 12
    Ssl3 : SslProtocols # 48
    Tls : SslProtocols # 192
    Default : SslProtocols # 240
    Tls11 : SslProtocols # 768
    Tls12 : SslProtocols # 3072
    Tls13 : SslProtocols # 12288

