import typing, abc
from System import IEquatable_1, Array_1, Attribute
from System.ComponentModel import TypeConverter, ITypeDescriptorContext, PropertyDescriptorCollection
from System.Globalization import CultureInfo
from System.Collections import ICollection, IDictionary
from System.Numerics import Vector2, Vector4

class Color(IEquatable_1[Color]):
    Empty : Color
    @property
    def A(self) -> int: ...
    @classmethod
    @property
    def AliceBlue(cls) -> Color: ...
    @classmethod
    @property
    def AntiqueWhite(cls) -> Color: ...
    @classmethod
    @property
    def Aqua(cls) -> Color: ...
    @classmethod
    @property
    def Aquamarine(cls) -> Color: ...
    @classmethod
    @property
    def Azure(cls) -> Color: ...
    @property
    def B(self) -> int: ...
    @classmethod
    @property
    def Beige(cls) -> Color: ...
    @classmethod
    @property
    def Bisque(cls) -> Color: ...
    @classmethod
    @property
    def Black(cls) -> Color: ...
    @classmethod
    @property
    def BlanchedAlmond(cls) -> Color: ...
    @classmethod
    @property
    def Blue(cls) -> Color: ...
    @classmethod
    @property
    def BlueViolet(cls) -> Color: ...
    @classmethod
    @property
    def Brown(cls) -> Color: ...
    @classmethod
    @property
    def BurlyWood(cls) -> Color: ...
    @classmethod
    @property
    def CadetBlue(cls) -> Color: ...
    @classmethod
    @property
    def Chartreuse(cls) -> Color: ...
    @classmethod
    @property
    def Chocolate(cls) -> Color: ...
    @classmethod
    @property
    def Coral(cls) -> Color: ...
    @classmethod
    @property
    def CornflowerBlue(cls) -> Color: ...
    @classmethod
    @property
    def Cornsilk(cls) -> Color: ...
    @classmethod
    @property
    def Crimson(cls) -> Color: ...
    @classmethod
    @property
    def Cyan(cls) -> Color: ...
    @classmethod
    @property
    def DarkBlue(cls) -> Color: ...
    @classmethod
    @property
    def DarkCyan(cls) -> Color: ...
    @classmethod
    @property
    def DarkGoldenrod(cls) -> Color: ...
    @classmethod
    @property
    def DarkGray(cls) -> Color: ...
    @classmethod
    @property
    def DarkGreen(cls) -> Color: ...
    @classmethod
    @property
    def DarkKhaki(cls) -> Color: ...
    @classmethod
    @property
    def DarkMagenta(cls) -> Color: ...
    @classmethod
    @property
    def DarkOliveGreen(cls) -> Color: ...
    @classmethod
    @property
    def DarkOrange(cls) -> Color: ...
    @classmethod
    @property
    def DarkOrchid(cls) -> Color: ...
    @classmethod
    @property
    def DarkRed(cls) -> Color: ...
    @classmethod
    @property
    def DarkSalmon(cls) -> Color: ...
    @classmethod
    @property
    def DarkSeaGreen(cls) -> Color: ...
    @classmethod
    @property
    def DarkSlateBlue(cls) -> Color: ...
    @classmethod
    @property
    def DarkSlateGray(cls) -> Color: ...
    @classmethod
    @property
    def DarkTurquoise(cls) -> Color: ...
    @classmethod
    @property
    def DarkViolet(cls) -> Color: ...
    @classmethod
    @property
    def DeepPink(cls) -> Color: ...
    @classmethod
    @property
    def DeepSkyBlue(cls) -> Color: ...
    @classmethod
    @property
    def DimGray(cls) -> Color: ...
    @classmethod
    @property
    def DodgerBlue(cls) -> Color: ...
    @classmethod
    @property
    def Firebrick(cls) -> Color: ...
    @classmethod
    @property
    def FloralWhite(cls) -> Color: ...
    @classmethod
    @property
    def ForestGreen(cls) -> Color: ...
    @classmethod
    @property
    def Fuchsia(cls) -> Color: ...
    @property
    def G(self) -> int: ...
    @classmethod
    @property
    def Gainsboro(cls) -> Color: ...
    @classmethod
    @property
    def GhostWhite(cls) -> Color: ...
    @classmethod
    @property
    def Gold(cls) -> Color: ...
    @classmethod
    @property
    def Goldenrod(cls) -> Color: ...
    @classmethod
    @property
    def Gray(cls) -> Color: ...
    @classmethod
    @property
    def Green(cls) -> Color: ...
    @classmethod
    @property
    def GreenYellow(cls) -> Color: ...
    @classmethod
    @property
    def Honeydew(cls) -> Color: ...
    @classmethod
    @property
    def HotPink(cls) -> Color: ...
    @classmethod
    @property
    def IndianRed(cls) -> Color: ...
    @classmethod
    @property
    def Indigo(cls) -> Color: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def IsKnownColor(self) -> bool: ...
    @property
    def IsNamedColor(self) -> bool: ...
    @property
    def IsSystemColor(self) -> bool: ...
    @classmethod
    @property
    def Ivory(cls) -> Color: ...
    @classmethod
    @property
    def Khaki(cls) -> Color: ...
    @classmethod
    @property
    def Lavender(cls) -> Color: ...
    @classmethod
    @property
    def LavenderBlush(cls) -> Color: ...
    @classmethod
    @property
    def LawnGreen(cls) -> Color: ...
    @classmethod
    @property
    def LemonChiffon(cls) -> Color: ...
    @classmethod
    @property
    def LightBlue(cls) -> Color: ...
    @classmethod
    @property
    def LightCoral(cls) -> Color: ...
    @classmethod
    @property
    def LightCyan(cls) -> Color: ...
    @classmethod
    @property
    def LightGoldenrodYellow(cls) -> Color: ...
    @classmethod
    @property
    def LightGray(cls) -> Color: ...
    @classmethod
    @property
    def LightGreen(cls) -> Color: ...
    @classmethod
    @property
    def LightPink(cls) -> Color: ...
    @classmethod
    @property
    def LightSalmon(cls) -> Color: ...
    @classmethod
    @property
    def LightSeaGreen(cls) -> Color: ...
    @classmethod
    @property
    def LightSkyBlue(cls) -> Color: ...
    @classmethod
    @property
    def LightSlateGray(cls) -> Color: ...
    @classmethod
    @property
    def LightSteelBlue(cls) -> Color: ...
    @classmethod
    @property
    def LightYellow(cls) -> Color: ...
    @classmethod
    @property
    def Lime(cls) -> Color: ...
    @classmethod
    @property
    def LimeGreen(cls) -> Color: ...
    @classmethod
    @property
    def Linen(cls) -> Color: ...
    @classmethod
    @property
    def Magenta(cls) -> Color: ...
    @classmethod
    @property
    def Maroon(cls) -> Color: ...
    @classmethod
    @property
    def MediumAquamarine(cls) -> Color: ...
    @classmethod
    @property
    def MediumBlue(cls) -> Color: ...
    @classmethod
    @property
    def MediumOrchid(cls) -> Color: ...
    @classmethod
    @property
    def MediumPurple(cls) -> Color: ...
    @classmethod
    @property
    def MediumSeaGreen(cls) -> Color: ...
    @classmethod
    @property
    def MediumSlateBlue(cls) -> Color: ...
    @classmethod
    @property
    def MediumSpringGreen(cls) -> Color: ...
    @classmethod
    @property
    def MediumTurquoise(cls) -> Color: ...
    @classmethod
    @property
    def MediumVioletRed(cls) -> Color: ...
    @classmethod
    @property
    def MidnightBlue(cls) -> Color: ...
    @classmethod
    @property
    def MintCream(cls) -> Color: ...
    @classmethod
    @property
    def MistyRose(cls) -> Color: ...
    @classmethod
    @property
    def Moccasin(cls) -> Color: ...
    @property
    def Name(self) -> str: ...
    @classmethod
    @property
    def NavajoWhite(cls) -> Color: ...
    @classmethod
    @property
    def Navy(cls) -> Color: ...
    @classmethod
    @property
    def OldLace(cls) -> Color: ...
    @classmethod
    @property
    def Olive(cls) -> Color: ...
    @classmethod
    @property
    def OliveDrab(cls) -> Color: ...
    @classmethod
    @property
    def Orange(cls) -> Color: ...
    @classmethod
    @property
    def OrangeRed(cls) -> Color: ...
    @classmethod
    @property
    def Orchid(cls) -> Color: ...
    @classmethod
    @property
    def PaleGoldenrod(cls) -> Color: ...
    @classmethod
    @property
    def PaleGreen(cls) -> Color: ...
    @classmethod
    @property
    def PaleTurquoise(cls) -> Color: ...
    @classmethod
    @property
    def PaleVioletRed(cls) -> Color: ...
    @classmethod
    @property
    def PapayaWhip(cls) -> Color: ...
    @classmethod
    @property
    def PeachPuff(cls) -> Color: ...
    @classmethod
    @property
    def Peru(cls) -> Color: ...
    @classmethod
    @property
    def Pink(cls) -> Color: ...
    @classmethod
    @property
    def Plum(cls) -> Color: ...
    @classmethod
    @property
    def PowderBlue(cls) -> Color: ...
    @classmethod
    @property
    def Purple(cls) -> Color: ...
    @property
    def R(self) -> int: ...
    @classmethod
    @property
    def RebeccaPurple(cls) -> Color: ...
    @classmethod
    @property
    def Red(cls) -> Color: ...
    @classmethod
    @property
    def RosyBrown(cls) -> Color: ...
    @classmethod
    @property
    def RoyalBlue(cls) -> Color: ...
    @classmethod
    @property
    def SaddleBrown(cls) -> Color: ...
    @classmethod
    @property
    def Salmon(cls) -> Color: ...
    @classmethod
    @property
    def SandyBrown(cls) -> Color: ...
    @classmethod
    @property
    def SeaGreen(cls) -> Color: ...
    @classmethod
    @property
    def SeaShell(cls) -> Color: ...
    @classmethod
    @property
    def Sienna(cls) -> Color: ...
    @classmethod
    @property
    def Silver(cls) -> Color: ...
    @classmethod
    @property
    def SkyBlue(cls) -> Color: ...
    @classmethod
    @property
    def SlateBlue(cls) -> Color: ...
    @classmethod
    @property
    def SlateGray(cls) -> Color: ...
    @classmethod
    @property
    def Snow(cls) -> Color: ...
    @classmethod
    @property
    def SpringGreen(cls) -> Color: ...
    @classmethod
    @property
    def SteelBlue(cls) -> Color: ...
    @classmethod
    @property
    def Tan(cls) -> Color: ...
    @classmethod
    @property
    def Teal(cls) -> Color: ...
    @classmethod
    @property
    def Thistle(cls) -> Color: ...
    @classmethod
    @property
    def Tomato(cls) -> Color: ...
    @classmethod
    @property
    def Transparent(cls) -> Color: ...
    @classmethod
    @property
    def Turquoise(cls) -> Color: ...
    @classmethod
    @property
    def Violet(cls) -> Color: ...
    @classmethod
    @property
    def Wheat(cls) -> Color: ...
    @classmethod
    @property
    def White(cls) -> Color: ...
    @classmethod
    @property
    def WhiteSmoke(cls) -> Color: ...
    @classmethod
    @property
    def Yellow(cls) -> Color: ...
    @classmethod
    @property
    def YellowGreen(cls) -> Color: ...
    @staticmethod
    def FromKnownColor(color: KnownColor) -> Color: ...
    @staticmethod
    def FromName(name: str) -> Color: ...
    def GetBrightness(self) -> float: ...
    def GetHashCode(self) -> int: ...
    def GetHue(self) -> float: ...
    def GetSaturation(self) -> float: ...
    def __eq__(self, left: Color, right: Color) -> bool: ...
    def __ne__(self, left: Color, right: Color) -> bool: ...
    def ToArgb(self) -> int: ...
    def ToKnownColor(self) -> KnownColor: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Color) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped FromArgb due to it being static, abstract and generic.

    FromArgb : FromArgb_MethodGroup
    class FromArgb_MethodGroup:
        @typing.overload
        def __call__(self, argb: int) -> Color:...
        @typing.overload
        def __call__(self, alpha: int, baseColor: Color) -> Color:...
        @typing.overload
        def __call__(self, red: int, green: int, blue: int) -> Color:...
        @typing.overload
        def __call__(self, alpha: int, red: int, green: int, blue: int) -> Color:...



