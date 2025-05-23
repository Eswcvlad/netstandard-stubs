import typing, abc
from System.Collections.Generic import IEnumerable_1, IComparer_1, IEqualityComparer_1
from System.Xml import XmlNodeType, XmlWriter, XmlReader, IXmlLineInfo
from System import Array_1, IEquatable_1
from System.Threading.Tasks import Task, Task_1
from System.Threading import CancellationToken
from System.IO import Stream, TextReader, TextWriter
from System.Xml.Serialization import IXmlSerializable
from System.Runtime.Serialization import ISerializable
from System.Collections import IComparer, IEqualityComparer

class LoadOptions(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : LoadOptions # 0
    PreserveWhitespace : LoadOptions # 1
    SetBaseUri : LoadOptions # 2
    SetLineInfo : LoadOptions # 4


class ReaderOptions(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : ReaderOptions # 0
    OmitDuplicateNamespaces : ReaderOptions # 1


class SaveOptions(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : SaveOptions # 0
    DisableFormatting : SaveOptions # 1
    OmitDuplicateNamespaces : SaveOptions # 2


class XAttribute(XObject):
    @typing.overload
    def __init__(self, name: XName, value: typing.Any) -> None: ...
    @typing.overload
    def __init__(self, other: XAttribute) -> None: ...
    @property
    def BaseUri(self) -> str: ...
    @property
    def Document(self) -> XDocument: ...
    @classmethod
    @property
    def EmptySequence(cls) -> IEnumerable_1[XAttribute]: ...
    @property
    def IsNamespaceDeclaration(self) -> bool: ...
    @property
    def Name(self) -> XName: ...
    @property
    def NextAttribute(self) -> XAttribute: ...
    @property
    def NodeType(self) -> XmlNodeType: ...
    @property
    def Parent(self) -> XElement: ...
    @property
    def PreviousAttribute(self) -> XAttribute: ...
    @property
    def Value(self) -> str: ...
    @Value.setter
    def Value(self, value: str) -> str: ...
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    # Operator not supported op_Explicit(attribute: XAttribute)
    def Remove(self) -> None: ...
    def SetValue(self, value: typing.Any) -> None: ...
    def ToString(self) -> str: ...


class XContainer(XNode):
    @property
    def BaseUri(self) -> str: ...
    @property
    def Document(self) -> XDocument: ...
    @property
    def FirstNode(self) -> XNode: ...
    @property
    def LastNode(self) -> XNode: ...
    @property
    def NextNode(self) -> XNode: ...
    @property
    def NodeType(self) -> XmlNodeType: ...
    @property
    def Parent(self) -> XElement: ...
    @property
    def PreviousNode(self) -> XNode: ...
    def CreateWriter(self) -> XmlWriter: ...
    def DescendantNodes(self) -> IEnumerable_1[XNode]: ...
    def Element(self, name: XName) -> XElement: ...
    def Nodes(self) -> IEnumerable_1[XNode]: ...
    def RemoveNodes(self) -> None: ...
    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        @typing.overload
        def __call__(self, content: Array_1[typing.Any]) -> None:...
        @typing.overload
        def __call__(self, content: typing.Any) -> None:...

    # Skipped AddFirst due to it being static, abstract and generic.

    AddFirst : AddFirst_MethodGroup
    class AddFirst_MethodGroup:
        @typing.overload
        def __call__(self, content: Array_1[typing.Any]) -> None:...
        @typing.overload
        def __call__(self, content: typing.Any) -> None:...

    # Skipped Descendants due to it being static, abstract and generic.

    Descendants : Descendants_MethodGroup
    class Descendants_MethodGroup:
        @typing.overload
        def __call__(self) -> IEnumerable_1[XElement]:...
        @typing.overload
        def __call__(self, name: XName) -> IEnumerable_1[XElement]:...

    # Skipped Elements due to it being static, abstract and generic.

    Elements : Elements_MethodGroup
    class Elements_MethodGroup:
        @typing.overload
        def __call__(self) -> IEnumerable_1[XElement]:...
        @typing.overload
        def __call__(self, name: XName) -> IEnumerable_1[XElement]:...

    # Skipped ReplaceNodes due to it being static, abstract and generic.

    ReplaceNodes : ReplaceNodes_MethodGroup
    class ReplaceNodes_MethodGroup:
        @typing.overload
        def __call__(self, content: Array_1[typing.Any]) -> None:...
        @typing.overload
        def __call__(self, content: typing.Any) -> None:...



class XDeclaration:
    @typing.overload
    def __init__(self, other: XDeclaration) -> None: ...
    @typing.overload
    def __init__(self, version: str, encoding: str, standalone: str) -> None: ...
    @property
    def Encoding(self) -> str: ...
    @Encoding.setter
    def Encoding(self, value: str) -> str: ...
    @property
    def Standalone(self) -> str: ...
    @Standalone.setter
    def Standalone(self, value: str) -> str: ...
    @property
    def Version(self) -> str: ...
    @Version.setter
    def Version(self, value: str) -> str: ...
    def ToString(self) -> str: ...


class XDocument(XContainer):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, content: Array_1[typing.Any]) -> None: ...
    @typing.overload
    def __init__(self, declaration: XDeclaration, content: Array_1[typing.Any]) -> None: ...
    @typing.overload
    def __init__(self, other: XDocument) -> None: ...
    @property
    def BaseUri(self) -> str: ...
    @property
    def Declaration(self) -> XDeclaration: ...
    @Declaration.setter
    def Declaration(self, value: XDeclaration) -> XDeclaration: ...
    @property
    def Document(self) -> XDocument: ...
    @property
    def DocumentType(self) -> XDocumentType: ...
    @property
    def FirstNode(self) -> XNode: ...
    @property
    def LastNode(self) -> XNode: ...
    @property
    def NextNode(self) -> XNode: ...
    @property
    def NodeType(self) -> XmlNodeType: ...
    @property
    def Parent(self) -> XElement: ...
    @property
    def PreviousNode(self) -> XNode: ...
    @property
    def Root(self) -> XElement: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...
    def WriteToAsync(self, writer: XmlWriter, cancellationToken: CancellationToken) -> Task: ...
    # Skipped Load due to it being static, abstract and generic.

    Load : Load_MethodGroup
    class Load_MethodGroup:
        @typing.overload
        def __call__(self, stream: Stream) -> XDocument:...
        @typing.overload
        def __call__(self, textReader: TextReader) -> XDocument:...
        @typing.overload
        def __call__(self, uri: str) -> XDocument:...
        @typing.overload
        def __call__(self, reader: XmlReader) -> XDocument:...
        @typing.overload
        def __call__(self, stream: Stream, options: LoadOptions) -> XDocument:...
        @typing.overload
        def __call__(self, textReader: TextReader, options: LoadOptions) -> XDocument:...
        @typing.overload
        def __call__(self, uri: str, options: LoadOptions) -> XDocument:...
        @typing.overload
        def __call__(self, reader: XmlReader, options: LoadOptions) -> XDocument:...

    # Skipped LoadAsync due to it being static, abstract and generic.

    LoadAsync : LoadAsync_MethodGroup
    class LoadAsync_MethodGroup:
        @typing.overload
        def __call__(self, stream: Stream, options: LoadOptions, cancellationToken: CancellationToken) -> Task_1[XDocument]:...
        @typing.overload
        def __call__(self, textReader: TextReader, options: LoadOptions, cancellationToken: CancellationToken) -> Task_1[XDocument]:...
        @typing.overload
        def __call__(self, reader: XmlReader, options: LoadOptions, cancellationToken: CancellationToken) -> Task_1[XDocument]:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, text: str) -> XDocument:...
        @typing.overload
        def __call__(self, text: str, options: LoadOptions) -> XDocument:...

    # Skipped Save due to it being static, abstract and generic.

    Save : Save_MethodGroup
    class Save_MethodGroup:
        @typing.overload
        def __call__(self, fileName: str) -> None:...
        @typing.overload
        def __call__(self, stream: Stream) -> None:...
        @typing.overload
        def __call__(self, textWriter: TextWriter) -> None:...
        @typing.overload
        def __call__(self, writer: XmlWriter) -> None:...
        @typing.overload
        def __call__(self, fileName: str, options: SaveOptions) -> None:...
        @typing.overload
        def __call__(self, stream: Stream, options: SaveOptions) -> None:...
        @typing.overload
        def __call__(self, textWriter: TextWriter, options: SaveOptions) -> None:...

    # Skipped SaveAsync due to it being static, abstract and generic.

    SaveAsync : SaveAsync_MethodGroup
    class SaveAsync_MethodGroup:
        @typing.overload
        def __call__(self, writer: XmlWriter, cancellationToken: CancellationToken) -> Task:...
        @typing.overload
        def __call__(self, stream: Stream, options: SaveOptions, cancellationToken: CancellationToken) -> Task:...
        @typing.overload
        def __call__(self, textWriter: TextWriter, options: SaveOptions, cancellationToken: CancellationToken) -> Task:...



class XDocumentType(XNode):
    @typing.overload
    def __init__(self, name: str, publicId: str, systemId: str, internalSubset: str) -> None: ...
    @typing.overload
    def __init__(self, other: XDocumentType) -> None: ...
    @property
    def BaseUri(self) -> str: ...
    @property
    def Document(self) -> XDocument: ...
    @property
    def InternalSubset(self) -> str: ...
    @InternalSubset.setter
    def InternalSubset(self, value: str) -> str: ...
    @property
    def Name(self) -> str: ...
    @Name.setter
    def Name(self, value: str) -> str: ...
    @property
    def NextNode(self) -> XNode: ...
    @property
    def NodeType(self) -> XmlNodeType: ...
    @property
    def Parent(self) -> XElement: ...
    @property
    def PreviousNode(self) -> XNode: ...
    @property
    def PublicId(self) -> str: ...
    @PublicId.setter
    def PublicId(self, value: str) -> str: ...
    @property
    def SystemId(self) -> str: ...
    @SystemId.setter
    def SystemId(self, value: str) -> str: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...
    def WriteToAsync(self, writer: XmlWriter, cancellationToken: CancellationToken) -> Task: ...


class XElement(XContainer, IXmlSerializable):
    @typing.overload
    def __init__(self, name: XName) -> None: ...
    @typing.overload
    def __init__(self, name: XName, content: typing.Any) -> None: ...
    @typing.overload
    def __init__(self, name: XName, content: Array_1[typing.Any]) -> None: ...
    @typing.overload
    def __init__(self, other: XElement) -> None: ...
    @typing.overload
    def __init__(self, other: XStreamingElement) -> None: ...
    @property
    def BaseUri(self) -> str: ...
    @property
    def Document(self) -> XDocument: ...
    @classmethod
    @property
    def EmptySequence(cls) -> IEnumerable_1[XElement]: ...
    @property
    def FirstAttribute(self) -> XAttribute: ...
    @property
    def FirstNode(self) -> XNode: ...
    @property
    def HasAttributes(self) -> bool: ...
    @property
    def HasElements(self) -> bool: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def LastAttribute(self) -> XAttribute: ...
    @property
    def LastNode(self) -> XNode: ...
    @property
    def Name(self) -> XName: ...
    @Name.setter
    def Name(self, value: XName) -> XName: ...
    @property
    def NextNode(self) -> XNode: ...
    @property
    def NodeType(self) -> XmlNodeType: ...
    @property
    def Parent(self) -> XElement: ...
    @property
    def PreviousNode(self) -> XNode: ...
    @property
    def Value(self) -> str: ...
    @Value.setter
    def Value(self, value: str) -> str: ...
    def Attribute(self, name: XName) -> XAttribute: ...
    def DescendantNodesAndSelf(self) -> IEnumerable_1[XNode]: ...
    def GetDefaultNamespace(self) -> XNamespace: ...
    def GetNamespaceOfPrefix(self, prefix: str) -> XNamespace: ...
    def GetPrefixOfNamespace(self, ns: XNamespace) -> str: ...
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    # Operator not supported op_Explicit(element: XElement)
    def RemoveAll(self) -> None: ...
    def RemoveAttributes(self) -> None: ...
    def SetAttributeValue(self, name: XName, value: typing.Any) -> None: ...
    def SetElementValue(self, name: XName, value: typing.Any) -> None: ...
    def SetValue(self, value: typing.Any) -> None: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...
    def WriteToAsync(self, writer: XmlWriter, cancellationToken: CancellationToken) -> Task: ...
    # Skipped AncestorsAndSelf due to it being static, abstract and generic.

    AncestorsAndSelf : AncestorsAndSelf_MethodGroup
    class AncestorsAndSelf_MethodGroup:
        @typing.overload
        def __call__(self) -> IEnumerable_1[XElement]:...
        @typing.overload
        def __call__(self, name: XName) -> IEnumerable_1[XElement]:...

    # Skipped Attributes due to it being static, abstract and generic.

    Attributes : Attributes_MethodGroup
    class Attributes_MethodGroup:
        @typing.overload
        def __call__(self) -> IEnumerable_1[XAttribute]:...
        @typing.overload
        def __call__(self, name: XName) -> IEnumerable_1[XAttribute]:...

    # Skipped DescendantsAndSelf due to it being static, abstract and generic.

    DescendantsAndSelf : DescendantsAndSelf_MethodGroup
    class DescendantsAndSelf_MethodGroup:
        @typing.overload
        def __call__(self) -> IEnumerable_1[XElement]:...
        @typing.overload
        def __call__(self, name: XName) -> IEnumerable_1[XElement]:...

    # Skipped Load due to it being static, abstract and generic.

    Load : Load_MethodGroup
    class Load_MethodGroup:
        @typing.overload
        def __call__(self, stream: Stream) -> XElement:...
        @typing.overload
        def __call__(self, textReader: TextReader) -> XElement:...
        @typing.overload
        def __call__(self, uri: str) -> XElement:...
        @typing.overload
        def __call__(self, reader: XmlReader) -> XElement:...
        @typing.overload
        def __call__(self, stream: Stream, options: LoadOptions) -> XElement:...
        @typing.overload
        def __call__(self, textReader: TextReader, options: LoadOptions) -> XElement:...
        @typing.overload
        def __call__(self, uri: str, options: LoadOptions) -> XElement:...
        @typing.overload
        def __call__(self, reader: XmlReader, options: LoadOptions) -> XElement:...

    # Skipped LoadAsync due to it being static, abstract and generic.

    LoadAsync : LoadAsync_MethodGroup
    class LoadAsync_MethodGroup:
        @typing.overload
        def __call__(self, stream: Stream, options: LoadOptions, cancellationToken: CancellationToken) -> Task_1[XElement]:...
        @typing.overload
        def __call__(self, textReader: TextReader, options: LoadOptions, cancellationToken: CancellationToken) -> Task_1[XElement]:...
        @typing.overload
        def __call__(self, reader: XmlReader, options: LoadOptions, cancellationToken: CancellationToken) -> Task_1[XElement]:...

    # Skipped Parse due to it being static, abstract and generic.

    Parse : Parse_MethodGroup
    class Parse_MethodGroup:
        @typing.overload
        def __call__(self, text: str) -> XElement:...
        @typing.overload
        def __call__(self, text: str, options: LoadOptions) -> XElement:...

    # Skipped ReplaceAll due to it being static, abstract and generic.

    ReplaceAll : ReplaceAll_MethodGroup
    class ReplaceAll_MethodGroup:
        @typing.overload
        def __call__(self, content: Array_1[typing.Any]) -> None:...
        @typing.overload
        def __call__(self, content: typing.Any) -> None:...

    # Skipped ReplaceAttributes due to it being static, abstract and generic.

    ReplaceAttributes : ReplaceAttributes_MethodGroup
    class ReplaceAttributes_MethodGroup:
        @typing.overload
        def __call__(self, content: Array_1[typing.Any]) -> None:...
        @typing.overload
        def __call__(self, content: typing.Any) -> None:...

    # Skipped Save due to it being static, abstract and generic.

    Save : Save_MethodGroup
    class Save_MethodGroup:
        @typing.overload
        def __call__(self, fileName: str) -> None:...
        @typing.overload
        def __call__(self, stream: Stream) -> None:...
        @typing.overload
        def __call__(self, textWriter: TextWriter) -> None:...
        @typing.overload
        def __call__(self, writer: XmlWriter) -> None:...
        @typing.overload
        def __call__(self, fileName: str, options: SaveOptions) -> None:...
        @typing.overload
        def __call__(self, stream: Stream, options: SaveOptions) -> None:...
        @typing.overload
        def __call__(self, textWriter: TextWriter, options: SaveOptions) -> None:...

    # Skipped SaveAsync due to it being static, abstract and generic.

    SaveAsync : SaveAsync_MethodGroup
    class SaveAsync_MethodGroup:
        @typing.overload
        def __call__(self, writer: XmlWriter, cancellationToken: CancellationToken) -> Task:...
        @typing.overload
        def __call__(self, stream: Stream, options: SaveOptions, cancellationToken: CancellationToken) -> Task:...
        @typing.overload
        def __call__(self, textWriter: TextWriter, options: SaveOptions, cancellationToken: CancellationToken) -> Task:...



class XName(ISerializable, IEquatable_1[XName]):
    @property
    def LocalName(self) -> str: ...
    @property
    def Namespace(self) -> XNamespace: ...
    @property
    def NamespaceName(self) -> str: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, left: XName, right: XName) -> bool: ...
    # Operator not supported op_Implicit(expandedName: String)
    def __ne__(self, left: XName, right: XName) -> bool: ...
    def ToString(self) -> str: ...
    # Skipped Get due to it being static, abstract and generic.

    Get : Get_MethodGroup
    class Get_MethodGroup:
        @typing.overload
        def __call__(self, expandedName: str) -> XName:...
        @typing.overload
        def __call__(self, localName: str, namespaceName: str) -> XName:...



