from System.Runtime.InteropServices import CriticalHandle, SafeBuffer, SafeHandle


class CriticalHandleMinusOneIsInvalid(CriticalHandle):
    """Provides a base class for Win32 critical handle implementations in
    which the value of -1 indicates an invalid handle."""

    @property
    def IsInvalid(self) -> bool:
        """Gets a value that indicates whether the handle is invalid.
        :return: ``True`` if the handle is not valid; otherwise, ``False``."""
        ...


class CriticalHandleZeroOrMinusOneIsInvalid(CriticalHandle):
    """Provides a base class for Win32 critical handle implementations in
    which the value of either 0 or -1 indicates an invalid handle."""

    @property
    def IsInvalid(self) -> bool:
        """Gets a value that indicates whether the handle is invalid.
        :return: ``True`` if the handle is not valid; otherwise, ``False``."""
        ...


class SafeFileHandle(SafeHandleZeroOrMinusOneIsInvalid):
    """Represents a wrapper class for a file handle."""

    def __init__(self, preexistingHandle: int, ownsHandle: bool) -> None:
        """Initializes a new instance of the ``SafeFileHandle`` class.
        :param preexistingHandle: An ``IntPtr`` object that represents the
            pre-existing handle to use.
        :param ownsHandle: ``True`` to reliably release the handle during the
            finalization phase; ``False`` to prevent reliable release (not
            recommended).
        """
        ...


class SafeHandleMinusOneIsInvalid(SafeHandle):
    """Provides a base class for Win32 safe handle implementations in which
    the value of -1 indicates an invalid handle."""

    @property
    def IsInvalid(self) -> bool:
        """Gets a value that indicates whether the handle is invalid.
        :return: ``True`` if the handle is not valid; otherwise, ``False``.
        """
        ...


class SafeHandleZeroOrMinusOneIsInvalid(SafeHandle):
    """Provides a base class for Win32 safe handle implementations in which
    the value of either 0 or -1 indicates an invalid handle."""

    @property
    def IsInvalid(self) -> bool:
        """Gets a value that indicates whether the handle is invalid.
        :return: ``True`` if the handle is not valid; otherwise, ``False``.
        """
        ...


class SafeMemoryMappedFileHandle(SafeHandleZeroOrMinusOneIsInvalid):
    """Provides a safe handle that represents a memory-mapped file for
    sequential access."""
    pass


class SafeMemoryMappedViewHandle(SafeBuffer):
    """Provides a safe handle that represents a view of a block of unmanaged
    memory for random access."""
    pass


class SafePipeHandle(SafeHandleZeroOrMinusOneIsInvalid):
    """Represents a wrapper class for a pipe handle."""

    def __init__(self, preexistingHandle: int, ownsHandle: bool) -> None:
        """Initializes a new instance of the ``SafePipeHandle`` class.
        :param preexistingHandle: An ``IntPtr`` object that represents the
            pre-existing handle to use.
        :param ownsHandle: ``True`` to reliably release the handle during the
            finalization phase; ``False`` to prevent reliable release (not
            recommended).
        """
        ...


class SafeProcessHandle(SafeHandleZeroOrMinusOneIsInvalid):
    """Provides a managed wrapper for a process handle."""

    def __init__(self, existingHandle: int, ownsHandle: bool) -> None:
        """Initializes a new instance of the ``SafeProcessHandle`` class from
        the specified handle, indicating whether to release the handle during
        the finalization phase.
        :param existingHandle: The handle to be wrapped.
        :param ownsHandle: ``True`` to reliably let ``SafeProcessHandle``
            release the handle during the finalization phase; otherwise,
            ``False``.
        """
        ...


class SafeWaitHandle(SafeHandleZeroOrMinusOneIsInvalid):
    """Represents a wrapper class for a wait handle."""

    def __init__(self, existingHandle: int, ownsHandle: bool) -> None:
        """Initializes a new instance of the ``SafeWaitHandle`` class.
        :param existingHandle: An ``IntPtr`` object that represents the
            pre-existing handle to use.
        :param ownsHandle: ``True`` to reliably release the handle during the
            finalization phase; ``False`` to prevent reliable release (not
            recommended).
        """
        ...


class SafeX509ChainHandle(SafeHandleZeroOrMinusOneIsInvalid):
    """Provides a wrapper class that represents the handle of an X.509 chain
    object. For more information, see
    ``System.Security.Cryptography.X509Certificates.X509Chain``."""
    pass