class ColorConverter(TypeConverter):
    def __init__(self) -> None: ...
    # Skipped CanConvertFrom due to it being static, abstract and generic.

    CanConvertFrom : CanConvertFrom_MethodGroup
    class CanConvertFrom_MethodGroup:
        @typing.overload
        def __call__(self, sourceType: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, sourceType: typing.Type[typing.Any]) -> bool:...

    # Skipped CanConvertTo due to it being static, abstract and generic.

    CanConvertTo : CanConvertTo_MethodGroup
    class CanConvertTo_MethodGroup:
        @typing.overload
        def __call__(self, destinationType: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, destinationType: typing.Type[typing.Any]) -> bool:...

    # Skipped ConvertFrom due to it being static, abstract and generic.

    ConvertFrom : ConvertFrom_MethodGroup
    class ConvertFrom_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any) -> typing.Any:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, culture: CultureInfo, value: typing.Any) -> typing.Any:...

    # Skipped ConvertTo due to it being static, abstract and generic.

    ConvertTo : ConvertTo_MethodGroup
    class ConvertTo_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any, destinationType: typing.Type[typing.Any]) -> typing.Any:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, culture: CultureInfo, value: typing.Any, destinationType: typing.Type[typing.Any]) -> typing.Any:...

    # Skipped GetStandardValues due to it being static, abstract and generic.

    GetStandardValues : GetStandardValues_MethodGroup
    class GetStandardValues_MethodGroup:
        @typing.overload
        def __call__(self) -> ICollection:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext) -> TypeConverter.StandardValuesCollection:...

    # Skipped GetStandardValuesSupported due to it being static, abstract and generic.

    GetStandardValuesSupported : GetStandardValuesSupported_MethodGroup
    class GetStandardValuesSupported_MethodGroup:
        @typing.overload
        def __call__(self) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext) -> bool:...