class XNamespace:
    @property
    def NamespaceName(self) -> str: ...
    # Skipped property None since it is a reserved python word. Use reflection to access.
    @classmethod
    @property
    def Xml(cls) -> XNamespace: ...
    @classmethod
    @property
    def Xmlns(cls) -> XNamespace: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    @staticmethod
    def Get(namespaceName: str) -> XNamespace: ...
    def GetHashCode(self) -> int: ...
    def GetName(self, localName: str) -> XName: ...
    def __add__(self, ns: XNamespace, localName: str) -> XName: ...
    def __eq__(self, left: XNamespace, right: XNamespace) -> bool: ...
    # Operator not supported op_Implicit(namespaceName: String)
    def __ne__(self, left: XNamespace, right: XNamespace) -> bool: ...
    def ToString(self) -> str: ...


class XNode(XObject):
    @property
    def BaseUri(self) -> str: ...
    @property
    def Document(self) -> XDocument: ...
    @classmethod
    @property
    def DocumentOrderComparer(cls) -> XNodeDocumentOrderComparer: ...
    @classmethod
    @property
    def EqualityComparer(cls) -> XNodeEqualityComparer: ...
    @property
    def NextNode(self) -> XNode: ...
    @property
    def NodeType(self) -> XmlNodeType: ...
    @property
    def Parent(self) -> XElement: ...
    @property
    def PreviousNode(self) -> XNode: ...
    @staticmethod
    def CompareDocumentOrder(n1: XNode, n2: XNode) -> int: ...
    @staticmethod
    def DeepEquals(n1: XNode, n2: XNode) -> bool: ...
    def IsAfter(self, node: XNode) -> bool: ...
    def IsBefore(self, node: XNode) -> bool: ...
    def NodesAfterSelf(self) -> IEnumerable_1[XNode]: ...
    def NodesBeforeSelf(self) -> IEnumerable_1[XNode]: ...
    @staticmethod
    def ReadFrom(reader: XmlReader) -> XNode: ...
    @staticmethod
    def ReadFromAsync(reader: XmlReader, cancellationToken: CancellationToken) -> Task_1[XNode]: ...
    def Remove(self) -> None: ...
    @abc.abstractmethod
    def WriteTo(self, writer: XmlWriter) -> None: ...
    @abc.abstractmethod
    def WriteToAsync(self, writer: XmlWriter, cancellationToken: CancellationToken) -> Task: ...
    # Skipped AddAfterSelf due to it being static, abstract and generic.

    AddAfterSelf : AddAfterSelf_MethodGroup
    class AddAfterSelf_MethodGroup:
        @typing.overload
        def __call__(self, content: Array_1[typing.Any]) -> None:...
        @typing.overload
        def __call__(self, content: typing.Any) -> None:...

    # Skipped AddBeforeSelf due to it being static, abstract and generic.

    AddBeforeSelf : AddBeforeSelf_MethodGroup
    class AddBeforeSelf_MethodGroup:
        @typing.overload
        def __call__(self, content: Array_1[typing.Any]) -> None:...
        @typing.overload
        def __call__(self, content: typing.Any) -> None:...

    # Skipped Ancestors due to it being static, abstract and generic.

    Ancestors : Ancestors_MethodGroup
    class Ancestors_MethodGroup:
        @typing.overload
        def __call__(self) -> IEnumerable_1[XElement]:...
        @typing.overload
        def __call__(self, name: XName) -> IEnumerable_1[XElement]:...

    # Skipped CreateReader due to it being static, abstract and generic.

    CreateReader : CreateReader_MethodGroup
    class CreateReader_MethodGroup:
        @typing.overload
        def __call__(self) -> XmlReader:...
        @typing.overload
        def __call__(self, readerOptions: ReaderOptions) -> XmlReader:...

    # Skipped ElementsAfterSelf due to it being static, abstract and generic.

    ElementsAfterSelf : ElementsAfterSelf_MethodGroup
    class ElementsAfterSelf_MethodGroup:
        @typing.overload
        def __call__(self) -> IEnumerable_1[XElement]:...
        @typing.overload
        def __call__(self, name: XName) -> IEnumerable_1[XElement]:...

    # Skipped ElementsBeforeSelf due to it being static, abstract and generic.

    ElementsBeforeSelf : ElementsBeforeSelf_MethodGroup
    class ElementsBeforeSelf_MethodGroup:
        @typing.overload
        def __call__(self) -> IEnumerable_1[XElement]:...
        @typing.overload
        def __call__(self, name: XName) -> IEnumerable_1[XElement]:...

    # Skipped ReplaceWith due to it being static, abstract and generic.

    ReplaceWith : ReplaceWith_MethodGroup
    class ReplaceWith_MethodGroup:
        @typing.overload
        def __call__(self, content: Array_1[typing.Any]) -> None:...
        @typing.overload
        def __call__(self, content: typing.Any) -> None:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, options: SaveOptions) -> str:...



