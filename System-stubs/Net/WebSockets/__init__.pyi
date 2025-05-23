import typing, abc
from System.Threading.Tasks import Task, Task_1, ValueTask_1, ValueTask
from System.Threading import CancellationToken
from System import Uri, ArraySegment_1, Memory_1, ReadOnlyMemory_1, TimeSpan, IDisposable, Exception
from System.Security.Cryptography.X509Certificates import X509CertificateCollection
from System.Net import CookieContainer, ICredentials, IWebProxy, CookieCollection
from System.Net.Security import RemoteCertificateValidationCallback
from System.IO import Stream
from System.Collections.Specialized import NameValueCollection
from System.Collections.Generic import IEnumerable_1
from System.Security.Principal import IPrincipal
from System.ComponentModel import Win32Exception
from System.Collections import IDictionary
from System.Reflection import MethodBase
from System.Runtime.Serialization import SerializationInfo, StreamingContext

class ClientWebSocket(WebSocket):
    def __init__(self) -> None: ...
    @property
    def CloseStatus(self) -> typing.Optional[WebSocketCloseStatus]: ...
    @property
    def CloseStatusDescription(self) -> str: ...
    @property
    def Options(self) -> ClientWebSocketOptions: ...
    @property
    def State(self) -> WebSocketState: ...
    @property
    def SubProtocol(self) -> str: ...
    def Abort(self) -> None: ...
    def CloseAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: str, cancellationToken: CancellationToken) -> Task: ...
    def CloseOutputAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: str, cancellationToken: CancellationToken) -> Task: ...
    def ConnectAsync(self, uri: Uri, cancellationToken: CancellationToken) -> Task: ...
    def Dispose(self) -> None: ...
    # Skipped ReceiveAsync due to it being static, abstract and generic.

    ReceiveAsync : ReceiveAsync_MethodGroup
    class ReceiveAsync_MethodGroup:
        @typing.overload
        def __call__(self, buffer: ArraySegment_1[int], cancellationToken: CancellationToken) -> Task_1[WebSocketReceiveResult]:...
        @typing.overload
        def __call__(self, buffer: Memory_1[int], cancellationToken: CancellationToken) -> ValueTask_1[ValueWebSocketReceiveResult]:...

    # Skipped SendAsync due to it being static, abstract and generic.

    SendAsync : SendAsync_MethodGroup
    class SendAsync_MethodGroup:
        @typing.overload
        def __call__(self, buffer: ArraySegment_1[int], messageType: WebSocketMessageType, endOfMessage: bool, cancellationToken: CancellationToken) -> Task:...
        @typing.overload
        def __call__(self, buffer: ReadOnlyMemory_1[int], messageType: WebSocketMessageType, messageFlags: WebSocketMessageFlags, cancellationToken: CancellationToken) -> ValueTask:...
        @typing.overload
        def __call__(self, buffer: ReadOnlyMemory_1[int], messageType: WebSocketMessageType, endOfMessage: bool, cancellationToken: CancellationToken) -> ValueTask:...



class ClientWebSocketOptions:
    @property
    def ClientCertificates(self) -> X509CertificateCollection: ...
    @ClientCertificates.setter
    def ClientCertificates(self, value: X509CertificateCollection) -> X509CertificateCollection: ...
    @property
    def Cookies(self) -> CookieContainer: ...
    @Cookies.setter
    def Cookies(self, value: CookieContainer) -> CookieContainer: ...
    @property
    def Credentials(self) -> ICredentials: ...
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> ICredentials: ...
    @property
    def DangerousDeflateOptions(self) -> WebSocketDeflateOptions: ...
    @DangerousDeflateOptions.setter
    def DangerousDeflateOptions(self, value: WebSocketDeflateOptions) -> WebSocketDeflateOptions: ...
    @property
    def KeepAliveInterval(self) -> TimeSpan: ...
    @KeepAliveInterval.setter
    def KeepAliveInterval(self, value: TimeSpan) -> TimeSpan: ...
    @property
    def Proxy(self) -> IWebProxy: ...
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> IWebProxy: ...
    @property
    def RemoteCertificateValidationCallback(self) -> RemoteCertificateValidationCallback: ...
    @RemoteCertificateValidationCallback.setter
    def RemoteCertificateValidationCallback(self, value: RemoteCertificateValidationCallback) -> RemoteCertificateValidationCallback: ...
    @property
    def UseDefaultCredentials(self) -> bool: ...
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> bool: ...
    def AddSubProtocol(self, subProtocol: str) -> None: ...
    def SetRequestHeader(self, headerName: str, headerValue: str) -> None: ...
    # Skipped SetBuffer due to it being static, abstract and generic.

    SetBuffer : SetBuffer_MethodGroup
    class SetBuffer_MethodGroup:
        @typing.overload
        def __call__(self, receiveBufferSize: int, sendBufferSize: int) -> None:...
        @typing.overload
        def __call__(self, receiveBufferSize: int, sendBufferSize: int, buffer: ArraySegment_1[int]) -> None:...