class ColorTranslator(abc.ABC):
    @staticmethod
    def FromHtml(htmlColor: str) -> Color: ...
    @staticmethod
    def FromOle(oleColor: int) -> Color: ...
    @staticmethod
    def FromWin32(win32Color: int) -> Color: ...
    @staticmethod
    def ToHtml(c: Color) -> str: ...
    @staticmethod
    def ToOle(c: Color) -> int: ...
    @staticmethod
    def ToWin32(c: Color) -> int: ...


class KnownColor(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    ActiveBorder : KnownColor # 1
    ActiveCaption : KnownColor # 2
    ActiveCaptionText : KnownColor # 3
    AppWorkspace : KnownColor # 4
    Control : KnownColor # 5
    ControlDark : KnownColor # 6
    ControlDarkDark : KnownColor # 7
    ControlLight : KnownColor # 8
    ControlLightLight : KnownColor # 9
    ControlText : KnownColor # 10
    Desktop : KnownColor # 11
    GrayText : KnownColor # 12
    Highlight : KnownColor # 13
    HighlightText : KnownColor # 14
    HotTrack : KnownColor # 15
    InactiveBorder : KnownColor # 16
    InactiveCaption : KnownColor # 17
    InactiveCaptionText : KnownColor # 18
    Info : KnownColor # 19
    InfoText : KnownColor # 20
    Menu : KnownColor # 21
    MenuText : KnownColor # 22
    ScrollBar : KnownColor # 23
    Window : KnownColor # 24
    WindowFrame : KnownColor # 25
    WindowText : KnownColor # 26
    Transparent : KnownColor # 27
    AliceBlue : KnownColor # 28
    AntiqueWhite : KnownColor # 29
    Aqua : KnownColor # 30
    Aquamarine : KnownColor # 31
    Azure : KnownColor # 32
    Beige : KnownColor # 33
    Bisque : KnownColor # 34
    Black : KnownColor # 35
    BlanchedAlmond : KnownColor # 36
    Blue : KnownColor # 37
    BlueViolet : KnownColor # 38
    Brown : KnownColor # 39
    BurlyWood : KnownColor # 40
    CadetBlue : KnownColor # 41
    Chartreuse : KnownColor # 42
    Chocolate : KnownColor # 43
    Coral : KnownColor # 44
    CornflowerBlue : KnownColor # 45
    Cornsilk : KnownColor # 46
    Crimson : KnownColor # 47
    Cyan : KnownColor # 48
    DarkBlue : KnownColor # 49
    DarkCyan : KnownColor # 50
    DarkGoldenrod : KnownColor # 51
    DarkGray : KnownColor # 52
    DarkGreen : KnownColor # 53
    DarkKhaki : KnownColor # 54
    DarkMagenta : KnownColor # 55
    DarkOliveGreen : KnownColor # 56
    DarkOrange : KnownColor # 57
    DarkOrchid : KnownColor # 58
    DarkRed : KnownColor # 59
    DarkSalmon : KnownColor # 60
    DarkSeaGreen : KnownColor # 61
    DarkSlateBlue : KnownColor # 62
    DarkSlateGray : KnownColor # 63
    DarkTurquoise : KnownColor # 64
    DarkViolet : KnownColor # 65
    DeepPink : KnownColor # 66
    DeepSkyBlue : KnownColor # 67
    DimGray : KnownColor # 68
    DodgerBlue : KnownColor # 69
    Firebrick : KnownColor # 70
    FloralWhite : KnownColor # 71
    ForestGreen : KnownColor # 72
    Fuchsia : KnownColor # 73
    Gainsboro : KnownColor # 74
    GhostWhite : KnownColor # 75
    Gold : KnownColor # 76
    Goldenrod : KnownColor # 77
    Gray : KnownColor # 78
    Green : KnownColor # 79
    GreenYellow : KnownColor # 80
    Honeydew : KnownColor # 81
    HotPink : KnownColor # 82
    IndianRed : KnownColor # 83
    Indigo : KnownColor # 84
    Ivory : KnownColor # 85
    Khaki : KnownColor # 86
    Lavender : KnownColor # 87
    LavenderBlush : KnownColor # 88
    LawnGreen : KnownColor # 89
    LemonChiffon : KnownColor # 90
    LightBlue : KnownColor # 91
    LightCoral : KnownColor # 92
    LightCyan : KnownColor # 93
    LightGoldenrodYellow : KnownColor # 94
    LightGray : KnownColor # 95
    LightGreen : KnownColor # 96
    LightPink : KnownColor # 97
    LightSalmon : KnownColor # 98
    LightSeaGreen : KnownColor # 99
    LightSkyBlue : KnownColor # 100
    LightSlateGray : KnownColor # 101
    LightSteelBlue : KnownColor # 102
    LightYellow : KnownColor # 103
    Lime : KnownColor # 104
    LimeGreen : KnownColor # 105
    Linen : KnownColor # 106
    Magenta : KnownColor # 107
    Maroon : KnownColor # 108
    MediumAquamarine : KnownColor # 109
    MediumBlue : KnownColor # 110
    MediumOrchid : KnownColor # 111
    MediumPurple : KnownColor # 112
    MediumSeaGreen : KnownColor # 113
    MediumSlateBlue : KnownColor # 114
    MediumSpringGreen : KnownColor # 115
    MediumTurquoise : KnownColor # 116
    MediumVioletRed : KnownColor # 117
    MidnightBlue : KnownColor # 118
    MintCream : KnownColor # 119
    MistyRose : KnownColor # 120
    Moccasin : KnownColor # 121
    NavajoWhite : KnownColor # 122
    Navy : KnownColor # 123
    OldLace : KnownColor # 124
    Olive : KnownColor # 125
    OliveDrab : KnownColor # 126
    Orange : KnownColor # 127
    OrangeRed : KnownColor # 128
    Orchid : KnownColor # 129
    PaleGoldenrod : KnownColor # 130
    PaleGreen : KnownColor # 131
    PaleTurquoise : KnownColor # 132
    PaleVioletRed : KnownColor # 133
    PapayaWhip : KnownColor # 134
    PeachPuff : KnownColor # 135
    Peru : KnownColor # 136
    Pink : KnownColor # 137
    Plum : KnownColor # 138
    PowderBlue : KnownColor # 139
    Purple : KnownColor # 140
    Red : KnownColor # 141
    RosyBrown : KnownColor # 142
    RoyalBlue : KnownColor # 143
    SaddleBrown : KnownColor # 144
    Salmon : KnownColor # 145
    SandyBrown : KnownColor # 146
    SeaGreen : KnownColor # 147
    SeaShell : KnownColor # 148
    Sienna : KnownColor # 149
    Silver : KnownColor # 150
    SkyBlue : KnownColor # 151
    SlateBlue : KnownColor # 152
    SlateGray : KnownColor # 153
    Snow : KnownColor # 154
    SpringGreen : KnownColor # 155
    SteelBlue : KnownColor # 156
    Tan : KnownColor # 157
    Teal : KnownColor # 158
    Thistle : KnownColor # 159
    Tomato : KnownColor # 160
    Turquoise : KnownColor # 161
    Violet : KnownColor # 162
    Wheat : KnownColor # 163
    White : KnownColor # 164
    WhiteSmoke : KnownColor # 165
    Yellow : KnownColor # 166
    YellowGreen : KnownColor # 167
    ButtonFace : KnownColor # 168
    ButtonHighlight : KnownColor # 169
    ButtonShadow : KnownColor # 170
    GradientActiveCaption : KnownColor # 171
    GradientInactiveCaption : KnownColor # 172
    MenuBar : KnownColor # 173
    MenuHighlight : KnownColor # 174
    RebeccaPurple : KnownColor # 175


class Point(IEquatable_1[Point]):
    @typing.overload
    def __init__(self, dw: int) -> None: ...
    @typing.overload
    def __init__(self, sz: Size) -> None: ...
    @typing.overload
    def __init__(self, x: int, y: int) -> None: ...
    Empty : Point
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def X(self) -> int: ...
    @X.setter
    def X(self, value: int) -> int: ...
    @property
    def Y(self) -> int: ...
    @Y.setter
    def Y(self, value: int) -> int: ...
    @staticmethod
    def Add(pt: Point, sz: Size) -> Point: ...
    @staticmethod
    def Ceiling(value: PointF) -> Point: ...
    def GetHashCode(self) -> int: ...
    def __add__(self, pt: Point, sz: Size) -> Point: ...
    def __eq__(self, left: Point, right: Point) -> bool: ...
    # Operator not supported op_Explicit(p: Point)
    # Operator not supported op_Implicit(p: Point)
    def __ne__(self, left: Point, right: Point) -> bool: ...
    def __sub__(self, pt: Point, sz: Size) -> Point: ...
    @staticmethod
    def Round(value: PointF) -> Point: ...
    @staticmethod
    def Subtract(pt: Point, sz: Size) -> Point: ...
    def ToString(self) -> str: ...
    @staticmethod
    def Truncate(value: PointF) -> Point: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Point) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Offset due to it being static, abstract and generic.

    Offset : Offset_MethodGroup
    class Offset_MethodGroup:
        @typing.overload
        def __call__(self, p: Point) -> None:...
        @typing.overload
        def __call__(self, dx: int, dy: int) -> None:...



