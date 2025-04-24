import typing, abc
from System import Guid, Array_1, Exception, IDisposable, DateTime
from System.Runtime.Serialization import ISerializable

class DependentCloneOption(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    BlockCommitUntilComplete : DependentCloneOption # 0
    RollbackIfNotComplete : DependentCloneOption # 1


class DependentTransaction(Transaction):
    @property
    def IsolationLevel(self) -> IsolationLevel: ...
    @property
    def PromoterType(self) -> Guid: ...
    @property
    def TransactionInformation(self) -> TransactionInformation: ...
    def Complete(self) -> None: ...


class Enlistment:
    def Done(self) -> None: ...


class EnlistmentOptions(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : EnlistmentOptions # 0
    EnlistDuringPrepareRequired : EnlistmentOptions # 1


class IEnlistmentNotification(typing.Protocol):
    @abc.abstractmethod
    def Commit(self, enlistment: Enlistment) -> None: ...
    @abc.abstractmethod
    def InDoubt(self, enlistment: Enlistment) -> None: ...
    @abc.abstractmethod
    def Prepare(self, preparingEnlistment: PreparingEnlistment) -> None: ...
    @abc.abstractmethod
    def Rollback(self, enlistment: Enlistment) -> None: ...


class IPromotableSinglePhaseNotification(ITransactionPromoter, typing.Protocol):
    @abc.abstractmethod
    def Initialize(self) -> None: ...
    @abc.abstractmethod
    def Rollback(self, singlePhaseEnlistment: SinglePhaseEnlistment) -> None: ...
    @abc.abstractmethod
    def SinglePhaseCommit(self, singlePhaseEnlistment: SinglePhaseEnlistment) -> None: ...


class ISinglePhaseNotification(IEnlistmentNotification, typing.Protocol):
    @abc.abstractmethod
    def SinglePhaseCommit(self, singlePhaseEnlistment: SinglePhaseEnlistment) -> None: ...


class IsolationLevel(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Serializable : IsolationLevel # 0
    RepeatableRead : IsolationLevel # 1
    ReadCommitted : IsolationLevel # 2
    ReadUncommitted : IsolationLevel # 3
    Snapshot : IsolationLevel # 4
    Chaos : IsolationLevel # 5
    Unspecified : IsolationLevel # 6


class ITransactionPromoter(typing.Protocol):
    @abc.abstractmethod
    def Promote(self) -> Array_1[int]: ...


class PreparingEnlistment(Enlistment):
    def Prepared(self) -> None: ...
    def RecoveryInformation(self) -> Array_1[int]: ...
    # Skipped ForceRollback due to it being static, abstract and generic.

    ForceRollback : ForceRollback_MethodGroup
    class ForceRollback_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, e: Exception) -> None:...



class SinglePhaseEnlistment(Enlistment):
    def Committed(self) -> None: ...
    # Skipped Aborted due to it being static, abstract and generic.

    Aborted : Aborted_MethodGroup
    class Aborted_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, e: Exception) -> None:...

    # Skipped InDoubt due to it being static, abstract and generic.

    InDoubt : InDoubt_MethodGroup
    class InDoubt_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, e: Exception) -> None:...



class Transaction(ISerializable, IDisposable):
    @classmethod
    @property
    def Current(cls) -> Transaction: ...
    @classmethod
    @Current.setter
    def Current(cls, value: Transaction) -> Transaction: ...
    @property
    def IsolationLevel(self) -> IsolationLevel: ...
    @property
    def PromoterType(self) -> Guid: ...
    @property
    def TransactionInformation(self) -> TransactionInformation: ...
    def Clone(self) -> Transaction: ...
    def DependentClone(self, cloneOption: DependentCloneOption) -> DependentTransaction: ...
    def Dispose(self) -> None: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def GetPromotedToken(self) -> Array_1[int]: ...
    def __eq__(self, x: Transaction, y: Transaction) -> bool: ...
    def __ne__(self, x: Transaction, y: Transaction) -> bool: ...
    def PromoteAndEnlistDurable(self, resourceManagerIdentifier: Guid, promotableNotification: IPromotableSinglePhaseNotification, enlistmentNotification: ISinglePhaseNotification, enlistmentOptions: EnlistmentOptions) -> Enlistment: ...
    def SetDistributedTransactionIdentifier(self, promotableNotification: IPromotableSinglePhaseNotification, distributedTransactionIdentifier: Guid) -> None: ...
    # Skipped EnlistDurable due to it being static, abstract and generic.

    EnlistDurable : EnlistDurable_MethodGroup
    class EnlistDurable_MethodGroup:
        @typing.overload
        def __call__(self, resourceManagerIdentifier: Guid, singlePhaseNotification: ISinglePhaseNotification, enlistmentOptions: EnlistmentOptions) -> Enlistment:...
        @typing.overload
        def __call__(self, resourceManagerIdentifier: Guid, enlistmentNotification: IEnlistmentNotification, enlistmentOptions: EnlistmentOptions) -> Enlistment:...

    # Skipped EnlistPromotableSinglePhase due to it being static, abstract and generic.

    EnlistPromotableSinglePhase : EnlistPromotableSinglePhase_MethodGroup
    class EnlistPromotableSinglePhase_MethodGroup:
        @typing.overload
        def __call__(self, promotableSinglePhaseNotification: IPromotableSinglePhaseNotification) -> bool:...
        @typing.overload
        def __call__(self, promotableSinglePhaseNotification: IPromotableSinglePhaseNotification, promoterType: Guid) -> bool:...

    # Skipped EnlistVolatile due to it being static, abstract and generic.

    EnlistVolatile : EnlistVolatile_MethodGroup
    class EnlistVolatile_MethodGroup:
        @typing.overload
        def __call__(self, singlePhaseNotification: ISinglePhaseNotification, enlistmentOptions: EnlistmentOptions) -> Enlistment:...
        @typing.overload
        def __call__(self, enlistmentNotification: IEnlistmentNotification, enlistmentOptions: EnlistmentOptions) -> Enlistment:...

    # Skipped Rollback due to it being static, abstract and generic.

    Rollback : Rollback_MethodGroup
    class Rollback_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, e: Exception) -> None:...



class TransactionInformation:
    @property
    def CreationTime(self) -> DateTime: ...
    @property
    def DistributedIdentifier(self) -> Guid: ...
    @property
    def LocalIdentifier(self) -> str: ...
    @property
    def Status(self) -> TransactionStatus: ...


class TransactionStatus(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Active : TransactionStatus # 0
    Committed : TransactionStatus # 1
    Aborted : TransactionStatus # 2
    InDoubt : TransactionStatus # 3

