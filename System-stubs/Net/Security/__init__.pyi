import typing
from System.IO import Stream, SeekOrigin
from System.Threading.Tasks import ValueTask, Task, ValueTask_1, Task_1
from System.Collections.Generic import IEnumerable_1, List_1
from System import MulticastDelegate, IAsyncResult, Array_1, AsyncCallback, Span_1, Memory_1, ReadOnlySpan_1, ReadOnlyMemory_1, IEquatable_1
from System.Reflection import MethodInfo
from System.Security.Cryptography.X509Certificates import X509CertificateCollection, X509Certificate, X509Chain, X509Certificate2Collection, X509Store, X509RevocationMode, X509Certificate2
from System.Security.Principal import TokenImpersonationLevel, IIdentity
from System.Net import NetworkCredential, TransportContext
from System.Security.Authentication.ExtendedProtection import ChannelBinding, ExtendedProtectionPolicy
from System.Threading import CancellationToken
from System.Security.Authentication import SslProtocols, CipherAlgorithmType, HashAlgorithmType, ExchangeAlgorithmType

class AuthenticatedStream(Stream):
    @property
    def CanRead(self) -> bool: ...
    @property
    def CanSeek(self) -> bool: ...
    @property
    def CanTimeout(self) -> bool: ...
    @property
    def CanWrite(self) -> bool: ...
    @property
    def IsAuthenticated(self) -> bool: ...
    @property
    def IsEncrypted(self) -> bool: ...
    @property
    def IsMutuallyAuthenticated(self) -> bool: ...
    @property
    def IsServer(self) -> bool: ...
    @property
    def IsSigned(self) -> bool: ...
    @property
    def LeaveInnerStreamOpen(self) -> bool: ...
    @property
    def Length(self) -> int: ...
    @property
    def Position(self) -> int: ...
    @Position.setter
    def Position(self, value: int) -> int: ...
    @property
    def ReadTimeout(self) -> int: ...
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> int: ...
    @property
    def WriteTimeout(self) -> int: ...
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> int: ...
    def DisposeAsync(self) -> ValueTask: ...