class PointConverter(TypeConverter):
    def __init__(self) -> None: ...
    # Skipped CanConvertFrom due to it being static, abstract and generic.

    CanConvertFrom : CanConvertFrom_MethodGroup
    class CanConvertFrom_MethodGroup:
        @typing.overload
        def __call__(self, sourceType: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, sourceType: typing.Type[typing.Any]) -> bool:...

    # Skipped CanConvertTo due to it being static, abstract and generic.

    CanConvertTo : CanConvertTo_MethodGroup
    class CanConvertTo_MethodGroup:
        @typing.overload
        def __call__(self, destinationType: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, destinationType: typing.Type[typing.Any]) -> bool:...

    # Skipped ConvertFrom due to it being static, abstract and generic.

    ConvertFrom : ConvertFrom_MethodGroup
    class ConvertFrom_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any) -> typing.Any:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, culture: CultureInfo, value: typing.Any) -> typing.Any:...

    # Skipped ConvertTo due to it being static, abstract and generic.

    ConvertTo : ConvertTo_MethodGroup
    class ConvertTo_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any, destinationType: typing.Type[typing.Any]) -> typing.Any:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, culture: CultureInfo, value: typing.Any, destinationType: typing.Type[typing.Any]) -> typing.Any:...

    # Skipped CreateInstance due to it being static, abstract and generic.

    CreateInstance : CreateInstance_MethodGroup
    class CreateInstance_MethodGroup:
        @typing.overload
        def __call__(self, propertyValues: IDictionary) -> typing.Any:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, propertyValues: IDictionary) -> typing.Any:...

    # Skipped GetCreateInstanceSupported due to it being static, abstract and generic.

    GetCreateInstanceSupported : GetCreateInstanceSupported_MethodGroup
    class GetCreateInstanceSupported_MethodGroup:
        @typing.overload
        def __call__(self) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext) -> bool:...

    # Skipped GetProperties due to it being static, abstract and generic.

    GetProperties : GetProperties_MethodGroup
    class GetProperties_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any) -> PropertyDescriptorCollection:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, value: typing.Any) -> PropertyDescriptorCollection:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, value: typing.Any, attributes: Array_1[Attribute]) -> PropertyDescriptorCollection:...

    # Skipped GetPropertiesSupported due to it being static, abstract and generic.

    GetPropertiesSupported : GetPropertiesSupported_MethodGroup
    class GetPropertiesSupported_MethodGroup:
        @typing.overload
        def __call__(self) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext) -> bool:...