class ValueWebSocketReceiveResult:
    def __init__(self, count: int, messageType: WebSocketMessageType, endOfMessage: bool) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def EndOfMessage(self) -> bool: ...
    @property
    def MessageType(self) -> WebSocketMessageType: ...


class WebSocket(IDisposable, abc.ABC):
    @property
    def CloseStatus(self) -> typing.Optional[WebSocketCloseStatus]: ...
    @property
    def CloseStatusDescription(self) -> str: ...
    @classmethod
    @property
    def DefaultKeepAliveInterval(cls) -> TimeSpan: ...
    @property
    def State(self) -> WebSocketState: ...
    @property
    def SubProtocol(self) -> str: ...
    @abc.abstractmethod
    def Abort(self) -> None: ...
    @abc.abstractmethod
    def CloseAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: str, cancellationToken: CancellationToken) -> Task: ...
    @abc.abstractmethod
    def CloseOutputAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: str, cancellationToken: CancellationToken) -> Task: ...
    @staticmethod
    def CreateClientBuffer(receiveBufferSize: int, sendBufferSize: int) -> ArraySegment_1[int]: ...
    @staticmethod
    def CreateClientWebSocket(innerStream: Stream, subProtocol: str, receiveBufferSize: int, sendBufferSize: int, keepAliveInterval: TimeSpan, useZeroMaskingKey: bool, internalBuffer: ArraySegment_1[int]) -> WebSocket: ...
    @staticmethod
    def CreateServerBuffer(receiveBufferSize: int) -> ArraySegment_1[int]: ...
    @abc.abstractmethod
    def Dispose(self) -> None: ...
    @staticmethod
    def IsApplicationTargeting45() -> bool: ...
    @staticmethod
    def RegisterPrefixes() -> None: ...
    # Skipped CreateFromStream due to it being static, abstract and generic.

    CreateFromStream : CreateFromStream_MethodGroup
    class CreateFromStream_MethodGroup:
        @typing.overload
        def __call__(self, stream: Stream, options: WebSocketCreationOptions) -> WebSocket:...
        @typing.overload
        def __call__(self, stream: Stream, isServer: bool, subProtocol: str, keepAliveInterval: TimeSpan) -> WebSocket:...

    # Skipped ReceiveAsync due to it being static, abstract and generic.

    ReceiveAsync : ReceiveAsync_MethodGroup
    class ReceiveAsync_MethodGroup:
        @typing.overload
        def __call__(self, buffer: ArraySegment_1[int], cancellationToken: CancellationToken) -> Task_1[WebSocketReceiveResult]:...
        @typing.overload
        def __call__(self, buffer: Memory_1[int], cancellationToken: CancellationToken) -> ValueTask_1[ValueWebSocketReceiveResult]:...

    # Skipped SendAsync due to it being static, abstract and generic.

    SendAsync : SendAsync_MethodGroup
    class SendAsync_MethodGroup:
        @typing.overload
        def __call__(self, buffer: ArraySegment_1[int], messageType: WebSocketMessageType, endOfMessage: bool, cancellationToken: CancellationToken) -> Task:...
        @typing.overload
        def __call__(self, buffer: ReadOnlyMemory_1[int], messageType: WebSocketMessageType, messageFlags: WebSocketMessageFlags, cancellationToken: CancellationToken = ...) -> ValueTask:...
        @typing.overload
        def __call__(self, buffer: ReadOnlyMemory_1[int], messageType: WebSocketMessageType, endOfMessage: bool, cancellationToken: CancellationToken) -> ValueTask:...