class AuthenticationLevel(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : AuthenticationLevel # 0
    MutualAuthRequested : AuthenticationLevel # 1
    MutualAuthRequired : AuthenticationLevel # 2


class CipherSuitesPolicy:
    def __init__(self, allowedCipherSuites: IEnumerable_1[TlsCipherSuite]) -> None: ...
    @property
    def AllowedCipherSuites(self) -> IEnumerable_1[TlsCipherSuite]: ...


class EncryptionPolicy(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    RequireEncryption : EncryptionPolicy # 0
    AllowNoEncryption : EncryptionPolicy # 1
    NoEncryption : EncryptionPolicy # 2


class LocalCertificateSelectionCallback(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, sender: typing.Any, targetHost: str, localCertificates: X509CertificateCollection, remoteCertificate: X509Certificate, acceptableIssuers: Array_1[str], callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> X509Certificate: ...
    def Invoke(self, sender: typing.Any, targetHost: str, localCertificates: X509CertificateCollection, remoteCertificate: X509Certificate, acceptableIssuers: Array_1[str]) -> X509Certificate: ...


class NegotiateStream(AuthenticatedStream):
    @typing.overload
    def __init__(self, innerStream: Stream) -> None: ...
    @typing.overload
    def __init__(self, innerStream: Stream, leaveInnerStreamOpen: bool) -> None: ...
    @property
    def CanRead(self) -> bool: ...
    @property
    def CanSeek(self) -> bool: ...
    @property
    def CanTimeout(self) -> bool: ...
    @property
    def CanWrite(self) -> bool: ...
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel: ...
    @property
    def IsAuthenticated(self) -> bool: ...
    @property
    def IsEncrypted(self) -> bool: ...
    @property
    def IsMutuallyAuthenticated(self) -> bool: ...
    @property
    def IsServer(self) -> bool: ...
    @property
    def IsSigned(self) -> bool: ...
    @property
    def LeaveInnerStreamOpen(self) -> bool: ...
    @property
    def Length(self) -> int: ...
    @property
    def Position(self) -> int: ...
    @Position.setter
    def Position(self, value: int) -> int: ...
    @property
    def ReadTimeout(self) -> int: ...
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> int: ...
    @property
    def RemoteIdentity(self) -> IIdentity: ...
    @property
    def WriteTimeout(self) -> int: ...
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> int: ...
    def BeginRead(self, buffer: Array_1[int], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult: ...
    def BeginWrite(self, buffer: Array_1[int], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult: ...
    def DisposeAsync(self) -> ValueTask: ...
    def EndAuthenticateAsClient(self, asyncResult: IAsyncResult) -> None: ...
    def EndAuthenticateAsServer(self, asyncResult: IAsyncResult) -> None: ...
    def EndRead(self, asyncResult: IAsyncResult) -> int: ...
    def EndWrite(self, asyncResult: IAsyncResult) -> None: ...
    def Flush(self) -> None: ...
    def Seek(self, offset: int, origin: SeekOrigin) -> int: ...
    def SetLength(self, value: int) -> None: ...
    # Skipped AuthenticateAsClient due to it being static, abstract and generic.

    AuthenticateAsClient : AuthenticateAsClient_MethodGroup
    class AuthenticateAsClient_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, targetName: str) -> None:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, binding: ChannelBinding, targetName: str) -> None:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel) -> None:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, binding: ChannelBinding, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel) -> None:...

    # Skipped AuthenticateAsClientAsync due to it being static, abstract and generic.

    AuthenticateAsClientAsync : AuthenticateAsClientAsync_MethodGroup
    class AuthenticateAsClientAsync_MethodGroup:
        @typing.overload
        def __call__(self) -> Task:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, targetName: str) -> Task:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, binding: ChannelBinding, targetName: str) -> Task:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel) -> Task:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, binding: ChannelBinding, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel) -> Task:...

    # Skipped AuthenticateAsServer due to it being static, abstract and generic.

    AuthenticateAsServer : AuthenticateAsServer_MethodGroup
    class AuthenticateAsServer_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, policy: ExtendedProtectionPolicy) -> None:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel) -> None:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, policy: ExtendedProtectionPolicy, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel) -> None:...

    # Skipped AuthenticateAsServerAsync due to it being static, abstract and generic.

    AuthenticateAsServerAsync : AuthenticateAsServerAsync_MethodGroup
    class AuthenticateAsServerAsync_MethodGroup:
        @typing.overload
        def __call__(self) -> Task:...
        @typing.overload
        def __call__(self, policy: ExtendedProtectionPolicy) -> Task:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel) -> Task:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, policy: ExtendedProtectionPolicy, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel) -> Task:...

    # Skipped BeginAuthenticateAsClient due to it being static, abstract and generic.

    BeginAuthenticateAsClient : BeginAuthenticateAsClient_MethodGroup
    class BeginAuthenticateAsClient_MethodGroup:
        @typing.overload
        def __call__(self, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, targetName: str, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, binding: ChannelBinding, targetName: str, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, binding: ChannelBinding, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult:...

    # Skipped BeginAuthenticateAsServer due to it being static, abstract and generic.

    BeginAuthenticateAsServer : BeginAuthenticateAsServer_MethodGroup
    class BeginAuthenticateAsServer_MethodGroup:
        @typing.overload
        def __call__(self, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult:...
        @typing.overload
        def __call__(self, policy: ExtendedProtectionPolicy, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult:...
        @typing.overload
        def __call__(self, credential: NetworkCredential, policy: ExtendedProtectionPolicy, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult:...

    # Skipped FlushAsync due to it being static, abstract and generic.

    FlushAsync : FlushAsync_MethodGroup
    class FlushAsync_MethodGroup:
        @typing.overload
        def __call__(self) -> Task:...
        @typing.overload
        def __call__(self, cancellationToken: CancellationToken) -> Task:...

    # Skipped Read due to it being static, abstract and generic.

    Read : Read_MethodGroup
    class Read_MethodGroup:
        @typing.overload
        def __call__(self, buffer: Span_1[int]) -> int:...
        @typing.overload
        def __call__(self, buffer: Array_1[int], offset: int, count: int) -> int:...

    # Skipped ReadAsync due to it being static, abstract and generic.

    ReadAsync : ReadAsync_MethodGroup
    class ReadAsync_MethodGroup:
        @typing.overload
        def __call__(self, buffer: Memory_1[int], cancellationToken: CancellationToken = ...) -> ValueTask_1[int]:...
        @typing.overload
        def __call__(self, buffer: Array_1[int], offset: int, count: int) -> Task_1[int]:...
        @typing.overload
        def __call__(self, buffer: Array_1[int], offset: int, count: int, cancellationToken: CancellationToken) -> Task_1[int]:...

    # Skipped Write due to it being static, abstract and generic.

    Write : Write_MethodGroup
    class Write_MethodGroup:
        @typing.overload
        def __call__(self, buffer: ReadOnlySpan_1[int]) -> None:...
        @typing.overload
        def __call__(self, buffer: Array_1[int], offset: int, count: int) -> None:...

    # Skipped WriteAsync due to it being static, abstract and generic.

    WriteAsync : WriteAsync_MethodGroup
    class WriteAsync_MethodGroup:
        @typing.overload
        def __call__(self, buffer: ReadOnlyMemory_1[int], cancellationToken: CancellationToken = ...) -> ValueTask:...
        @typing.overload
        def __call__(self, buffer: Array_1[int], offset: int, count: int) -> Task:...
        @typing.overload
        def __call__(self, buffer: Array_1[int], offset: int, count: int, cancellationToken: CancellationToken) -> Task:...



class ProtectionLevel(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : ProtectionLevel # 0
    Sign : ProtectionLevel # 1
    EncryptAndSign : ProtectionLevel # 2


class RemoteCertificateValidationCallback(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, sender: typing.Any, certificate: X509Certificate, chain: X509Chain, sslPolicyErrors: SslPolicyErrors, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> bool: ...
    def Invoke(self, sender: typing.Any, certificate: X509Certificate, chain: X509Chain, sslPolicyErrors: SslPolicyErrors) -> bool: ...


class ServerCertificateSelectionCallback(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, sender: typing.Any, hostName: str, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> X509Certificate: ...
    def Invoke(self, sender: typing.Any, hostName: str) -> X509Certificate: ...


class ServerOptionsSelectionCallback(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, stream: SslStream, clientHelloInfo: SslClientHelloInfo, state: typing.Any, cancellationToken: CancellationToken, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> ValueTask_1[SslServerAuthenticationOptions]: ...
    def Invoke(self, stream: SslStream, clientHelloInfo: SslClientHelloInfo, state: typing.Any, cancellationToken: CancellationToken) -> ValueTask_1[SslServerAuthenticationOptions]: ...


class SslApplicationProtocol(IEquatable_1[SslApplicationProtocol]):
    @typing.overload
    def __init__(self, protocol: Array_1[int]) -> None: ...
    @typing.overload
    def __init__(self, protocol: str) -> None: ...
    Http11 : SslApplicationProtocol
    Http2 : SslApplicationProtocol
    Http3 : SslApplicationProtocol
    @property
    def Protocol(self) -> ReadOnlyMemory_1[int]: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, left: SslApplicationProtocol, right: SslApplicationProtocol) -> bool: ...
    def __ne__(self, left: SslApplicationProtocol, right: SslApplicationProtocol) -> bool: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: SslApplicationProtocol) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class SslCertificateTrust:
    @staticmethod
    def CreateForX509Collection(trustList: X509Certificate2Collection, sendTrustInHandshake: bool = ...) -> SslCertificateTrust: ...
    @staticmethod
    def CreateForX509Store(store: X509Store, sendTrustInHandshake: bool = ...) -> SslCertificateTrust: ...


class SslClientAuthenticationOptions:
    def __init__(self) -> None: ...
    @property
    def AllowRenegotiation(self) -> bool: ...
    @AllowRenegotiation.setter
    def AllowRenegotiation(self, value: bool) -> bool: ...
    @property
    def ApplicationProtocols(self) -> List_1[SslApplicationProtocol]: ...
    @ApplicationProtocols.setter
    def ApplicationProtocols(self, value: List_1[SslApplicationProtocol]) -> List_1[SslApplicationProtocol]: ...
    @property
    def CertificateRevocationCheckMode(self) -> X509RevocationMode: ...
    @CertificateRevocationCheckMode.setter
    def CertificateRevocationCheckMode(self, value: X509RevocationMode) -> X509RevocationMode: ...
    @property
    def CipherSuitesPolicy(self) -> CipherSuitesPolicy: ...
    @CipherSuitesPolicy.setter
    def CipherSuitesPolicy(self, value: CipherSuitesPolicy) -> CipherSuitesPolicy: ...
    @property
    def ClientCertificates(self) -> X509CertificateCollection: ...
    @ClientCertificates.setter
    def ClientCertificates(self, value: X509CertificateCollection) -> X509CertificateCollection: ...
    @property
    def EnabledSslProtocols(self) -> SslProtocols: ...
    @EnabledSslProtocols.setter
    def EnabledSslProtocols(self, value: SslProtocols) -> SslProtocols: ...
    @property
    def EncryptionPolicy(self) -> EncryptionPolicy: ...
    @EncryptionPolicy.setter
    def EncryptionPolicy(self, value: EncryptionPolicy) -> EncryptionPolicy: ...
    @property
    def LocalCertificateSelectionCallback(self) -> LocalCertificateSelectionCallback: ...
    @LocalCertificateSelectionCallback.setter
    def LocalCertificateSelectionCallback(self, value: LocalCertificateSelectionCallback) -> LocalCertificateSelectionCallback: ...
    @property
    def RemoteCertificateValidationCallback(self) -> RemoteCertificateValidationCallback: ...
    @RemoteCertificateValidationCallback.setter
    def RemoteCertificateValidationCallback(self, value: RemoteCertificateValidationCallback) -> RemoteCertificateValidationCallback: ...
    @property
    def TargetHost(self) -> str: ...
    @TargetHost.setter
    def TargetHost(self, value: str) -> str: ...


class SslClientHelloInfo:
    @property
    def ServerName(self) -> str: ...
    @property
    def SslProtocols(self) -> SslProtocols: ...


class SslPolicyErrors(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : SslPolicyErrors # 0
    RemoteCertificateNotAvailable : SslPolicyErrors # 1
    RemoteCertificateNameMismatch : SslPolicyErrors # 2
    RemoteCertificateChainErrors : SslPolicyErrors # 4


class SslServerAuthenticationOptions:
    def __init__(self) -> None: ...
    @property
    def AllowRenegotiation(self) -> bool: ...
    @AllowRenegotiation.setter
    def AllowRenegotiation(self, value: bool) -> bool: ...
    @property
    def ApplicationProtocols(self) -> List_1[SslApplicationProtocol]: ...
    @ApplicationProtocols.setter
    def ApplicationProtocols(self, value: List_1[SslApplicationProtocol]) -> List_1[SslApplicationProtocol]: ...
    @property
    def CertificateRevocationCheckMode(self) -> X509RevocationMode: ...
    @CertificateRevocationCheckMode.setter
    def CertificateRevocationCheckMode(self, value: X509RevocationMode) -> X509RevocationMode: ...
    @property
    def CipherSuitesPolicy(self) -> CipherSuitesPolicy: ...
    @CipherSuitesPolicy.setter
    def CipherSuitesPolicy(self, value: CipherSuitesPolicy) -> CipherSuitesPolicy: ...
    @property
    def ClientCertificateRequired(self) -> bool: ...
    @ClientCertificateRequired.setter
    def ClientCertificateRequired(self, value: bool) -> bool: ...
    @property
    def EnabledSslProtocols(self) -> SslProtocols: ...
    @EnabledSslProtocols.setter
    def EnabledSslProtocols(self, value: SslProtocols) -> SslProtocols: ...
    @property
    def EncryptionPolicy(self) -> EncryptionPolicy: ...
    @EncryptionPolicy.setter
    def EncryptionPolicy(self, value: EncryptionPolicy) -> EncryptionPolicy: ...
    @property
    def RemoteCertificateValidationCallback(self) -> RemoteCertificateValidationCallback: ...
    @RemoteCertificateValidationCallback.setter
    def RemoteCertificateValidationCallback(self, value: RemoteCertificateValidationCallback) -> RemoteCertificateValidationCallback: ...
    @property
    def ServerCertificate(self) -> X509Certificate: ...
    @ServerCertificate.setter
    def ServerCertificate(self, value: X509Certificate) -> X509Certificate: ...
    @property
    def ServerCertificateContext(self) -> SslStreamCertificateContext: ...
    @ServerCertificateContext.setter
    def ServerCertificateContext(self, value: SslStreamCertificateContext) -> SslStreamCertificateContext: ...
    @property
    def ServerCertificateSelectionCallback(self) -> ServerCertificateSelectionCallback: ...
    @ServerCertificateSelectionCallback.setter
    def ServerCertificateSelectionCallback(self, value: ServerCertificateSelectionCallback) -> ServerCertificateSelectionCallback: ...


class SslStream(AuthenticatedStream):
    @typing.overload
    def __init__(self, innerStream: Stream) -> None: ...
    @typing.overload
    def __init__(self, innerStream: Stream, leaveInnerStreamOpen: bool) -> None: ...
    @typing.overload
    def __init__(self, innerStream: Stream, leaveInnerStreamOpen: bool, userCertificateValidationCallback: RemoteCertificateValidationCallback) -> None: ...
    @typing.overload
    def __init__(self, innerStream: Stream, leaveInnerStreamOpen: bool, userCertificateValidationCallback: RemoteCertificateValidationCallback, userCertificateSelectionCallback: LocalCertificateSelectionCallback) -> None: ...
    @typing.overload
    def __init__(self, innerStream: Stream, leaveInnerStreamOpen: bool, userCertificateValidationCallback: RemoteCertificateValidationCallback, userCertificateSelectionCallback: LocalCertificateSelectionCallback, encryptionPolicy: EncryptionPolicy) -> None: ...
    @property
    def CanRead(self) -> bool: ...
    @property
    def CanSeek(self) -> bool: ...
    @property
    def CanTimeout(self) -> bool: ...
    @property
    def CanWrite(self) -> bool: ...
    @property
    def CheckCertRevocationStatus(self) -> bool: ...
    @property
    def CipherAlgorithm(self) -> CipherAlgorithmType: ...
    @property
    def CipherStrength(self) -> int: ...
    @property
    def HashAlgorithm(self) -> HashAlgorithmType: ...
    @property
    def HashStrength(self) -> int: ...
    @property
    def IsAuthenticated(self) -> bool: ...
    @property
    def IsEncrypted(self) -> bool: ...
    @property
    def IsMutuallyAuthenticated(self) -> bool: ...
    @property
    def IsServer(self) -> bool: ...
    @property
    def IsSigned(self) -> bool: ...
    @property
    def KeyExchangeAlgorithm(self) -> ExchangeAlgorithmType: ...
    @property
    def KeyExchangeStrength(self) -> int: ...
    @property
    def LeaveInnerStreamOpen(self) -> bool: ...
    @property
    def Length(self) -> int: ...
    @property
    def LocalCertificate(self) -> X509Certificate: ...
    @property
    def NegotiatedApplicationProtocol(self) -> SslApplicationProtocol: ...
    @property
    def NegotiatedCipherSuite(self) -> TlsCipherSuite: ...
    @property
    def Position(self) -> int: ...
    @Position.setter
    def Position(self, value: int) -> int: ...
    @property
    def ReadTimeout(self) -> int: ...
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> int: ...
    @property
    def RemoteCertificate(self) -> X509Certificate: ...
    @property
    def SslProtocol(self) -> SslProtocols: ...
    @property
    def TargetHostName(self) -> str: ...
    @property
    def TransportContext(self) -> TransportContext: ...
    @property
    def WriteTimeout(self) -> int: ...
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> int: ...
    def BeginRead(self, buffer: Array_1[int], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult: ...
    def BeginWrite(self, buffer: Array_1[int], offset: int, count: int, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult: ...
    def DisposeAsync(self) -> ValueTask: ...
    def EndAuthenticateAsClient(self, asyncResult: IAsyncResult) -> None: ...
    def EndAuthenticateAsServer(self, asyncResult: IAsyncResult) -> None: ...
    def EndRead(self, asyncResult: IAsyncResult) -> int: ...
    def EndWrite(self, asyncResult: IAsyncResult) -> None: ...
    def Flush(self) -> None: ...
    def NegotiateClientCertificateAsync(self, cancellationToken: CancellationToken = ...) -> Task: ...
    def ReadByte(self) -> int: ...
    def Seek(self, offset: int, origin: SeekOrigin) -> int: ...
    def SetLength(self, value: int) -> None: ...
    def ShutdownAsync(self) -> Task: ...
    # Skipped AuthenticateAsClient due to it being static, abstract and generic.

    AuthenticateAsClient : AuthenticateAsClient_MethodGroup
    class AuthenticateAsClient_MethodGroup:
        @typing.overload
        def __call__(self, targetHost: str) -> None:...
        @typing.overload
        def __call__(self, sslClientAuthenticationOptions: SslClientAuthenticationOptions) -> None:...
        @typing.overload
        def __call__(self, targetHost: str, clientCertificates: X509CertificateCollection, checkCertificateRevocation: bool) -> None:...
        @typing.overload
        def __call__(self, targetHost: str, clientCertificates: X509CertificateCollection, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool) -> None:...

    # Skipped AuthenticateAsClientAsync due to it being static, abstract and generic.

    AuthenticateAsClientAsync : AuthenticateAsClientAsync_MethodGroup
    class AuthenticateAsClientAsync_MethodGroup:
        @typing.overload
        def __call__(self, targetHost: str) -> Task:...
        @typing.overload
        def __call__(self, sslClientAuthenticationOptions: SslClientAuthenticationOptions, cancellationToken: CancellationToken = ...) -> Task:...
        @typing.overload
        def __call__(self, targetHost: str, clientCertificates: X509CertificateCollection, checkCertificateRevocation: bool) -> Task:...
        @typing.overload
        def __call__(self, targetHost: str, clientCertificates: X509CertificateCollection, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool) -> Task:...

    # Skipped AuthenticateAsServer due to it being static, abstract and generic.

    AuthenticateAsServer : AuthenticateAsServer_MethodGroup
    class AuthenticateAsServer_MethodGroup:
        @typing.overload
        def __call__(self, serverCertificate: X509Certificate) -> None:...
        @typing.overload
        def __call__(self, sslServerAuthenticationOptions: SslServerAuthenticationOptions) -> None:...
        @typing.overload
        def __call__(self, serverCertificate: X509Certificate, clientCertificateRequired: bool, checkCertificateRevocation: bool) -> None:...
        @typing.overload
        def __call__(self, serverCertificate: X509Certificate, clientCertificateRequired: bool, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool) -> None:...

    # Skipped AuthenticateAsServerAsync due to it being static, abstract and generic.

    AuthenticateAsServerAsync : AuthenticateAsServerAsync_MethodGroup
    class AuthenticateAsServerAsync_MethodGroup:
        @typing.overload
        def __call__(self, serverCertificate: X509Certificate) -> Task:...
        @typing.overload
        def __call__(self, sslServerAuthenticationOptions: SslServerAuthenticationOptions, cancellationToken: CancellationToken = ...) -> Task:...
        @typing.overload
        def __call__(self, optionsCallback: ServerOptionsSelectionCallback, state: typing.Any, cancellationToken: CancellationToken = ...) -> Task:...
        @typing.overload
        def __call__(self, serverCertificate: X509Certificate, clientCertificateRequired: bool, checkCertificateRevocation: bool) -> Task:...
        @typing.overload
        def __call__(self, serverCertificate: X509Certificate, clientCertificateRequired: bool, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool) -> Task:...

    # Skipped BeginAuthenticateAsClient due to it being static, abstract and generic.

    BeginAuthenticateAsClient : BeginAuthenticateAsClient_MethodGroup
    class BeginAuthenticateAsClient_MethodGroup:
        @typing.overload
        def __call__(self, targetHost: str, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult:...
        @typing.overload
        def __call__(self, targetHost: str, clientCertificates: X509CertificateCollection, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult:...
        @typing.overload
        def __call__(self, targetHost: str, clientCertificates: X509CertificateCollection, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult:...

    # Skipped BeginAuthenticateAsServer due to it being static, abstract and generic.

    BeginAuthenticateAsServer : BeginAuthenticateAsServer_MethodGroup
    class BeginAuthenticateAsServer_MethodGroup:
        @typing.overload
        def __call__(self, serverCertificate: X509Certificate, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult:...
        @typing.overload
        def __call__(self, serverCertificate: X509Certificate, clientCertificateRequired: bool, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult:...
        @typing.overload
        def __call__(self, serverCertificate: X509Certificate, clientCertificateRequired: bool, enabledSslProtocols: SslProtocols, checkCertificateRevocation: bool, asyncCallback: AsyncCallback, asyncState: typing.Any) -> IAsyncResult:...

    # Skipped FlushAsync due to it being static, abstract and generic.

    FlushAsync : FlushAsync_MethodGroup
    class FlushAsync_MethodGroup:
        @typing.overload
        def __call__(self) -> Task:...
        @typing.overload
        def __call__(self, cancellationToken: CancellationToken) -> Task:...

    # Skipped Read due to it being static, abstract and generic.

    Read : Read_MethodGroup
    class Read_MethodGroup:
        @typing.overload
        def __call__(self, buffer: Span_1[int]) -> int:...
        @typing.overload
        def __call__(self, buffer: Array_1[int], offset: int, count: int) -> int:...

    # Skipped ReadAsync due to it being static, abstract and generic.

    ReadAsync : ReadAsync_MethodGroup
    class ReadAsync_MethodGroup:
        @typing.overload
        def __call__(self, buffer: Memory_1[int], cancellationToken: CancellationToken = ...) -> ValueTask_1[int]:...
        @typing.overload
        def __call__(self, buffer: Array_1[int], offset: int, count: int) -> Task_1[int]:...
        @typing.overload
        def __call__(self, buffer: Array_1[int], offset: int, count: int, cancellationToken: CancellationToken) -> Task_1[int]:...

    # Skipped Write due to it being static, abstract and generic.

    Write : Write_MethodGroup
    class Write_MethodGroup:
        @typing.overload
        def __call__(self, buffer: Array_1[int]) -> None:...
        @typing.overload
        def __call__(self, buffer: ReadOnlySpan_1[int]) -> None:...
        @typing.overload
        def __call__(self, buffer: Array_1[int], offset: int, count: int) -> None:...

    # Skipped WriteAsync due to it being static, abstract and generic.

    WriteAsync : WriteAsync_MethodGroup
    class WriteAsync_MethodGroup:
        @typing.overload
        def __call__(self, buffer: ReadOnlyMemory_1[int], cancellationToken: CancellationToken = ...) -> ValueTask:...
        @typing.overload
        def __call__(self, buffer: Array_1[int], offset: int, count: int) -> Task:...
        @typing.overload
        def __call__(self, buffer: Array_1[int], offset: int, count: int, cancellationToken: CancellationToken) -> Task:...



class SslStreamCertificateContext:
    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup
    class Create_MethodGroup:
        @typing.overload
        def __call__(self, target: X509Certificate2, additionalCertificates: X509Certificate2Collection, offline: bool) -> SslStreamCertificateContext:...
        @typing.overload
        def __call__(self, target: X509Certificate2, additionalCertificates: X509Certificate2Collection, offline: bool = ..., trust: SslCertificateTrust = ...) -> SslStreamCertificateContext:...



class TlsCipherSuite(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    TLS_NULL_WITH_NULL_NULL : TlsCipherSuite # 0
    TLS_RSA_WITH_NULL_MD5 : TlsCipherSuite # 1
    TLS_RSA_WITH_NULL_SHA : TlsCipherSuite # 2
    TLS_RSA_EXPORT_WITH_RC4_40_MD5 : TlsCipherSuite # 3
    TLS_RSA_WITH_RC4_128_MD5 : TlsCipherSuite # 4
    TLS_RSA_WITH_RC4_128_SHA : TlsCipherSuite # 5
    TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5 : TlsCipherSuite # 6
    TLS_RSA_WITH_IDEA_CBC_SHA : TlsCipherSuite # 7
    TLS_RSA_EXPORT_WITH_DES40_CBC_SHA : TlsCipherSuite # 8
    TLS_RSA_WITH_DES_CBC_SHA : TlsCipherSuite # 9
    TLS_RSA_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 10
    TLS_DH_DSS_EXPORT_WITH_DES40_CBC_SHA : TlsCipherSuite # 11
    TLS_DH_DSS_WITH_DES_CBC_SHA : TlsCipherSuite # 12
    TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 13
    TLS_DH_RSA_EXPORT_WITH_DES40_CBC_SHA : TlsCipherSuite # 14
    TLS_DH_RSA_WITH_DES_CBC_SHA : TlsCipherSuite # 15
    TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 16
    TLS_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA : TlsCipherSuite # 17
    TLS_DHE_DSS_WITH_DES_CBC_SHA : TlsCipherSuite # 18
    TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 19
    TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA : TlsCipherSuite # 20
    TLS_DHE_RSA_WITH_DES_CBC_SHA : TlsCipherSuite # 21
    TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 22
    TLS_DH_anon_EXPORT_WITH_RC4_40_MD5 : TlsCipherSuite # 23
    TLS_DH_anon_WITH_RC4_128_MD5 : TlsCipherSuite # 24
    TLS_DH_anon_EXPORT_WITH_DES40_CBC_SHA : TlsCipherSuite # 25
    TLS_DH_anon_WITH_DES_CBC_SHA : TlsCipherSuite # 26
    TLS_DH_anon_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 27
    TLS_KRB5_WITH_DES_CBC_SHA : TlsCipherSuite # 30
    TLS_KRB5_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 31
    TLS_KRB5_WITH_RC4_128_SHA : TlsCipherSuite # 32
    TLS_KRB5_WITH_IDEA_CBC_SHA : TlsCipherSuite # 33
    TLS_KRB5_WITH_DES_CBC_MD5 : TlsCipherSuite # 34
    TLS_KRB5_WITH_3DES_EDE_CBC_MD5 : TlsCipherSuite # 35
    TLS_KRB5_WITH_RC4_128_MD5 : TlsCipherSuite # 36
    TLS_KRB5_WITH_IDEA_CBC_MD5 : TlsCipherSuite # 37
    TLS_KRB5_EXPORT_WITH_DES_CBC_40_SHA : TlsCipherSuite # 38
    TLS_KRB5_EXPORT_WITH_RC2_CBC_40_SHA : TlsCipherSuite # 39
    TLS_KRB5_EXPORT_WITH_RC4_40_SHA : TlsCipherSuite # 40
    TLS_KRB5_EXPORT_WITH_DES_CBC_40_MD5 : TlsCipherSuite # 41
    TLS_KRB5_EXPORT_WITH_RC2_CBC_40_MD5 : TlsCipherSuite # 42
    TLS_KRB5_EXPORT_WITH_RC4_40_MD5 : TlsCipherSuite # 43
    TLS_PSK_WITH_NULL_SHA : TlsCipherSuite # 44
    TLS_DHE_PSK_WITH_NULL_SHA : TlsCipherSuite # 45
    TLS_RSA_PSK_WITH_NULL_SHA : TlsCipherSuite # 46
    TLS_RSA_WITH_AES_128_CBC_SHA : TlsCipherSuite # 47
    TLS_DH_DSS_WITH_AES_128_CBC_SHA : TlsCipherSuite # 48
    TLS_DH_RSA_WITH_AES_128_CBC_SHA : TlsCipherSuite # 49
    TLS_DHE_DSS_WITH_AES_128_CBC_SHA : TlsCipherSuite # 50
    TLS_DHE_RSA_WITH_AES_128_CBC_SHA : TlsCipherSuite # 51
    TLS_DH_anon_WITH_AES_128_CBC_SHA : TlsCipherSuite # 52
    TLS_RSA_WITH_AES_256_CBC_SHA : TlsCipherSuite # 53
    TLS_DH_DSS_WITH_AES_256_CBC_SHA : TlsCipherSuite # 54
    TLS_DH_RSA_WITH_AES_256_CBC_SHA : TlsCipherSuite # 55
    TLS_DHE_DSS_WITH_AES_256_CBC_SHA : TlsCipherSuite # 56
    TLS_DHE_RSA_WITH_AES_256_CBC_SHA : TlsCipherSuite # 57
    TLS_DH_anon_WITH_AES_256_CBC_SHA : TlsCipherSuite # 58
    TLS_RSA_WITH_NULL_SHA256 : TlsCipherSuite # 59
    TLS_RSA_WITH_AES_128_CBC_SHA256 : TlsCipherSuite # 60
    TLS_RSA_WITH_AES_256_CBC_SHA256 : TlsCipherSuite # 61
    TLS_DH_DSS_WITH_AES_128_CBC_SHA256 : TlsCipherSuite # 62
    TLS_DH_RSA_WITH_AES_128_CBC_SHA256 : TlsCipherSuite # 63
    TLS_DHE_DSS_WITH_AES_128_CBC_SHA256 : TlsCipherSuite # 64
    TLS_RSA_WITH_CAMELLIA_128_CBC_SHA : TlsCipherSuite # 65
    TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA : TlsCipherSuite # 66
    TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA : TlsCipherSuite # 67
    TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA : TlsCipherSuite # 68
    TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA : TlsCipherSuite # 69
    TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA : TlsCipherSuite # 70
    TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 : TlsCipherSuite # 103
    TLS_DH_DSS_WITH_AES_256_CBC_SHA256 : TlsCipherSuite # 104
    TLS_DH_RSA_WITH_AES_256_CBC_SHA256 : TlsCipherSuite # 105
    TLS_DHE_DSS_WITH_AES_256_CBC_SHA256 : TlsCipherSuite # 106
    TLS_DHE_RSA_WITH_AES_256_CBC_SHA256 : TlsCipherSuite # 107
    TLS_DH_anon_WITH_AES_128_CBC_SHA256 : TlsCipherSuite # 108
    TLS_DH_anon_WITH_AES_256_CBC_SHA256 : TlsCipherSuite # 109
    TLS_RSA_WITH_CAMELLIA_256_CBC_SHA : TlsCipherSuite # 132
    TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA : TlsCipherSuite # 133
    TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA : TlsCipherSuite # 134
    TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA : TlsCipherSuite # 135
    TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA : TlsCipherSuite # 136
    TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA : TlsCipherSuite # 137
    TLS_PSK_WITH_RC4_128_SHA : TlsCipherSuite # 138
    TLS_PSK_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 139
    TLS_PSK_WITH_AES_128_CBC_SHA : TlsCipherSuite # 140
    TLS_PSK_WITH_AES_256_CBC_SHA : TlsCipherSuite # 141
    TLS_DHE_PSK_WITH_RC4_128_SHA : TlsCipherSuite # 142
    TLS_DHE_PSK_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 143
    TLS_DHE_PSK_WITH_AES_128_CBC_SHA : TlsCipherSuite # 144
    TLS_DHE_PSK_WITH_AES_256_CBC_SHA : TlsCipherSuite # 145
    TLS_RSA_PSK_WITH_RC4_128_SHA : TlsCipherSuite # 146
    TLS_RSA_PSK_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 147
    TLS_RSA_PSK_WITH_AES_128_CBC_SHA : TlsCipherSuite # 148
    TLS_RSA_PSK_WITH_AES_256_CBC_SHA : TlsCipherSuite # 149
    TLS_RSA_WITH_SEED_CBC_SHA : TlsCipherSuite # 150
    TLS_DH_DSS_WITH_SEED_CBC_SHA : TlsCipherSuite # 151
    TLS_DH_RSA_WITH_SEED_CBC_SHA : TlsCipherSuite # 152
    TLS_DHE_DSS_WITH_SEED_CBC_SHA : TlsCipherSuite # 153
    TLS_DHE_RSA_WITH_SEED_CBC_SHA : TlsCipherSuite # 154
    TLS_DH_anon_WITH_SEED_CBC_SHA : TlsCipherSuite # 155
    TLS_RSA_WITH_AES_128_GCM_SHA256 : TlsCipherSuite # 156
    TLS_RSA_WITH_AES_256_GCM_SHA384 : TlsCipherSuite # 157
    TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 : TlsCipherSuite # 158
    TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 : TlsCipherSuite # 159
    TLS_DH_RSA_WITH_AES_128_GCM_SHA256 : TlsCipherSuite # 160
    TLS_DH_RSA_WITH_AES_256_GCM_SHA384 : TlsCipherSuite # 161
    TLS_DHE_DSS_WITH_AES_128_GCM_SHA256 : TlsCipherSuite # 162
    TLS_DHE_DSS_WITH_AES_256_GCM_SHA384 : TlsCipherSuite # 163
    TLS_DH_DSS_WITH_AES_128_GCM_SHA256 : TlsCipherSuite # 164
    TLS_DH_DSS_WITH_AES_256_GCM_SHA384 : TlsCipherSuite # 165
    TLS_DH_anon_WITH_AES_128_GCM_SHA256 : TlsCipherSuite # 166
    TLS_DH_anon_WITH_AES_256_GCM_SHA384 : TlsCipherSuite # 167
    TLS_PSK_WITH_AES_128_GCM_SHA256 : TlsCipherSuite # 168
    TLS_PSK_WITH_AES_256_GCM_SHA384 : TlsCipherSuite # 169
    TLS_DHE_PSK_WITH_AES_128_GCM_SHA256 : TlsCipherSuite # 170
    TLS_DHE_PSK_WITH_AES_256_GCM_SHA384 : TlsCipherSuite # 171
    TLS_RSA_PSK_WITH_AES_128_GCM_SHA256 : TlsCipherSuite # 172
    TLS_RSA_PSK_WITH_AES_256_GCM_SHA384 : TlsCipherSuite # 173
    TLS_PSK_WITH_AES_128_CBC_SHA256 : TlsCipherSuite # 174
    TLS_PSK_WITH_AES_256_CBC_SHA384 : TlsCipherSuite # 175
    TLS_PSK_WITH_NULL_SHA256 : TlsCipherSuite # 176
    TLS_PSK_WITH_NULL_SHA384 : TlsCipherSuite # 177
    TLS_DHE_PSK_WITH_AES_128_CBC_SHA256 : TlsCipherSuite # 178
    TLS_DHE_PSK_WITH_AES_256_CBC_SHA384 : TlsCipherSuite # 179
    TLS_DHE_PSK_WITH_NULL_SHA256 : TlsCipherSuite # 180
    TLS_DHE_PSK_WITH_NULL_SHA384 : TlsCipherSuite # 181
    TLS_RSA_PSK_WITH_AES_128_CBC_SHA256 : TlsCipherSuite # 182
    TLS_RSA_PSK_WITH_AES_256_CBC_SHA384 : TlsCipherSuite # 183
    TLS_RSA_PSK_WITH_NULL_SHA256 : TlsCipherSuite # 184
    TLS_RSA_PSK_WITH_NULL_SHA384 : TlsCipherSuite # 185
    TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256 : TlsCipherSuite # 186
    TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA256 : TlsCipherSuite # 187
    TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA256 : TlsCipherSuite # 188
    TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA256 : TlsCipherSuite # 189
    TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 : TlsCipherSuite # 190
    TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA256 : TlsCipherSuite # 191
    TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256 : TlsCipherSuite # 192
    TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA256 : TlsCipherSuite # 193
    TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA256 : TlsCipherSuite # 194
    TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA256 : TlsCipherSuite # 195
    TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA256 : TlsCipherSuite # 196
    TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA256 : TlsCipherSuite # 197
    TLS_AES_128_GCM_SHA256 : TlsCipherSuite # 4865
    TLS_AES_256_GCM_SHA384 : TlsCipherSuite # 4866
    TLS_CHACHA20_POLY1305_SHA256 : TlsCipherSuite # 4867
    TLS_AES_128_CCM_SHA256 : TlsCipherSuite # 4868
    TLS_AES_128_CCM_8_SHA256 : TlsCipherSuite # 4869
    TLS_ECDH_ECDSA_WITH_NULL_SHA : TlsCipherSuite # 49153
    TLS_ECDH_ECDSA_WITH_RC4_128_SHA : TlsCipherSuite # 49154
    TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 49155
    TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA : TlsCipherSuite # 49156
    TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA : TlsCipherSuite # 49157
    TLS_ECDHE_ECDSA_WITH_NULL_SHA : TlsCipherSuite # 49158
    TLS_ECDHE_ECDSA_WITH_RC4_128_SHA : TlsCipherSuite # 49159
    TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 49160
    TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA : TlsCipherSuite # 49161
    TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA : TlsCipherSuite # 49162
    TLS_ECDH_RSA_WITH_NULL_SHA : TlsCipherSuite # 49163
    TLS_ECDH_RSA_WITH_RC4_128_SHA : TlsCipherSuite # 49164
    TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 49165
    TLS_ECDH_RSA_WITH_AES_128_CBC_SHA : TlsCipherSuite # 49166
    TLS_ECDH_RSA_WITH_AES_256_CBC_SHA : TlsCipherSuite # 49167
    TLS_ECDHE_RSA_WITH_NULL_SHA : TlsCipherSuite # 49168
    TLS_ECDHE_RSA_WITH_RC4_128_SHA : TlsCipherSuite # 49169
    TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 49170
    TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA : TlsCipherSuite # 49171
    TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA : TlsCipherSuite # 49172
    TLS_ECDH_anon_WITH_NULL_SHA : TlsCipherSuite # 49173
    TLS_ECDH_anon_WITH_RC4_128_SHA : TlsCipherSuite # 49174
    TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 49175
    TLS_ECDH_anon_WITH_AES_128_CBC_SHA : TlsCipherSuite # 49176
    TLS_ECDH_anon_WITH_AES_256_CBC_SHA : TlsCipherSuite # 49177
    TLS_SRP_SHA_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 49178
    TLS_SRP_SHA_RSA_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 49179
    TLS_SRP_SHA_DSS_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 49180
    TLS_SRP_SHA_WITH_AES_128_CBC_SHA : TlsCipherSuite # 49181
    TLS_SRP_SHA_RSA_WITH_AES_128_CBC_SHA : TlsCipherSuite # 49182
    TLS_SRP_SHA_DSS_WITH_AES_128_CBC_SHA : TlsCipherSuite # 49183
    TLS_SRP_SHA_WITH_AES_256_CBC_SHA : TlsCipherSuite # 49184
    TLS_SRP_SHA_RSA_WITH_AES_256_CBC_SHA : TlsCipherSuite # 49185
    TLS_SRP_SHA_DSS_WITH_AES_256_CBC_SHA : TlsCipherSuite # 49186
    TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 : TlsCipherSuite # 49187
    TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 : TlsCipherSuite # 49188
    TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256 : TlsCipherSuite # 49189
    TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384 : TlsCipherSuite # 49190
    TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 : TlsCipherSuite # 49191
    TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 : TlsCipherSuite # 49192
    TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256 : TlsCipherSuite # 49193
    TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384 : TlsCipherSuite # 49194
    TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 : TlsCipherSuite # 49195
    TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 : TlsCipherSuite # 49196
    TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256 : TlsCipherSuite # 49197
    TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384 : TlsCipherSuite # 49198
    TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 : TlsCipherSuite # 49199
    TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 : TlsCipherSuite # 49200
    TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256 : TlsCipherSuite # 49201
    TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384 : TlsCipherSuite # 49202
    TLS_ECDHE_PSK_WITH_RC4_128_SHA : TlsCipherSuite # 49203
    TLS_ECDHE_PSK_WITH_3DES_EDE_CBC_SHA : TlsCipherSuite # 49204
    TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA : TlsCipherSuite # 49205
    TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA : TlsCipherSuite # 49206
    TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA256 : TlsCipherSuite # 49207
    TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384 : TlsCipherSuite # 49208
    TLS_ECDHE_PSK_WITH_NULL_SHA : TlsCipherSuite # 49209
    TLS_ECDHE_PSK_WITH_NULL_SHA256 : TlsCipherSuite # 49210
    TLS_ECDHE_PSK_WITH_NULL_SHA384 : TlsCipherSuite # 49211
    TLS_RSA_WITH_ARIA_128_CBC_SHA256 : TlsCipherSuite # 49212
    TLS_RSA_WITH_ARIA_256_CBC_SHA384 : TlsCipherSuite # 49213
    TLS_DH_DSS_WITH_ARIA_128_CBC_SHA256 : TlsCipherSuite # 49214
    TLS_DH_DSS_WITH_ARIA_256_CBC_SHA384 : TlsCipherSuite # 49215
    TLS_DH_RSA_WITH_ARIA_128_CBC_SHA256 : TlsCipherSuite # 49216
    TLS_DH_RSA_WITH_ARIA_256_CBC_SHA384 : TlsCipherSuite # 49217
    TLS_DHE_DSS_WITH_ARIA_128_CBC_SHA256 : TlsCipherSuite # 49218
    TLS_DHE_DSS_WITH_ARIA_256_CBC_SHA384 : TlsCipherSuite # 49219
    TLS_DHE_RSA_WITH_ARIA_128_CBC_SHA256 : TlsCipherSuite # 49220
    TLS_DHE_RSA_WITH_ARIA_256_CBC_SHA384 : TlsCipherSuite # 49221
    TLS_DH_anon_WITH_ARIA_128_CBC_SHA256 : TlsCipherSuite # 49222
    TLS_DH_anon_WITH_ARIA_256_CBC_SHA384 : TlsCipherSuite # 49223
    TLS_ECDHE_ECDSA_WITH_ARIA_128_CBC_SHA256 : TlsCipherSuite # 49224
    TLS_ECDHE_ECDSA_WITH_ARIA_256_CBC_SHA384 : TlsCipherSuite # 49225
    TLS_ECDH_ECDSA_WITH_ARIA_128_CBC_SHA256 : TlsCipherSuite # 49226
    TLS_ECDH_ECDSA_WITH_ARIA_256_CBC_SHA384 : TlsCipherSuite # 49227
    TLS_ECDHE_RSA_WITH_ARIA_128_CBC_SHA256 : TlsCipherSuite # 49228
    TLS_ECDHE_RSA_WITH_ARIA_256_CBC_SHA384 : TlsCipherSuite # 49229
    TLS_ECDH_RSA_WITH_ARIA_128_CBC_SHA256 : TlsCipherSuite # 49230
    TLS_ECDH_RSA_WITH_ARIA_256_CBC_SHA384 : TlsCipherSuite # 49231
    TLS_RSA_WITH_ARIA_128_GCM_SHA256 : TlsCipherSuite # 49232
    TLS_RSA_WITH_ARIA_256_GCM_SHA384 : TlsCipherSuite # 49233
    TLS_DHE_RSA_WITH_ARIA_128_GCM_SHA256 : TlsCipherSuite # 49234
    TLS_DHE_RSA_WITH_ARIA_256_GCM_SHA384 : TlsCipherSuite # 49235
    TLS_DH_RSA_WITH_ARIA_128_GCM_SHA256 : TlsCipherSuite # 49236
    TLS_DH_RSA_WITH_ARIA_256_GCM_SHA384 : TlsCipherSuite # 49237
    TLS_DHE_DSS_WITH_ARIA_128_GCM_SHA256 : TlsCipherSuite # 49238
    TLS_DHE_DSS_WITH_ARIA_256_GCM_SHA384 : TlsCipherSuite # 49239
    TLS_DH_DSS_WITH_ARIA_128_GCM_SHA256 : TlsCipherSuite # 49240
    TLS_DH_DSS_WITH_ARIA_256_GCM_SHA384 : TlsCipherSuite # 49241
    TLS_DH_anon_WITH_ARIA_128_GCM_SHA256 : TlsCipherSuite # 49242
    TLS_DH_anon_WITH_ARIA_256_GCM_SHA384 : TlsCipherSuite # 49243
    TLS_ECDHE_ECDSA_WITH_ARIA_128_GCM_SHA256 : TlsCipherSuite # 49244
    TLS_ECDHE_ECDSA_WITH_ARIA_256_GCM_SHA384 : TlsCipherSuite # 49245
    TLS_ECDH_ECDSA_WITH_ARIA_128_GCM_SHA256 : TlsCipherSuite # 49246
    TLS_ECDH_ECDSA_WITH_ARIA_256_GCM_SHA384 : TlsCipherSuite # 49247
    TLS_ECDHE_RSA_WITH_ARIA_128_GCM_SHA256 : TlsCipherSuite # 49248
    TLS_ECDHE_RSA_WITH_ARIA_256_GCM_SHA384 : TlsCipherSuite # 49249
    TLS_ECDH_RSA_WITH_ARIA_128_GCM_SHA256 : TlsCipherSuite # 49250
    TLS_ECDH_RSA_WITH_ARIA_256_GCM_SHA384 : TlsCipherSuite # 49251
    TLS_PSK_WITH_ARIA_128_CBC_SHA256 : TlsCipherSuite # 49252
    TLS_PSK_WITH_ARIA_256_CBC_SHA384 : TlsCipherSuite # 49253
    TLS_DHE_PSK_WITH_ARIA_128_CBC_SHA256 : TlsCipherSuite # 49254
    TLS_DHE_PSK_WITH_ARIA_256_CBC_SHA384 : TlsCipherSuite # 49255
    TLS_RSA_PSK_WITH_ARIA_128_CBC_SHA256 : TlsCipherSuite # 49256
    TLS_RSA_PSK_WITH_ARIA_256_CBC_SHA384 : TlsCipherSuite # 49257
    TLS_PSK_WITH_ARIA_128_GCM_SHA256 : TlsCipherSuite # 49258
    TLS_PSK_WITH_ARIA_256_GCM_SHA384 : TlsCipherSuite # 49259
    TLS_DHE_PSK_WITH_ARIA_128_GCM_SHA256 : TlsCipherSuite # 49260
    TLS_DHE_PSK_WITH_ARIA_256_GCM_SHA384 : TlsCipherSuite # 49261
    TLS_RSA_PSK_WITH_ARIA_128_GCM_SHA256 : TlsCipherSuite # 49262
    TLS_RSA_PSK_WITH_ARIA_256_GCM_SHA384 : TlsCipherSuite # 49263
    TLS_ECDHE_PSK_WITH_ARIA_128_CBC_SHA256 : TlsCipherSuite # 49264
    TLS_ECDHE_PSK_WITH_ARIA_256_CBC_SHA384 : TlsCipherSuite # 49265
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_CBC_SHA256 : TlsCipherSuite # 49266
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_CBC_SHA384 : TlsCipherSuite # 49267
    TLS_ECDH_ECDSA_WITH_CAMELLIA_128_CBC_SHA256 : TlsCipherSuite # 49268
    TLS_ECDH_ECDSA_WITH_CAMELLIA_256_CBC_SHA384 : TlsCipherSuite # 49269
    TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 : TlsCipherSuite # 49270
    TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384 : TlsCipherSuite # 49271
    TLS_ECDH_RSA_WITH_CAMELLIA_128_CBC_SHA256 : TlsCipherSuite # 49272
    TLS_ECDH_RSA_WITH_CAMELLIA_256_CBC_SHA384 : TlsCipherSuite # 49273
    TLS_RSA_WITH_CAMELLIA_128_GCM_SHA256 : TlsCipherSuite # 49274
    TLS_RSA_WITH_CAMELLIA_256_GCM_SHA384 : TlsCipherSuite # 49275
    TLS_DHE_RSA_WITH_CAMELLIA_128_GCM_SHA256 : TlsCipherSuite # 49276
    TLS_DHE_RSA_WITH_CAMELLIA_256_GCM_SHA384 : TlsCipherSuite # 49277
    TLS_DH_RSA_WITH_CAMELLIA_128_GCM_SHA256 : TlsCipherSuite # 49278
    TLS_DH_RSA_WITH_CAMELLIA_256_GCM_SHA384 : TlsCipherSuite # 49279
    TLS_DHE_DSS_WITH_CAMELLIA_128_GCM_SHA256 : TlsCipherSuite # 49280
    TLS_DHE_DSS_WITH_CAMELLIA_256_GCM_SHA384 : TlsCipherSuite # 49281
    TLS_DH_DSS_WITH_CAMELLIA_128_GCM_SHA256 : TlsCipherSuite # 49282
    TLS_DH_DSS_WITH_CAMELLIA_256_GCM_SHA384 : TlsCipherSuite # 49283
    TLS_DH_anon_WITH_CAMELLIA_128_GCM_SHA256 : TlsCipherSuite # 49284
    TLS_DH_anon_WITH_CAMELLIA_256_GCM_SHA384 : TlsCipherSuite # 49285
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_GCM_SHA256 : TlsCipherSuite # 49286
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_GCM_SHA384 : TlsCipherSuite # 49287
    TLS_ECDH_ECDSA_WITH_CAMELLIA_128_GCM_SHA256 : TlsCipherSuite # 49288
    TLS_ECDH_ECDSA_WITH_CAMELLIA_256_GCM_SHA384 : TlsCipherSuite # 49289
    TLS_ECDHE_RSA_WITH_CAMELLIA_128_GCM_SHA256 : TlsCipherSuite # 49290
    TLS_ECDHE_RSA_WITH_CAMELLIA_256_GCM_SHA384 : TlsCipherSuite # 49291
    TLS_ECDH_RSA_WITH_CAMELLIA_128_GCM_SHA256 : TlsCipherSuite # 49292
    TLS_ECDH_RSA_WITH_CAMELLIA_256_GCM_SHA384 : TlsCipherSuite # 49293
    TLS_PSK_WITH_CAMELLIA_128_GCM_SHA256 : TlsCipherSuite # 49294
    TLS_PSK_WITH_CAMELLIA_256_GCM_SHA384 : TlsCipherSuite # 49295
    TLS_DHE_PSK_WITH_CAMELLIA_128_GCM_SHA256 : TlsCipherSuite # 49296
    TLS_DHE_PSK_WITH_CAMELLIA_256_GCM_SHA384 : TlsCipherSuite # 49297
    TLS_RSA_PSK_WITH_CAMELLIA_128_GCM_SHA256 : TlsCipherSuite # 49298
    TLS_RSA_PSK_WITH_CAMELLIA_256_GCM_SHA384 : TlsCipherSuite # 49299
    TLS_PSK_WITH_CAMELLIA_128_CBC_SHA256 : TlsCipherSuite # 49300
    TLS_PSK_WITH_CAMELLIA_256_CBC_SHA384 : TlsCipherSuite # 49301
    TLS_DHE_PSK_WITH_CAMELLIA_128_CBC_SHA256 : TlsCipherSuite # 49302
    TLS_DHE_PSK_WITH_CAMELLIA_256_CBC_SHA384 : TlsCipherSuite # 49303
    TLS_RSA_PSK_WITH_CAMELLIA_128_CBC_SHA256 : TlsCipherSuite # 49304
    TLS_RSA_PSK_WITH_CAMELLIA_256_CBC_SHA384 : TlsCipherSuite # 49305
    TLS_ECDHE_PSK_WITH_CAMELLIA_128_CBC_SHA256 : TlsCipherSuite # 49306
    TLS_ECDHE_PSK_WITH_CAMELLIA_256_CBC_SHA384 : TlsCipherSuite # 49307
    TLS_RSA_WITH_AES_128_CCM : TlsCipherSuite # 49308
    TLS_RSA_WITH_AES_256_CCM : TlsCipherSuite # 49309
    TLS_DHE_RSA_WITH_AES_128_CCM : TlsCipherSuite # 49310
    TLS_DHE_RSA_WITH_AES_256_CCM : TlsCipherSuite # 49311
    TLS_RSA_WITH_AES_128_CCM_8 : TlsCipherSuite # 49312
    TLS_RSA_WITH_AES_256_CCM_8 : TlsCipherSuite # 49313
    TLS_DHE_RSA_WITH_AES_128_CCM_8 : TlsCipherSuite # 49314
    TLS_DHE_RSA_WITH_AES_256_CCM_8 : TlsCipherSuite # 49315
    TLS_PSK_WITH_AES_128_CCM : TlsCipherSuite # 49316
    TLS_PSK_WITH_AES_256_CCM : TlsCipherSuite # 49317
    TLS_DHE_PSK_WITH_AES_128_CCM : TlsCipherSuite # 49318
    TLS_DHE_PSK_WITH_AES_256_CCM : TlsCipherSuite # 49319
    TLS_PSK_WITH_AES_128_CCM_8 : TlsCipherSuite # 49320
    TLS_PSK_WITH_AES_256_CCM_8 : TlsCipherSuite # 49321
    TLS_PSK_DHE_WITH_AES_128_CCM_8 : TlsCipherSuite # 49322
    TLS_PSK_DHE_WITH_AES_256_CCM_8 : TlsCipherSuite # 49323
    TLS_ECDHE_ECDSA_WITH_AES_128_CCM : TlsCipherSuite # 49324
    TLS_ECDHE_ECDSA_WITH_AES_256_CCM : TlsCipherSuite # 49325
    TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8 : TlsCipherSuite # 49326
    TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8 : TlsCipherSuite # 49327
    TLS_ECCPWD_WITH_AES_128_GCM_SHA256 : TlsCipherSuite # 49328
    TLS_ECCPWD_WITH_AES_256_GCM_SHA384 : TlsCipherSuite # 49329
    TLS_ECCPWD_WITH_AES_128_CCM_SHA256 : TlsCipherSuite # 49330
    TLS_ECCPWD_WITH_AES_256_CCM_SHA384 : TlsCipherSuite # 49331
    TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 : TlsCipherSuite # 52392
    TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 : TlsCipherSuite # 52393
    TLS_DHE_RSA_WITH_CHACHA20_POLY1305_SHA256 : TlsCipherSuite # 52394
    TLS_PSK_WITH_CHACHA20_POLY1305_SHA256 : TlsCipherSuite # 52395
    TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256 : TlsCipherSuite # 52396
    TLS_DHE_PSK_WITH_CHACHA20_POLY1305_SHA256 : TlsCipherSuite # 52397
    TLS_RSA_PSK_WITH_CHACHA20_POLY1305_SHA256 : TlsCipherSuite # 52398
    TLS_ECDHE_PSK_WITH_AES_128_GCM_SHA256 : TlsCipherSuite # 53249
    TLS_ECDHE_PSK_WITH_AES_256_GCM_SHA384 : TlsCipherSuite # 53250
    TLS_ECDHE_PSK_WITH_AES_128_CCM_8_SHA256 : TlsCipherSuite # 53251
    TLS_ECDHE_PSK_WITH_AES_128_CCM_SHA256 : TlsCipherSuite # 53253