class PointF(IEquatable_1[PointF]):
    @typing.overload
    def __init__(self, vector: Vector2) -> None: ...
    @typing.overload
    def __init__(self, x: float, y: float) -> None: ...
    Empty : PointF
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def X(self) -> float: ...
    @X.setter
    def X(self, value: float) -> float: ...
    @property
    def Y(self) -> float: ...
    @Y.setter
    def Y(self, value: float) -> float: ...
    def GetHashCode(self) -> int: ...
    @typing.overload
    def __add__(self, pt: PointF, sz: Size) -> PointF: ...
    @typing.overload
    def __add__(self, pt: PointF, sz: SizeF) -> PointF: ...
    def __eq__(self, left: PointF, right: PointF) -> bool: ...
    # Operator not supported op_Explicit(point: PointF)
    # Operator not supported op_Explicit(vector: Vector2)
    def __ne__(self, left: PointF, right: PointF) -> bool: ...
    @typing.overload
    def __sub__(self, pt: PointF, sz: Size) -> PointF: ...
    @typing.overload
    def __sub__(self, pt: PointF, sz: SizeF) -> PointF: ...
    def ToString(self) -> str: ...
    def ToVector2(self) -> Vector2: ...
    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        @typing.overload
        def __call__(self, pt: PointF, sz: Size) -> PointF:...
        @typing.overload
        def __call__(self, pt: PointF, sz: SizeF) -> PointF:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: PointF) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Subtract due to it being static, abstract and generic.

    Subtract : Subtract_MethodGroup
    class Subtract_MethodGroup:
        @typing.overload
        def __call__(self, pt: PointF, sz: Size) -> PointF:...
        @typing.overload
        def __call__(self, pt: PointF, sz: SizeF) -> PointF:...



class Rectangle(IEquatable_1[Rectangle]):
    @typing.overload
    def __init__(self, location: Point, size: Size) -> None: ...
    @typing.overload
    def __init__(self, x: int, y: int, width: int, height: int) -> None: ...
    Empty : Rectangle
    @property
    def Bottom(self) -> int: ...
    @property
    def Height(self) -> int: ...
    @Height.setter
    def Height(self, value: int) -> int: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def Left(self) -> int: ...
    @property
    def Location(self) -> Point: ...
    @Location.setter
    def Location(self, value: Point) -> Point: ...
    @property
    def Right(self) -> int: ...
    @property
    def Size(self) -> Size: ...
    @Size.setter
    def Size(self, value: Size) -> Size: ...
    @property
    def Top(self) -> int: ...
    @property
    def Width(self) -> int: ...
    @Width.setter
    def Width(self, value: int) -> int: ...
    @property
    def X(self) -> int: ...
    @X.setter
    def X(self, value: int) -> int: ...
    @property
    def Y(self) -> int: ...
    @Y.setter
    def Y(self, value: int) -> int: ...
    @staticmethod
    def Ceiling(value: RectangleF) -> Rectangle: ...
    @staticmethod
    def FromLTRB(left: int, top: int, right: int, bottom: int) -> Rectangle: ...
    def GetHashCode(self) -> int: ...
    def IntersectsWith(self, rect: Rectangle) -> bool: ...
    def __eq__(self, left: Rectangle, right: Rectangle) -> bool: ...
    def __ne__(self, left: Rectangle, right: Rectangle) -> bool: ...
    @staticmethod
    def Round(value: RectangleF) -> Rectangle: ...
    def ToString(self) -> str: ...
    @staticmethod
    def Truncate(value: RectangleF) -> Rectangle: ...
    @staticmethod
    def Union(a: Rectangle, b: Rectangle) -> Rectangle: ...
    # Skipped Contains due to it being static, abstract and generic.

    Contains : Contains_MethodGroup
    class Contains_MethodGroup:
        @typing.overload
        def __call__(self, pt: Point) -> bool:...
        @typing.overload
        def __call__(self, rect: Rectangle) -> bool:...
        @typing.overload
        def __call__(self, x: int, y: int) -> bool:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Rectangle) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Inflate due to it being static, abstract and generic.

    Inflate : Inflate_MethodGroup
    class Inflate_MethodGroup:
        @typing.overload
        def __call__(self, size: Size) -> None:...
        @typing.overload
        def __call__(self, width: int, height: int) -> None:...
        @typing.overload
        def __call__(self, rect: Rectangle, x: int, y: int) -> Rectangle:...

    # Skipped Intersect due to it being static, abstract and generic.

    Intersect : Intersect_MethodGroup
    class Intersect_MethodGroup:
        @typing.overload
        def __call__(self, rect: Rectangle) -> None:...
        @typing.overload
        def __call__(self, a: Rectangle, b: Rectangle) -> Rectangle:...

    # Skipped Offset due to it being static, abstract and generic.

    Offset : Offset_MethodGroup
    class Offset_MethodGroup:
        @typing.overload
        def __call__(self, pos: Point) -> None:...
        @typing.overload
        def __call__(self, x: int, y: int) -> None:...