class WebSocketCloseStatus(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    NormalClosure : WebSocketCloseStatus # 1000
    EndpointUnavailable : WebSocketCloseStatus # 1001
    ProtocolError : WebSocketCloseStatus # 1002
    InvalidMessageType : WebSocketCloseStatus # 1003
    Empty : WebSocketCloseStatus # 1005
    InvalidPayloadData : WebSocketCloseStatus # 1007
    PolicyViolation : WebSocketCloseStatus # 1008
    MessageTooBig : WebSocketCloseStatus # 1009
    MandatoryExtension : WebSocketCloseStatus # 1010
    InternalServerError : WebSocketCloseStatus # 1011


class WebSocketContext(abc.ABC):
    @property
    def CookieCollection(self) -> CookieCollection: ...
    @property
    def Headers(self) -> NameValueCollection: ...
    @property
    def IsAuthenticated(self) -> bool: ...
    @property
    def IsLocal(self) -> bool: ...
    @property
    def IsSecureConnection(self) -> bool: ...
    @property
    def Origin(self) -> str: ...
    @property
    def RequestUri(self) -> Uri: ...
    @property
    def SecWebSocketKey(self) -> str: ...
    @property
    def SecWebSocketProtocols(self) -> IEnumerable_1[str]: ...
    @property
    def SecWebSocketVersion(self) -> str: ...
    @property
    def User(self) -> IPrincipal: ...
    @property
    def WebSocket(self) -> WebSocket: ...


class WebSocketCreationOptions:
    def __init__(self) -> None: ...
    @property
    def DangerousDeflateOptions(self) -> WebSocketDeflateOptions: ...
    @DangerousDeflateOptions.setter
    def DangerousDeflateOptions(self, value: WebSocketDeflateOptions) -> WebSocketDeflateOptions: ...
    @property
    def IsServer(self) -> bool: ...
    @IsServer.setter
    def IsServer(self, value: bool) -> bool: ...
    @property
    def KeepAliveInterval(self) -> TimeSpan: ...
    @KeepAliveInterval.setter
    def KeepAliveInterval(self, value: TimeSpan) -> TimeSpan: ...
    @property
    def SubProtocol(self) -> str: ...
    @SubProtocol.setter
    def SubProtocol(self, value: str) -> str: ...


class WebSocketDeflateOptions:
    def __init__(self) -> None: ...
    @property
    def ClientContextTakeover(self) -> bool: ...
    @ClientContextTakeover.setter
    def ClientContextTakeover(self, value: bool) -> bool: ...
    @property
    def ClientMaxWindowBits(self) -> int: ...
    @ClientMaxWindowBits.setter
    def ClientMaxWindowBits(self, value: int) -> int: ...
    @property
    def ServerContextTakeover(self) -> bool: ...
    @ServerContextTakeover.setter
    def ServerContextTakeover(self, value: bool) -> bool: ...
    @property
    def ServerMaxWindowBits(self) -> int: ...
    @ServerMaxWindowBits.setter
    def ServerMaxWindowBits(self, value: int) -> int: ...


class WebSocketError(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Success : WebSocketError # 0
    InvalidMessageType : WebSocketError # 1
    Faulted : WebSocketError # 2
    NativeError : WebSocketError # 3
    NotAWebSocket : WebSocketError # 4
    UnsupportedVersion : WebSocketError # 5
    UnsupportedProtocol : WebSocketError # 6
    HeaderError : WebSocketError # 7
    ConnectionClosedPrematurely : WebSocketError # 8
    InvalidState : WebSocketError # 9


class WebSocketException(Win32Exception):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, error: WebSocketError) -> None: ...
    @typing.overload
    def __init__(self, error: WebSocketError, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, error: WebSocketError, message: str) -> None: ...
    @typing.overload
    def __init__(self, error: WebSocketError, message: str, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, error: WebSocketError, nativeError: int) -> None: ...
    @typing.overload
    def __init__(self, error: WebSocketError, nativeError: int, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, error: WebSocketError, nativeError: int, message: str) -> None: ...
    @typing.overload
    def __init__(self, error: WebSocketError, nativeError: int, message: str, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, nativeError: int) -> None: ...
    @typing.overload
    def __init__(self, nativeError: int, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, nativeError: int, message: str) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def ErrorCode(self) -> int: ...
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
    def NativeErrorCode(self) -> int: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    @property
    def WebSocketErrorCode(self) -> WebSocketError: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class WebSocketMessageFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : WebSocketMessageFlags # 0
    EndOfMessage : WebSocketMessageFlags # 1
    DisableCompression : WebSocketMessageFlags # 2


class WebSocketMessageType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Text : WebSocketMessageType # 0
    Binary : WebSocketMessageType # 1
    Close : WebSocketMessageType # 2


class WebSocketReceiveResult:
    @typing.overload
    def __init__(self, count: int, messageType: WebSocketMessageType, endOfMessage: bool) -> None: ...
    @typing.overload
    def __init__(self, count: int, messageType: WebSocketMessageType, endOfMessage: bool, closeStatus: typing.Optional[WebSocketCloseStatus], closeStatusDescription: str) -> None: ...
    @property
    def CloseStatus(self) -> typing.Optional[WebSocketCloseStatus]: ...
    @property
    def CloseStatusDescription(self) -> str: ...
    @property
    def Count(self) -> int: ...
    @property
    def EndOfMessage(self) -> bool: ...
    @property
    def MessageType(self) -> WebSocketMessageType: ...


class WebSocketState(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : WebSocketState # 0
    Connecting : WebSocketState # 1
    Open : WebSocketState # 2
    CloseSent : WebSocketState # 3
    CloseReceived : WebSocketState # 4
    Closed : WebSocketState # 5
    Aborted : WebSocketState # 6