class XNodeDocumentOrderComparer(IComparer_1[XNode], IComparer):
    def __init__(self) -> None: ...
    def Compare(self, x: XNode, y: XNode) -> int: ...


class XNodeEqualityComparer(IEqualityComparer_1[XNode], IEqualityComparer):
    def __init__(self) -> None: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...
        @typing.overload
        def __call__(self, x: XNode, y: XNode) -> bool:...

    # Skipped GetHashCode due to it being static, abstract and generic.

    GetHashCode : GetHashCode_MethodGroup
    class GetHashCode_MethodGroup:
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, obj: XNode) -> int:...



class XObject(IXmlLineInfo, abc.ABC):
    @property
    def BaseUri(self) -> str: ...
    @property
    def Document(self) -> XDocument: ...
    @property
    def NodeType(self) -> XmlNodeType: ...
    @property
    def Parent(self) -> XElement: ...
    def AddAnnotation(self, annotation: typing.Any) -> None: ...
    # Skipped Annotation due to it being static, abstract and generic.

    Annotation : Annotation_MethodGroup
    class Annotation_MethodGroup:
        def __getitem__(self, t:typing.Type[Annotation_1_T1]) -> Annotation_1[Annotation_1_T1]: ...

        Annotation_1_T1 = typing.TypeVar('Annotation_1_T1')
        class Annotation_1(typing.Generic[Annotation_1_T1]):
            Annotation_1_T = XObject.Annotation_MethodGroup.Annotation_1_T1
            def __call__(self) -> Annotation_1_T:...

        def __call__(self, type: typing.Type[typing.Any]) -> typing.Any:...

    # Skipped Annotations due to it being static, abstract and generic.

    Annotations : Annotations_MethodGroup
    class Annotations_MethodGroup:
        def __getitem__(self, t:typing.Type[Annotations_1_T1]) -> Annotations_1[Annotations_1_T1]: ...

        Annotations_1_T1 = typing.TypeVar('Annotations_1_T1')
        class Annotations_1(typing.Generic[Annotations_1_T1]):
            Annotations_1_T = XObject.Annotations_MethodGroup.Annotations_1_T1
            def __call__(self) -> IEnumerable_1[Annotations_1_T]:...

        def __call__(self, type: typing.Type[typing.Any]) -> IEnumerable_1[typing.Any]:...

    # Skipped RemoveAnnotations due to it being static, abstract and generic.

    RemoveAnnotations : RemoveAnnotations_MethodGroup
    class RemoveAnnotations_MethodGroup:
        def __getitem__(self, t:typing.Type[RemoveAnnotations_1_T1]) -> RemoveAnnotations_1[RemoveAnnotations_1_T1]: ...

        RemoveAnnotations_1_T1 = typing.TypeVar('RemoveAnnotations_1_T1')
        class RemoveAnnotations_1(typing.Generic[RemoveAnnotations_1_T1]):
            RemoveAnnotations_1_T = XObject.RemoveAnnotations_MethodGroup.RemoveAnnotations_1_T1
            def __call__(self) -> None:...

        def __call__(self, type: typing.Type[typing.Any]) -> None:...