class RectangleConverter(TypeConverter):
    def __init__(self) -> None: ...
    # Skipped CanConvertFrom due to it being static, abstract and generic.

    CanConvertFrom : CanConvertFrom_MethodGroup
    class CanConvertFrom_MethodGroup:
        @typing.overload
        def __call__(self, sourceType: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, sourceType: typing.Type[typing.Any]) -> bool:...

    # Skipped CanConvertTo due to it being static, abstract and generic.

    CanConvertTo : CanConvertTo_MethodGroup
    class CanConvertTo_MethodGroup:
        @typing.overload
        def __call__(self, destinationType: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, destinationType: typing.Type[typing.Any]) -> bool:...

    # Skipped ConvertFrom due to it being static, abstract and generic.

    ConvertFrom : ConvertFrom_MethodGroup
    class ConvertFrom_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any) -> typing.Any:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, culture: CultureInfo, value: typing.Any) -> typing.Any:...

    # Skipped ConvertTo due to it being static, abstract and generic.

    ConvertTo : ConvertTo_MethodGroup
    class ConvertTo_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any, destinationType: typing.Type[typing.Any]) -> typing.Any:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, culture: CultureInfo, value: typing.Any, destinationType: typing.Type[typing.Any]) -> typing.Any:...

    # Skipped CreateInstance due to it being static, abstract and generic.

    CreateInstance : CreateInstance_MethodGroup
    class CreateInstance_MethodGroup:
        @typing.overload
        def __call__(self, propertyValues: IDictionary) -> typing.Any:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, propertyValues: IDictionary) -> typing.Any:...

    # Skipped GetCreateInstanceSupported due to it being static, abstract and generic.

    GetCreateInstanceSupported : GetCreateInstanceSupported_MethodGroup
    class GetCreateInstanceSupported_MethodGroup:
        @typing.overload
        def __call__(self) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext) -> bool:...

    # Skipped GetProperties due to it being static, abstract and generic.

    GetProperties : GetProperties_MethodGroup
    class GetProperties_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any) -> PropertyDescriptorCollection:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, value: typing.Any) -> PropertyDescriptorCollection:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, value: typing.Any, attributes: Array_1[Attribute]) -> PropertyDescriptorCollection:...

    # Skipped GetPropertiesSupported due to it being static, abstract and generic.

    GetPropertiesSupported : GetPropertiesSupported_MethodGroup
    class GetPropertiesSupported_MethodGroup:
        @typing.overload
        def __call__(self) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext) -> bool:...



class RectangleF(IEquatable_1[RectangleF]):
    @typing.overload
    def __init__(self, location: PointF, size: SizeF) -> None: ...
    @typing.overload
    def __init__(self, vector: Vector4) -> None: ...
    @typing.overload
    def __init__(self, x: float, y: float, width: float, height: float) -> None: ...
    Empty : RectangleF
    @property
    def Bottom(self) -> float: ...
    @property
    def Height(self) -> float: ...
    @Height.setter
    def Height(self, value: float) -> float: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def Left(self) -> float: ...
    @property
    def Location(self) -> PointF: ...
    @Location.setter
    def Location(self, value: PointF) -> PointF: ...
    @property
    def Right(self) -> float: ...
    @property
    def Size(self) -> SizeF: ...
    @Size.setter
    def Size(self, value: SizeF) -> SizeF: ...
    @property
    def Top(self) -> float: ...
    @property
    def Width(self) -> float: ...
    @Width.setter
    def Width(self, value: float) -> float: ...
    @property
    def X(self) -> float: ...
    @X.setter
    def X(self, value: float) -> float: ...
    @property
    def Y(self) -> float: ...
    @Y.setter
    def Y(self, value: float) -> float: ...
    @staticmethod
    def FromLTRB(left: float, top: float, right: float, bottom: float) -> RectangleF: ...
    def GetHashCode(self) -> int: ...
    def IntersectsWith(self, rect: RectangleF) -> bool: ...
    def __eq__(self, left: RectangleF, right: RectangleF) -> bool: ...
    # Operator not supported op_Explicit(rectangle: RectangleF)
    # Operator not supported op_Explicit(vector: Vector4)
    # Operator not supported op_Implicit(r: Rectangle)
    def __ne__(self, left: RectangleF, right: RectangleF) -> bool: ...
    def ToString(self) -> str: ...
    def ToVector4(self) -> Vector4: ...
    @staticmethod
    def Union(a: RectangleF, b: RectangleF) -> RectangleF: ...
    # Skipped Contains due to it being static, abstract and generic.

    Contains : Contains_MethodGroup
    class Contains_MethodGroup:
        @typing.overload
        def __call__(self, pt: PointF) -> bool:...
        @typing.overload
        def __call__(self, rect: RectangleF) -> bool:...
        @typing.overload
        def __call__(self, x: float, y: float) -> bool:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: RectangleF) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Inflate due to it being static, abstract and generic.

    Inflate : Inflate_MethodGroup
    class Inflate_MethodGroup:
        @typing.overload
        def __call__(self, size: SizeF) -> None:...
        @typing.overload
        def __call__(self, x: float, y: float) -> None:...
        @typing.overload
        def __call__(self, rect: RectangleF, x: float, y: float) -> RectangleF:...

    # Skipped Intersect due to it being static, abstract and generic.

    Intersect : Intersect_MethodGroup
    class Intersect_MethodGroup:
        @typing.overload
        def __call__(self, rect: RectangleF) -> None:...
        @typing.overload
        def __call__(self, a: RectangleF, b: RectangleF) -> RectangleF:...

    # Skipped Offset due to it being static, abstract and generic.

    Offset : Offset_MethodGroup
    class Offset_MethodGroup:
        @typing.overload
        def __call__(self, pos: PointF) -> None:...
        @typing.overload
        def __call__(self, x: float, y: float) -> None:...



class Size(IEquatable_1[Size]):
    @typing.overload
    def __init__(self, pt: Point) -> None: ...
    @typing.overload
    def __init__(self, width: int, height: int) -> None: ...
    Empty : Size
    @property
    def Height(self) -> int: ...
    @Height.setter
    def Height(self, value: int) -> int: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def Width(self) -> int: ...
    @Width.setter
    def Width(self, value: int) -> int: ...
    @staticmethod
    def Add(sz1: Size, sz2: Size) -> Size: ...
    @staticmethod
    def Ceiling(value: SizeF) -> Size: ...
    def GetHashCode(self) -> int: ...
    def __add__(self, sz1: Size, sz2: Size) -> Size: ...
    @typing.overload
    def __truediv__(self, left: Size, right: float) -> SizeF: ...
    @typing.overload
    def __truediv__(self, left: Size, right: int) -> Size: ...
    def __eq__(self, sz1: Size, sz2: Size) -> bool: ...
    # Operator not supported op_Explicit(size: Size)
    # Operator not supported op_Implicit(p: Size)
    def __ne__(self, sz1: Size, sz2: Size) -> bool: ...
    @typing.overload
    def __mul__(self, left: float, right: Size) -> SizeF: ...
    @typing.overload
    def __mul__(self, left: int, right: Size) -> Size: ...
    @typing.overload
    def __mul__(self, left: Size, right: float) -> SizeF: ...
    @typing.overload
    def __mul__(self, left: Size, right: int) -> Size: ...
    def __sub__(self, sz1: Size, sz2: Size) -> Size: ...
    @staticmethod
    def Round(value: SizeF) -> Size: ...
    @staticmethod
    def Subtract(sz1: Size, sz2: Size) -> Size: ...
    def ToString(self) -> str: ...
    @staticmethod
    def Truncate(value: SizeF) -> Size: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Size) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class SizeConverter(TypeConverter):
    def __init__(self) -> None: ...
    # Skipped CanConvertFrom due to it being static, abstract and generic.

    CanConvertFrom : CanConvertFrom_MethodGroup
    class CanConvertFrom_MethodGroup:
        @typing.overload
        def __call__(self, sourceType: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, sourceType: typing.Type[typing.Any]) -> bool:...

    # Skipped CanConvertTo due to it being static, abstract and generic.

    CanConvertTo : CanConvertTo_MethodGroup
    class CanConvertTo_MethodGroup:
        @typing.overload
        def __call__(self, destinationType: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, destinationType: typing.Type[typing.Any]) -> bool:...

    # Skipped ConvertFrom due to it being static, abstract and generic.

    ConvertFrom : ConvertFrom_MethodGroup
    class ConvertFrom_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any) -> typing.Any:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, culture: CultureInfo, value: typing.Any) -> typing.Any:...

    # Skipped ConvertTo due to it being static, abstract and generic.

    ConvertTo : ConvertTo_MethodGroup
    class ConvertTo_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any, destinationType: typing.Type[typing.Any]) -> typing.Any:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, culture: CultureInfo, value: typing.Any, destinationType: typing.Type[typing.Any]) -> typing.Any:...

    # Skipped CreateInstance due to it being static, abstract and generic.

    CreateInstance : CreateInstance_MethodGroup
    class CreateInstance_MethodGroup:
        @typing.overload
        def __call__(self, propertyValues: IDictionary) -> typing.Any:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, propertyValues: IDictionary) -> typing.Any:...

    # Skipped GetCreateInstanceSupported due to it being static, abstract and generic.

    GetCreateInstanceSupported : GetCreateInstanceSupported_MethodGroup
    class GetCreateInstanceSupported_MethodGroup:
        @typing.overload
        def __call__(self) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext) -> bool:...

    # Skipped GetProperties due to it being static, abstract and generic.

    GetProperties : GetProperties_MethodGroup
    class GetProperties_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any) -> PropertyDescriptorCollection:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, value: typing.Any) -> PropertyDescriptorCollection:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, value: typing.Any, attributes: Array_1[Attribute]) -> PropertyDescriptorCollection:...

    # Skipped GetPropertiesSupported due to it being static, abstract and generic.

    GetPropertiesSupported : GetPropertiesSupported_MethodGroup
    class GetPropertiesSupported_MethodGroup:
        @typing.overload
        def __call__(self) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext) -> bool:...