class XStreamingElement:
    @typing.overload
    def __init__(self, name: XName) -> None: ...
    @typing.overload
    def __init__(self, name: XName, content: typing.Any) -> None: ...
    @typing.overload
    def __init__(self, name: XName, content: Array_1[typing.Any]) -> None: ...
    @property
    def Name(self) -> XName: ...
    @Name.setter
    def Name(self, value: XName) -> XName: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...
    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        @typing.overload
        def __call__(self, content: Array_1[typing.Any]) -> None:...
        @typing.overload
        def __call__(self, content: typing.Any) -> None:...

    # Skipped Save due to it being static, abstract and generic.

    Save : Save_MethodGroup
    class Save_MethodGroup:
        @typing.overload
        def __call__(self, fileName: str) -> None:...
        @typing.overload
        def __call__(self, stream: Stream) -> None:...
        @typing.overload
        def __call__(self, textWriter: TextWriter) -> None:...
        @typing.overload
        def __call__(self, writer: XmlWriter) -> None:...
        @typing.overload
        def __call__(self, fileName: str, options: SaveOptions) -> None:...
        @typing.overload
        def __call__(self, stream: Stream, options: SaveOptions) -> None:...
        @typing.overload
        def __call__(self, textWriter: TextWriter, options: SaveOptions) -> None:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, options: SaveOptions) -> str:...