class SizeF(IEquatable_1[SizeF]):
    @typing.overload
    def __init__(self, pt: PointF) -> None: ...
    @typing.overload
    def __init__(self, size: SizeF) -> None: ...
    @typing.overload
    def __init__(self, vector: Vector2) -> None: ...
    @typing.overload
    def __init__(self, width: float, height: float) -> None: ...
    Empty : SizeF
    @property
    def Height(self) -> float: ...
    @Height.setter
    def Height(self, value: float) -> float: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def Width(self) -> float: ...
    @Width.setter
    def Width(self, value: float) -> float: ...
    @staticmethod
    def Add(sz1: SizeF, sz2: SizeF) -> SizeF: ...
    def GetHashCode(self) -> int: ...
    def __add__(self, sz1: SizeF, sz2: SizeF) -> SizeF: ...
    def __truediv__(self, left: SizeF, right: float) -> SizeF: ...
    def __eq__(self, sz1: SizeF, sz2: SizeF) -> bool: ...
    # Operator not supported op_Explicit(size: SizeF)
    # Operator not supported op_Explicit(size: SizeF)
    # Operator not supported op_Explicit(vector: Vector2)
    def __ne__(self, sz1: SizeF, sz2: SizeF) -> bool: ...
    @typing.overload
    def __mul__(self, left: float, right: SizeF) -> SizeF: ...
    @typing.overload
    def __mul__(self, left: SizeF, right: float) -> SizeF: ...
    def __sub__(self, sz1: SizeF, sz2: SizeF) -> SizeF: ...
    @staticmethod
    def Subtract(sz1: SizeF, sz2: SizeF) -> SizeF: ...
    def ToPointF(self) -> PointF: ...
    def ToSize(self) -> Size: ...
    def ToString(self) -> str: ...
    def ToVector2(self) -> Vector2: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: SizeF) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class SizeFConverter(TypeConverter):
    def __init__(self) -> None: ...
    # Skipped CanConvertFrom due to it being static, abstract and generic.

    CanConvertFrom : CanConvertFrom_MethodGroup
    class CanConvertFrom_MethodGroup:
        @typing.overload
        def __call__(self, sourceType: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, sourceType: typing.Type[typing.Any]) -> bool:...

    # Skipped CanConvertTo due to it being static, abstract and generic.

    CanConvertTo : CanConvertTo_MethodGroup
    class CanConvertTo_MethodGroup:
        @typing.overload
        def __call__(self, destinationType: typing.Type[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, destinationType: typing.Type[typing.Any]) -> bool:...

    # Skipped ConvertFrom due to it being static, abstract and generic.

    ConvertFrom : ConvertFrom_MethodGroup
    class ConvertFrom_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any) -> typing.Any:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, culture: CultureInfo, value: typing.Any) -> typing.Any:...

    # Skipped ConvertTo due to it being static, abstract and generic.

    ConvertTo : ConvertTo_MethodGroup
    class ConvertTo_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any, destinationType: typing.Type[typing.Any]) -> typing.Any:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, culture: CultureInfo, value: typing.Any, destinationType: typing.Type[typing.Any]) -> typing.Any:...

    # Skipped CreateInstance due to it being static, abstract and generic.

    CreateInstance : CreateInstance_MethodGroup
    class CreateInstance_MethodGroup:
        @typing.overload
        def __call__(self, propertyValues: IDictionary) -> typing.Any:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, propertyValues: IDictionary) -> typing.Any:...

    # Skipped GetCreateInstanceSupported due to it being static, abstract and generic.

    GetCreateInstanceSupported : GetCreateInstanceSupported_MethodGroup
    class GetCreateInstanceSupported_MethodGroup:
        @typing.overload
        def __call__(self) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext) -> bool:...

    # Skipped GetProperties due to it being static, abstract and generic.

    GetProperties : GetProperties_MethodGroup
    class GetProperties_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any) -> PropertyDescriptorCollection:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, value: typing.Any) -> PropertyDescriptorCollection:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext, value: typing.Any, attributes: Array_1[Attribute]) -> PropertyDescriptorCollection:...

    # Skipped GetPropertiesSupported due to it being static, abstract and generic.

    GetPropertiesSupported : GetPropertiesSupported_MethodGroup
    class GetPropertiesSupported_MethodGroup:
        @typing.overload
        def __call__(self) -> bool:...
        @typing.overload
        def __call__(self, context: ITypeDescriptorContext) -> bool:...



class SystemColors(abc.ABC):
    @classmethod
    @property
    def ActiveBorder(cls) -> Color: ...
    @classmethod
    @property
    def ActiveCaption(cls) -> Color: ...
    @classmethod
    @property
    def ActiveCaptionText(cls) -> Color: ...
    @classmethod
    @property
    def AppWorkspace(cls) -> Color: ...
    @classmethod
    @property
    def ButtonFace(cls) -> Color: ...
    @classmethod
    @property
    def ButtonHighlight(cls) -> Color: ...
    @classmethod
    @property
    def ButtonShadow(cls) -> Color: ...
    @classmethod
    @property
    def Control(cls) -> Color: ...
    @classmethod
    @property
    def ControlDark(cls) -> Color: ...
    @classmethod
    @property
    def ControlDarkDark(cls) -> Color: ...
    @classmethod
    @property
    def ControlLight(cls) -> Color: ...
    @classmethod
    @property
    def ControlLightLight(cls) -> Color: ...
    @classmethod
    @property
    def ControlText(cls) -> Color: ...
    @classmethod
    @property
    def Desktop(cls) -> Color: ...
    @classmethod
    @property
    def GradientActiveCaption(cls) -> Color: ...
    @classmethod
    @property
    def GradientInactiveCaption(cls) -> Color: ...
    @classmethod
    @property
    def GrayText(cls) -> Color: ...
    @classmethod
    @property
    def Highlight(cls) -> Color: ...
    @classmethod
    @property
    def HighlightText(cls) -> Color: ...
    @classmethod
    @property
    def HotTrack(cls) -> Color: ...
    @classmethod
    @property
    def InactiveBorder(cls) -> Color: ...
    @classmethod
    @property
    def InactiveCaption(cls) -> Color: ...
    @classmethod
    @property
    def InactiveCaptionText(cls) -> Color: ...
    @classmethod
    @property
    def Info(cls) -> Color: ...
    @classmethod
    @property
    def InfoText(cls) -> Color: ...
    @classmethod
    @property
    def Menu(cls) -> Color: ...
    @classmethod
    @property
    def MenuBar(cls) -> Color: ...
    @classmethod
    @property
    def MenuHighlight(cls) -> Color: ...
    @classmethod
    @property
    def MenuText(cls) -> Color: ...
    @classmethod
    @property
    def ScrollBar(cls) -> Color: ...
    @classmethod
    @property
    def Window(cls) -> Color: ...
    @classmethod
    @property
    def WindowFrame(cls) -> Color: ...
    @classmethod
    @property
    def WindowText(cls) -> Color: ...

