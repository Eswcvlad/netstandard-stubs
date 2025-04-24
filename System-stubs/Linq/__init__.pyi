import typing, clr, abc
from System.Collections.Generic import IEnumerable_1, IEqualityComparer_1, IComparer_1, Dictionary_2, HashSet_1, List_1, IList_1, IEnumerator_1
from System import Func_3, Func_2, Decimal, Array_1, Index, Range, ValueTuple_2, ValueTuple_3, Func_1, Action_1
from System.Collections import IEnumerable
from System.Linq.Expressions import Expression, Expression_1
from System.Collections.Concurrent import Partitioner_1
from System.Threading import CancellationToken

class Enumerable(abc.ABC):
    @staticmethod
    def Range(start: int, count: int) -> IEnumerable_1[int]: ...
    # Skipped Aggregate due to it being static, abstract and generic.

    Aggregate : Aggregate_MethodGroup
    class Aggregate_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[Aggregate_1_T1]) -> Aggregate_1[Aggregate_1_T1]: ...

        Aggregate_1_T1 = typing.TypeVar('Aggregate_1_T1')
        class Aggregate_1(typing.Generic[Aggregate_1_T1]):
            Aggregate_1_TSource = Enumerable.Aggregate_MethodGroup.Aggregate_1_T1
            def __call__(self, source: IEnumerable_1[Aggregate_1_TSource], func: Func_3[Aggregate_1_TSource, Aggregate_1_TSource, Aggregate_1_TSource]) -> Aggregate_1_TSource:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Aggregate_2_T1], typing.Type[Aggregate_2_T2]]) -> Aggregate_2[Aggregate_2_T1, Aggregate_2_T2]: ...

        Aggregate_2_T1 = typing.TypeVar('Aggregate_2_T1')
        Aggregate_2_T2 = typing.TypeVar('Aggregate_2_T2')
        class Aggregate_2(typing.Generic[Aggregate_2_T1, Aggregate_2_T2]):
            Aggregate_2_TSource = Enumerable.Aggregate_MethodGroup.Aggregate_2_T1
            Aggregate_2_TAccumulate = Enumerable.Aggregate_MethodGroup.Aggregate_2_T2
            def __call__(self, source: IEnumerable_1[Aggregate_2_TSource], seed: Aggregate_2_TAccumulate, func: Func_3[Aggregate_2_TAccumulate, Aggregate_2_TSource, Aggregate_2_TAccumulate]) -> Aggregate_2_TAccumulate:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Aggregate_3_T1], typing.Type[Aggregate_3_T2], typing.Type[Aggregate_3_T3]]) -> Aggregate_3[Aggregate_3_T1, Aggregate_3_T2, Aggregate_3_T3]: ...

        Aggregate_3_T1 = typing.TypeVar('Aggregate_3_T1')
        Aggregate_3_T2 = typing.TypeVar('Aggregate_3_T2')
        Aggregate_3_T3 = typing.TypeVar('Aggregate_3_T3')
        class Aggregate_3(typing.Generic[Aggregate_3_T1, Aggregate_3_T2, Aggregate_3_T3]):
            Aggregate_3_TSource = Enumerable.Aggregate_MethodGroup.Aggregate_3_T1
            Aggregate_3_TAccumulate = Enumerable.Aggregate_MethodGroup.Aggregate_3_T2
            Aggregate_3_TResult = Enumerable.Aggregate_MethodGroup.Aggregate_3_T3
            def __call__(self, source: IEnumerable_1[Aggregate_3_TSource], seed: Aggregate_3_TAccumulate, func: Func_3[Aggregate_3_TAccumulate, Aggregate_3_TSource, Aggregate_3_TAccumulate], resultSelector: Func_2[Aggregate_3_TAccumulate, Aggregate_3_TResult]) -> Aggregate_3_TResult:...


    # Skipped All due to it being static, abstract and generic.

    All : All_MethodGroup
    class All_MethodGroup:
        def __getitem__(self, t:typing.Type[All_1_T1]) -> All_1[All_1_T1]: ...

        All_1_T1 = typing.TypeVar('All_1_T1')
        class All_1(typing.Generic[All_1_T1]):
            All_1_TSource = Enumerable.All_MethodGroup.All_1_T1
            def __call__(self, source: IEnumerable_1[All_1_TSource], predicate: Func_2[All_1_TSource, bool]) -> bool:...


    # Skipped Any due to it being static, abstract and generic.

    Any : Any_MethodGroup
    class Any_MethodGroup:
        def __getitem__(self, t:typing.Type[Any_1_T1]) -> Any_1[Any_1_T1]: ...

        Any_1_T1 = typing.TypeVar('Any_1_T1')
        class Any_1(typing.Generic[Any_1_T1]):
            Any_1_TSource = Enumerable.Any_MethodGroup.Any_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[Any_1_TSource]) -> bool:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Any_1_TSource], predicate: Func_2[Any_1_TSource, bool]) -> bool:...


    # Skipped Append due to it being static, abstract and generic.

    Append : Append_MethodGroup
    class Append_MethodGroup:
        def __getitem__(self, t:typing.Type[Append_1_T1]) -> Append_1[Append_1_T1]: ...

        Append_1_T1 = typing.TypeVar('Append_1_T1')
        class Append_1(typing.Generic[Append_1_T1]):
            Append_1_TSource = Enumerable.Append_MethodGroup.Append_1_T1
            def __call__(self, source: IEnumerable_1[Append_1_TSource], element: Append_1_TSource) -> IEnumerable_1[Append_1_TSource]:...


    # Skipped AsEnumerable due to it being static, abstract and generic.

    AsEnumerable : AsEnumerable_MethodGroup
    class AsEnumerable_MethodGroup:
        def __getitem__(self, t:typing.Type[AsEnumerable_1_T1]) -> AsEnumerable_1[AsEnumerable_1_T1]: ...

        AsEnumerable_1_T1 = typing.TypeVar('AsEnumerable_1_T1')
        class AsEnumerable_1(typing.Generic[AsEnumerable_1_T1]):
            AsEnumerable_1_TSource = Enumerable.AsEnumerable_MethodGroup.AsEnumerable_1_T1
            def __call__(self, source: IEnumerable_1[AsEnumerable_1_TSource]) -> IEnumerable_1[AsEnumerable_1_TSource]:...


    # Skipped Average due to it being static, abstract and generic.

    Average : Average_MethodGroup
    class Average_MethodGroup:
        def __getitem__(self, t:typing.Type[Average_1_T1]) -> Average_1[Average_1_T1]: ...

        Average_1_T1 = typing.TypeVar('Average_1_T1')
        class Average_1(typing.Generic[Average_1_T1]):
            Average_1_TSource = Enumerable.Average_MethodGroup.Average_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[Average_1_TSource], selector: Func_2[Average_1_TSource, float]) -> float:...
            # Method Average(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: IEnumerable_1[Average_1_TSource], selector: Func_2[Average_1_TSource, int]) -> float:...
            # Method Average(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: IEnumerable_1[Average_1_TSource], selector: Func_2[Average_1_TSource, Decimal]) -> Decimal:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Average_1_TSource], selector: Func_2[Average_1_TSource, typing.Optional[int]]) -> typing.Optional[float]:...
            # Method Average(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            # Method Average(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            # Method Average(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: IEnumerable_1[Average_1_TSource], selector: Func_2[Average_1_TSource, typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

        @typing.overload
        def __call__(self, source: IEnumerable_1[float]) -> float:...
        # Method Average(source : IEnumerable`1) was skipped since it collides with above method
        # Method Average(source : IEnumerable`1) was skipped since it collides with above method
        # Method Average(source : IEnumerable`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: IEnumerable_1[Decimal]) -> Decimal:...
        @typing.overload
        def __call__(self, source: IEnumerable_1[typing.Optional[int]]) -> typing.Optional[float]:...
        # Method Average(source : IEnumerable`1) was skipped since it collides with above method
        # Method Average(source : IEnumerable`1) was skipped since it collides with above method
        # Method Average(source : IEnumerable`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: IEnumerable_1[typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

    # Skipped Cast due to it being static, abstract and generic.

    Cast : Cast_MethodGroup
    class Cast_MethodGroup:
        def __getitem__(self, t:typing.Type[Cast_1_T1]) -> Cast_1[Cast_1_T1]: ...

        Cast_1_T1 = typing.TypeVar('Cast_1_T1')
        class Cast_1(typing.Generic[Cast_1_T1]):
            Cast_1_TResult = Enumerable.Cast_MethodGroup.Cast_1_T1
            def __call__(self, source: IEnumerable) -> IEnumerable_1[Cast_1_TResult]:...


    # Skipped Chunk due to it being static, abstract and generic.

    Chunk : Chunk_MethodGroup
    class Chunk_MethodGroup:
        def __getitem__(self, t:typing.Type[Chunk_1_T1]) -> Chunk_1[Chunk_1_T1]: ...

        Chunk_1_T1 = typing.TypeVar('Chunk_1_T1')
        class Chunk_1(typing.Generic[Chunk_1_T1]):
            Chunk_1_TSource = Enumerable.Chunk_MethodGroup.Chunk_1_T1
            def __call__(self, source: IEnumerable_1[Chunk_1_TSource], size: int) -> IEnumerable_1[Array_1[Chunk_1_TSource]]:...


    # Skipped Concat due to it being static, abstract and generic.

    Concat : Concat_MethodGroup
    class Concat_MethodGroup:
        def __getitem__(self, t:typing.Type[Concat_1_T1]) -> Concat_1[Concat_1_T1]: ...

        Concat_1_T1 = typing.TypeVar('Concat_1_T1')
        class Concat_1(typing.Generic[Concat_1_T1]):
            Concat_1_TSource = Enumerable.Concat_MethodGroup.Concat_1_T1
            def __call__(self, first: IEnumerable_1[Concat_1_TSource], second: IEnumerable_1[Concat_1_TSource]) -> IEnumerable_1[Concat_1_TSource]:...


    # Skipped Contains due to it being static, abstract and generic.

    Contains : Contains_MethodGroup
    class Contains_MethodGroup:
        def __getitem__(self, t:typing.Type[Contains_1_T1]) -> Contains_1[Contains_1_T1]: ...

        Contains_1_T1 = typing.TypeVar('Contains_1_T1')
        class Contains_1(typing.Generic[Contains_1_T1]):
            Contains_1_TSource = Enumerable.Contains_MethodGroup.Contains_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[Contains_1_TSource], value: Contains_1_TSource) -> bool:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Contains_1_TSource], value: Contains_1_TSource, comparer: IEqualityComparer_1[Contains_1_TSource]) -> bool:...


    # Skipped Count due to it being static, abstract and generic.

    Count : Count_MethodGroup
    class Count_MethodGroup:
        def __getitem__(self, t:typing.Type[Count_1_T1]) -> Count_1[Count_1_T1]: ...

        Count_1_T1 = typing.TypeVar('Count_1_T1')
        class Count_1(typing.Generic[Count_1_T1]):
            Count_1_TSource = Enumerable.Count_MethodGroup.Count_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[Count_1_TSource]) -> int:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Count_1_TSource], predicate: Func_2[Count_1_TSource, bool]) -> int:...


    # Skipped DefaultIfEmpty due to it being static, abstract and generic.

    DefaultIfEmpty : DefaultIfEmpty_MethodGroup
    class DefaultIfEmpty_MethodGroup:
        def __getitem__(self, t:typing.Type[DefaultIfEmpty_1_T1]) -> DefaultIfEmpty_1[DefaultIfEmpty_1_T1]: ...

        DefaultIfEmpty_1_T1 = typing.TypeVar('DefaultIfEmpty_1_T1')
        class DefaultIfEmpty_1(typing.Generic[DefaultIfEmpty_1_T1]):
            DefaultIfEmpty_1_TSource = Enumerable.DefaultIfEmpty_MethodGroup.DefaultIfEmpty_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[DefaultIfEmpty_1_TSource]) -> IEnumerable_1[DefaultIfEmpty_1_TSource]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[DefaultIfEmpty_1_TSource], defaultValue: DefaultIfEmpty_1_TSource) -> IEnumerable_1[DefaultIfEmpty_1_TSource]:...


    # Skipped Distinct due to it being static, abstract and generic.

    Distinct : Distinct_MethodGroup
    class Distinct_MethodGroup:
        def __getitem__(self, t:typing.Type[Distinct_1_T1]) -> Distinct_1[Distinct_1_T1]: ...

        Distinct_1_T1 = typing.TypeVar('Distinct_1_T1')
        class Distinct_1(typing.Generic[Distinct_1_T1]):
            Distinct_1_TSource = Enumerable.Distinct_MethodGroup.Distinct_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[Distinct_1_TSource]) -> IEnumerable_1[Distinct_1_TSource]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Distinct_1_TSource], comparer: IEqualityComparer_1[Distinct_1_TSource]) -> IEnumerable_1[Distinct_1_TSource]:...


    # Skipped DistinctBy due to it being static, abstract and generic.

    DistinctBy : DistinctBy_MethodGroup
    class DistinctBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[DistinctBy_2_T1], typing.Type[DistinctBy_2_T2]]) -> DistinctBy_2[DistinctBy_2_T1, DistinctBy_2_T2]: ...

        DistinctBy_2_T1 = typing.TypeVar('DistinctBy_2_T1')
        DistinctBy_2_T2 = typing.TypeVar('DistinctBy_2_T2')
        class DistinctBy_2(typing.Generic[DistinctBy_2_T1, DistinctBy_2_T2]):
            DistinctBy_2_TSource = Enumerable.DistinctBy_MethodGroup.DistinctBy_2_T1
            DistinctBy_2_TKey = Enumerable.DistinctBy_MethodGroup.DistinctBy_2_T2
            @typing.overload
            def __call__(self, source: IEnumerable_1[DistinctBy_2_TSource], keySelector: Func_2[DistinctBy_2_TSource, DistinctBy_2_TKey]) -> IEnumerable_1[DistinctBy_2_TSource]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[DistinctBy_2_TSource], keySelector: Func_2[DistinctBy_2_TSource, DistinctBy_2_TKey], comparer: IEqualityComparer_1[DistinctBy_2_TKey]) -> IEnumerable_1[DistinctBy_2_TSource]:...


    # Skipped ElementAt due to it being static, abstract and generic.

    ElementAt : ElementAt_MethodGroup
    class ElementAt_MethodGroup:
        def __getitem__(self, t:typing.Type[ElementAt_1_T1]) -> ElementAt_1[ElementAt_1_T1]: ...

        ElementAt_1_T1 = typing.TypeVar('ElementAt_1_T1')
        class ElementAt_1(typing.Generic[ElementAt_1_T1]):
            ElementAt_1_TSource = Enumerable.ElementAt_MethodGroup.ElementAt_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[ElementAt_1_TSource], index: int) -> ElementAt_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[ElementAt_1_TSource], index: Index) -> ElementAt_1_TSource:...


    # Skipped ElementAtOrDefault due to it being static, abstract and generic.

    ElementAtOrDefault : ElementAtOrDefault_MethodGroup
    class ElementAtOrDefault_MethodGroup:
        def __getitem__(self, t:typing.Type[ElementAtOrDefault_1_T1]) -> ElementAtOrDefault_1[ElementAtOrDefault_1_T1]: ...

        ElementAtOrDefault_1_T1 = typing.TypeVar('ElementAtOrDefault_1_T1')
        class ElementAtOrDefault_1(typing.Generic[ElementAtOrDefault_1_T1]):
            ElementAtOrDefault_1_TSource = Enumerable.ElementAtOrDefault_MethodGroup.ElementAtOrDefault_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[ElementAtOrDefault_1_TSource], index: int) -> ElementAtOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[ElementAtOrDefault_1_TSource], index: Index) -> ElementAtOrDefault_1_TSource:...


    # Skipped Empty due to it being static, abstract and generic.

    Empty : Empty_MethodGroup
    class Empty_MethodGroup:
        def __getitem__(self, t:typing.Type[Empty_1_T1]) -> Empty_1[Empty_1_T1]: ...

        Empty_1_T1 = typing.TypeVar('Empty_1_T1')
        class Empty_1(typing.Generic[Empty_1_T1]):
            Empty_1_TResult = Enumerable.Empty_MethodGroup.Empty_1_T1
            def __call__(self) -> IEnumerable_1[Empty_1_TResult]:...


    # Skipped Except due to it being static, abstract and generic.

    Except : Except_MethodGroup
    class Except_MethodGroup:
        def __getitem__(self, t:typing.Type[Except_1_T1]) -> Except_1[Except_1_T1]: ...

        Except_1_T1 = typing.TypeVar('Except_1_T1')
        class Except_1(typing.Generic[Except_1_T1]):
            Except_1_TSource = Enumerable.Except_MethodGroup.Except_1_T1
            @typing.overload
            def __call__(self, first: IEnumerable_1[Except_1_TSource], second: IEnumerable_1[Except_1_TSource]) -> IEnumerable_1[Except_1_TSource]:...
            @typing.overload
            def __call__(self, first: IEnumerable_1[Except_1_TSource], second: IEnumerable_1[Except_1_TSource], comparer: IEqualityComparer_1[Except_1_TSource]) -> IEnumerable_1[Except_1_TSource]:...


    # Skipped ExceptBy due to it being static, abstract and generic.

    ExceptBy : ExceptBy_MethodGroup
    class ExceptBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[ExceptBy_2_T1], typing.Type[ExceptBy_2_T2]]) -> ExceptBy_2[ExceptBy_2_T1, ExceptBy_2_T2]: ...

        ExceptBy_2_T1 = typing.TypeVar('ExceptBy_2_T1')
        ExceptBy_2_T2 = typing.TypeVar('ExceptBy_2_T2')
        class ExceptBy_2(typing.Generic[ExceptBy_2_T1, ExceptBy_2_T2]):
            ExceptBy_2_TSource = Enumerable.ExceptBy_MethodGroup.ExceptBy_2_T1
            ExceptBy_2_TKey = Enumerable.ExceptBy_MethodGroup.ExceptBy_2_T2
            @typing.overload
            def __call__(self, first: IEnumerable_1[ExceptBy_2_TSource], second: IEnumerable_1[ExceptBy_2_TKey], keySelector: Func_2[ExceptBy_2_TSource, ExceptBy_2_TKey]) -> IEnumerable_1[ExceptBy_2_TSource]:...
            @typing.overload
            def __call__(self, first: IEnumerable_1[ExceptBy_2_TSource], second: IEnumerable_1[ExceptBy_2_TKey], keySelector: Func_2[ExceptBy_2_TSource, ExceptBy_2_TKey], comparer: IEqualityComparer_1[ExceptBy_2_TKey]) -> IEnumerable_1[ExceptBy_2_TSource]:...


    # Skipped First due to it being static, abstract and generic.

    First : First_MethodGroup
    class First_MethodGroup:
        def __getitem__(self, t:typing.Type[First_1_T1]) -> First_1[First_1_T1]: ...

        First_1_T1 = typing.TypeVar('First_1_T1')
        class First_1(typing.Generic[First_1_T1]):
            First_1_TSource = Enumerable.First_MethodGroup.First_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[First_1_TSource]) -> First_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[First_1_TSource], predicate: Func_2[First_1_TSource, bool]) -> First_1_TSource:...


    # Skipped FirstOrDefault due to it being static, abstract and generic.

    FirstOrDefault : FirstOrDefault_MethodGroup
    class FirstOrDefault_MethodGroup:
        def __getitem__(self, t:typing.Type[FirstOrDefault_1_T1]) -> FirstOrDefault_1[FirstOrDefault_1_T1]: ...

        FirstOrDefault_1_T1 = typing.TypeVar('FirstOrDefault_1_T1')
        class FirstOrDefault_1(typing.Generic[FirstOrDefault_1_T1]):
            FirstOrDefault_1_TSource = Enumerable.FirstOrDefault_MethodGroup.FirstOrDefault_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[FirstOrDefault_1_TSource]) -> FirstOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[FirstOrDefault_1_TSource], predicate: Func_2[FirstOrDefault_1_TSource, bool]) -> FirstOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[FirstOrDefault_1_TSource], defaultValue: FirstOrDefault_1_TSource) -> FirstOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[FirstOrDefault_1_TSource], predicate: Func_2[FirstOrDefault_1_TSource, bool], defaultValue: FirstOrDefault_1_TSource) -> FirstOrDefault_1_TSource:...


    # Skipped GroupBy due to it being static, abstract and generic.

    GroupBy : GroupBy_MethodGroup
    class GroupBy_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[GroupBy_2_T1], typing.Type[GroupBy_2_T2]]) -> GroupBy_2[GroupBy_2_T1, GroupBy_2_T2]: ...

        GroupBy_2_T1 = typing.TypeVar('GroupBy_2_T1')
        GroupBy_2_T2 = typing.TypeVar('GroupBy_2_T2')
        class GroupBy_2(typing.Generic[GroupBy_2_T1, GroupBy_2_T2]):
            GroupBy_2_TSource = Enumerable.GroupBy_MethodGroup.GroupBy_2_T1
            GroupBy_2_TKey = Enumerable.GroupBy_MethodGroup.GroupBy_2_T2
            @typing.overload
            def __call__(self, source: IEnumerable_1[GroupBy_2_TSource], keySelector: Func_2[GroupBy_2_TSource, GroupBy_2_TKey]) -> IEnumerable_1[IGrouping_2[GroupBy_2_TKey, GroupBy_2_TSource]]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[GroupBy_2_TSource], keySelector: Func_2[GroupBy_2_TSource, GroupBy_2_TKey], comparer: IEqualityComparer_1[GroupBy_2_TKey]) -> IEnumerable_1[IGrouping_2[GroupBy_2_TKey, GroupBy_2_TSource]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[GroupBy_3_T1], typing.Type[GroupBy_3_T2], typing.Type[GroupBy_3_T3]]) -> GroupBy_3[GroupBy_3_T1, GroupBy_3_T2, GroupBy_3_T3]: ...

        GroupBy_3_T1 = typing.TypeVar('GroupBy_3_T1')
        GroupBy_3_T2 = typing.TypeVar('GroupBy_3_T2')
        GroupBy_3_T3 = typing.TypeVar('GroupBy_3_T3')
        class GroupBy_3(typing.Generic[GroupBy_3_T1, GroupBy_3_T2, GroupBy_3_T3]):
            GroupBy_3_TSource = Enumerable.GroupBy_MethodGroup.GroupBy_3_T1
            GroupBy_3_TKey = Enumerable.GroupBy_MethodGroup.GroupBy_3_T2
            GroupBy_3_TElement = Enumerable.GroupBy_MethodGroup.GroupBy_3_T3
            GroupBy_3_TResult = Enumerable.GroupBy_MethodGroup.GroupBy_3_T3
            @typing.overload
            def __call__(self, source: IEnumerable_1[GroupBy_3_TSource], keySelector: Func_2[GroupBy_3_TSource, GroupBy_3_TKey], elementSelector: Func_2[GroupBy_3_TSource, GroupBy_3_TElement]) -> IEnumerable_1[IGrouping_2[GroupBy_3_TKey, GroupBy_3_TElement]]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[GroupBy_3_TSource], keySelector: Func_2[GroupBy_3_TSource, GroupBy_3_TKey], resultSelector: Func_3[GroupBy_3_TKey, IEnumerable_1[GroupBy_3_TSource], GroupBy_3_TResult]) -> IEnumerable_1[GroupBy_3_TResult]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[GroupBy_3_TSource], keySelector: Func_2[GroupBy_3_TSource, GroupBy_3_TKey], elementSelector: Func_2[GroupBy_3_TSource, GroupBy_3_TElement], comparer: IEqualityComparer_1[GroupBy_3_TKey]) -> IEnumerable_1[IGrouping_2[GroupBy_3_TKey, GroupBy_3_TElement]]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[GroupBy_3_TSource], keySelector: Func_2[GroupBy_3_TSource, GroupBy_3_TKey], resultSelector: Func_3[GroupBy_3_TKey, IEnumerable_1[GroupBy_3_TSource], GroupBy_3_TResult], comparer: IEqualityComparer_1[GroupBy_3_TKey]) -> IEnumerable_1[GroupBy_3_TResult]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[GroupBy_4_T1], typing.Type[GroupBy_4_T2], typing.Type[GroupBy_4_T3], typing.Type[GroupBy_4_T4]]) -> GroupBy_4[GroupBy_4_T1, GroupBy_4_T2, GroupBy_4_T3, GroupBy_4_T4]: ...

        GroupBy_4_T1 = typing.TypeVar('GroupBy_4_T1')
        GroupBy_4_T2 = typing.TypeVar('GroupBy_4_T2')
        GroupBy_4_T3 = typing.TypeVar('GroupBy_4_T3')
        GroupBy_4_T4 = typing.TypeVar('GroupBy_4_T4')
        class GroupBy_4(typing.Generic[GroupBy_4_T1, GroupBy_4_T2, GroupBy_4_T3, GroupBy_4_T4]):
            GroupBy_4_TSource = Enumerable.GroupBy_MethodGroup.GroupBy_4_T1
            GroupBy_4_TKey = Enumerable.GroupBy_MethodGroup.GroupBy_4_T2
            GroupBy_4_TElement = Enumerable.GroupBy_MethodGroup.GroupBy_4_T3
            GroupBy_4_TResult = Enumerable.GroupBy_MethodGroup.GroupBy_4_T4
            @typing.overload
            def __call__(self, source: IEnumerable_1[GroupBy_4_TSource], keySelector: Func_2[GroupBy_4_TSource, GroupBy_4_TKey], elementSelector: Func_2[GroupBy_4_TSource, GroupBy_4_TElement], resultSelector: Func_3[GroupBy_4_TKey, IEnumerable_1[GroupBy_4_TElement], GroupBy_4_TResult]) -> IEnumerable_1[GroupBy_4_TResult]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[GroupBy_4_TSource], keySelector: Func_2[GroupBy_4_TSource, GroupBy_4_TKey], elementSelector: Func_2[GroupBy_4_TSource, GroupBy_4_TElement], resultSelector: Func_3[GroupBy_4_TKey, IEnumerable_1[GroupBy_4_TElement], GroupBy_4_TResult], comparer: IEqualityComparer_1[GroupBy_4_TKey]) -> IEnumerable_1[GroupBy_4_TResult]:...


    # Skipped GroupJoin due to it being static, abstract and generic.

    GroupJoin : GroupJoin_MethodGroup
    class GroupJoin_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[GroupJoin_4_T1], typing.Type[GroupJoin_4_T2], typing.Type[GroupJoin_4_T3], typing.Type[GroupJoin_4_T4]]) -> GroupJoin_4[GroupJoin_4_T1, GroupJoin_4_T2, GroupJoin_4_T3, GroupJoin_4_T4]: ...

        GroupJoin_4_T1 = typing.TypeVar('GroupJoin_4_T1')
        GroupJoin_4_T2 = typing.TypeVar('GroupJoin_4_T2')
        GroupJoin_4_T3 = typing.TypeVar('GroupJoin_4_T3')
        GroupJoin_4_T4 = typing.TypeVar('GroupJoin_4_T4')
        class GroupJoin_4(typing.Generic[GroupJoin_4_T1, GroupJoin_4_T2, GroupJoin_4_T3, GroupJoin_4_T4]):
            GroupJoin_4_TOuter = Enumerable.GroupJoin_MethodGroup.GroupJoin_4_T1
            GroupJoin_4_TInner = Enumerable.GroupJoin_MethodGroup.GroupJoin_4_T2
            GroupJoin_4_TKey = Enumerable.GroupJoin_MethodGroup.GroupJoin_4_T3
            GroupJoin_4_TResult = Enumerable.GroupJoin_MethodGroup.GroupJoin_4_T4
            @typing.overload
            def __call__(self, outer: IEnumerable_1[GroupJoin_4_TOuter], inner: IEnumerable_1[GroupJoin_4_TInner], outerKeySelector: Func_2[GroupJoin_4_TOuter, GroupJoin_4_TKey], innerKeySelector: Func_2[GroupJoin_4_TInner, GroupJoin_4_TKey], resultSelector: Func_3[GroupJoin_4_TOuter, IEnumerable_1[GroupJoin_4_TInner], GroupJoin_4_TResult]) -> IEnumerable_1[GroupJoin_4_TResult]:...
            @typing.overload
            def __call__(self, outer: IEnumerable_1[GroupJoin_4_TOuter], inner: IEnumerable_1[GroupJoin_4_TInner], outerKeySelector: Func_2[GroupJoin_4_TOuter, GroupJoin_4_TKey], innerKeySelector: Func_2[GroupJoin_4_TInner, GroupJoin_4_TKey], resultSelector: Func_3[GroupJoin_4_TOuter, IEnumerable_1[GroupJoin_4_TInner], GroupJoin_4_TResult], comparer: IEqualityComparer_1[GroupJoin_4_TKey]) -> IEnumerable_1[GroupJoin_4_TResult]:...


    # Skipped Intersect due to it being static, abstract and generic.

    Intersect : Intersect_MethodGroup
    class Intersect_MethodGroup:
        def __getitem__(self, t:typing.Type[Intersect_1_T1]) -> Intersect_1[Intersect_1_T1]: ...

        Intersect_1_T1 = typing.TypeVar('Intersect_1_T1')
        class Intersect_1(typing.Generic[Intersect_1_T1]):
            Intersect_1_TSource = Enumerable.Intersect_MethodGroup.Intersect_1_T1
            @typing.overload
            def __call__(self, first: IEnumerable_1[Intersect_1_TSource], second: IEnumerable_1[Intersect_1_TSource]) -> IEnumerable_1[Intersect_1_TSource]:...
            @typing.overload
            def __call__(self, first: IEnumerable_1[Intersect_1_TSource], second: IEnumerable_1[Intersect_1_TSource], comparer: IEqualityComparer_1[Intersect_1_TSource]) -> IEnumerable_1[Intersect_1_TSource]:...


    # Skipped IntersectBy due to it being static, abstract and generic.

    IntersectBy : IntersectBy_MethodGroup
    class IntersectBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[IntersectBy_2_T1], typing.Type[IntersectBy_2_T2]]) -> IntersectBy_2[IntersectBy_2_T1, IntersectBy_2_T2]: ...

        IntersectBy_2_T1 = typing.TypeVar('IntersectBy_2_T1')
        IntersectBy_2_T2 = typing.TypeVar('IntersectBy_2_T2')
        class IntersectBy_2(typing.Generic[IntersectBy_2_T1, IntersectBy_2_T2]):
            IntersectBy_2_TSource = Enumerable.IntersectBy_MethodGroup.IntersectBy_2_T1
            IntersectBy_2_TKey = Enumerable.IntersectBy_MethodGroup.IntersectBy_2_T2
            @typing.overload
            def __call__(self, first: IEnumerable_1[IntersectBy_2_TSource], second: IEnumerable_1[IntersectBy_2_TKey], keySelector: Func_2[IntersectBy_2_TSource, IntersectBy_2_TKey]) -> IEnumerable_1[IntersectBy_2_TSource]:...
            @typing.overload
            def __call__(self, first: IEnumerable_1[IntersectBy_2_TSource], second: IEnumerable_1[IntersectBy_2_TKey], keySelector: Func_2[IntersectBy_2_TSource, IntersectBy_2_TKey], comparer: IEqualityComparer_1[IntersectBy_2_TKey]) -> IEnumerable_1[IntersectBy_2_TSource]:...


    # Skipped Join due to it being static, abstract and generic.

    Join : Join_MethodGroup
    class Join_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Join_4_T1], typing.Type[Join_4_T2], typing.Type[Join_4_T3], typing.Type[Join_4_T4]]) -> Join_4[Join_4_T1, Join_4_T2, Join_4_T3, Join_4_T4]: ...

        Join_4_T1 = typing.TypeVar('Join_4_T1')
        Join_4_T2 = typing.TypeVar('Join_4_T2')
        Join_4_T3 = typing.TypeVar('Join_4_T3')
        Join_4_T4 = typing.TypeVar('Join_4_T4')
        class Join_4(typing.Generic[Join_4_T1, Join_4_T2, Join_4_T3, Join_4_T4]):
            Join_4_TOuter = Enumerable.Join_MethodGroup.Join_4_T1
            Join_4_TInner = Enumerable.Join_MethodGroup.Join_4_T2
            Join_4_TKey = Enumerable.Join_MethodGroup.Join_4_T3
            Join_4_TResult = Enumerable.Join_MethodGroup.Join_4_T4
            @typing.overload
            def __call__(self, outer: IEnumerable_1[Join_4_TOuter], inner: IEnumerable_1[Join_4_TInner], outerKeySelector: Func_2[Join_4_TOuter, Join_4_TKey], innerKeySelector: Func_2[Join_4_TInner, Join_4_TKey], resultSelector: Func_3[Join_4_TOuter, Join_4_TInner, Join_4_TResult]) -> IEnumerable_1[Join_4_TResult]:...
            @typing.overload
            def __call__(self, outer: IEnumerable_1[Join_4_TOuter], inner: IEnumerable_1[Join_4_TInner], outerKeySelector: Func_2[Join_4_TOuter, Join_4_TKey], innerKeySelector: Func_2[Join_4_TInner, Join_4_TKey], resultSelector: Func_3[Join_4_TOuter, Join_4_TInner, Join_4_TResult], comparer: IEqualityComparer_1[Join_4_TKey]) -> IEnumerable_1[Join_4_TResult]:...


    # Skipped Last due to it being static, abstract and generic.

    Last : Last_MethodGroup
    class Last_MethodGroup:
        def __getitem__(self, t:typing.Type[Last_1_T1]) -> Last_1[Last_1_T1]: ...

        Last_1_T1 = typing.TypeVar('Last_1_T1')
        class Last_1(typing.Generic[Last_1_T1]):
            Last_1_TSource = Enumerable.Last_MethodGroup.Last_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[Last_1_TSource]) -> Last_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Last_1_TSource], predicate: Func_2[Last_1_TSource, bool]) -> Last_1_TSource:...


    # Skipped LastOrDefault due to it being static, abstract and generic.

    LastOrDefault : LastOrDefault_MethodGroup
    class LastOrDefault_MethodGroup:
        def __getitem__(self, t:typing.Type[LastOrDefault_1_T1]) -> LastOrDefault_1[LastOrDefault_1_T1]: ...

        LastOrDefault_1_T1 = typing.TypeVar('LastOrDefault_1_T1')
        class LastOrDefault_1(typing.Generic[LastOrDefault_1_T1]):
            LastOrDefault_1_TSource = Enumerable.LastOrDefault_MethodGroup.LastOrDefault_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[LastOrDefault_1_TSource]) -> LastOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[LastOrDefault_1_TSource], predicate: Func_2[LastOrDefault_1_TSource, bool]) -> LastOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[LastOrDefault_1_TSource], defaultValue: LastOrDefault_1_TSource) -> LastOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[LastOrDefault_1_TSource], predicate: Func_2[LastOrDefault_1_TSource, bool], defaultValue: LastOrDefault_1_TSource) -> LastOrDefault_1_TSource:...


    # Skipped LongCount due to it being static, abstract and generic.

    LongCount : LongCount_MethodGroup
    class LongCount_MethodGroup:
        def __getitem__(self, t:typing.Type[LongCount_1_T1]) -> LongCount_1[LongCount_1_T1]: ...

        LongCount_1_T1 = typing.TypeVar('LongCount_1_T1')
        class LongCount_1(typing.Generic[LongCount_1_T1]):
            LongCount_1_TSource = Enumerable.LongCount_MethodGroup.LongCount_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[LongCount_1_TSource]) -> int:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[LongCount_1_TSource], predicate: Func_2[LongCount_1_TSource, bool]) -> int:...


    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[Max_1_T1]) -> Max_1[Max_1_T1]: ...

        Max_1_T1 = typing.TypeVar('Max_1_T1')
        class Max_1(typing.Generic[Max_1_T1]):
            Max_1_TSource = Enumerable.Max_MethodGroup.Max_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[Max_1_TSource]) -> Max_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Max_1_TSource], selector: Func_2[Max_1_TSource, float]) -> float:...
            # Method Max(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: IEnumerable_1[Max_1_TSource], selector: Func_2[Max_1_TSource, int]) -> int:...
            # Method Max(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: IEnumerable_1[Max_1_TSource], selector: Func_2[Max_1_TSource, Decimal]) -> Decimal:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Max_1_TSource], selector: Func_2[Max_1_TSource, typing.Optional[int]]) -> typing.Optional[int]:...
            # Method Max(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            # Method Max(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            # Method Max(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: IEnumerable_1[Max_1_TSource], selector: Func_2[Max_1_TSource, typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Max_1_TSource], comparer: IComparer_1[Max_1_TSource]) -> Max_1_TSource:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Max_2_T1], typing.Type[Max_2_T2]]) -> Max_2[Max_2_T1, Max_2_T2]: ...

        Max_2_T1 = typing.TypeVar('Max_2_T1')
        Max_2_T2 = typing.TypeVar('Max_2_T2')
        class Max_2(typing.Generic[Max_2_T1, Max_2_T2]):
            Max_2_TSource = Enumerable.Max_MethodGroup.Max_2_T1
            Max_2_TResult = Enumerable.Max_MethodGroup.Max_2_T2
            def __call__(self, source: IEnumerable_1[Max_2_TSource], selector: Func_2[Max_2_TSource, Max_2_TResult]) -> Max_2_TResult:...

        @typing.overload
        def __call__(self, source: IEnumerable_1[float]) -> float:...
        # Method Max(source : IEnumerable`1) was skipped since it collides with above method
        # Method Max(source : IEnumerable`1) was skipped since it collides with above method
        # Method Max(source : IEnumerable`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: IEnumerable_1[Decimal]) -> Decimal:...
        @typing.overload
        def __call__(self, source: IEnumerable_1[typing.Optional[int]]) -> typing.Optional[int]:...
        # Method Max(source : IEnumerable`1) was skipped since it collides with above method
        # Method Max(source : IEnumerable`1) was skipped since it collides with above method
        # Method Max(source : IEnumerable`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: IEnumerable_1[typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

    # Skipped MaxBy due to it being static, abstract and generic.

    MaxBy : MaxBy_MethodGroup
    class MaxBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[MaxBy_2_T1], typing.Type[MaxBy_2_T2]]) -> MaxBy_2[MaxBy_2_T1, MaxBy_2_T2]: ...

        MaxBy_2_T1 = typing.TypeVar('MaxBy_2_T1')
        MaxBy_2_T2 = typing.TypeVar('MaxBy_2_T2')
        class MaxBy_2(typing.Generic[MaxBy_2_T1, MaxBy_2_T2]):
            MaxBy_2_TSource = Enumerable.MaxBy_MethodGroup.MaxBy_2_T1
            MaxBy_2_TKey = Enumerable.MaxBy_MethodGroup.MaxBy_2_T2
            @typing.overload
            def __call__(self, source: IEnumerable_1[MaxBy_2_TSource], keySelector: Func_2[MaxBy_2_TSource, MaxBy_2_TKey]) -> MaxBy_2_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[MaxBy_2_TSource], keySelector: Func_2[MaxBy_2_TSource, MaxBy_2_TKey], comparer: IComparer_1[MaxBy_2_TKey]) -> MaxBy_2_TSource:...


    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[Min_1_T1]) -> Min_1[Min_1_T1]: ...

        Min_1_T1 = typing.TypeVar('Min_1_T1')
        class Min_1(typing.Generic[Min_1_T1]):
            Min_1_TSource = Enumerable.Min_MethodGroup.Min_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[Min_1_TSource]) -> Min_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Min_1_TSource], selector: Func_2[Min_1_TSource, float]) -> float:...
            # Method Min(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: IEnumerable_1[Min_1_TSource], selector: Func_2[Min_1_TSource, int]) -> int:...
            # Method Min(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: IEnumerable_1[Min_1_TSource], selector: Func_2[Min_1_TSource, Decimal]) -> Decimal:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Min_1_TSource], selector: Func_2[Min_1_TSource, typing.Optional[int]]) -> typing.Optional[int]:...
            # Method Min(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            # Method Min(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            # Method Min(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: IEnumerable_1[Min_1_TSource], selector: Func_2[Min_1_TSource, typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Min_1_TSource], comparer: IComparer_1[Min_1_TSource]) -> Min_1_TSource:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Min_2_T1], typing.Type[Min_2_T2]]) -> Min_2[Min_2_T1, Min_2_T2]: ...

        Min_2_T1 = typing.TypeVar('Min_2_T1')
        Min_2_T2 = typing.TypeVar('Min_2_T2')
        class Min_2(typing.Generic[Min_2_T1, Min_2_T2]):
            Min_2_TSource = Enumerable.Min_MethodGroup.Min_2_T1
            Min_2_TResult = Enumerable.Min_MethodGroup.Min_2_T2
            def __call__(self, source: IEnumerable_1[Min_2_TSource], selector: Func_2[Min_2_TSource, Min_2_TResult]) -> Min_2_TResult:...

        @typing.overload
        def __call__(self, source: IEnumerable_1[float]) -> float:...
        # Method Min(source : IEnumerable`1) was skipped since it collides with above method
        # Method Min(source : IEnumerable`1) was skipped since it collides with above method
        # Method Min(source : IEnumerable`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: IEnumerable_1[Decimal]) -> Decimal:...
        @typing.overload
        def __call__(self, source: IEnumerable_1[typing.Optional[int]]) -> typing.Optional[int]:...
        # Method Min(source : IEnumerable`1) was skipped since it collides with above method
        # Method Min(source : IEnumerable`1) was skipped since it collides with above method
        # Method Min(source : IEnumerable`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: IEnumerable_1[typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

    # Skipped MinBy due to it being static, abstract and generic.

    MinBy : MinBy_MethodGroup
    class MinBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[MinBy_2_T1], typing.Type[MinBy_2_T2]]) -> MinBy_2[MinBy_2_T1, MinBy_2_T2]: ...

        MinBy_2_T1 = typing.TypeVar('MinBy_2_T1')
        MinBy_2_T2 = typing.TypeVar('MinBy_2_T2')
        class MinBy_2(typing.Generic[MinBy_2_T1, MinBy_2_T2]):
            MinBy_2_TSource = Enumerable.MinBy_MethodGroup.MinBy_2_T1
            MinBy_2_TKey = Enumerable.MinBy_MethodGroup.MinBy_2_T2
            @typing.overload
            def __call__(self, source: IEnumerable_1[MinBy_2_TSource], keySelector: Func_2[MinBy_2_TSource, MinBy_2_TKey]) -> MinBy_2_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[MinBy_2_TSource], keySelector: Func_2[MinBy_2_TSource, MinBy_2_TKey], comparer: IComparer_1[MinBy_2_TKey]) -> MinBy_2_TSource:...


    # Skipped OfType due to it being static, abstract and generic.

    OfType : OfType_MethodGroup
    class OfType_MethodGroup:
        def __getitem__(self, t:typing.Type[OfType_1_T1]) -> OfType_1[OfType_1_T1]: ...

        OfType_1_T1 = typing.TypeVar('OfType_1_T1')
        class OfType_1(typing.Generic[OfType_1_T1]):
            OfType_1_TResult = Enumerable.OfType_MethodGroup.OfType_1_T1
            def __call__(self, source: IEnumerable) -> IEnumerable_1[OfType_1_TResult]:...


    # Skipped OrderBy due to it being static, abstract and generic.

    OrderBy : OrderBy_MethodGroup
    class OrderBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[OrderBy_2_T1], typing.Type[OrderBy_2_T2]]) -> OrderBy_2[OrderBy_2_T1, OrderBy_2_T2]: ...

        OrderBy_2_T1 = typing.TypeVar('OrderBy_2_T1')
        OrderBy_2_T2 = typing.TypeVar('OrderBy_2_T2')
        class OrderBy_2(typing.Generic[OrderBy_2_T1, OrderBy_2_T2]):
            OrderBy_2_TSource = Enumerable.OrderBy_MethodGroup.OrderBy_2_T1
            OrderBy_2_TKey = Enumerable.OrderBy_MethodGroup.OrderBy_2_T2
            @typing.overload
            def __call__(self, source: IEnumerable_1[OrderBy_2_TSource], keySelector: Func_2[OrderBy_2_TSource, OrderBy_2_TKey]) -> IOrderedEnumerable_1[OrderBy_2_TSource]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[OrderBy_2_TSource], keySelector: Func_2[OrderBy_2_TSource, OrderBy_2_TKey], comparer: IComparer_1[OrderBy_2_TKey]) -> IOrderedEnumerable_1[OrderBy_2_TSource]:...


    # Skipped OrderByDescending due to it being static, abstract and generic.

    OrderByDescending : OrderByDescending_MethodGroup
    class OrderByDescending_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[OrderByDescending_2_T1], typing.Type[OrderByDescending_2_T2]]) -> OrderByDescending_2[OrderByDescending_2_T1, OrderByDescending_2_T2]: ...

        OrderByDescending_2_T1 = typing.TypeVar('OrderByDescending_2_T1')
        OrderByDescending_2_T2 = typing.TypeVar('OrderByDescending_2_T2')
        class OrderByDescending_2(typing.Generic[OrderByDescending_2_T1, OrderByDescending_2_T2]):
            OrderByDescending_2_TSource = Enumerable.OrderByDescending_MethodGroup.OrderByDescending_2_T1
            OrderByDescending_2_TKey = Enumerable.OrderByDescending_MethodGroup.OrderByDescending_2_T2
            @typing.overload
            def __call__(self, source: IEnumerable_1[OrderByDescending_2_TSource], keySelector: Func_2[OrderByDescending_2_TSource, OrderByDescending_2_TKey]) -> IOrderedEnumerable_1[OrderByDescending_2_TSource]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[OrderByDescending_2_TSource], keySelector: Func_2[OrderByDescending_2_TSource, OrderByDescending_2_TKey], comparer: IComparer_1[OrderByDescending_2_TKey]) -> IOrderedEnumerable_1[OrderByDescending_2_TSource]:...


    # Skipped Prepend due to it being static, abstract and generic.

    Prepend : Prepend_MethodGroup
    class Prepend_MethodGroup:
        def __getitem__(self, t:typing.Type[Prepend_1_T1]) -> Prepend_1[Prepend_1_T1]: ...

        Prepend_1_T1 = typing.TypeVar('Prepend_1_T1')
        class Prepend_1(typing.Generic[Prepend_1_T1]):
            Prepend_1_TSource = Enumerable.Prepend_MethodGroup.Prepend_1_T1
            def __call__(self, source: IEnumerable_1[Prepend_1_TSource], element: Prepend_1_TSource) -> IEnumerable_1[Prepend_1_TSource]:...


    # Skipped Repeat due to it being static, abstract and generic.

    Repeat : Repeat_MethodGroup
    class Repeat_MethodGroup:
        def __getitem__(self, t:typing.Type[Repeat_1_T1]) -> Repeat_1[Repeat_1_T1]: ...

        Repeat_1_T1 = typing.TypeVar('Repeat_1_T1')
        class Repeat_1(typing.Generic[Repeat_1_T1]):
            Repeat_1_TResult = Enumerable.Repeat_MethodGroup.Repeat_1_T1
            def __call__(self, element: Repeat_1_TResult, count: int) -> IEnumerable_1[Repeat_1_TResult]:...


    # Skipped Reverse due to it being static, abstract and generic.

    Reverse : Reverse_MethodGroup
    class Reverse_MethodGroup:
        def __getitem__(self, t:typing.Type[Reverse_1_T1]) -> Reverse_1[Reverse_1_T1]: ...

        Reverse_1_T1 = typing.TypeVar('Reverse_1_T1')
        class Reverse_1(typing.Generic[Reverse_1_T1]):
            Reverse_1_TSource = Enumerable.Reverse_MethodGroup.Reverse_1_T1
            def __call__(self, source: IEnumerable_1[Reverse_1_TSource]) -> IEnumerable_1[Reverse_1_TSource]:...


    # Skipped Select due to it being static, abstract and generic.

    Select : Select_MethodGroup
    class Select_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Select_2_T1], typing.Type[Select_2_T2]]) -> Select_2[Select_2_T1, Select_2_T2]: ...

        Select_2_T1 = typing.TypeVar('Select_2_T1')
        Select_2_T2 = typing.TypeVar('Select_2_T2')
        class Select_2(typing.Generic[Select_2_T1, Select_2_T2]):
            Select_2_TSource = Enumerable.Select_MethodGroup.Select_2_T1
            Select_2_TResult = Enumerable.Select_MethodGroup.Select_2_T2
            @typing.overload
            def __call__(self, source: IEnumerable_1[Select_2_TSource], selector: Func_3[Select_2_TSource, int, Select_2_TResult]) -> IEnumerable_1[Select_2_TResult]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Select_2_TSource], selector: Func_2[Select_2_TSource, Select_2_TResult]) -> IEnumerable_1[Select_2_TResult]:...


    # Skipped SelectMany due to it being static, abstract and generic.

    SelectMany : SelectMany_MethodGroup
    class SelectMany_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[SelectMany_2_T1], typing.Type[SelectMany_2_T2]]) -> SelectMany_2[SelectMany_2_T1, SelectMany_2_T2]: ...

        SelectMany_2_T1 = typing.TypeVar('SelectMany_2_T1')
        SelectMany_2_T2 = typing.TypeVar('SelectMany_2_T2')
        class SelectMany_2(typing.Generic[SelectMany_2_T1, SelectMany_2_T2]):
            SelectMany_2_TSource = Enumerable.SelectMany_MethodGroup.SelectMany_2_T1
            SelectMany_2_TResult = Enumerable.SelectMany_MethodGroup.SelectMany_2_T2
            @typing.overload
            def __call__(self, source: IEnumerable_1[SelectMany_2_TSource], selector: Func_3[SelectMany_2_TSource, int, IEnumerable_1[SelectMany_2_TResult]]) -> IEnumerable_1[SelectMany_2_TResult]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[SelectMany_2_TSource], selector: Func_2[SelectMany_2_TSource, IEnumerable_1[SelectMany_2_TResult]]) -> IEnumerable_1[SelectMany_2_TResult]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[SelectMany_3_T1], typing.Type[SelectMany_3_T2], typing.Type[SelectMany_3_T3]]) -> SelectMany_3[SelectMany_3_T1, SelectMany_3_T2, SelectMany_3_T3]: ...

        SelectMany_3_T1 = typing.TypeVar('SelectMany_3_T1')
        SelectMany_3_T2 = typing.TypeVar('SelectMany_3_T2')
        SelectMany_3_T3 = typing.TypeVar('SelectMany_3_T3')
        class SelectMany_3(typing.Generic[SelectMany_3_T1, SelectMany_3_T2, SelectMany_3_T3]):
            SelectMany_3_TSource = Enumerable.SelectMany_MethodGroup.SelectMany_3_T1
            SelectMany_3_TCollection = Enumerable.SelectMany_MethodGroup.SelectMany_3_T2
            SelectMany_3_TResult = Enumerable.SelectMany_MethodGroup.SelectMany_3_T3
            @typing.overload
            def __call__(self, source: IEnumerable_1[SelectMany_3_TSource], collectionSelector: Func_3[SelectMany_3_TSource, int, IEnumerable_1[SelectMany_3_TCollection]], resultSelector: Func_3[SelectMany_3_TSource, SelectMany_3_TCollection, SelectMany_3_TResult]) -> IEnumerable_1[SelectMany_3_TResult]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[SelectMany_3_TSource], collectionSelector: Func_2[SelectMany_3_TSource, IEnumerable_1[SelectMany_3_TCollection]], resultSelector: Func_3[SelectMany_3_TSource, SelectMany_3_TCollection, SelectMany_3_TResult]) -> IEnumerable_1[SelectMany_3_TResult]:...


    # Skipped SequenceEqual due to it being static, abstract and generic.

    SequenceEqual : SequenceEqual_MethodGroup
    class SequenceEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[SequenceEqual_1_T1]) -> SequenceEqual_1[SequenceEqual_1_T1]: ...

        SequenceEqual_1_T1 = typing.TypeVar('SequenceEqual_1_T1')
        class SequenceEqual_1(typing.Generic[SequenceEqual_1_T1]):
            SequenceEqual_1_TSource = Enumerable.SequenceEqual_MethodGroup.SequenceEqual_1_T1
            @typing.overload
            def __call__(self, first: IEnumerable_1[SequenceEqual_1_TSource], second: IEnumerable_1[SequenceEqual_1_TSource]) -> bool:...
            @typing.overload
            def __call__(self, first: IEnumerable_1[SequenceEqual_1_TSource], second: IEnumerable_1[SequenceEqual_1_TSource], comparer: IEqualityComparer_1[SequenceEqual_1_TSource]) -> bool:...


    # Skipped Single due to it being static, abstract and generic.

    Single : Single_MethodGroup
    class Single_MethodGroup:
        def __getitem__(self, t:typing.Type[Single_1_T1]) -> Single_1[Single_1_T1]: ...

        Single_1_T1 = typing.TypeVar('Single_1_T1')
        class Single_1(typing.Generic[Single_1_T1]):
            Single_1_TSource = Enumerable.Single_MethodGroup.Single_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[Single_1_TSource]) -> Single_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Single_1_TSource], predicate: Func_2[Single_1_TSource, bool]) -> Single_1_TSource:...


    # Skipped SingleOrDefault due to it being static, abstract and generic.

    SingleOrDefault : SingleOrDefault_MethodGroup
    class SingleOrDefault_MethodGroup:
        def __getitem__(self, t:typing.Type[SingleOrDefault_1_T1]) -> SingleOrDefault_1[SingleOrDefault_1_T1]: ...

        SingleOrDefault_1_T1 = typing.TypeVar('SingleOrDefault_1_T1')
        class SingleOrDefault_1(typing.Generic[SingleOrDefault_1_T1]):
            SingleOrDefault_1_TSource = Enumerable.SingleOrDefault_MethodGroup.SingleOrDefault_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[SingleOrDefault_1_TSource]) -> SingleOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[SingleOrDefault_1_TSource], predicate: Func_2[SingleOrDefault_1_TSource, bool]) -> SingleOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[SingleOrDefault_1_TSource], defaultValue: SingleOrDefault_1_TSource) -> SingleOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[SingleOrDefault_1_TSource], predicate: Func_2[SingleOrDefault_1_TSource, bool], defaultValue: SingleOrDefault_1_TSource) -> SingleOrDefault_1_TSource:...


    # Skipped Skip due to it being static, abstract and generic.

    Skip : Skip_MethodGroup
    class Skip_MethodGroup:
        def __getitem__(self, t:typing.Type[Skip_1_T1]) -> Skip_1[Skip_1_T1]: ...

        Skip_1_T1 = typing.TypeVar('Skip_1_T1')
        class Skip_1(typing.Generic[Skip_1_T1]):
            Skip_1_TSource = Enumerable.Skip_MethodGroup.Skip_1_T1
            def __call__(self, source: IEnumerable_1[Skip_1_TSource], count: int) -> IEnumerable_1[Skip_1_TSource]:...


    # Skipped SkipLast due to it being static, abstract and generic.

    SkipLast : SkipLast_MethodGroup
    class SkipLast_MethodGroup:
        def __getitem__(self, t:typing.Type[SkipLast_1_T1]) -> SkipLast_1[SkipLast_1_T1]: ...

        SkipLast_1_T1 = typing.TypeVar('SkipLast_1_T1')
        class SkipLast_1(typing.Generic[SkipLast_1_T1]):
            SkipLast_1_TSource = Enumerable.SkipLast_MethodGroup.SkipLast_1_T1
            def __call__(self, source: IEnumerable_1[SkipLast_1_TSource], count: int) -> IEnumerable_1[SkipLast_1_TSource]:...


    # Skipped SkipWhile due to it being static, abstract and generic.

    SkipWhile : SkipWhile_MethodGroup
    class SkipWhile_MethodGroup:
        def __getitem__(self, t:typing.Type[SkipWhile_1_T1]) -> SkipWhile_1[SkipWhile_1_T1]: ...

        SkipWhile_1_T1 = typing.TypeVar('SkipWhile_1_T1')
        class SkipWhile_1(typing.Generic[SkipWhile_1_T1]):
            SkipWhile_1_TSource = Enumerable.SkipWhile_MethodGroup.SkipWhile_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[SkipWhile_1_TSource], predicate: Func_3[SkipWhile_1_TSource, int, bool]) -> IEnumerable_1[SkipWhile_1_TSource]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[SkipWhile_1_TSource], predicate: Func_2[SkipWhile_1_TSource, bool]) -> IEnumerable_1[SkipWhile_1_TSource]:...


    # Skipped Sum due to it being static, abstract and generic.

    Sum : Sum_MethodGroup
    class Sum_MethodGroup:
        def __getitem__(self, t:typing.Type[Sum_1_T1]) -> Sum_1[Sum_1_T1]: ...

        Sum_1_T1 = typing.TypeVar('Sum_1_T1')
        class Sum_1(typing.Generic[Sum_1_T1]):
            Sum_1_TSource = Enumerable.Sum_MethodGroup.Sum_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[Sum_1_TSource], selector: Func_2[Sum_1_TSource, float]) -> float:...
            # Method Sum(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: IEnumerable_1[Sum_1_TSource], selector: Func_2[Sum_1_TSource, int]) -> int:...
            # Method Sum(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: IEnumerable_1[Sum_1_TSource], selector: Func_2[Sum_1_TSource, Decimal]) -> Decimal:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Sum_1_TSource], selector: Func_2[Sum_1_TSource, typing.Optional[int]]) -> typing.Optional[int]:...
            # Method Sum(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            # Method Sum(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            # Method Sum(source : IEnumerable`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: IEnumerable_1[Sum_1_TSource], selector: Func_2[Sum_1_TSource, typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

        @typing.overload
        def __call__(self, source: IEnumerable_1[float]) -> float:...
        # Method Sum(source : IEnumerable`1) was skipped since it collides with above method
        # Method Sum(source : IEnumerable`1) was skipped since it collides with above method
        # Method Sum(source : IEnumerable`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: IEnumerable_1[Decimal]) -> Decimal:...
        @typing.overload
        def __call__(self, source: IEnumerable_1[typing.Optional[int]]) -> typing.Optional[int]:...
        # Method Sum(source : IEnumerable`1) was skipped since it collides with above method
        # Method Sum(source : IEnumerable`1) was skipped since it collides with above method
        # Method Sum(source : IEnumerable`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: IEnumerable_1[typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

    # Skipped Take due to it being static, abstract and generic.

    Take : Take_MethodGroup
    class Take_MethodGroup:
        def __getitem__(self, t:typing.Type[Take_1_T1]) -> Take_1[Take_1_T1]: ...

        Take_1_T1 = typing.TypeVar('Take_1_T1')
        class Take_1(typing.Generic[Take_1_T1]):
            Take_1_TSource = Enumerable.Take_MethodGroup.Take_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[Take_1_TSource], count: int) -> IEnumerable_1[Take_1_TSource]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Take_1_TSource], range: Range) -> IEnumerable_1[Take_1_TSource]:...


    # Skipped TakeLast due to it being static, abstract and generic.

    TakeLast : TakeLast_MethodGroup
    class TakeLast_MethodGroup:
        def __getitem__(self, t:typing.Type[TakeLast_1_T1]) -> TakeLast_1[TakeLast_1_T1]: ...

        TakeLast_1_T1 = typing.TypeVar('TakeLast_1_T1')
        class TakeLast_1(typing.Generic[TakeLast_1_T1]):
            TakeLast_1_TSource = Enumerable.TakeLast_MethodGroup.TakeLast_1_T1
            def __call__(self, source: IEnumerable_1[TakeLast_1_TSource], count: int) -> IEnumerable_1[TakeLast_1_TSource]:...


    # Skipped TakeWhile due to it being static, abstract and generic.

    TakeWhile : TakeWhile_MethodGroup
    class TakeWhile_MethodGroup:
        def __getitem__(self, t:typing.Type[TakeWhile_1_T1]) -> TakeWhile_1[TakeWhile_1_T1]: ...

        TakeWhile_1_T1 = typing.TypeVar('TakeWhile_1_T1')
        class TakeWhile_1(typing.Generic[TakeWhile_1_T1]):
            TakeWhile_1_TSource = Enumerable.TakeWhile_MethodGroup.TakeWhile_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[TakeWhile_1_TSource], predicate: Func_3[TakeWhile_1_TSource, int, bool]) -> IEnumerable_1[TakeWhile_1_TSource]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[TakeWhile_1_TSource], predicate: Func_2[TakeWhile_1_TSource, bool]) -> IEnumerable_1[TakeWhile_1_TSource]:...


    # Skipped ThenBy due to it being static, abstract and generic.

    ThenBy : ThenBy_MethodGroup
    class ThenBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[ThenBy_2_T1], typing.Type[ThenBy_2_T2]]) -> ThenBy_2[ThenBy_2_T1, ThenBy_2_T2]: ...

        ThenBy_2_T1 = typing.TypeVar('ThenBy_2_T1')
        ThenBy_2_T2 = typing.TypeVar('ThenBy_2_T2')
        class ThenBy_2(typing.Generic[ThenBy_2_T1, ThenBy_2_T2]):
            ThenBy_2_TSource = Enumerable.ThenBy_MethodGroup.ThenBy_2_T1
            ThenBy_2_TKey = Enumerable.ThenBy_MethodGroup.ThenBy_2_T2
            @typing.overload
            def __call__(self, source: IOrderedEnumerable_1[ThenBy_2_TSource], keySelector: Func_2[ThenBy_2_TSource, ThenBy_2_TKey]) -> IOrderedEnumerable_1[ThenBy_2_TSource]:...
            @typing.overload
            def __call__(self, source: IOrderedEnumerable_1[ThenBy_2_TSource], keySelector: Func_2[ThenBy_2_TSource, ThenBy_2_TKey], comparer: IComparer_1[ThenBy_2_TKey]) -> IOrderedEnumerable_1[ThenBy_2_TSource]:...


    # Skipped ThenByDescending due to it being static, abstract and generic.

    ThenByDescending : ThenByDescending_MethodGroup
    class ThenByDescending_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[ThenByDescending_2_T1], typing.Type[ThenByDescending_2_T2]]) -> ThenByDescending_2[ThenByDescending_2_T1, ThenByDescending_2_T2]: ...

        ThenByDescending_2_T1 = typing.TypeVar('ThenByDescending_2_T1')
        ThenByDescending_2_T2 = typing.TypeVar('ThenByDescending_2_T2')
        class ThenByDescending_2(typing.Generic[ThenByDescending_2_T1, ThenByDescending_2_T2]):
            ThenByDescending_2_TSource = Enumerable.ThenByDescending_MethodGroup.ThenByDescending_2_T1
            ThenByDescending_2_TKey = Enumerable.ThenByDescending_MethodGroup.ThenByDescending_2_T2
            @typing.overload
            def __call__(self, source: IOrderedEnumerable_1[ThenByDescending_2_TSource], keySelector: Func_2[ThenByDescending_2_TSource, ThenByDescending_2_TKey]) -> IOrderedEnumerable_1[ThenByDescending_2_TSource]:...
            @typing.overload
            def __call__(self, source: IOrderedEnumerable_1[ThenByDescending_2_TSource], keySelector: Func_2[ThenByDescending_2_TSource, ThenByDescending_2_TKey], comparer: IComparer_1[ThenByDescending_2_TKey]) -> IOrderedEnumerable_1[ThenByDescending_2_TSource]:...


    # Skipped ToArray due to it being static, abstract and generic.

    ToArray : ToArray_MethodGroup
    class ToArray_MethodGroup:
        def __getitem__(self, t:typing.Type[ToArray_1_T1]) -> ToArray_1[ToArray_1_T1]: ...

        ToArray_1_T1 = typing.TypeVar('ToArray_1_T1')
        class ToArray_1(typing.Generic[ToArray_1_T1]):
            ToArray_1_TSource = Enumerable.ToArray_MethodGroup.ToArray_1_T1
            def __call__(self, source: IEnumerable_1[ToArray_1_TSource]) -> Array_1[ToArray_1_TSource]:...


    # Skipped ToDictionary due to it being static, abstract and generic.

    ToDictionary : ToDictionary_MethodGroup
    class ToDictionary_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToDictionary_2_T1], typing.Type[ToDictionary_2_T2]]) -> ToDictionary_2[ToDictionary_2_T1, ToDictionary_2_T2]: ...

        ToDictionary_2_T1 = typing.TypeVar('ToDictionary_2_T1')
        ToDictionary_2_T2 = typing.TypeVar('ToDictionary_2_T2')
        class ToDictionary_2(typing.Generic[ToDictionary_2_T1, ToDictionary_2_T2]):
            ToDictionary_2_TSource = Enumerable.ToDictionary_MethodGroup.ToDictionary_2_T1
            ToDictionary_2_TKey = Enumerable.ToDictionary_MethodGroup.ToDictionary_2_T2
            @typing.overload
            def __call__(self, source: IEnumerable_1[ToDictionary_2_TSource], keySelector: Func_2[ToDictionary_2_TSource, ToDictionary_2_TKey]) -> Dictionary_2[ToDictionary_2_TKey, ToDictionary_2_TSource]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[ToDictionary_2_TSource], keySelector: Func_2[ToDictionary_2_TSource, ToDictionary_2_TKey], comparer: IEqualityComparer_1[ToDictionary_2_TKey]) -> Dictionary_2[ToDictionary_2_TKey, ToDictionary_2_TSource]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToDictionary_3_T1], typing.Type[ToDictionary_3_T2], typing.Type[ToDictionary_3_T3]]) -> ToDictionary_3[ToDictionary_3_T1, ToDictionary_3_T2, ToDictionary_3_T3]: ...

        ToDictionary_3_T1 = typing.TypeVar('ToDictionary_3_T1')
        ToDictionary_3_T2 = typing.TypeVar('ToDictionary_3_T2')
        ToDictionary_3_T3 = typing.TypeVar('ToDictionary_3_T3')
        class ToDictionary_3(typing.Generic[ToDictionary_3_T1, ToDictionary_3_T2, ToDictionary_3_T3]):
            ToDictionary_3_TSource = Enumerable.ToDictionary_MethodGroup.ToDictionary_3_T1
            ToDictionary_3_TKey = Enumerable.ToDictionary_MethodGroup.ToDictionary_3_T2
            ToDictionary_3_TElement = Enumerable.ToDictionary_MethodGroup.ToDictionary_3_T3
            @typing.overload
            def __call__(self, source: IEnumerable_1[ToDictionary_3_TSource], keySelector: Func_2[ToDictionary_3_TSource, ToDictionary_3_TKey], elementSelector: Func_2[ToDictionary_3_TSource, ToDictionary_3_TElement]) -> Dictionary_2[ToDictionary_3_TKey, ToDictionary_3_TElement]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[ToDictionary_3_TSource], keySelector: Func_2[ToDictionary_3_TSource, ToDictionary_3_TKey], elementSelector: Func_2[ToDictionary_3_TSource, ToDictionary_3_TElement], comparer: IEqualityComparer_1[ToDictionary_3_TKey]) -> Dictionary_2[ToDictionary_3_TKey, ToDictionary_3_TElement]:...


    # Skipped ToHashSet due to it being static, abstract and generic.

    ToHashSet : ToHashSet_MethodGroup
    class ToHashSet_MethodGroup:
        def __getitem__(self, t:typing.Type[ToHashSet_1_T1]) -> ToHashSet_1[ToHashSet_1_T1]: ...

        ToHashSet_1_T1 = typing.TypeVar('ToHashSet_1_T1')
        class ToHashSet_1(typing.Generic[ToHashSet_1_T1]):
            ToHashSet_1_TSource = Enumerable.ToHashSet_MethodGroup.ToHashSet_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[ToHashSet_1_TSource]) -> HashSet_1[ToHashSet_1_TSource]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[ToHashSet_1_TSource], comparer: IEqualityComparer_1[ToHashSet_1_TSource]) -> HashSet_1[ToHashSet_1_TSource]:...


    # Skipped ToList due to it being static, abstract and generic.

    ToList : ToList_MethodGroup
    class ToList_MethodGroup:
        def __getitem__(self, t:typing.Type[ToList_1_T1]) -> ToList_1[ToList_1_T1]: ...

        ToList_1_T1 = typing.TypeVar('ToList_1_T1')
        class ToList_1(typing.Generic[ToList_1_T1]):
            ToList_1_TSource = Enumerable.ToList_MethodGroup.ToList_1_T1
            def __call__(self, source: IEnumerable_1[ToList_1_TSource]) -> List_1[ToList_1_TSource]:...


    # Skipped ToLookup due to it being static, abstract and generic.

    ToLookup : ToLookup_MethodGroup
    class ToLookup_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToLookup_2_T1], typing.Type[ToLookup_2_T2]]) -> ToLookup_2[ToLookup_2_T1, ToLookup_2_T2]: ...

        ToLookup_2_T1 = typing.TypeVar('ToLookup_2_T1')
        ToLookup_2_T2 = typing.TypeVar('ToLookup_2_T2')
        class ToLookup_2(typing.Generic[ToLookup_2_T1, ToLookup_2_T2]):
            ToLookup_2_TSource = Enumerable.ToLookup_MethodGroup.ToLookup_2_T1
            ToLookup_2_TKey = Enumerable.ToLookup_MethodGroup.ToLookup_2_T2
            @typing.overload
            def __call__(self, source: IEnumerable_1[ToLookup_2_TSource], keySelector: Func_2[ToLookup_2_TSource, ToLookup_2_TKey]) -> ILookup_2[ToLookup_2_TKey, ToLookup_2_TSource]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[ToLookup_2_TSource], keySelector: Func_2[ToLookup_2_TSource, ToLookup_2_TKey], comparer: IEqualityComparer_1[ToLookup_2_TKey]) -> ILookup_2[ToLookup_2_TKey, ToLookup_2_TSource]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToLookup_3_T1], typing.Type[ToLookup_3_T2], typing.Type[ToLookup_3_T3]]) -> ToLookup_3[ToLookup_3_T1, ToLookup_3_T2, ToLookup_3_T3]: ...

        ToLookup_3_T1 = typing.TypeVar('ToLookup_3_T1')
        ToLookup_3_T2 = typing.TypeVar('ToLookup_3_T2')
        ToLookup_3_T3 = typing.TypeVar('ToLookup_3_T3')
        class ToLookup_3(typing.Generic[ToLookup_3_T1, ToLookup_3_T2, ToLookup_3_T3]):
            ToLookup_3_TSource = Enumerable.ToLookup_MethodGroup.ToLookup_3_T1
            ToLookup_3_TKey = Enumerable.ToLookup_MethodGroup.ToLookup_3_T2
            ToLookup_3_TElement = Enumerable.ToLookup_MethodGroup.ToLookup_3_T3
            @typing.overload
            def __call__(self, source: IEnumerable_1[ToLookup_3_TSource], keySelector: Func_2[ToLookup_3_TSource, ToLookup_3_TKey], elementSelector: Func_2[ToLookup_3_TSource, ToLookup_3_TElement]) -> ILookup_2[ToLookup_3_TKey, ToLookup_3_TElement]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[ToLookup_3_TSource], keySelector: Func_2[ToLookup_3_TSource, ToLookup_3_TKey], elementSelector: Func_2[ToLookup_3_TSource, ToLookup_3_TElement], comparer: IEqualityComparer_1[ToLookup_3_TKey]) -> ILookup_2[ToLookup_3_TKey, ToLookup_3_TElement]:...


    # Skipped TryGetNonEnumeratedCount due to it being static, abstract and generic.

    TryGetNonEnumeratedCount : TryGetNonEnumeratedCount_MethodGroup
    class TryGetNonEnumeratedCount_MethodGroup:
        def __getitem__(self, t:typing.Type[TryGetNonEnumeratedCount_1_T1]) -> TryGetNonEnumeratedCount_1[TryGetNonEnumeratedCount_1_T1]: ...

        TryGetNonEnumeratedCount_1_T1 = typing.TypeVar('TryGetNonEnumeratedCount_1_T1')
        class TryGetNonEnumeratedCount_1(typing.Generic[TryGetNonEnumeratedCount_1_T1]):
            TryGetNonEnumeratedCount_1_TSource = Enumerable.TryGetNonEnumeratedCount_MethodGroup.TryGetNonEnumeratedCount_1_T1
            def __call__(self, source: IEnumerable_1[TryGetNonEnumeratedCount_1_TSource], count: clr.Reference[int]) -> bool:...


    # Skipped Union due to it being static, abstract and generic.

    Union : Union_MethodGroup
    class Union_MethodGroup:
        def __getitem__(self, t:typing.Type[Union_1_T1]) -> Union_1[Union_1_T1]: ...

        Union_1_T1 = typing.TypeVar('Union_1_T1')
        class Union_1(typing.Generic[Union_1_T1]):
            Union_1_TSource = Enumerable.Union_MethodGroup.Union_1_T1
            @typing.overload
            def __call__(self, first: IEnumerable_1[Union_1_TSource], second: IEnumerable_1[Union_1_TSource]) -> IEnumerable_1[Union_1_TSource]:...
            @typing.overload
            def __call__(self, first: IEnumerable_1[Union_1_TSource], second: IEnumerable_1[Union_1_TSource], comparer: IEqualityComparer_1[Union_1_TSource]) -> IEnumerable_1[Union_1_TSource]:...


    # Skipped UnionBy due to it being static, abstract and generic.

    UnionBy : UnionBy_MethodGroup
    class UnionBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[UnionBy_2_T1], typing.Type[UnionBy_2_T2]]) -> UnionBy_2[UnionBy_2_T1, UnionBy_2_T2]: ...

        UnionBy_2_T1 = typing.TypeVar('UnionBy_2_T1')
        UnionBy_2_T2 = typing.TypeVar('UnionBy_2_T2')
        class UnionBy_2(typing.Generic[UnionBy_2_T1, UnionBy_2_T2]):
            UnionBy_2_TSource = Enumerable.UnionBy_MethodGroup.UnionBy_2_T1
            UnionBy_2_TKey = Enumerable.UnionBy_MethodGroup.UnionBy_2_T2
            @typing.overload
            def __call__(self, first: IEnumerable_1[UnionBy_2_TSource], second: IEnumerable_1[UnionBy_2_TSource], keySelector: Func_2[UnionBy_2_TSource, UnionBy_2_TKey]) -> IEnumerable_1[UnionBy_2_TSource]:...
            @typing.overload
            def __call__(self, first: IEnumerable_1[UnionBy_2_TSource], second: IEnumerable_1[UnionBy_2_TSource], keySelector: Func_2[UnionBy_2_TSource, UnionBy_2_TKey], comparer: IEqualityComparer_1[UnionBy_2_TKey]) -> IEnumerable_1[UnionBy_2_TSource]:...


    # Skipped Where due to it being static, abstract and generic.

    Where : Where_MethodGroup
    class Where_MethodGroup:
        def __getitem__(self, t:typing.Type[Where_1_T1]) -> Where_1[Where_1_T1]: ...

        Where_1_T1 = typing.TypeVar('Where_1_T1')
        class Where_1(typing.Generic[Where_1_T1]):
            Where_1_TSource = Enumerable.Where_MethodGroup.Where_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[Where_1_TSource], predicate: Func_3[Where_1_TSource, int, bool]) -> IEnumerable_1[Where_1_TSource]:...
            @typing.overload
            def __call__(self, source: IEnumerable_1[Where_1_TSource], predicate: Func_2[Where_1_TSource, bool]) -> IEnumerable_1[Where_1_TSource]:...


    # Skipped Zip due to it being static, abstract and generic.

    Zip : Zip_MethodGroup
    class Zip_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Zip_2_T1], typing.Type[Zip_2_T2]]) -> Zip_2[Zip_2_T1, Zip_2_T2]: ...

        Zip_2_T1 = typing.TypeVar('Zip_2_T1')
        Zip_2_T2 = typing.TypeVar('Zip_2_T2')
        class Zip_2(typing.Generic[Zip_2_T1, Zip_2_T2]):
            Zip_2_TFirst = Enumerable.Zip_MethodGroup.Zip_2_T1
            Zip_2_TSecond = Enumerable.Zip_MethodGroup.Zip_2_T2
            def __call__(self, first: IEnumerable_1[Zip_2_TFirst], second: IEnumerable_1[Zip_2_TSecond]) -> IEnumerable_1[ValueTuple_2[Zip_2_TFirst, Zip_2_TSecond]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Zip_3_T1], typing.Type[Zip_3_T2], typing.Type[Zip_3_T3]]) -> Zip_3[Zip_3_T1, Zip_3_T2, Zip_3_T3]: ...

        Zip_3_T1 = typing.TypeVar('Zip_3_T1')
        Zip_3_T2 = typing.TypeVar('Zip_3_T2')
        Zip_3_T3 = typing.TypeVar('Zip_3_T3')
        class Zip_3(typing.Generic[Zip_3_T1, Zip_3_T2, Zip_3_T3]):
            Zip_3_TFirst = Enumerable.Zip_MethodGroup.Zip_3_T1
            Zip_3_TSecond = Enumerable.Zip_MethodGroup.Zip_3_T2
            Zip_3_TResult = Enumerable.Zip_MethodGroup.Zip_3_T3
            Zip_3_TThird = Enumerable.Zip_MethodGroup.Zip_3_T3
            @typing.overload
            def __call__(self, first: IEnumerable_1[Zip_3_TFirst], second: IEnumerable_1[Zip_3_TSecond], resultSelector: Func_3[Zip_3_TFirst, Zip_3_TSecond, Zip_3_TResult]) -> IEnumerable_1[Zip_3_TResult]:...
            @typing.overload
            def __call__(self, first: IEnumerable_1[Zip_3_TFirst], second: IEnumerable_1[Zip_3_TSecond], third: IEnumerable_1[Zip_3_TThird]) -> IEnumerable_1[ValueTuple_3[Zip_3_TFirst, Zip_3_TSecond, Zip_3_TThird]]:...




class EnumerableExecutor_GenericClasses(abc.ABCMeta):
    Generic_EnumerableExecutor_GenericClasses_EnumerableExecutor_1_T = typing.TypeVar('Generic_EnumerableExecutor_GenericClasses_EnumerableExecutor_1_T')
    def __getitem__(self, types : typing.Type[Generic_EnumerableExecutor_GenericClasses_EnumerableExecutor_1_T]) -> typing.Type[EnumerableExecutor_1[Generic_EnumerableExecutor_GenericClasses_EnumerableExecutor_1_T]]: ...

class EnumerableExecutor(EnumerableExecutor_0, metaclass =EnumerableExecutor_GenericClasses): ...

class EnumerableExecutor_0(abc.ABC):
    pass


EnumerableExecutor_1_T = typing.TypeVar('EnumerableExecutor_1_T')
class EnumerableExecutor_1(typing.Generic[EnumerableExecutor_1_T], EnumerableExecutor_0):
    def __init__(self, expression: Expression) -> None: ...


class EnumerableQuery_GenericClasses(abc.ABCMeta):
    Generic_EnumerableQuery_GenericClasses_EnumerableQuery_1_T = typing.TypeVar('Generic_EnumerableQuery_GenericClasses_EnumerableQuery_1_T')
    def __getitem__(self, types : typing.Type[Generic_EnumerableQuery_GenericClasses_EnumerableQuery_1_T]) -> typing.Type[EnumerableQuery_1[Generic_EnumerableQuery_GenericClasses_EnumerableQuery_1_T]]: ...

class EnumerableQuery(EnumerableQuery_0, metaclass =EnumerableQuery_GenericClasses): ...

class EnumerableQuery_0(abc.ABC):
    pass


EnumerableQuery_1_T = typing.TypeVar('EnumerableQuery_1_T')
class EnumerableQuery_1(typing.Generic[EnumerableQuery_1_T], EnumerableQuery_0, IOrderedQueryable_1[EnumerableQuery_1_T], IQueryProvider):
    @typing.overload
    def __init__(self, enumerable: IEnumerable_1[EnumerableQuery_1_T]) -> None: ...
    @typing.overload
    def __init__(self, expression: Expression) -> None: ...
    def ToString(self) -> str: ...


class Grouping_GenericClasses(abc.ABCMeta):
    Generic_Grouping_GenericClasses_Grouping_2_TKey = typing.TypeVar('Generic_Grouping_GenericClasses_Grouping_2_TKey')
    Generic_Grouping_GenericClasses_Grouping_2_TElement = typing.TypeVar('Generic_Grouping_GenericClasses_Grouping_2_TElement')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Grouping_GenericClasses_Grouping_2_TKey], typing.Type[Generic_Grouping_GenericClasses_Grouping_2_TElement]]) -> typing.Type[Grouping_2[Generic_Grouping_GenericClasses_Grouping_2_TKey, Generic_Grouping_GenericClasses_Grouping_2_TElement]]: ...

Grouping : Grouping_GenericClasses

Grouping_2_TKey = typing.TypeVar('Grouping_2_TKey')
Grouping_2_TElement = typing.TypeVar('Grouping_2_TElement')
class Grouping_2(typing.Generic[Grouping_2_TKey, Grouping_2_TElement], IList_1[Grouping_2_TElement], IGrouping_2[Grouping_2_TKey, Grouping_2_TElement]):
    @property
    def Key(self) -> Grouping_2_TKey: ...
    def GetEnumerator(self) -> IEnumerator_1[Grouping_2_TElement]: ...


class IGrouping_GenericClasses(abc.ABCMeta):
    Generic_IGrouping_GenericClasses_IGrouping_2_TKey = typing.TypeVar('Generic_IGrouping_GenericClasses_IGrouping_2_TKey')
    Generic_IGrouping_GenericClasses_IGrouping_2_TElement = typing.TypeVar('Generic_IGrouping_GenericClasses_IGrouping_2_TElement')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IGrouping_GenericClasses_IGrouping_2_TKey], typing.Type[Generic_IGrouping_GenericClasses_IGrouping_2_TElement]]) -> typing.Type[IGrouping_2[Generic_IGrouping_GenericClasses_IGrouping_2_TKey, Generic_IGrouping_GenericClasses_IGrouping_2_TElement]]: ...

IGrouping : IGrouping_GenericClasses

IGrouping_2_TKey = typing.TypeVar('IGrouping_2_TKey', covariant=True)
IGrouping_2_TElement = typing.TypeVar('IGrouping_2_TElement', covariant=True)
class IGrouping_2(typing.Generic[IGrouping_2_TKey, IGrouping_2_TElement], IEnumerable_1[IGrouping_2_TElement], typing.Protocol):
    @property
    def Key(self) -> IGrouping_2_TKey: ...


class ILookup_GenericClasses(abc.ABCMeta):
    Generic_ILookup_GenericClasses_ILookup_2_TKey = typing.TypeVar('Generic_ILookup_GenericClasses_ILookup_2_TKey')
    Generic_ILookup_GenericClasses_ILookup_2_TElement = typing.TypeVar('Generic_ILookup_GenericClasses_ILookup_2_TElement')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ILookup_GenericClasses_ILookup_2_TKey], typing.Type[Generic_ILookup_GenericClasses_ILookup_2_TElement]]) -> typing.Type[ILookup_2[Generic_ILookup_GenericClasses_ILookup_2_TKey, Generic_ILookup_GenericClasses_ILookup_2_TElement]]: ...

ILookup : ILookup_GenericClasses

ILookup_2_TKey = typing.TypeVar('ILookup_2_TKey')
ILookup_2_TElement = typing.TypeVar('ILookup_2_TElement')
class ILookup_2(typing.Generic[ILookup_2_TKey, ILookup_2_TElement], IEnumerable_1[IGrouping_2[ILookup_2_TKey, ILookup_2_TElement]], typing.Protocol):
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> IEnumerable_1[ILookup_2_TElement]: ...
    @abc.abstractmethod
    def Contains(self, key: ILookup_2_TKey) -> bool: ...


class IOrderedEnumerable_GenericClasses(abc.ABCMeta):
    Generic_IOrderedEnumerable_GenericClasses_IOrderedEnumerable_1_TElement = typing.TypeVar('Generic_IOrderedEnumerable_GenericClasses_IOrderedEnumerable_1_TElement')
    def __getitem__(self, types : typing.Type[Generic_IOrderedEnumerable_GenericClasses_IOrderedEnumerable_1_TElement]) -> typing.Type[IOrderedEnumerable_1[Generic_IOrderedEnumerable_GenericClasses_IOrderedEnumerable_1_TElement]]: ...

IOrderedEnumerable : IOrderedEnumerable_GenericClasses

IOrderedEnumerable_1_TElement = typing.TypeVar('IOrderedEnumerable_1_TElement', covariant=True)
class IOrderedEnumerable_1(typing.Generic[IOrderedEnumerable_1_TElement], IEnumerable_1[IOrderedEnumerable_1_TElement], typing.Protocol):
    # Skipped CreateOrderedEnumerable due to it being static, abstract and generic.

    CreateOrderedEnumerable : CreateOrderedEnumerable_MethodGroup[IOrderedEnumerable_1_TElement]
    CreateOrderedEnumerable_MethodGroup_IOrderedEnumerable_1_TElement = typing.TypeVar('CreateOrderedEnumerable_MethodGroup_IOrderedEnumerable_1_TElement', covariant=True)
    class CreateOrderedEnumerable_MethodGroup(typing.Generic[CreateOrderedEnumerable_MethodGroup_IOrderedEnumerable_1_TElement]):
        CreateOrderedEnumerable_MethodGroup_IOrderedEnumerable_1_TElement = IOrderedEnumerable_1.CreateOrderedEnumerable_MethodGroup_IOrderedEnumerable_1_TElement
        def __getitem__(self, t:typing.Type[CreateOrderedEnumerable_1_T1]) -> CreateOrderedEnumerable_1[CreateOrderedEnumerable_MethodGroup_IOrderedEnumerable_1_TElement, CreateOrderedEnumerable_1_T1]: ...

        CreateOrderedEnumerable_1_IOrderedEnumerable_1_TElement = typing.TypeVar('CreateOrderedEnumerable_1_IOrderedEnumerable_1_TElement', covariant=True)
        CreateOrderedEnumerable_1_T1 = typing.TypeVar('CreateOrderedEnumerable_1_T1')
        class CreateOrderedEnumerable_1(typing.Generic[CreateOrderedEnumerable_1_IOrderedEnumerable_1_TElement, CreateOrderedEnumerable_1_T1]):
            CreateOrderedEnumerable_1_IOrderedEnumerable_1_TElement = IOrderedEnumerable_1.CreateOrderedEnumerable_MethodGroup.CreateOrderedEnumerable_1_IOrderedEnumerable_1_TElement
            CreateOrderedEnumerable_1_TKey = IOrderedEnumerable_1.CreateOrderedEnumerable_MethodGroup.CreateOrderedEnumerable_1_T1
            def __call__(self, keySelector: Func_2[CreateOrderedEnumerable_1_IOrderedEnumerable_1_TElement, CreateOrderedEnumerable_1_TKey], comparer: IComparer_1[CreateOrderedEnumerable_1_TKey], descending: bool) -> IOrderedEnumerable_1[CreateOrderedEnumerable_1_IOrderedEnumerable_1_TElement]:...




class IOrderedQueryable_GenericClasses(abc.ABCMeta):
    Generic_IOrderedQueryable_GenericClasses_IOrderedQueryable_1_T = typing.TypeVar('Generic_IOrderedQueryable_GenericClasses_IOrderedQueryable_1_T')
    def __getitem__(self, types : typing.Type[Generic_IOrderedQueryable_GenericClasses_IOrderedQueryable_1_T]) -> typing.Type[IOrderedQueryable_1[Generic_IOrderedQueryable_GenericClasses_IOrderedQueryable_1_T]]: ...

class IOrderedQueryable(IOrderedQueryable_0, metaclass =IOrderedQueryable_GenericClasses): ...

class IOrderedQueryable_0(IQueryable_0, typing.Protocol):
    pass


IOrderedQueryable_1_T = typing.TypeVar('IOrderedQueryable_1_T', covariant=True)
class IOrderedQueryable_1(typing.Generic[IOrderedQueryable_1_T], IOrderedQueryable_0, IQueryable_1[IOrderedQueryable_1_T], typing.Protocol):
    pass


class IQueryable_GenericClasses(abc.ABCMeta):
    Generic_IQueryable_GenericClasses_IQueryable_1_T = typing.TypeVar('Generic_IQueryable_GenericClasses_IQueryable_1_T')
    def __getitem__(self, types : typing.Type[Generic_IQueryable_GenericClasses_IQueryable_1_T]) -> typing.Type[IQueryable_1[Generic_IQueryable_GenericClasses_IQueryable_1_T]]: ...

class IQueryable(IQueryable_0, metaclass =IQueryable_GenericClasses): ...

class IQueryable_0(IEnumerable, typing.Protocol):
    @property
    def ElementType(self) -> typing.Type[typing.Any]: ...
    @property
    def Expression(self) -> Expression: ...
    @property
    def Provider(self) -> IQueryProvider: ...


IQueryable_1_T = typing.TypeVar('IQueryable_1_T', covariant=True)
class IQueryable_1(typing.Generic[IQueryable_1_T], IQueryable_0, IEnumerable_1[IQueryable_1_T], typing.Protocol):
    pass


class IQueryProvider(typing.Protocol):
    # Skipped CreateQuery due to it being static, abstract and generic.

    CreateQuery : CreateQuery_MethodGroup
    class CreateQuery_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateQuery_1_T1]) -> CreateQuery_1[CreateQuery_1_T1]: ...

        CreateQuery_1_T1 = typing.TypeVar('CreateQuery_1_T1')
        class CreateQuery_1(typing.Generic[CreateQuery_1_T1]):
            CreateQuery_1_TElement = IQueryProvider.CreateQuery_MethodGroup.CreateQuery_1_T1
            def __call__(self, expression: Expression) -> IQueryable_1[CreateQuery_1_TElement]:...

        def __call__(self, expression: Expression) -> IQueryable:...

    # Skipped Execute due to it being static, abstract and generic.

    Execute : Execute_MethodGroup
    class Execute_MethodGroup:
        def __getitem__(self, t:typing.Type[Execute_1_T1]) -> Execute_1[Execute_1_T1]: ...

        Execute_1_T1 = typing.TypeVar('Execute_1_T1')
        class Execute_1(typing.Generic[Execute_1_T1]):
            Execute_1_TResult = IQueryProvider.Execute_MethodGroup.Execute_1_T1
            def __call__(self, expression: Expression) -> Execute_1_TResult:...

        def __call__(self, expression: Expression) -> typing.Any:...



class Lookup_GenericClasses(abc.ABCMeta):
    Generic_Lookup_GenericClasses_Lookup_2_TKey = typing.TypeVar('Generic_Lookup_GenericClasses_Lookup_2_TKey')
    Generic_Lookup_GenericClasses_Lookup_2_TElement = typing.TypeVar('Generic_Lookup_GenericClasses_Lookup_2_TElement')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Lookup_GenericClasses_Lookup_2_TKey], typing.Type[Generic_Lookup_GenericClasses_Lookup_2_TElement]]) -> typing.Type[Lookup_2[Generic_Lookup_GenericClasses_Lookup_2_TKey, Generic_Lookup_GenericClasses_Lookup_2_TElement]]: ...

Lookup : Lookup_GenericClasses

Lookup_2_TKey = typing.TypeVar('Lookup_2_TKey')
Lookup_2_TElement = typing.TypeVar('Lookup_2_TElement')
class Lookup_2(typing.Generic[Lookup_2_TKey, Lookup_2_TElement], ILookup_2[Lookup_2_TKey, Lookup_2_TElement]):
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> IEnumerable_1[Lookup_2_TElement]: ...
    def Contains(self, key: Lookup_2_TKey) -> bool: ...
    def GetEnumerator(self) -> IEnumerator_1[IGrouping_2[Lookup_2_TKey, Lookup_2_TElement]]: ...
    # Skipped ApplyResultSelector due to it being static, abstract and generic.

    ApplyResultSelector : ApplyResultSelector_MethodGroup[Lookup_2_TKey, Lookup_2_TElement]
    ApplyResultSelector_MethodGroup_Lookup_2_TKey = typing.TypeVar('ApplyResultSelector_MethodGroup_Lookup_2_TKey')
    ApplyResultSelector_MethodGroup_Lookup_2_TElement = typing.TypeVar('ApplyResultSelector_MethodGroup_Lookup_2_TElement')
    class ApplyResultSelector_MethodGroup(typing.Generic[ApplyResultSelector_MethodGroup_Lookup_2_TKey, ApplyResultSelector_MethodGroup_Lookup_2_TElement]):
        ApplyResultSelector_MethodGroup_Lookup_2_TKey = Lookup_2.ApplyResultSelector_MethodGroup_Lookup_2_TKey
        ApplyResultSelector_MethodGroup_Lookup_2_TElement = Lookup_2.ApplyResultSelector_MethodGroup_Lookup_2_TElement
        def __getitem__(self, t:typing.Type[ApplyResultSelector_1_T1]) -> ApplyResultSelector_1[ApplyResultSelector_MethodGroup_Lookup_2_TKey, ApplyResultSelector_MethodGroup_Lookup_2_TElement, ApplyResultSelector_1_T1]: ...

        ApplyResultSelector_1_Lookup_2_TKey = typing.TypeVar('ApplyResultSelector_1_Lookup_2_TKey')
        ApplyResultSelector_1_Lookup_2_TElement = typing.TypeVar('ApplyResultSelector_1_Lookup_2_TElement')
        ApplyResultSelector_1_T1 = typing.TypeVar('ApplyResultSelector_1_T1')
        class ApplyResultSelector_1(typing.Generic[ApplyResultSelector_1_Lookup_2_TKey, ApplyResultSelector_1_Lookup_2_TElement, ApplyResultSelector_1_T1]):
            ApplyResultSelector_1_Lookup_2_TKey = Lookup_2.ApplyResultSelector_MethodGroup.ApplyResultSelector_1_Lookup_2_TKey
            ApplyResultSelector_1_Lookup_2_TElement = Lookup_2.ApplyResultSelector_MethodGroup.ApplyResultSelector_1_Lookup_2_TElement
            ApplyResultSelector_1_TResult = Lookup_2.ApplyResultSelector_MethodGroup.ApplyResultSelector_1_T1
            def __call__(self, resultSelector: Func_3[ApplyResultSelector_1_Lookup_2_TKey, IEnumerable_1[ApplyResultSelector_1_Lookup_2_TElement], ApplyResultSelector_1_TResult]) -> IEnumerable_1[ApplyResultSelector_1_TResult]:...




class OrderedParallelQuery_GenericClasses(abc.ABCMeta):
    Generic_OrderedParallelQuery_GenericClasses_OrderedParallelQuery_1_TSource = typing.TypeVar('Generic_OrderedParallelQuery_GenericClasses_OrderedParallelQuery_1_TSource')
    def __getitem__(self, types : typing.Type[Generic_OrderedParallelQuery_GenericClasses_OrderedParallelQuery_1_TSource]) -> typing.Type[OrderedParallelQuery_1[Generic_OrderedParallelQuery_GenericClasses_OrderedParallelQuery_1_TSource]]: ...

OrderedParallelQuery : OrderedParallelQuery_GenericClasses

OrderedParallelQuery_1_TSource = typing.TypeVar('OrderedParallelQuery_1_TSource')
class OrderedParallelQuery_1(typing.Generic[OrderedParallelQuery_1_TSource], ParallelQuery_1[OrderedParallelQuery_1_TSource]):
    def GetEnumerator(self) -> IEnumerator_1[OrderedParallelQuery_1_TSource]: ...


class ParallelEnumerable(abc.ABC):
    @staticmethod
    def Range(start: int, count: int) -> ParallelQuery_1[int]: ...
    # Skipped Aggregate due to it being static, abstract and generic.

    Aggregate : Aggregate_MethodGroup
    class Aggregate_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[Aggregate_1_T1]) -> Aggregate_1[Aggregate_1_T1]: ...

        Aggregate_1_T1 = typing.TypeVar('Aggregate_1_T1')
        class Aggregate_1(typing.Generic[Aggregate_1_T1]):
            Aggregate_1_TSource = ParallelEnumerable.Aggregate_MethodGroup.Aggregate_1_T1
            def __call__(self, source: ParallelQuery_1[Aggregate_1_TSource], func: Func_3[Aggregate_1_TSource, Aggregate_1_TSource, Aggregate_1_TSource]) -> Aggregate_1_TSource:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Aggregate_2_T1], typing.Type[Aggregate_2_T2]]) -> Aggregate_2[Aggregate_2_T1, Aggregate_2_T2]: ...

        Aggregate_2_T1 = typing.TypeVar('Aggregate_2_T1')
        Aggregate_2_T2 = typing.TypeVar('Aggregate_2_T2')
        class Aggregate_2(typing.Generic[Aggregate_2_T1, Aggregate_2_T2]):
            Aggregate_2_TSource = ParallelEnumerable.Aggregate_MethodGroup.Aggregate_2_T1
            Aggregate_2_TAccumulate = ParallelEnumerable.Aggregate_MethodGroup.Aggregate_2_T2
            def __call__(self, source: ParallelQuery_1[Aggregate_2_TSource], seed: Aggregate_2_TAccumulate, func: Func_3[Aggregate_2_TAccumulate, Aggregate_2_TSource, Aggregate_2_TAccumulate]) -> Aggregate_2_TAccumulate:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Aggregate_3_T1], typing.Type[Aggregate_3_T2], typing.Type[Aggregate_3_T3]]) -> Aggregate_3[Aggregate_3_T1, Aggregate_3_T2, Aggregate_3_T3]: ...

        Aggregate_3_T1 = typing.TypeVar('Aggregate_3_T1')
        Aggregate_3_T2 = typing.TypeVar('Aggregate_3_T2')
        Aggregate_3_T3 = typing.TypeVar('Aggregate_3_T3')
        class Aggregate_3(typing.Generic[Aggregate_3_T1, Aggregate_3_T2, Aggregate_3_T3]):
            Aggregate_3_TSource = ParallelEnumerable.Aggregate_MethodGroup.Aggregate_3_T1
            Aggregate_3_TAccumulate = ParallelEnumerable.Aggregate_MethodGroup.Aggregate_3_T2
            Aggregate_3_TResult = ParallelEnumerable.Aggregate_MethodGroup.Aggregate_3_T3
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Aggregate_3_TSource], seed: Aggregate_3_TAccumulate, func: Func_3[Aggregate_3_TAccumulate, Aggregate_3_TSource, Aggregate_3_TAccumulate], resultSelector: Func_2[Aggregate_3_TAccumulate, Aggregate_3_TResult]) -> Aggregate_3_TResult:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Aggregate_3_TSource], seedFactory: Func_1[Aggregate_3_TAccumulate], updateAccumulatorFunc: Func_3[Aggregate_3_TAccumulate, Aggregate_3_TSource, Aggregate_3_TAccumulate], combineAccumulatorsFunc: Func_3[Aggregate_3_TAccumulate, Aggregate_3_TAccumulate, Aggregate_3_TAccumulate], resultSelector: Func_2[Aggregate_3_TAccumulate, Aggregate_3_TResult]) -> Aggregate_3_TResult:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Aggregate_3_TSource], seed: Aggregate_3_TAccumulate, updateAccumulatorFunc: Func_3[Aggregate_3_TAccumulate, Aggregate_3_TSource, Aggregate_3_TAccumulate], combineAccumulatorsFunc: Func_3[Aggregate_3_TAccumulate, Aggregate_3_TAccumulate, Aggregate_3_TAccumulate], resultSelector: Func_2[Aggregate_3_TAccumulate, Aggregate_3_TResult]) -> Aggregate_3_TResult:...


    # Skipped All due to it being static, abstract and generic.

    All : All_MethodGroup
    class All_MethodGroup:
        def __getitem__(self, t:typing.Type[All_1_T1]) -> All_1[All_1_T1]: ...

        All_1_T1 = typing.TypeVar('All_1_T1')
        class All_1(typing.Generic[All_1_T1]):
            All_1_TSource = ParallelEnumerable.All_MethodGroup.All_1_T1
            def __call__(self, source: ParallelQuery_1[All_1_TSource], predicate: Func_2[All_1_TSource, bool]) -> bool:...


    # Skipped Any due to it being static, abstract and generic.

    Any : Any_MethodGroup
    class Any_MethodGroup:
        def __getitem__(self, t:typing.Type[Any_1_T1]) -> Any_1[Any_1_T1]: ...

        Any_1_T1 = typing.TypeVar('Any_1_T1')
        class Any_1(typing.Generic[Any_1_T1]):
            Any_1_TSource = ParallelEnumerable.Any_MethodGroup.Any_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Any_1_TSource]) -> bool:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Any_1_TSource], predicate: Func_2[Any_1_TSource, bool]) -> bool:...


    # Skipped AsEnumerable due to it being static, abstract and generic.

    AsEnumerable : AsEnumerable_MethodGroup
    class AsEnumerable_MethodGroup:
        def __getitem__(self, t:typing.Type[AsEnumerable_1_T1]) -> AsEnumerable_1[AsEnumerable_1_T1]: ...

        AsEnumerable_1_T1 = typing.TypeVar('AsEnumerable_1_T1')
        class AsEnumerable_1(typing.Generic[AsEnumerable_1_T1]):
            AsEnumerable_1_TSource = ParallelEnumerable.AsEnumerable_MethodGroup.AsEnumerable_1_T1
            def __call__(self, source: ParallelQuery_1[AsEnumerable_1_TSource]) -> IEnumerable_1[AsEnumerable_1_TSource]:...


    # Skipped AsOrdered due to it being static, abstract and generic.

    AsOrdered : AsOrdered_MethodGroup
    class AsOrdered_MethodGroup:
        def __getitem__(self, t:typing.Type[AsOrdered_1_T1]) -> AsOrdered_1[AsOrdered_1_T1]: ...

        AsOrdered_1_T1 = typing.TypeVar('AsOrdered_1_T1')
        class AsOrdered_1(typing.Generic[AsOrdered_1_T1]):
            AsOrdered_1_TSource = ParallelEnumerable.AsOrdered_MethodGroup.AsOrdered_1_T1
            def __call__(self, source: ParallelQuery_1[AsOrdered_1_TSource]) -> ParallelQuery_1[AsOrdered_1_TSource]:...

        def __call__(self, source: ParallelQuery) -> ParallelQuery:...

    # Skipped AsParallel due to it being static, abstract and generic.

    AsParallel : AsParallel_MethodGroup
    class AsParallel_MethodGroup:
        def __getitem__(self, t:typing.Type[AsParallel_1_T1]) -> AsParallel_1[AsParallel_1_T1]: ...

        AsParallel_1_T1 = typing.TypeVar('AsParallel_1_T1')
        class AsParallel_1(typing.Generic[AsParallel_1_T1]):
            AsParallel_1_TSource = ParallelEnumerable.AsParallel_MethodGroup.AsParallel_1_T1
            @typing.overload
            def __call__(self, source: IEnumerable_1[AsParallel_1_TSource]) -> ParallelQuery_1[AsParallel_1_TSource]:...
            @typing.overload
            def __call__(self, source: Partitioner_1[AsParallel_1_TSource]) -> ParallelQuery_1[AsParallel_1_TSource]:...

        def __call__(self, source: IEnumerable) -> ParallelQuery:...

    # Skipped AsSequential due to it being static, abstract and generic.

    AsSequential : AsSequential_MethodGroup
    class AsSequential_MethodGroup:
        def __getitem__(self, t:typing.Type[AsSequential_1_T1]) -> AsSequential_1[AsSequential_1_T1]: ...

        AsSequential_1_T1 = typing.TypeVar('AsSequential_1_T1')
        class AsSequential_1(typing.Generic[AsSequential_1_T1]):
            AsSequential_1_TSource = ParallelEnumerable.AsSequential_MethodGroup.AsSequential_1_T1
            def __call__(self, source: ParallelQuery_1[AsSequential_1_TSource]) -> IEnumerable_1[AsSequential_1_TSource]:...


    # Skipped AsUnordered due to it being static, abstract and generic.

    AsUnordered : AsUnordered_MethodGroup
    class AsUnordered_MethodGroup:
        def __getitem__(self, t:typing.Type[AsUnordered_1_T1]) -> AsUnordered_1[AsUnordered_1_T1]: ...

        AsUnordered_1_T1 = typing.TypeVar('AsUnordered_1_T1')
        class AsUnordered_1(typing.Generic[AsUnordered_1_T1]):
            AsUnordered_1_TSource = ParallelEnumerable.AsUnordered_MethodGroup.AsUnordered_1_T1
            def __call__(self, source: ParallelQuery_1[AsUnordered_1_TSource]) -> ParallelQuery_1[AsUnordered_1_TSource]:...


    # Skipped Average due to it being static, abstract and generic.

    Average : Average_MethodGroup
    class Average_MethodGroup:
        def __getitem__(self, t:typing.Type[Average_1_T1]) -> Average_1[Average_1_T1]: ...

        Average_1_T1 = typing.TypeVar('Average_1_T1')
        class Average_1(typing.Generic[Average_1_T1]):
            Average_1_TSource = ParallelEnumerable.Average_MethodGroup.Average_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Average_1_TSource], selector: Func_2[Average_1_TSource, float]) -> float:...
            # Method Average(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Average_1_TSource], selector: Func_2[Average_1_TSource, int]) -> float:...
            # Method Average(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Average_1_TSource], selector: Func_2[Average_1_TSource, Decimal]) -> Decimal:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Average_1_TSource], selector: Func_2[Average_1_TSource, typing.Optional[int]]) -> typing.Optional[float]:...
            # Method Average(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            # Method Average(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            # Method Average(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Average_1_TSource], selector: Func_2[Average_1_TSource, typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

        @typing.overload
        def __call__(self, source: ParallelQuery_1[float]) -> float:...
        # Method Average(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Average(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Average(source : ParallelQuery`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: ParallelQuery_1[Decimal]) -> Decimal:...
        @typing.overload
        def __call__(self, source: ParallelQuery_1[typing.Optional[int]]) -> typing.Optional[float]:...
        # Method Average(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Average(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Average(source : ParallelQuery`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: ParallelQuery_1[typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

    # Skipped Cast due to it being static, abstract and generic.

    Cast : Cast_MethodGroup
    class Cast_MethodGroup:
        def __getitem__(self, t:typing.Type[Cast_1_T1]) -> Cast_1[Cast_1_T1]: ...

        Cast_1_T1 = typing.TypeVar('Cast_1_T1')
        class Cast_1(typing.Generic[Cast_1_T1]):
            Cast_1_TResult = ParallelEnumerable.Cast_MethodGroup.Cast_1_T1
            def __call__(self, source: ParallelQuery) -> ParallelQuery_1[Cast_1_TResult]:...


    # Skipped Concat due to it being static, abstract and generic.

    Concat : Concat_MethodGroup
    class Concat_MethodGroup:
        def __getitem__(self, t:typing.Type[Concat_1_T1]) -> Concat_1[Concat_1_T1]: ...

        Concat_1_T1 = typing.TypeVar('Concat_1_T1')
        class Concat_1(typing.Generic[Concat_1_T1]):
            Concat_1_TSource = ParallelEnumerable.Concat_MethodGroup.Concat_1_T1
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Concat_1_TSource], second: ParallelQuery_1[Concat_1_TSource]) -> ParallelQuery_1[Concat_1_TSource]:...
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Concat_1_TSource], second: IEnumerable_1[Concat_1_TSource]) -> ParallelQuery_1[Concat_1_TSource]:...


    # Skipped Contains due to it being static, abstract and generic.

    Contains : Contains_MethodGroup
    class Contains_MethodGroup:
        def __getitem__(self, t:typing.Type[Contains_1_T1]) -> Contains_1[Contains_1_T1]: ...

        Contains_1_T1 = typing.TypeVar('Contains_1_T1')
        class Contains_1(typing.Generic[Contains_1_T1]):
            Contains_1_TSource = ParallelEnumerable.Contains_MethodGroup.Contains_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Contains_1_TSource], value: Contains_1_TSource) -> bool:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Contains_1_TSource], value: Contains_1_TSource, comparer: IEqualityComparer_1[Contains_1_TSource]) -> bool:...


    # Skipped Count due to it being static, abstract and generic.

    Count : Count_MethodGroup
    class Count_MethodGroup:
        def __getitem__(self, t:typing.Type[Count_1_T1]) -> Count_1[Count_1_T1]: ...

        Count_1_T1 = typing.TypeVar('Count_1_T1')
        class Count_1(typing.Generic[Count_1_T1]):
            Count_1_TSource = ParallelEnumerable.Count_MethodGroup.Count_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Count_1_TSource]) -> int:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Count_1_TSource], predicate: Func_2[Count_1_TSource, bool]) -> int:...


    # Skipped DefaultIfEmpty due to it being static, abstract and generic.

    DefaultIfEmpty : DefaultIfEmpty_MethodGroup
    class DefaultIfEmpty_MethodGroup:
        def __getitem__(self, t:typing.Type[DefaultIfEmpty_1_T1]) -> DefaultIfEmpty_1[DefaultIfEmpty_1_T1]: ...

        DefaultIfEmpty_1_T1 = typing.TypeVar('DefaultIfEmpty_1_T1')
        class DefaultIfEmpty_1(typing.Generic[DefaultIfEmpty_1_T1]):
            DefaultIfEmpty_1_TSource = ParallelEnumerable.DefaultIfEmpty_MethodGroup.DefaultIfEmpty_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[DefaultIfEmpty_1_TSource]) -> ParallelQuery_1[DefaultIfEmpty_1_TSource]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[DefaultIfEmpty_1_TSource], defaultValue: DefaultIfEmpty_1_TSource) -> ParallelQuery_1[DefaultIfEmpty_1_TSource]:...


    # Skipped Distinct due to it being static, abstract and generic.

    Distinct : Distinct_MethodGroup
    class Distinct_MethodGroup:
        def __getitem__(self, t:typing.Type[Distinct_1_T1]) -> Distinct_1[Distinct_1_T1]: ...

        Distinct_1_T1 = typing.TypeVar('Distinct_1_T1')
        class Distinct_1(typing.Generic[Distinct_1_T1]):
            Distinct_1_TSource = ParallelEnumerable.Distinct_MethodGroup.Distinct_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Distinct_1_TSource]) -> ParallelQuery_1[Distinct_1_TSource]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Distinct_1_TSource], comparer: IEqualityComparer_1[Distinct_1_TSource]) -> ParallelQuery_1[Distinct_1_TSource]:...


    # Skipped ElementAt due to it being static, abstract and generic.

    ElementAt : ElementAt_MethodGroup
    class ElementAt_MethodGroup:
        def __getitem__(self, t:typing.Type[ElementAt_1_T1]) -> ElementAt_1[ElementAt_1_T1]: ...

        ElementAt_1_T1 = typing.TypeVar('ElementAt_1_T1')
        class ElementAt_1(typing.Generic[ElementAt_1_T1]):
            ElementAt_1_TSource = ParallelEnumerable.ElementAt_MethodGroup.ElementAt_1_T1
            def __call__(self, source: ParallelQuery_1[ElementAt_1_TSource], index: int) -> ElementAt_1_TSource:...


    # Skipped ElementAtOrDefault due to it being static, abstract and generic.

    ElementAtOrDefault : ElementAtOrDefault_MethodGroup
    class ElementAtOrDefault_MethodGroup:
        def __getitem__(self, t:typing.Type[ElementAtOrDefault_1_T1]) -> ElementAtOrDefault_1[ElementAtOrDefault_1_T1]: ...

        ElementAtOrDefault_1_T1 = typing.TypeVar('ElementAtOrDefault_1_T1')
        class ElementAtOrDefault_1(typing.Generic[ElementAtOrDefault_1_T1]):
            ElementAtOrDefault_1_TSource = ParallelEnumerable.ElementAtOrDefault_MethodGroup.ElementAtOrDefault_1_T1
            def __call__(self, source: ParallelQuery_1[ElementAtOrDefault_1_TSource], index: int) -> ElementAtOrDefault_1_TSource:...


    # Skipped Empty due to it being static, abstract and generic.

    Empty : Empty_MethodGroup
    class Empty_MethodGroup:
        def __getitem__(self, t:typing.Type[Empty_1_T1]) -> Empty_1[Empty_1_T1]: ...

        Empty_1_T1 = typing.TypeVar('Empty_1_T1')
        class Empty_1(typing.Generic[Empty_1_T1]):
            Empty_1_TResult = ParallelEnumerable.Empty_MethodGroup.Empty_1_T1
            def __call__(self) -> ParallelQuery_1[Empty_1_TResult]:...


    # Skipped Except due to it being static, abstract and generic.

    Except : Except_MethodGroup
    class Except_MethodGroup:
        def __getitem__(self, t:typing.Type[Except_1_T1]) -> Except_1[Except_1_T1]: ...

        Except_1_T1 = typing.TypeVar('Except_1_T1')
        class Except_1(typing.Generic[Except_1_T1]):
            Except_1_TSource = ParallelEnumerable.Except_MethodGroup.Except_1_T1
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Except_1_TSource], second: ParallelQuery_1[Except_1_TSource]) -> ParallelQuery_1[Except_1_TSource]:...
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Except_1_TSource], second: IEnumerable_1[Except_1_TSource]) -> ParallelQuery_1[Except_1_TSource]:...
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Except_1_TSource], second: ParallelQuery_1[Except_1_TSource], comparer: IEqualityComparer_1[Except_1_TSource]) -> ParallelQuery_1[Except_1_TSource]:...
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Except_1_TSource], second: IEnumerable_1[Except_1_TSource], comparer: IEqualityComparer_1[Except_1_TSource]) -> ParallelQuery_1[Except_1_TSource]:...


    # Skipped First due to it being static, abstract and generic.

    First : First_MethodGroup
    class First_MethodGroup:
        def __getitem__(self, t:typing.Type[First_1_T1]) -> First_1[First_1_T1]: ...

        First_1_T1 = typing.TypeVar('First_1_T1')
        class First_1(typing.Generic[First_1_T1]):
            First_1_TSource = ParallelEnumerable.First_MethodGroup.First_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[First_1_TSource]) -> First_1_TSource:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[First_1_TSource], predicate: Func_2[First_1_TSource, bool]) -> First_1_TSource:...


    # Skipped FirstOrDefault due to it being static, abstract and generic.

    FirstOrDefault : FirstOrDefault_MethodGroup
    class FirstOrDefault_MethodGroup:
        def __getitem__(self, t:typing.Type[FirstOrDefault_1_T1]) -> FirstOrDefault_1[FirstOrDefault_1_T1]: ...

        FirstOrDefault_1_T1 = typing.TypeVar('FirstOrDefault_1_T1')
        class FirstOrDefault_1(typing.Generic[FirstOrDefault_1_T1]):
            FirstOrDefault_1_TSource = ParallelEnumerable.FirstOrDefault_MethodGroup.FirstOrDefault_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[FirstOrDefault_1_TSource]) -> FirstOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[FirstOrDefault_1_TSource], predicate: Func_2[FirstOrDefault_1_TSource, bool]) -> FirstOrDefault_1_TSource:...


    # Skipped ForAll due to it being static, abstract and generic.

    ForAll : ForAll_MethodGroup
    class ForAll_MethodGroup:
        def __getitem__(self, t:typing.Type[ForAll_1_T1]) -> ForAll_1[ForAll_1_T1]: ...

        ForAll_1_T1 = typing.TypeVar('ForAll_1_T1')
        class ForAll_1(typing.Generic[ForAll_1_T1]):
            ForAll_1_TSource = ParallelEnumerable.ForAll_MethodGroup.ForAll_1_T1
            def __call__(self, source: ParallelQuery_1[ForAll_1_TSource], action: Action_1[ForAll_1_TSource]) -> None:...


    # Skipped GroupBy due to it being static, abstract and generic.

    GroupBy : GroupBy_MethodGroup
    class GroupBy_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[GroupBy_2_T1], typing.Type[GroupBy_2_T2]]) -> GroupBy_2[GroupBy_2_T1, GroupBy_2_T2]: ...

        GroupBy_2_T1 = typing.TypeVar('GroupBy_2_T1')
        GroupBy_2_T2 = typing.TypeVar('GroupBy_2_T2')
        class GroupBy_2(typing.Generic[GroupBy_2_T1, GroupBy_2_T2]):
            GroupBy_2_TSource = ParallelEnumerable.GroupBy_MethodGroup.GroupBy_2_T1
            GroupBy_2_TKey = ParallelEnumerable.GroupBy_MethodGroup.GroupBy_2_T2
            @typing.overload
            def __call__(self, source: ParallelQuery_1[GroupBy_2_TSource], keySelector: Func_2[GroupBy_2_TSource, GroupBy_2_TKey]) -> ParallelQuery_1[IGrouping_2[GroupBy_2_TKey, GroupBy_2_TSource]]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[GroupBy_2_TSource], keySelector: Func_2[GroupBy_2_TSource, GroupBy_2_TKey], comparer: IEqualityComparer_1[GroupBy_2_TKey]) -> ParallelQuery_1[IGrouping_2[GroupBy_2_TKey, GroupBy_2_TSource]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[GroupBy_3_T1], typing.Type[GroupBy_3_T2], typing.Type[GroupBy_3_T3]]) -> GroupBy_3[GroupBy_3_T1, GroupBy_3_T2, GroupBy_3_T3]: ...

        GroupBy_3_T1 = typing.TypeVar('GroupBy_3_T1')
        GroupBy_3_T2 = typing.TypeVar('GroupBy_3_T2')
        GroupBy_3_T3 = typing.TypeVar('GroupBy_3_T3')
        class GroupBy_3(typing.Generic[GroupBy_3_T1, GroupBy_3_T2, GroupBy_3_T3]):
            GroupBy_3_TSource = ParallelEnumerable.GroupBy_MethodGroup.GroupBy_3_T1
            GroupBy_3_TKey = ParallelEnumerable.GroupBy_MethodGroup.GroupBy_3_T2
            GroupBy_3_TElement = ParallelEnumerable.GroupBy_MethodGroup.GroupBy_3_T3
            GroupBy_3_TResult = ParallelEnumerable.GroupBy_MethodGroup.GroupBy_3_T3
            @typing.overload
            def __call__(self, source: ParallelQuery_1[GroupBy_3_TSource], keySelector: Func_2[GroupBy_3_TSource, GroupBy_3_TKey], elementSelector: Func_2[GroupBy_3_TSource, GroupBy_3_TElement]) -> ParallelQuery_1[IGrouping_2[GroupBy_3_TKey, GroupBy_3_TElement]]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[GroupBy_3_TSource], keySelector: Func_2[GroupBy_3_TSource, GroupBy_3_TKey], resultSelector: Func_3[GroupBy_3_TKey, IEnumerable_1[GroupBy_3_TSource], GroupBy_3_TResult]) -> ParallelQuery_1[GroupBy_3_TResult]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[GroupBy_3_TSource], keySelector: Func_2[GroupBy_3_TSource, GroupBy_3_TKey], elementSelector: Func_2[GroupBy_3_TSource, GroupBy_3_TElement], comparer: IEqualityComparer_1[GroupBy_3_TKey]) -> ParallelQuery_1[IGrouping_2[GroupBy_3_TKey, GroupBy_3_TElement]]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[GroupBy_3_TSource], keySelector: Func_2[GroupBy_3_TSource, GroupBy_3_TKey], resultSelector: Func_3[GroupBy_3_TKey, IEnumerable_1[GroupBy_3_TSource], GroupBy_3_TResult], comparer: IEqualityComparer_1[GroupBy_3_TKey]) -> ParallelQuery_1[GroupBy_3_TResult]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[GroupBy_4_T1], typing.Type[GroupBy_4_T2], typing.Type[GroupBy_4_T3], typing.Type[GroupBy_4_T4]]) -> GroupBy_4[GroupBy_4_T1, GroupBy_4_T2, GroupBy_4_T3, GroupBy_4_T4]: ...

        GroupBy_4_T1 = typing.TypeVar('GroupBy_4_T1')
        GroupBy_4_T2 = typing.TypeVar('GroupBy_4_T2')
        GroupBy_4_T3 = typing.TypeVar('GroupBy_4_T3')
        GroupBy_4_T4 = typing.TypeVar('GroupBy_4_T4')
        class GroupBy_4(typing.Generic[GroupBy_4_T1, GroupBy_4_T2, GroupBy_4_T3, GroupBy_4_T4]):
            GroupBy_4_TSource = ParallelEnumerable.GroupBy_MethodGroup.GroupBy_4_T1
            GroupBy_4_TKey = ParallelEnumerable.GroupBy_MethodGroup.GroupBy_4_T2
            GroupBy_4_TElement = ParallelEnumerable.GroupBy_MethodGroup.GroupBy_4_T3
            GroupBy_4_TResult = ParallelEnumerable.GroupBy_MethodGroup.GroupBy_4_T4
            @typing.overload
            def __call__(self, source: ParallelQuery_1[GroupBy_4_TSource], keySelector: Func_2[GroupBy_4_TSource, GroupBy_4_TKey], elementSelector: Func_2[GroupBy_4_TSource, GroupBy_4_TElement], resultSelector: Func_3[GroupBy_4_TKey, IEnumerable_1[GroupBy_4_TElement], GroupBy_4_TResult]) -> ParallelQuery_1[GroupBy_4_TResult]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[GroupBy_4_TSource], keySelector: Func_2[GroupBy_4_TSource, GroupBy_4_TKey], elementSelector: Func_2[GroupBy_4_TSource, GroupBy_4_TElement], resultSelector: Func_3[GroupBy_4_TKey, IEnumerable_1[GroupBy_4_TElement], GroupBy_4_TResult], comparer: IEqualityComparer_1[GroupBy_4_TKey]) -> ParallelQuery_1[GroupBy_4_TResult]:...


    # Skipped GroupJoin due to it being static, abstract and generic.

    GroupJoin : GroupJoin_MethodGroup
    class GroupJoin_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[GroupJoin_4_T1], typing.Type[GroupJoin_4_T2], typing.Type[GroupJoin_4_T3], typing.Type[GroupJoin_4_T4]]) -> GroupJoin_4[GroupJoin_4_T1, GroupJoin_4_T2, GroupJoin_4_T3, GroupJoin_4_T4]: ...

        GroupJoin_4_T1 = typing.TypeVar('GroupJoin_4_T1')
        GroupJoin_4_T2 = typing.TypeVar('GroupJoin_4_T2')
        GroupJoin_4_T3 = typing.TypeVar('GroupJoin_4_T3')
        GroupJoin_4_T4 = typing.TypeVar('GroupJoin_4_T4')
        class GroupJoin_4(typing.Generic[GroupJoin_4_T1, GroupJoin_4_T2, GroupJoin_4_T3, GroupJoin_4_T4]):
            GroupJoin_4_TOuter = ParallelEnumerable.GroupJoin_MethodGroup.GroupJoin_4_T1
            GroupJoin_4_TInner = ParallelEnumerable.GroupJoin_MethodGroup.GroupJoin_4_T2
            GroupJoin_4_TKey = ParallelEnumerable.GroupJoin_MethodGroup.GroupJoin_4_T3
            GroupJoin_4_TResult = ParallelEnumerable.GroupJoin_MethodGroup.GroupJoin_4_T4
            @typing.overload
            def __call__(self, outer: ParallelQuery_1[GroupJoin_4_TOuter], inner: ParallelQuery_1[GroupJoin_4_TInner], outerKeySelector: Func_2[GroupJoin_4_TOuter, GroupJoin_4_TKey], innerKeySelector: Func_2[GroupJoin_4_TInner, GroupJoin_4_TKey], resultSelector: Func_3[GroupJoin_4_TOuter, IEnumerable_1[GroupJoin_4_TInner], GroupJoin_4_TResult]) -> ParallelQuery_1[GroupJoin_4_TResult]:...
            @typing.overload
            def __call__(self, outer: ParallelQuery_1[GroupJoin_4_TOuter], inner: IEnumerable_1[GroupJoin_4_TInner], outerKeySelector: Func_2[GroupJoin_4_TOuter, GroupJoin_4_TKey], innerKeySelector: Func_2[GroupJoin_4_TInner, GroupJoin_4_TKey], resultSelector: Func_3[GroupJoin_4_TOuter, IEnumerable_1[GroupJoin_4_TInner], GroupJoin_4_TResult]) -> ParallelQuery_1[GroupJoin_4_TResult]:...
            @typing.overload
            def __call__(self, outer: ParallelQuery_1[GroupJoin_4_TOuter], inner: ParallelQuery_1[GroupJoin_4_TInner], outerKeySelector: Func_2[GroupJoin_4_TOuter, GroupJoin_4_TKey], innerKeySelector: Func_2[GroupJoin_4_TInner, GroupJoin_4_TKey], resultSelector: Func_3[GroupJoin_4_TOuter, IEnumerable_1[GroupJoin_4_TInner], GroupJoin_4_TResult], comparer: IEqualityComparer_1[GroupJoin_4_TKey]) -> ParallelQuery_1[GroupJoin_4_TResult]:...
            @typing.overload
            def __call__(self, outer: ParallelQuery_1[GroupJoin_4_TOuter], inner: IEnumerable_1[GroupJoin_4_TInner], outerKeySelector: Func_2[GroupJoin_4_TOuter, GroupJoin_4_TKey], innerKeySelector: Func_2[GroupJoin_4_TInner, GroupJoin_4_TKey], resultSelector: Func_3[GroupJoin_4_TOuter, IEnumerable_1[GroupJoin_4_TInner], GroupJoin_4_TResult], comparer: IEqualityComparer_1[GroupJoin_4_TKey]) -> ParallelQuery_1[GroupJoin_4_TResult]:...


    # Skipped Intersect due to it being static, abstract and generic.

    Intersect : Intersect_MethodGroup
    class Intersect_MethodGroup:
        def __getitem__(self, t:typing.Type[Intersect_1_T1]) -> Intersect_1[Intersect_1_T1]: ...

        Intersect_1_T1 = typing.TypeVar('Intersect_1_T1')
        class Intersect_1(typing.Generic[Intersect_1_T1]):
            Intersect_1_TSource = ParallelEnumerable.Intersect_MethodGroup.Intersect_1_T1
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Intersect_1_TSource], second: ParallelQuery_1[Intersect_1_TSource]) -> ParallelQuery_1[Intersect_1_TSource]:...
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Intersect_1_TSource], second: IEnumerable_1[Intersect_1_TSource]) -> ParallelQuery_1[Intersect_1_TSource]:...
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Intersect_1_TSource], second: ParallelQuery_1[Intersect_1_TSource], comparer: IEqualityComparer_1[Intersect_1_TSource]) -> ParallelQuery_1[Intersect_1_TSource]:...
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Intersect_1_TSource], second: IEnumerable_1[Intersect_1_TSource], comparer: IEqualityComparer_1[Intersect_1_TSource]) -> ParallelQuery_1[Intersect_1_TSource]:...


    # Skipped Join due to it being static, abstract and generic.

    Join : Join_MethodGroup
    class Join_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Join_4_T1], typing.Type[Join_4_T2], typing.Type[Join_4_T3], typing.Type[Join_4_T4]]) -> Join_4[Join_4_T1, Join_4_T2, Join_4_T3, Join_4_T4]: ...

        Join_4_T1 = typing.TypeVar('Join_4_T1')
        Join_4_T2 = typing.TypeVar('Join_4_T2')
        Join_4_T3 = typing.TypeVar('Join_4_T3')
        Join_4_T4 = typing.TypeVar('Join_4_T4')
        class Join_4(typing.Generic[Join_4_T1, Join_4_T2, Join_4_T3, Join_4_T4]):
            Join_4_TOuter = ParallelEnumerable.Join_MethodGroup.Join_4_T1
            Join_4_TInner = ParallelEnumerable.Join_MethodGroup.Join_4_T2
            Join_4_TKey = ParallelEnumerable.Join_MethodGroup.Join_4_T3
            Join_4_TResult = ParallelEnumerable.Join_MethodGroup.Join_4_T4
            @typing.overload
            def __call__(self, outer: ParallelQuery_1[Join_4_TOuter], inner: ParallelQuery_1[Join_4_TInner], outerKeySelector: Func_2[Join_4_TOuter, Join_4_TKey], innerKeySelector: Func_2[Join_4_TInner, Join_4_TKey], resultSelector: Func_3[Join_4_TOuter, Join_4_TInner, Join_4_TResult]) -> ParallelQuery_1[Join_4_TResult]:...
            @typing.overload
            def __call__(self, outer: ParallelQuery_1[Join_4_TOuter], inner: IEnumerable_1[Join_4_TInner], outerKeySelector: Func_2[Join_4_TOuter, Join_4_TKey], innerKeySelector: Func_2[Join_4_TInner, Join_4_TKey], resultSelector: Func_3[Join_4_TOuter, Join_4_TInner, Join_4_TResult]) -> ParallelQuery_1[Join_4_TResult]:...
            @typing.overload
            def __call__(self, outer: ParallelQuery_1[Join_4_TOuter], inner: ParallelQuery_1[Join_4_TInner], outerKeySelector: Func_2[Join_4_TOuter, Join_4_TKey], innerKeySelector: Func_2[Join_4_TInner, Join_4_TKey], resultSelector: Func_3[Join_4_TOuter, Join_4_TInner, Join_4_TResult], comparer: IEqualityComparer_1[Join_4_TKey]) -> ParallelQuery_1[Join_4_TResult]:...
            @typing.overload
            def __call__(self, outer: ParallelQuery_1[Join_4_TOuter], inner: IEnumerable_1[Join_4_TInner], outerKeySelector: Func_2[Join_4_TOuter, Join_4_TKey], innerKeySelector: Func_2[Join_4_TInner, Join_4_TKey], resultSelector: Func_3[Join_4_TOuter, Join_4_TInner, Join_4_TResult], comparer: IEqualityComparer_1[Join_4_TKey]) -> ParallelQuery_1[Join_4_TResult]:...


    # Skipped Last due to it being static, abstract and generic.

    Last : Last_MethodGroup
    class Last_MethodGroup:
        def __getitem__(self, t:typing.Type[Last_1_T1]) -> Last_1[Last_1_T1]: ...

        Last_1_T1 = typing.TypeVar('Last_1_T1')
        class Last_1(typing.Generic[Last_1_T1]):
            Last_1_TSource = ParallelEnumerable.Last_MethodGroup.Last_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Last_1_TSource]) -> Last_1_TSource:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Last_1_TSource], predicate: Func_2[Last_1_TSource, bool]) -> Last_1_TSource:...


    # Skipped LastOrDefault due to it being static, abstract and generic.

    LastOrDefault : LastOrDefault_MethodGroup
    class LastOrDefault_MethodGroup:
        def __getitem__(self, t:typing.Type[LastOrDefault_1_T1]) -> LastOrDefault_1[LastOrDefault_1_T1]: ...

        LastOrDefault_1_T1 = typing.TypeVar('LastOrDefault_1_T1')
        class LastOrDefault_1(typing.Generic[LastOrDefault_1_T1]):
            LastOrDefault_1_TSource = ParallelEnumerable.LastOrDefault_MethodGroup.LastOrDefault_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[LastOrDefault_1_TSource]) -> LastOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[LastOrDefault_1_TSource], predicate: Func_2[LastOrDefault_1_TSource, bool]) -> LastOrDefault_1_TSource:...


    # Skipped LongCount due to it being static, abstract and generic.

    LongCount : LongCount_MethodGroup
    class LongCount_MethodGroup:
        def __getitem__(self, t:typing.Type[LongCount_1_T1]) -> LongCount_1[LongCount_1_T1]: ...

        LongCount_1_T1 = typing.TypeVar('LongCount_1_T1')
        class LongCount_1(typing.Generic[LongCount_1_T1]):
            LongCount_1_TSource = ParallelEnumerable.LongCount_MethodGroup.LongCount_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[LongCount_1_TSource]) -> int:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[LongCount_1_TSource], predicate: Func_2[LongCount_1_TSource, bool]) -> int:...


    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[Max_1_T1]) -> Max_1[Max_1_T1]: ...

        Max_1_T1 = typing.TypeVar('Max_1_T1')
        class Max_1(typing.Generic[Max_1_T1]):
            Max_1_TSource = ParallelEnumerable.Max_MethodGroup.Max_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Max_1_TSource]) -> Max_1_TSource:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Max_1_TSource], selector: Func_2[Max_1_TSource, float]) -> float:...
            # Method Max(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Max_1_TSource], selector: Func_2[Max_1_TSource, int]) -> int:...
            # Method Max(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Max_1_TSource], selector: Func_2[Max_1_TSource, Decimal]) -> Decimal:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Max_1_TSource], selector: Func_2[Max_1_TSource, typing.Optional[int]]) -> typing.Optional[int]:...
            # Method Max(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            # Method Max(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            # Method Max(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Max_1_TSource], selector: Func_2[Max_1_TSource, typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Max_2_T1], typing.Type[Max_2_T2]]) -> Max_2[Max_2_T1, Max_2_T2]: ...

        Max_2_T1 = typing.TypeVar('Max_2_T1')
        Max_2_T2 = typing.TypeVar('Max_2_T2')
        class Max_2(typing.Generic[Max_2_T1, Max_2_T2]):
            Max_2_TSource = ParallelEnumerable.Max_MethodGroup.Max_2_T1
            Max_2_TResult = ParallelEnumerable.Max_MethodGroup.Max_2_T2
            def __call__(self, source: ParallelQuery_1[Max_2_TSource], selector: Func_2[Max_2_TSource, Max_2_TResult]) -> Max_2_TResult:...

        @typing.overload
        def __call__(self, source: ParallelQuery_1[float]) -> float:...
        # Method Max(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Max(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Max(source : ParallelQuery`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: ParallelQuery_1[Decimal]) -> Decimal:...
        @typing.overload
        def __call__(self, source: ParallelQuery_1[typing.Optional[int]]) -> typing.Optional[int]:...
        # Method Max(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Max(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Max(source : ParallelQuery`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: ParallelQuery_1[typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[Min_1_T1]) -> Min_1[Min_1_T1]: ...

        Min_1_T1 = typing.TypeVar('Min_1_T1')
        class Min_1(typing.Generic[Min_1_T1]):
            Min_1_TSource = ParallelEnumerable.Min_MethodGroup.Min_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Min_1_TSource]) -> Min_1_TSource:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Min_1_TSource], selector: Func_2[Min_1_TSource, float]) -> float:...
            # Method Min(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Min_1_TSource], selector: Func_2[Min_1_TSource, int]) -> int:...
            # Method Min(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Min_1_TSource], selector: Func_2[Min_1_TSource, Decimal]) -> Decimal:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Min_1_TSource], selector: Func_2[Min_1_TSource, typing.Optional[int]]) -> typing.Optional[int]:...
            # Method Min(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            # Method Min(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            # Method Min(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Min_1_TSource], selector: Func_2[Min_1_TSource, typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Min_2_T1], typing.Type[Min_2_T2]]) -> Min_2[Min_2_T1, Min_2_T2]: ...

        Min_2_T1 = typing.TypeVar('Min_2_T1')
        Min_2_T2 = typing.TypeVar('Min_2_T2')
        class Min_2(typing.Generic[Min_2_T1, Min_2_T2]):
            Min_2_TSource = ParallelEnumerable.Min_MethodGroup.Min_2_T1
            Min_2_TResult = ParallelEnumerable.Min_MethodGroup.Min_2_T2
            def __call__(self, source: ParallelQuery_1[Min_2_TSource], selector: Func_2[Min_2_TSource, Min_2_TResult]) -> Min_2_TResult:...

        @typing.overload
        def __call__(self, source: ParallelQuery_1[float]) -> float:...
        # Method Min(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Min(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Min(source : ParallelQuery`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: ParallelQuery_1[Decimal]) -> Decimal:...
        @typing.overload
        def __call__(self, source: ParallelQuery_1[typing.Optional[int]]) -> typing.Optional[int]:...
        # Method Min(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Min(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Min(source : ParallelQuery`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: ParallelQuery_1[typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

    # Skipped OfType due to it being static, abstract and generic.

    OfType : OfType_MethodGroup
    class OfType_MethodGroup:
        def __getitem__(self, t:typing.Type[OfType_1_T1]) -> OfType_1[OfType_1_T1]: ...

        OfType_1_T1 = typing.TypeVar('OfType_1_T1')
        class OfType_1(typing.Generic[OfType_1_T1]):
            OfType_1_TResult = ParallelEnumerable.OfType_MethodGroup.OfType_1_T1
            def __call__(self, source: ParallelQuery) -> ParallelQuery_1[OfType_1_TResult]:...


    # Skipped OrderBy due to it being static, abstract and generic.

    OrderBy : OrderBy_MethodGroup
    class OrderBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[OrderBy_2_T1], typing.Type[OrderBy_2_T2]]) -> OrderBy_2[OrderBy_2_T1, OrderBy_2_T2]: ...

        OrderBy_2_T1 = typing.TypeVar('OrderBy_2_T1')
        OrderBy_2_T2 = typing.TypeVar('OrderBy_2_T2')
        class OrderBy_2(typing.Generic[OrderBy_2_T1, OrderBy_2_T2]):
            OrderBy_2_TSource = ParallelEnumerable.OrderBy_MethodGroup.OrderBy_2_T1
            OrderBy_2_TKey = ParallelEnumerable.OrderBy_MethodGroup.OrderBy_2_T2
            @typing.overload
            def __call__(self, source: ParallelQuery_1[OrderBy_2_TSource], keySelector: Func_2[OrderBy_2_TSource, OrderBy_2_TKey]) -> OrderedParallelQuery_1[OrderBy_2_TSource]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[OrderBy_2_TSource], keySelector: Func_2[OrderBy_2_TSource, OrderBy_2_TKey], comparer: IComparer_1[OrderBy_2_TKey]) -> OrderedParallelQuery_1[OrderBy_2_TSource]:...


    # Skipped OrderByDescending due to it being static, abstract and generic.

    OrderByDescending : OrderByDescending_MethodGroup
    class OrderByDescending_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[OrderByDescending_2_T1], typing.Type[OrderByDescending_2_T2]]) -> OrderByDescending_2[OrderByDescending_2_T1, OrderByDescending_2_T2]: ...

        OrderByDescending_2_T1 = typing.TypeVar('OrderByDescending_2_T1')
        OrderByDescending_2_T2 = typing.TypeVar('OrderByDescending_2_T2')
        class OrderByDescending_2(typing.Generic[OrderByDescending_2_T1, OrderByDescending_2_T2]):
            OrderByDescending_2_TSource = ParallelEnumerable.OrderByDescending_MethodGroup.OrderByDescending_2_T1
            OrderByDescending_2_TKey = ParallelEnumerable.OrderByDescending_MethodGroup.OrderByDescending_2_T2
            @typing.overload
            def __call__(self, source: ParallelQuery_1[OrderByDescending_2_TSource], keySelector: Func_2[OrderByDescending_2_TSource, OrderByDescending_2_TKey]) -> OrderedParallelQuery_1[OrderByDescending_2_TSource]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[OrderByDescending_2_TSource], keySelector: Func_2[OrderByDescending_2_TSource, OrderByDescending_2_TKey], comparer: IComparer_1[OrderByDescending_2_TKey]) -> OrderedParallelQuery_1[OrderByDescending_2_TSource]:...


    # Skipped Repeat due to it being static, abstract and generic.

    Repeat : Repeat_MethodGroup
    class Repeat_MethodGroup:
        def __getitem__(self, t:typing.Type[Repeat_1_T1]) -> Repeat_1[Repeat_1_T1]: ...

        Repeat_1_T1 = typing.TypeVar('Repeat_1_T1')
        class Repeat_1(typing.Generic[Repeat_1_T1]):
            Repeat_1_TResult = ParallelEnumerable.Repeat_MethodGroup.Repeat_1_T1
            def __call__(self, element: Repeat_1_TResult, count: int) -> ParallelQuery_1[Repeat_1_TResult]:...


    # Skipped Reverse due to it being static, abstract and generic.

    Reverse : Reverse_MethodGroup
    class Reverse_MethodGroup:
        def __getitem__(self, t:typing.Type[Reverse_1_T1]) -> Reverse_1[Reverse_1_T1]: ...

        Reverse_1_T1 = typing.TypeVar('Reverse_1_T1')
        class Reverse_1(typing.Generic[Reverse_1_T1]):
            Reverse_1_TSource = ParallelEnumerable.Reverse_MethodGroup.Reverse_1_T1
            def __call__(self, source: ParallelQuery_1[Reverse_1_TSource]) -> ParallelQuery_1[Reverse_1_TSource]:...


    # Skipped Select due to it being static, abstract and generic.

    Select : Select_MethodGroup
    class Select_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Select_2_T1], typing.Type[Select_2_T2]]) -> Select_2[Select_2_T1, Select_2_T2]: ...

        Select_2_T1 = typing.TypeVar('Select_2_T1')
        Select_2_T2 = typing.TypeVar('Select_2_T2')
        class Select_2(typing.Generic[Select_2_T1, Select_2_T2]):
            Select_2_TSource = ParallelEnumerable.Select_MethodGroup.Select_2_T1
            Select_2_TResult = ParallelEnumerable.Select_MethodGroup.Select_2_T2
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Select_2_TSource], selector: Func_3[Select_2_TSource, int, Select_2_TResult]) -> ParallelQuery_1[Select_2_TResult]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Select_2_TSource], selector: Func_2[Select_2_TSource, Select_2_TResult]) -> ParallelQuery_1[Select_2_TResult]:...


    # Skipped SelectMany due to it being static, abstract and generic.

    SelectMany : SelectMany_MethodGroup
    class SelectMany_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[SelectMany_2_T1], typing.Type[SelectMany_2_T2]]) -> SelectMany_2[SelectMany_2_T1, SelectMany_2_T2]: ...

        SelectMany_2_T1 = typing.TypeVar('SelectMany_2_T1')
        SelectMany_2_T2 = typing.TypeVar('SelectMany_2_T2')
        class SelectMany_2(typing.Generic[SelectMany_2_T1, SelectMany_2_T2]):
            SelectMany_2_TSource = ParallelEnumerable.SelectMany_MethodGroup.SelectMany_2_T1
            SelectMany_2_TResult = ParallelEnumerable.SelectMany_MethodGroup.SelectMany_2_T2
            @typing.overload
            def __call__(self, source: ParallelQuery_1[SelectMany_2_TSource], selector: Func_3[SelectMany_2_TSource, int, IEnumerable_1[SelectMany_2_TResult]]) -> ParallelQuery_1[SelectMany_2_TResult]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[SelectMany_2_TSource], selector: Func_2[SelectMany_2_TSource, IEnumerable_1[SelectMany_2_TResult]]) -> ParallelQuery_1[SelectMany_2_TResult]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[SelectMany_3_T1], typing.Type[SelectMany_3_T2], typing.Type[SelectMany_3_T3]]) -> SelectMany_3[SelectMany_3_T1, SelectMany_3_T2, SelectMany_3_T3]: ...

        SelectMany_3_T1 = typing.TypeVar('SelectMany_3_T1')
        SelectMany_3_T2 = typing.TypeVar('SelectMany_3_T2')
        SelectMany_3_T3 = typing.TypeVar('SelectMany_3_T3')
        class SelectMany_3(typing.Generic[SelectMany_3_T1, SelectMany_3_T2, SelectMany_3_T3]):
            SelectMany_3_TSource = ParallelEnumerable.SelectMany_MethodGroup.SelectMany_3_T1
            SelectMany_3_TCollection = ParallelEnumerable.SelectMany_MethodGroup.SelectMany_3_T2
            SelectMany_3_TResult = ParallelEnumerable.SelectMany_MethodGroup.SelectMany_3_T3
            @typing.overload
            def __call__(self, source: ParallelQuery_1[SelectMany_3_TSource], collectionSelector: Func_3[SelectMany_3_TSource, int, IEnumerable_1[SelectMany_3_TCollection]], resultSelector: Func_3[SelectMany_3_TSource, SelectMany_3_TCollection, SelectMany_3_TResult]) -> ParallelQuery_1[SelectMany_3_TResult]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[SelectMany_3_TSource], collectionSelector: Func_2[SelectMany_3_TSource, IEnumerable_1[SelectMany_3_TCollection]], resultSelector: Func_3[SelectMany_3_TSource, SelectMany_3_TCollection, SelectMany_3_TResult]) -> ParallelQuery_1[SelectMany_3_TResult]:...


    # Skipped SequenceEqual due to it being static, abstract and generic.

    SequenceEqual : SequenceEqual_MethodGroup
    class SequenceEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[SequenceEqual_1_T1]) -> SequenceEqual_1[SequenceEqual_1_T1]: ...

        SequenceEqual_1_T1 = typing.TypeVar('SequenceEqual_1_T1')
        class SequenceEqual_1(typing.Generic[SequenceEqual_1_T1]):
            SequenceEqual_1_TSource = ParallelEnumerable.SequenceEqual_MethodGroup.SequenceEqual_1_T1
            @typing.overload
            def __call__(self, first: ParallelQuery_1[SequenceEqual_1_TSource], second: ParallelQuery_1[SequenceEqual_1_TSource]) -> bool:...
            @typing.overload
            def __call__(self, first: ParallelQuery_1[SequenceEqual_1_TSource], second: IEnumerable_1[SequenceEqual_1_TSource]) -> bool:...
            @typing.overload
            def __call__(self, first: ParallelQuery_1[SequenceEqual_1_TSource], second: ParallelQuery_1[SequenceEqual_1_TSource], comparer: IEqualityComparer_1[SequenceEqual_1_TSource]) -> bool:...
            @typing.overload
            def __call__(self, first: ParallelQuery_1[SequenceEqual_1_TSource], second: IEnumerable_1[SequenceEqual_1_TSource], comparer: IEqualityComparer_1[SequenceEqual_1_TSource]) -> bool:...


    # Skipped Single due to it being static, abstract and generic.

    Single : Single_MethodGroup
    class Single_MethodGroup:
        def __getitem__(self, t:typing.Type[Single_1_T1]) -> Single_1[Single_1_T1]: ...

        Single_1_T1 = typing.TypeVar('Single_1_T1')
        class Single_1(typing.Generic[Single_1_T1]):
            Single_1_TSource = ParallelEnumerable.Single_MethodGroup.Single_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Single_1_TSource]) -> Single_1_TSource:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Single_1_TSource], predicate: Func_2[Single_1_TSource, bool]) -> Single_1_TSource:...


    # Skipped SingleOrDefault due to it being static, abstract and generic.

    SingleOrDefault : SingleOrDefault_MethodGroup
    class SingleOrDefault_MethodGroup:
        def __getitem__(self, t:typing.Type[SingleOrDefault_1_T1]) -> SingleOrDefault_1[SingleOrDefault_1_T1]: ...

        SingleOrDefault_1_T1 = typing.TypeVar('SingleOrDefault_1_T1')
        class SingleOrDefault_1(typing.Generic[SingleOrDefault_1_T1]):
            SingleOrDefault_1_TSource = ParallelEnumerable.SingleOrDefault_MethodGroup.SingleOrDefault_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[SingleOrDefault_1_TSource]) -> SingleOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[SingleOrDefault_1_TSource], predicate: Func_2[SingleOrDefault_1_TSource, bool]) -> SingleOrDefault_1_TSource:...


    # Skipped Skip due to it being static, abstract and generic.

    Skip : Skip_MethodGroup
    class Skip_MethodGroup:
        def __getitem__(self, t:typing.Type[Skip_1_T1]) -> Skip_1[Skip_1_T1]: ...

        Skip_1_T1 = typing.TypeVar('Skip_1_T1')
        class Skip_1(typing.Generic[Skip_1_T1]):
            Skip_1_TSource = ParallelEnumerable.Skip_MethodGroup.Skip_1_T1
            def __call__(self, source: ParallelQuery_1[Skip_1_TSource], count: int) -> ParallelQuery_1[Skip_1_TSource]:...


    # Skipped SkipWhile due to it being static, abstract and generic.

    SkipWhile : SkipWhile_MethodGroup
    class SkipWhile_MethodGroup:
        def __getitem__(self, t:typing.Type[SkipWhile_1_T1]) -> SkipWhile_1[SkipWhile_1_T1]: ...

        SkipWhile_1_T1 = typing.TypeVar('SkipWhile_1_T1')
        class SkipWhile_1(typing.Generic[SkipWhile_1_T1]):
            SkipWhile_1_TSource = ParallelEnumerable.SkipWhile_MethodGroup.SkipWhile_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[SkipWhile_1_TSource], predicate: Func_3[SkipWhile_1_TSource, int, bool]) -> ParallelQuery_1[SkipWhile_1_TSource]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[SkipWhile_1_TSource], predicate: Func_2[SkipWhile_1_TSource, bool]) -> ParallelQuery_1[SkipWhile_1_TSource]:...


    # Skipped Sum due to it being static, abstract and generic.

    Sum : Sum_MethodGroup
    class Sum_MethodGroup:
        def __getitem__(self, t:typing.Type[Sum_1_T1]) -> Sum_1[Sum_1_T1]: ...

        Sum_1_T1 = typing.TypeVar('Sum_1_T1')
        class Sum_1(typing.Generic[Sum_1_T1]):
            Sum_1_TSource = ParallelEnumerable.Sum_MethodGroup.Sum_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Sum_1_TSource], selector: Func_2[Sum_1_TSource, float]) -> float:...
            # Method Sum(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Sum_1_TSource], selector: Func_2[Sum_1_TSource, int]) -> int:...
            # Method Sum(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Sum_1_TSource], selector: Func_2[Sum_1_TSource, Decimal]) -> Decimal:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Sum_1_TSource], selector: Func_2[Sum_1_TSource, typing.Optional[int]]) -> typing.Optional[int]:...
            # Method Sum(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            # Method Sum(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            # Method Sum(source : ParallelQuery`1, selector : Func`2) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Sum_1_TSource], selector: Func_2[Sum_1_TSource, typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

        @typing.overload
        def __call__(self, source: ParallelQuery_1[float]) -> float:...
        # Method Sum(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Sum(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Sum(source : ParallelQuery`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: ParallelQuery_1[Decimal]) -> Decimal:...
        @typing.overload
        def __call__(self, source: ParallelQuery_1[typing.Optional[int]]) -> typing.Optional[int]:...
        # Method Sum(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Sum(source : ParallelQuery`1) was skipped since it collides with above method
        # Method Sum(source : ParallelQuery`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: ParallelQuery_1[typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

    # Skipped Take due to it being static, abstract and generic.

    Take : Take_MethodGroup
    class Take_MethodGroup:
        def __getitem__(self, t:typing.Type[Take_1_T1]) -> Take_1[Take_1_T1]: ...

        Take_1_T1 = typing.TypeVar('Take_1_T1')
        class Take_1(typing.Generic[Take_1_T1]):
            Take_1_TSource = ParallelEnumerable.Take_MethodGroup.Take_1_T1
            def __call__(self, source: ParallelQuery_1[Take_1_TSource], count: int) -> ParallelQuery_1[Take_1_TSource]:...


    # Skipped TakeWhile due to it being static, abstract and generic.

    TakeWhile : TakeWhile_MethodGroup
    class TakeWhile_MethodGroup:
        def __getitem__(self, t:typing.Type[TakeWhile_1_T1]) -> TakeWhile_1[TakeWhile_1_T1]: ...

        TakeWhile_1_T1 = typing.TypeVar('TakeWhile_1_T1')
        class TakeWhile_1(typing.Generic[TakeWhile_1_T1]):
            TakeWhile_1_TSource = ParallelEnumerable.TakeWhile_MethodGroup.TakeWhile_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[TakeWhile_1_TSource], predicate: Func_3[TakeWhile_1_TSource, int, bool]) -> ParallelQuery_1[TakeWhile_1_TSource]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[TakeWhile_1_TSource], predicate: Func_2[TakeWhile_1_TSource, bool]) -> ParallelQuery_1[TakeWhile_1_TSource]:...


    # Skipped ThenBy due to it being static, abstract and generic.

    ThenBy : ThenBy_MethodGroup
    class ThenBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[ThenBy_2_T1], typing.Type[ThenBy_2_T2]]) -> ThenBy_2[ThenBy_2_T1, ThenBy_2_T2]: ...

        ThenBy_2_T1 = typing.TypeVar('ThenBy_2_T1')
        ThenBy_2_T2 = typing.TypeVar('ThenBy_2_T2')
        class ThenBy_2(typing.Generic[ThenBy_2_T1, ThenBy_2_T2]):
            ThenBy_2_TSource = ParallelEnumerable.ThenBy_MethodGroup.ThenBy_2_T1
            ThenBy_2_TKey = ParallelEnumerable.ThenBy_MethodGroup.ThenBy_2_T2
            @typing.overload
            def __call__(self, source: OrderedParallelQuery_1[ThenBy_2_TSource], keySelector: Func_2[ThenBy_2_TSource, ThenBy_2_TKey]) -> OrderedParallelQuery_1[ThenBy_2_TSource]:...
            @typing.overload
            def __call__(self, source: OrderedParallelQuery_1[ThenBy_2_TSource], keySelector: Func_2[ThenBy_2_TSource, ThenBy_2_TKey], comparer: IComparer_1[ThenBy_2_TKey]) -> OrderedParallelQuery_1[ThenBy_2_TSource]:...


    # Skipped ThenByDescending due to it being static, abstract and generic.

    ThenByDescending : ThenByDescending_MethodGroup
    class ThenByDescending_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[ThenByDescending_2_T1], typing.Type[ThenByDescending_2_T2]]) -> ThenByDescending_2[ThenByDescending_2_T1, ThenByDescending_2_T2]: ...

        ThenByDescending_2_T1 = typing.TypeVar('ThenByDescending_2_T1')
        ThenByDescending_2_T2 = typing.TypeVar('ThenByDescending_2_T2')
        class ThenByDescending_2(typing.Generic[ThenByDescending_2_T1, ThenByDescending_2_T2]):
            ThenByDescending_2_TSource = ParallelEnumerable.ThenByDescending_MethodGroup.ThenByDescending_2_T1
            ThenByDescending_2_TKey = ParallelEnumerable.ThenByDescending_MethodGroup.ThenByDescending_2_T2
            @typing.overload
            def __call__(self, source: OrderedParallelQuery_1[ThenByDescending_2_TSource], keySelector: Func_2[ThenByDescending_2_TSource, ThenByDescending_2_TKey]) -> OrderedParallelQuery_1[ThenByDescending_2_TSource]:...
            @typing.overload
            def __call__(self, source: OrderedParallelQuery_1[ThenByDescending_2_TSource], keySelector: Func_2[ThenByDescending_2_TSource, ThenByDescending_2_TKey], comparer: IComparer_1[ThenByDescending_2_TKey]) -> OrderedParallelQuery_1[ThenByDescending_2_TSource]:...


    # Skipped ToArray due to it being static, abstract and generic.

    ToArray : ToArray_MethodGroup
    class ToArray_MethodGroup:
        def __getitem__(self, t:typing.Type[ToArray_1_T1]) -> ToArray_1[ToArray_1_T1]: ...

        ToArray_1_T1 = typing.TypeVar('ToArray_1_T1')
        class ToArray_1(typing.Generic[ToArray_1_T1]):
            ToArray_1_TSource = ParallelEnumerable.ToArray_MethodGroup.ToArray_1_T1
            def __call__(self, source: ParallelQuery_1[ToArray_1_TSource]) -> Array_1[ToArray_1_TSource]:...


    # Skipped ToDictionary due to it being static, abstract and generic.

    ToDictionary : ToDictionary_MethodGroup
    class ToDictionary_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToDictionary_2_T1], typing.Type[ToDictionary_2_T2]]) -> ToDictionary_2[ToDictionary_2_T1, ToDictionary_2_T2]: ...

        ToDictionary_2_T1 = typing.TypeVar('ToDictionary_2_T1')
        ToDictionary_2_T2 = typing.TypeVar('ToDictionary_2_T2')
        class ToDictionary_2(typing.Generic[ToDictionary_2_T1, ToDictionary_2_T2]):
            ToDictionary_2_TSource = ParallelEnumerable.ToDictionary_MethodGroup.ToDictionary_2_T1
            ToDictionary_2_TKey = ParallelEnumerable.ToDictionary_MethodGroup.ToDictionary_2_T2
            @typing.overload
            def __call__(self, source: ParallelQuery_1[ToDictionary_2_TSource], keySelector: Func_2[ToDictionary_2_TSource, ToDictionary_2_TKey]) -> Dictionary_2[ToDictionary_2_TKey, ToDictionary_2_TSource]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[ToDictionary_2_TSource], keySelector: Func_2[ToDictionary_2_TSource, ToDictionary_2_TKey], comparer: IEqualityComparer_1[ToDictionary_2_TKey]) -> Dictionary_2[ToDictionary_2_TKey, ToDictionary_2_TSource]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToDictionary_3_T1], typing.Type[ToDictionary_3_T2], typing.Type[ToDictionary_3_T3]]) -> ToDictionary_3[ToDictionary_3_T1, ToDictionary_3_T2, ToDictionary_3_T3]: ...

        ToDictionary_3_T1 = typing.TypeVar('ToDictionary_3_T1')
        ToDictionary_3_T2 = typing.TypeVar('ToDictionary_3_T2')
        ToDictionary_3_T3 = typing.TypeVar('ToDictionary_3_T3')
        class ToDictionary_3(typing.Generic[ToDictionary_3_T1, ToDictionary_3_T2, ToDictionary_3_T3]):
            ToDictionary_3_TSource = ParallelEnumerable.ToDictionary_MethodGroup.ToDictionary_3_T1
            ToDictionary_3_TKey = ParallelEnumerable.ToDictionary_MethodGroup.ToDictionary_3_T2
            ToDictionary_3_TElement = ParallelEnumerable.ToDictionary_MethodGroup.ToDictionary_3_T3
            @typing.overload
            def __call__(self, source: ParallelQuery_1[ToDictionary_3_TSource], keySelector: Func_2[ToDictionary_3_TSource, ToDictionary_3_TKey], elementSelector: Func_2[ToDictionary_3_TSource, ToDictionary_3_TElement]) -> Dictionary_2[ToDictionary_3_TKey, ToDictionary_3_TElement]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[ToDictionary_3_TSource], keySelector: Func_2[ToDictionary_3_TSource, ToDictionary_3_TKey], elementSelector: Func_2[ToDictionary_3_TSource, ToDictionary_3_TElement], comparer: IEqualityComparer_1[ToDictionary_3_TKey]) -> Dictionary_2[ToDictionary_3_TKey, ToDictionary_3_TElement]:...


    # Skipped ToList due to it being static, abstract and generic.

    ToList : ToList_MethodGroup
    class ToList_MethodGroup:
        def __getitem__(self, t:typing.Type[ToList_1_T1]) -> ToList_1[ToList_1_T1]: ...

        ToList_1_T1 = typing.TypeVar('ToList_1_T1')
        class ToList_1(typing.Generic[ToList_1_T1]):
            ToList_1_TSource = ParallelEnumerable.ToList_MethodGroup.ToList_1_T1
            def __call__(self, source: ParallelQuery_1[ToList_1_TSource]) -> List_1[ToList_1_TSource]:...


    # Skipped ToLookup due to it being static, abstract and generic.

    ToLookup : ToLookup_MethodGroup
    class ToLookup_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToLookup_2_T1], typing.Type[ToLookup_2_T2]]) -> ToLookup_2[ToLookup_2_T1, ToLookup_2_T2]: ...

        ToLookup_2_T1 = typing.TypeVar('ToLookup_2_T1')
        ToLookup_2_T2 = typing.TypeVar('ToLookup_2_T2')
        class ToLookup_2(typing.Generic[ToLookup_2_T1, ToLookup_2_T2]):
            ToLookup_2_TSource = ParallelEnumerable.ToLookup_MethodGroup.ToLookup_2_T1
            ToLookup_2_TKey = ParallelEnumerable.ToLookup_MethodGroup.ToLookup_2_T2
            @typing.overload
            def __call__(self, source: ParallelQuery_1[ToLookup_2_TSource], keySelector: Func_2[ToLookup_2_TSource, ToLookup_2_TKey]) -> ILookup_2[ToLookup_2_TKey, ToLookup_2_TSource]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[ToLookup_2_TSource], keySelector: Func_2[ToLookup_2_TSource, ToLookup_2_TKey], comparer: IEqualityComparer_1[ToLookup_2_TKey]) -> ILookup_2[ToLookup_2_TKey, ToLookup_2_TSource]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[ToLookup_3_T1], typing.Type[ToLookup_3_T2], typing.Type[ToLookup_3_T3]]) -> ToLookup_3[ToLookup_3_T1, ToLookup_3_T2, ToLookup_3_T3]: ...

        ToLookup_3_T1 = typing.TypeVar('ToLookup_3_T1')
        ToLookup_3_T2 = typing.TypeVar('ToLookup_3_T2')
        ToLookup_3_T3 = typing.TypeVar('ToLookup_3_T3')
        class ToLookup_3(typing.Generic[ToLookup_3_T1, ToLookup_3_T2, ToLookup_3_T3]):
            ToLookup_3_TSource = ParallelEnumerable.ToLookup_MethodGroup.ToLookup_3_T1
            ToLookup_3_TKey = ParallelEnumerable.ToLookup_MethodGroup.ToLookup_3_T2
            ToLookup_3_TElement = ParallelEnumerable.ToLookup_MethodGroup.ToLookup_3_T3
            @typing.overload
            def __call__(self, source: ParallelQuery_1[ToLookup_3_TSource], keySelector: Func_2[ToLookup_3_TSource, ToLookup_3_TKey], elementSelector: Func_2[ToLookup_3_TSource, ToLookup_3_TElement]) -> ILookup_2[ToLookup_3_TKey, ToLookup_3_TElement]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[ToLookup_3_TSource], keySelector: Func_2[ToLookup_3_TSource, ToLookup_3_TKey], elementSelector: Func_2[ToLookup_3_TSource, ToLookup_3_TElement], comparer: IEqualityComparer_1[ToLookup_3_TKey]) -> ILookup_2[ToLookup_3_TKey, ToLookup_3_TElement]:...


    # Skipped Union due to it being static, abstract and generic.

    Union : Union_MethodGroup
    class Union_MethodGroup:
        def __getitem__(self, t:typing.Type[Union_1_T1]) -> Union_1[Union_1_T1]: ...

        Union_1_T1 = typing.TypeVar('Union_1_T1')
        class Union_1(typing.Generic[Union_1_T1]):
            Union_1_TSource = ParallelEnumerable.Union_MethodGroup.Union_1_T1
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Union_1_TSource], second: ParallelQuery_1[Union_1_TSource]) -> ParallelQuery_1[Union_1_TSource]:...
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Union_1_TSource], second: IEnumerable_1[Union_1_TSource]) -> ParallelQuery_1[Union_1_TSource]:...
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Union_1_TSource], second: ParallelQuery_1[Union_1_TSource], comparer: IEqualityComparer_1[Union_1_TSource]) -> ParallelQuery_1[Union_1_TSource]:...
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Union_1_TSource], second: IEnumerable_1[Union_1_TSource], comparer: IEqualityComparer_1[Union_1_TSource]) -> ParallelQuery_1[Union_1_TSource]:...


    # Skipped Where due to it being static, abstract and generic.

    Where : Where_MethodGroup
    class Where_MethodGroup:
        def __getitem__(self, t:typing.Type[Where_1_T1]) -> Where_1[Where_1_T1]: ...

        Where_1_T1 = typing.TypeVar('Where_1_T1')
        class Where_1(typing.Generic[Where_1_T1]):
            Where_1_TSource = ParallelEnumerable.Where_MethodGroup.Where_1_T1
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Where_1_TSource], predicate: Func_3[Where_1_TSource, int, bool]) -> ParallelQuery_1[Where_1_TSource]:...
            @typing.overload
            def __call__(self, source: ParallelQuery_1[Where_1_TSource], predicate: Func_2[Where_1_TSource, bool]) -> ParallelQuery_1[Where_1_TSource]:...


    # Skipped WithCancellation due to it being static, abstract and generic.

    WithCancellation : WithCancellation_MethodGroup
    class WithCancellation_MethodGroup:
        def __getitem__(self, t:typing.Type[WithCancellation_1_T1]) -> WithCancellation_1[WithCancellation_1_T1]: ...

        WithCancellation_1_T1 = typing.TypeVar('WithCancellation_1_T1')
        class WithCancellation_1(typing.Generic[WithCancellation_1_T1]):
            WithCancellation_1_TSource = ParallelEnumerable.WithCancellation_MethodGroup.WithCancellation_1_T1
            def __call__(self, source: ParallelQuery_1[WithCancellation_1_TSource], cancellationToken: CancellationToken) -> ParallelQuery_1[WithCancellation_1_TSource]:...


    # Skipped WithDegreeOfParallelism due to it being static, abstract and generic.

    WithDegreeOfParallelism : WithDegreeOfParallelism_MethodGroup
    class WithDegreeOfParallelism_MethodGroup:
        def __getitem__(self, t:typing.Type[WithDegreeOfParallelism_1_T1]) -> WithDegreeOfParallelism_1[WithDegreeOfParallelism_1_T1]: ...

        WithDegreeOfParallelism_1_T1 = typing.TypeVar('WithDegreeOfParallelism_1_T1')
        class WithDegreeOfParallelism_1(typing.Generic[WithDegreeOfParallelism_1_T1]):
            WithDegreeOfParallelism_1_TSource = ParallelEnumerable.WithDegreeOfParallelism_MethodGroup.WithDegreeOfParallelism_1_T1
            def __call__(self, source: ParallelQuery_1[WithDegreeOfParallelism_1_TSource], degreeOfParallelism: int) -> ParallelQuery_1[WithDegreeOfParallelism_1_TSource]:...


    # Skipped WithExecutionMode due to it being static, abstract and generic.

    WithExecutionMode : WithExecutionMode_MethodGroup
    class WithExecutionMode_MethodGroup:
        def __getitem__(self, t:typing.Type[WithExecutionMode_1_T1]) -> WithExecutionMode_1[WithExecutionMode_1_T1]: ...

        WithExecutionMode_1_T1 = typing.TypeVar('WithExecutionMode_1_T1')
        class WithExecutionMode_1(typing.Generic[WithExecutionMode_1_T1]):
            WithExecutionMode_1_TSource = ParallelEnumerable.WithExecutionMode_MethodGroup.WithExecutionMode_1_T1
            def __call__(self, source: ParallelQuery_1[WithExecutionMode_1_TSource], executionMode: ParallelExecutionMode) -> ParallelQuery_1[WithExecutionMode_1_TSource]:...


    # Skipped WithMergeOptions due to it being static, abstract and generic.

    WithMergeOptions : WithMergeOptions_MethodGroup
    class WithMergeOptions_MethodGroup:
        def __getitem__(self, t:typing.Type[WithMergeOptions_1_T1]) -> WithMergeOptions_1[WithMergeOptions_1_T1]: ...

        WithMergeOptions_1_T1 = typing.TypeVar('WithMergeOptions_1_T1')
        class WithMergeOptions_1(typing.Generic[WithMergeOptions_1_T1]):
            WithMergeOptions_1_TSource = ParallelEnumerable.WithMergeOptions_MethodGroup.WithMergeOptions_1_T1
            def __call__(self, source: ParallelQuery_1[WithMergeOptions_1_TSource], mergeOptions: ParallelMergeOptions) -> ParallelQuery_1[WithMergeOptions_1_TSource]:...


    # Skipped Zip due to it being static, abstract and generic.

    Zip : Zip_MethodGroup
    class Zip_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Zip_3_T1], typing.Type[Zip_3_T2], typing.Type[Zip_3_T3]]) -> Zip_3[Zip_3_T1, Zip_3_T2, Zip_3_T3]: ...

        Zip_3_T1 = typing.TypeVar('Zip_3_T1')
        Zip_3_T2 = typing.TypeVar('Zip_3_T2')
        Zip_3_T3 = typing.TypeVar('Zip_3_T3')
        class Zip_3(typing.Generic[Zip_3_T1, Zip_3_T2, Zip_3_T3]):
            Zip_3_TFirst = ParallelEnumerable.Zip_MethodGroup.Zip_3_T1
            Zip_3_TSecond = ParallelEnumerable.Zip_MethodGroup.Zip_3_T2
            Zip_3_TResult = ParallelEnumerable.Zip_MethodGroup.Zip_3_T3
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Zip_3_TFirst], second: ParallelQuery_1[Zip_3_TSecond], resultSelector: Func_3[Zip_3_TFirst, Zip_3_TSecond, Zip_3_TResult]) -> ParallelQuery_1[Zip_3_TResult]:...
            @typing.overload
            def __call__(self, first: ParallelQuery_1[Zip_3_TFirst], second: IEnumerable_1[Zip_3_TSecond], resultSelector: Func_3[Zip_3_TFirst, Zip_3_TSecond, Zip_3_TResult]) -> ParallelQuery_1[Zip_3_TResult]:...




class ParallelExecutionMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Default : ParallelExecutionMode # 0
    ForceParallelism : ParallelExecutionMode # 1


class ParallelMergeOptions(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Default : ParallelMergeOptions # 0
    NotBuffered : ParallelMergeOptions # 1
    AutoBuffered : ParallelMergeOptions # 2
    FullyBuffered : ParallelMergeOptions # 3


class ParallelQuery_GenericClasses(abc.ABCMeta):
    Generic_ParallelQuery_GenericClasses_ParallelQuery_1_TSource = typing.TypeVar('Generic_ParallelQuery_GenericClasses_ParallelQuery_1_TSource')
    def __getitem__(self, types : typing.Type[Generic_ParallelQuery_GenericClasses_ParallelQuery_1_TSource]) -> typing.Type[ParallelQuery_1[Generic_ParallelQuery_GenericClasses_ParallelQuery_1_TSource]]: ...

class ParallelQuery(ParallelQuery_0, metaclass =ParallelQuery_GenericClasses): ...

class ParallelQuery_0(IEnumerable):
    pass


ParallelQuery_1_TSource = typing.TypeVar('ParallelQuery_1_TSource')
class ParallelQuery_1(typing.Generic[ParallelQuery_1_TSource], ParallelQuery_0, IEnumerable_1[ParallelQuery_1_TSource]):
    def GetEnumerator(self) -> IEnumerator_1[ParallelQuery_1_TSource]: ...


class Queryable(abc.ABC):
    # Skipped Aggregate due to it being static, abstract and generic.

    Aggregate : Aggregate_MethodGroup
    class Aggregate_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[Aggregate_1_T1]) -> Aggregate_1[Aggregate_1_T1]: ...

        Aggregate_1_T1 = typing.TypeVar('Aggregate_1_T1')
        class Aggregate_1(typing.Generic[Aggregate_1_T1]):
            Aggregate_1_TSource = Queryable.Aggregate_MethodGroup.Aggregate_1_T1
            def __call__(self, source: IQueryable_1[Aggregate_1_TSource], func: Expression_1[Func_3[Aggregate_1_TSource, Aggregate_1_TSource, Aggregate_1_TSource]]) -> Aggregate_1_TSource:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Aggregate_2_T1], typing.Type[Aggregate_2_T2]]) -> Aggregate_2[Aggregate_2_T1, Aggregate_2_T2]: ...

        Aggregate_2_T1 = typing.TypeVar('Aggregate_2_T1')
        Aggregate_2_T2 = typing.TypeVar('Aggregate_2_T2')
        class Aggregate_2(typing.Generic[Aggregate_2_T1, Aggregate_2_T2]):
            Aggregate_2_TSource = Queryable.Aggregate_MethodGroup.Aggregate_2_T1
            Aggregate_2_TAccumulate = Queryable.Aggregate_MethodGroup.Aggregate_2_T2
            def __call__(self, source: IQueryable_1[Aggregate_2_TSource], seed: Aggregate_2_TAccumulate, func: Expression_1[Func_3[Aggregate_2_TAccumulate, Aggregate_2_TSource, Aggregate_2_TAccumulate]]) -> Aggregate_2_TAccumulate:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Aggregate_3_T1], typing.Type[Aggregate_3_T2], typing.Type[Aggregate_3_T3]]) -> Aggregate_3[Aggregate_3_T1, Aggregate_3_T2, Aggregate_3_T3]: ...

        Aggregate_3_T1 = typing.TypeVar('Aggregate_3_T1')
        Aggregate_3_T2 = typing.TypeVar('Aggregate_3_T2')
        Aggregate_3_T3 = typing.TypeVar('Aggregate_3_T3')
        class Aggregate_3(typing.Generic[Aggregate_3_T1, Aggregate_3_T2, Aggregate_3_T3]):
            Aggregate_3_TSource = Queryable.Aggregate_MethodGroup.Aggregate_3_T1
            Aggregate_3_TAccumulate = Queryable.Aggregate_MethodGroup.Aggregate_3_T2
            Aggregate_3_TResult = Queryable.Aggregate_MethodGroup.Aggregate_3_T3
            def __call__(self, source: IQueryable_1[Aggregate_3_TSource], seed: Aggregate_3_TAccumulate, func: Expression_1[Func_3[Aggregate_3_TAccumulate, Aggregate_3_TSource, Aggregate_3_TAccumulate]], selector: Expression_1[Func_2[Aggregate_3_TAccumulate, Aggregate_3_TResult]]) -> Aggregate_3_TResult:...


    # Skipped All due to it being static, abstract and generic.

    All : All_MethodGroup
    class All_MethodGroup:
        def __getitem__(self, t:typing.Type[All_1_T1]) -> All_1[All_1_T1]: ...

        All_1_T1 = typing.TypeVar('All_1_T1')
        class All_1(typing.Generic[All_1_T1]):
            All_1_TSource = Queryable.All_MethodGroup.All_1_T1
            def __call__(self, source: IQueryable_1[All_1_TSource], predicate: Expression_1[Func_2[All_1_TSource, bool]]) -> bool:...


    # Skipped Any due to it being static, abstract and generic.

    Any : Any_MethodGroup
    class Any_MethodGroup:
        def __getitem__(self, t:typing.Type[Any_1_T1]) -> Any_1[Any_1_T1]: ...

        Any_1_T1 = typing.TypeVar('Any_1_T1')
        class Any_1(typing.Generic[Any_1_T1]):
            Any_1_TSource = Queryable.Any_MethodGroup.Any_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[Any_1_TSource]) -> bool:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Any_1_TSource], predicate: Expression_1[Func_2[Any_1_TSource, bool]]) -> bool:...


    # Skipped Append due to it being static, abstract and generic.

    Append : Append_MethodGroup
    class Append_MethodGroup:
        def __getitem__(self, t:typing.Type[Append_1_T1]) -> Append_1[Append_1_T1]: ...

        Append_1_T1 = typing.TypeVar('Append_1_T1')
        class Append_1(typing.Generic[Append_1_T1]):
            Append_1_TSource = Queryable.Append_MethodGroup.Append_1_T1
            def __call__(self, source: IQueryable_1[Append_1_TSource], element: Append_1_TSource) -> IQueryable_1[Append_1_TSource]:...


    # Skipped AsQueryable due to it being static, abstract and generic.

    AsQueryable : AsQueryable_MethodGroup
    class AsQueryable_MethodGroup:
        def __getitem__(self, t:typing.Type[AsQueryable_1_T1]) -> AsQueryable_1[AsQueryable_1_T1]: ...

        AsQueryable_1_T1 = typing.TypeVar('AsQueryable_1_T1')
        class AsQueryable_1(typing.Generic[AsQueryable_1_T1]):
            AsQueryable_1_TElement = Queryable.AsQueryable_MethodGroup.AsQueryable_1_T1
            def __call__(self, source: IEnumerable_1[AsQueryable_1_TElement]) -> IQueryable_1[AsQueryable_1_TElement]:...

        def __call__(self, source: IEnumerable) -> IQueryable:...

    # Skipped Average due to it being static, abstract and generic.

    Average : Average_MethodGroup
    class Average_MethodGroup:
        def __getitem__(self, t:typing.Type[Average_1_T1]) -> Average_1[Average_1_T1]: ...

        Average_1_T1 = typing.TypeVar('Average_1_T1')
        class Average_1(typing.Generic[Average_1_T1]):
            Average_1_TSource = Queryable.Average_MethodGroup.Average_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[Average_1_TSource], selector: Expression_1[Func_2[Average_1_TSource, int]]) -> float:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Average_1_TSource], selector: Expression_1[Func_2[Average_1_TSource, typing.Optional[int]]]) -> typing.Optional[float]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Average_1_TSource], selector: Expression_1[Func_2[Average_1_TSource, float]]) -> float:...
            # Method Average(source : IQueryable`1, selector : Expression`1) was skipped since it collides with above method
            # Method Average(source : IQueryable`1, selector : Expression`1) was skipped since it collides with above method
            # Method Average(source : IQueryable`1, selector : Expression`1) was skipped since it collides with above method
            # Method Average(source : IQueryable`1, selector : Expression`1) was skipped since it collides with above method
            # Method Average(source : IQueryable`1, selector : Expression`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: IQueryable_1[Average_1_TSource], selector: Expression_1[Func_2[Average_1_TSource, Decimal]]) -> Decimal:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Average_1_TSource], selector: Expression_1[Func_2[Average_1_TSource, typing.Optional[Decimal]]]) -> typing.Optional[Decimal]:...

        @typing.overload
        def __call__(self, source: IQueryable_1[float]) -> float:...
        # Method Average(source : IQueryable`1) was skipped since it collides with above method
        # Method Average(source : IQueryable`1) was skipped since it collides with above method
        # Method Average(source : IQueryable`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: IQueryable_1[Decimal]) -> Decimal:...
        @typing.overload
        def __call__(self, source: IQueryable_1[typing.Optional[int]]) -> typing.Optional[float]:...
        # Method Average(source : IQueryable`1) was skipped since it collides with above method
        # Method Average(source : IQueryable`1) was skipped since it collides with above method
        # Method Average(source : IQueryable`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: IQueryable_1[typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

    # Skipped Cast due to it being static, abstract and generic.

    Cast : Cast_MethodGroup
    class Cast_MethodGroup:
        def __getitem__(self, t:typing.Type[Cast_1_T1]) -> Cast_1[Cast_1_T1]: ...

        Cast_1_T1 = typing.TypeVar('Cast_1_T1')
        class Cast_1(typing.Generic[Cast_1_T1]):
            Cast_1_TResult = Queryable.Cast_MethodGroup.Cast_1_T1
            def __call__(self, source: IQueryable) -> IQueryable_1[Cast_1_TResult]:...


    # Skipped Chunk due to it being static, abstract and generic.

    Chunk : Chunk_MethodGroup
    class Chunk_MethodGroup:
        def __getitem__(self, t:typing.Type[Chunk_1_T1]) -> Chunk_1[Chunk_1_T1]: ...

        Chunk_1_T1 = typing.TypeVar('Chunk_1_T1')
        class Chunk_1(typing.Generic[Chunk_1_T1]):
            Chunk_1_TSource = Queryable.Chunk_MethodGroup.Chunk_1_T1
            def __call__(self, source: IQueryable_1[Chunk_1_TSource], size: int) -> IQueryable_1[Array_1[Chunk_1_TSource]]:...


    # Skipped Concat due to it being static, abstract and generic.

    Concat : Concat_MethodGroup
    class Concat_MethodGroup:
        def __getitem__(self, t:typing.Type[Concat_1_T1]) -> Concat_1[Concat_1_T1]: ...

        Concat_1_T1 = typing.TypeVar('Concat_1_T1')
        class Concat_1(typing.Generic[Concat_1_T1]):
            Concat_1_TSource = Queryable.Concat_MethodGroup.Concat_1_T1
            def __call__(self, source1: IQueryable_1[Concat_1_TSource], source2: IEnumerable_1[Concat_1_TSource]) -> IQueryable_1[Concat_1_TSource]:...


    # Skipped Contains due to it being static, abstract and generic.

    Contains : Contains_MethodGroup
    class Contains_MethodGroup:
        def __getitem__(self, t:typing.Type[Contains_1_T1]) -> Contains_1[Contains_1_T1]: ...

        Contains_1_T1 = typing.TypeVar('Contains_1_T1')
        class Contains_1(typing.Generic[Contains_1_T1]):
            Contains_1_TSource = Queryable.Contains_MethodGroup.Contains_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[Contains_1_TSource], item: Contains_1_TSource) -> bool:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Contains_1_TSource], item: Contains_1_TSource, comparer: IEqualityComparer_1[Contains_1_TSource]) -> bool:...


    # Skipped Count due to it being static, abstract and generic.

    Count : Count_MethodGroup
    class Count_MethodGroup:
        def __getitem__(self, t:typing.Type[Count_1_T1]) -> Count_1[Count_1_T1]: ...

        Count_1_T1 = typing.TypeVar('Count_1_T1')
        class Count_1(typing.Generic[Count_1_T1]):
            Count_1_TSource = Queryable.Count_MethodGroup.Count_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[Count_1_TSource]) -> int:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Count_1_TSource], predicate: Expression_1[Func_2[Count_1_TSource, bool]]) -> int:...


    # Skipped DefaultIfEmpty due to it being static, abstract and generic.

    DefaultIfEmpty : DefaultIfEmpty_MethodGroup
    class DefaultIfEmpty_MethodGroup:
        def __getitem__(self, t:typing.Type[DefaultIfEmpty_1_T1]) -> DefaultIfEmpty_1[DefaultIfEmpty_1_T1]: ...

        DefaultIfEmpty_1_T1 = typing.TypeVar('DefaultIfEmpty_1_T1')
        class DefaultIfEmpty_1(typing.Generic[DefaultIfEmpty_1_T1]):
            DefaultIfEmpty_1_TSource = Queryable.DefaultIfEmpty_MethodGroup.DefaultIfEmpty_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[DefaultIfEmpty_1_TSource]) -> IQueryable_1[DefaultIfEmpty_1_TSource]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[DefaultIfEmpty_1_TSource], defaultValue: DefaultIfEmpty_1_TSource) -> IQueryable_1[DefaultIfEmpty_1_TSource]:...


    # Skipped Distinct due to it being static, abstract and generic.

    Distinct : Distinct_MethodGroup
    class Distinct_MethodGroup:
        def __getitem__(self, t:typing.Type[Distinct_1_T1]) -> Distinct_1[Distinct_1_T1]: ...

        Distinct_1_T1 = typing.TypeVar('Distinct_1_T1')
        class Distinct_1(typing.Generic[Distinct_1_T1]):
            Distinct_1_TSource = Queryable.Distinct_MethodGroup.Distinct_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[Distinct_1_TSource]) -> IQueryable_1[Distinct_1_TSource]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Distinct_1_TSource], comparer: IEqualityComparer_1[Distinct_1_TSource]) -> IQueryable_1[Distinct_1_TSource]:...


    # Skipped DistinctBy due to it being static, abstract and generic.

    DistinctBy : DistinctBy_MethodGroup
    class DistinctBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[DistinctBy_2_T1], typing.Type[DistinctBy_2_T2]]) -> DistinctBy_2[DistinctBy_2_T1, DistinctBy_2_T2]: ...

        DistinctBy_2_T1 = typing.TypeVar('DistinctBy_2_T1')
        DistinctBy_2_T2 = typing.TypeVar('DistinctBy_2_T2')
        class DistinctBy_2(typing.Generic[DistinctBy_2_T1, DistinctBy_2_T2]):
            DistinctBy_2_TSource = Queryable.DistinctBy_MethodGroup.DistinctBy_2_T1
            DistinctBy_2_TKey = Queryable.DistinctBy_MethodGroup.DistinctBy_2_T2
            @typing.overload
            def __call__(self, source: IQueryable_1[DistinctBy_2_TSource], keySelector: Expression_1[Func_2[DistinctBy_2_TSource, DistinctBy_2_TKey]]) -> IQueryable_1[DistinctBy_2_TSource]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[DistinctBy_2_TSource], keySelector: Expression_1[Func_2[DistinctBy_2_TSource, DistinctBy_2_TKey]], comparer: IEqualityComparer_1[DistinctBy_2_TKey]) -> IQueryable_1[DistinctBy_2_TSource]:...


    # Skipped ElementAt due to it being static, abstract and generic.

    ElementAt : ElementAt_MethodGroup
    class ElementAt_MethodGroup:
        def __getitem__(self, t:typing.Type[ElementAt_1_T1]) -> ElementAt_1[ElementAt_1_T1]: ...

        ElementAt_1_T1 = typing.TypeVar('ElementAt_1_T1')
        class ElementAt_1(typing.Generic[ElementAt_1_T1]):
            ElementAt_1_TSource = Queryable.ElementAt_MethodGroup.ElementAt_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[ElementAt_1_TSource], index: int) -> ElementAt_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[ElementAt_1_TSource], index: Index) -> ElementAt_1_TSource:...


    # Skipped ElementAtOrDefault due to it being static, abstract and generic.

    ElementAtOrDefault : ElementAtOrDefault_MethodGroup
    class ElementAtOrDefault_MethodGroup:
        def __getitem__(self, t:typing.Type[ElementAtOrDefault_1_T1]) -> ElementAtOrDefault_1[ElementAtOrDefault_1_T1]: ...

        ElementAtOrDefault_1_T1 = typing.TypeVar('ElementAtOrDefault_1_T1')
        class ElementAtOrDefault_1(typing.Generic[ElementAtOrDefault_1_T1]):
            ElementAtOrDefault_1_TSource = Queryable.ElementAtOrDefault_MethodGroup.ElementAtOrDefault_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[ElementAtOrDefault_1_TSource], index: int) -> ElementAtOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[ElementAtOrDefault_1_TSource], index: Index) -> ElementAtOrDefault_1_TSource:...


    # Skipped Except due to it being static, abstract and generic.

    Except : Except_MethodGroup
    class Except_MethodGroup:
        def __getitem__(self, t:typing.Type[Except_1_T1]) -> Except_1[Except_1_T1]: ...

        Except_1_T1 = typing.TypeVar('Except_1_T1')
        class Except_1(typing.Generic[Except_1_T1]):
            Except_1_TSource = Queryable.Except_MethodGroup.Except_1_T1
            @typing.overload
            def __call__(self, source1: IQueryable_1[Except_1_TSource], source2: IEnumerable_1[Except_1_TSource]) -> IQueryable_1[Except_1_TSource]:...
            @typing.overload
            def __call__(self, source1: IQueryable_1[Except_1_TSource], source2: IEnumerable_1[Except_1_TSource], comparer: IEqualityComparer_1[Except_1_TSource]) -> IQueryable_1[Except_1_TSource]:...


    # Skipped ExceptBy due to it being static, abstract and generic.

    ExceptBy : ExceptBy_MethodGroup
    class ExceptBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[ExceptBy_2_T1], typing.Type[ExceptBy_2_T2]]) -> ExceptBy_2[ExceptBy_2_T1, ExceptBy_2_T2]: ...

        ExceptBy_2_T1 = typing.TypeVar('ExceptBy_2_T1')
        ExceptBy_2_T2 = typing.TypeVar('ExceptBy_2_T2')
        class ExceptBy_2(typing.Generic[ExceptBy_2_T1, ExceptBy_2_T2]):
            ExceptBy_2_TSource = Queryable.ExceptBy_MethodGroup.ExceptBy_2_T1
            ExceptBy_2_TKey = Queryable.ExceptBy_MethodGroup.ExceptBy_2_T2
            @typing.overload
            def __call__(self, source1: IQueryable_1[ExceptBy_2_TSource], source2: IEnumerable_1[ExceptBy_2_TKey], keySelector: Expression_1[Func_2[ExceptBy_2_TSource, ExceptBy_2_TKey]]) -> IQueryable_1[ExceptBy_2_TSource]:...
            @typing.overload
            def __call__(self, source1: IQueryable_1[ExceptBy_2_TSource], source2: IEnumerable_1[ExceptBy_2_TKey], keySelector: Expression_1[Func_2[ExceptBy_2_TSource, ExceptBy_2_TKey]], comparer: IEqualityComparer_1[ExceptBy_2_TKey]) -> IQueryable_1[ExceptBy_2_TSource]:...


    # Skipped First due to it being static, abstract and generic.

    First : First_MethodGroup
    class First_MethodGroup:
        def __getitem__(self, t:typing.Type[First_1_T1]) -> First_1[First_1_T1]: ...

        First_1_T1 = typing.TypeVar('First_1_T1')
        class First_1(typing.Generic[First_1_T1]):
            First_1_TSource = Queryable.First_MethodGroup.First_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[First_1_TSource]) -> First_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[First_1_TSource], predicate: Expression_1[Func_2[First_1_TSource, bool]]) -> First_1_TSource:...


    # Skipped FirstOrDefault due to it being static, abstract and generic.

    FirstOrDefault : FirstOrDefault_MethodGroup
    class FirstOrDefault_MethodGroup:
        def __getitem__(self, t:typing.Type[FirstOrDefault_1_T1]) -> FirstOrDefault_1[FirstOrDefault_1_T1]: ...

        FirstOrDefault_1_T1 = typing.TypeVar('FirstOrDefault_1_T1')
        class FirstOrDefault_1(typing.Generic[FirstOrDefault_1_T1]):
            FirstOrDefault_1_TSource = Queryable.FirstOrDefault_MethodGroup.FirstOrDefault_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[FirstOrDefault_1_TSource]) -> FirstOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[FirstOrDefault_1_TSource], predicate: Expression_1[Func_2[FirstOrDefault_1_TSource, bool]]) -> FirstOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[FirstOrDefault_1_TSource], defaultValue: FirstOrDefault_1_TSource) -> FirstOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[FirstOrDefault_1_TSource], predicate: Expression_1[Func_2[FirstOrDefault_1_TSource, bool]], defaultValue: FirstOrDefault_1_TSource) -> FirstOrDefault_1_TSource:...


    # Skipped GroupBy due to it being static, abstract and generic.

    GroupBy : GroupBy_MethodGroup
    class GroupBy_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[GroupBy_2_T1], typing.Type[GroupBy_2_T2]]) -> GroupBy_2[GroupBy_2_T1, GroupBy_2_T2]: ...

        GroupBy_2_T1 = typing.TypeVar('GroupBy_2_T1')
        GroupBy_2_T2 = typing.TypeVar('GroupBy_2_T2')
        class GroupBy_2(typing.Generic[GroupBy_2_T1, GroupBy_2_T2]):
            GroupBy_2_TSource = Queryable.GroupBy_MethodGroup.GroupBy_2_T1
            GroupBy_2_TKey = Queryable.GroupBy_MethodGroup.GroupBy_2_T2
            @typing.overload
            def __call__(self, source: IQueryable_1[GroupBy_2_TSource], keySelector: Expression_1[Func_2[GroupBy_2_TSource, GroupBy_2_TKey]]) -> IQueryable_1[IGrouping_2[GroupBy_2_TKey, GroupBy_2_TSource]]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[GroupBy_2_TSource], keySelector: Expression_1[Func_2[GroupBy_2_TSource, GroupBy_2_TKey]], comparer: IEqualityComparer_1[GroupBy_2_TKey]) -> IQueryable_1[IGrouping_2[GroupBy_2_TKey, GroupBy_2_TSource]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[GroupBy_3_T1], typing.Type[GroupBy_3_T2], typing.Type[GroupBy_3_T3]]) -> GroupBy_3[GroupBy_3_T1, GroupBy_3_T2, GroupBy_3_T3]: ...

        GroupBy_3_T1 = typing.TypeVar('GroupBy_3_T1')
        GroupBy_3_T2 = typing.TypeVar('GroupBy_3_T2')
        GroupBy_3_T3 = typing.TypeVar('GroupBy_3_T3')
        class GroupBy_3(typing.Generic[GroupBy_3_T1, GroupBy_3_T2, GroupBy_3_T3]):
            GroupBy_3_TSource = Queryable.GroupBy_MethodGroup.GroupBy_3_T1
            GroupBy_3_TKey = Queryable.GroupBy_MethodGroup.GroupBy_3_T2
            GroupBy_3_TElement = Queryable.GroupBy_MethodGroup.GroupBy_3_T3
            GroupBy_3_TResult = Queryable.GroupBy_MethodGroup.GroupBy_3_T3
            @typing.overload
            def __call__(self, source: IQueryable_1[GroupBy_3_TSource], keySelector: Expression_1[Func_2[GroupBy_3_TSource, GroupBy_3_TKey]], elementSelector: Expression_1[Func_2[GroupBy_3_TSource, GroupBy_3_TElement]]) -> IQueryable_1[IGrouping_2[GroupBy_3_TKey, GroupBy_3_TElement]]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[GroupBy_3_TSource], keySelector: Expression_1[Func_2[GroupBy_3_TSource, GroupBy_3_TKey]], resultSelector: Expression_1[Func_3[GroupBy_3_TKey, IEnumerable_1[GroupBy_3_TSource], GroupBy_3_TResult]]) -> IQueryable_1[GroupBy_3_TResult]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[GroupBy_3_TSource], keySelector: Expression_1[Func_2[GroupBy_3_TSource, GroupBy_3_TKey]], elementSelector: Expression_1[Func_2[GroupBy_3_TSource, GroupBy_3_TElement]], comparer: IEqualityComparer_1[GroupBy_3_TKey]) -> IQueryable_1[IGrouping_2[GroupBy_3_TKey, GroupBy_3_TElement]]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[GroupBy_3_TSource], keySelector: Expression_1[Func_2[GroupBy_3_TSource, GroupBy_3_TKey]], resultSelector: Expression_1[Func_3[GroupBy_3_TKey, IEnumerable_1[GroupBy_3_TSource], GroupBy_3_TResult]], comparer: IEqualityComparer_1[GroupBy_3_TKey]) -> IQueryable_1[GroupBy_3_TResult]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[GroupBy_4_T1], typing.Type[GroupBy_4_T2], typing.Type[GroupBy_4_T3], typing.Type[GroupBy_4_T4]]) -> GroupBy_4[GroupBy_4_T1, GroupBy_4_T2, GroupBy_4_T3, GroupBy_4_T4]: ...

        GroupBy_4_T1 = typing.TypeVar('GroupBy_4_T1')
        GroupBy_4_T2 = typing.TypeVar('GroupBy_4_T2')
        GroupBy_4_T3 = typing.TypeVar('GroupBy_4_T3')
        GroupBy_4_T4 = typing.TypeVar('GroupBy_4_T4')
        class GroupBy_4(typing.Generic[GroupBy_4_T1, GroupBy_4_T2, GroupBy_4_T3, GroupBy_4_T4]):
            GroupBy_4_TSource = Queryable.GroupBy_MethodGroup.GroupBy_4_T1
            GroupBy_4_TKey = Queryable.GroupBy_MethodGroup.GroupBy_4_T2
            GroupBy_4_TElement = Queryable.GroupBy_MethodGroup.GroupBy_4_T3
            GroupBy_4_TResult = Queryable.GroupBy_MethodGroup.GroupBy_4_T4
            @typing.overload
            def __call__(self, source: IQueryable_1[GroupBy_4_TSource], keySelector: Expression_1[Func_2[GroupBy_4_TSource, GroupBy_4_TKey]], elementSelector: Expression_1[Func_2[GroupBy_4_TSource, GroupBy_4_TElement]], resultSelector: Expression_1[Func_3[GroupBy_4_TKey, IEnumerable_1[GroupBy_4_TElement], GroupBy_4_TResult]]) -> IQueryable_1[GroupBy_4_TResult]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[GroupBy_4_TSource], keySelector: Expression_1[Func_2[GroupBy_4_TSource, GroupBy_4_TKey]], elementSelector: Expression_1[Func_2[GroupBy_4_TSource, GroupBy_4_TElement]], resultSelector: Expression_1[Func_3[GroupBy_4_TKey, IEnumerable_1[GroupBy_4_TElement], GroupBy_4_TResult]], comparer: IEqualityComparer_1[GroupBy_4_TKey]) -> IQueryable_1[GroupBy_4_TResult]:...


    # Skipped GroupJoin due to it being static, abstract and generic.

    GroupJoin : GroupJoin_MethodGroup
    class GroupJoin_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[GroupJoin_4_T1], typing.Type[GroupJoin_4_T2], typing.Type[GroupJoin_4_T3], typing.Type[GroupJoin_4_T4]]) -> GroupJoin_4[GroupJoin_4_T1, GroupJoin_4_T2, GroupJoin_4_T3, GroupJoin_4_T4]: ...

        GroupJoin_4_T1 = typing.TypeVar('GroupJoin_4_T1')
        GroupJoin_4_T2 = typing.TypeVar('GroupJoin_4_T2')
        GroupJoin_4_T3 = typing.TypeVar('GroupJoin_4_T3')
        GroupJoin_4_T4 = typing.TypeVar('GroupJoin_4_T4')
        class GroupJoin_4(typing.Generic[GroupJoin_4_T1, GroupJoin_4_T2, GroupJoin_4_T3, GroupJoin_4_T4]):
            GroupJoin_4_TOuter = Queryable.GroupJoin_MethodGroup.GroupJoin_4_T1
            GroupJoin_4_TInner = Queryable.GroupJoin_MethodGroup.GroupJoin_4_T2
            GroupJoin_4_TKey = Queryable.GroupJoin_MethodGroup.GroupJoin_4_T3
            GroupJoin_4_TResult = Queryable.GroupJoin_MethodGroup.GroupJoin_4_T4
            @typing.overload
            def __call__(self, outer: IQueryable_1[GroupJoin_4_TOuter], inner: IEnumerable_1[GroupJoin_4_TInner], outerKeySelector: Expression_1[Func_2[GroupJoin_4_TOuter, GroupJoin_4_TKey]], innerKeySelector: Expression_1[Func_2[GroupJoin_4_TInner, GroupJoin_4_TKey]], resultSelector: Expression_1[Func_3[GroupJoin_4_TOuter, IEnumerable_1[GroupJoin_4_TInner], GroupJoin_4_TResult]]) -> IQueryable_1[GroupJoin_4_TResult]:...
            @typing.overload
            def __call__(self, outer: IQueryable_1[GroupJoin_4_TOuter], inner: IEnumerable_1[GroupJoin_4_TInner], outerKeySelector: Expression_1[Func_2[GroupJoin_4_TOuter, GroupJoin_4_TKey]], innerKeySelector: Expression_1[Func_2[GroupJoin_4_TInner, GroupJoin_4_TKey]], resultSelector: Expression_1[Func_3[GroupJoin_4_TOuter, IEnumerable_1[GroupJoin_4_TInner], GroupJoin_4_TResult]], comparer: IEqualityComparer_1[GroupJoin_4_TKey]) -> IQueryable_1[GroupJoin_4_TResult]:...


    # Skipped Intersect due to it being static, abstract and generic.

    Intersect : Intersect_MethodGroup
    class Intersect_MethodGroup:
        def __getitem__(self, t:typing.Type[Intersect_1_T1]) -> Intersect_1[Intersect_1_T1]: ...

        Intersect_1_T1 = typing.TypeVar('Intersect_1_T1')
        class Intersect_1(typing.Generic[Intersect_1_T1]):
            Intersect_1_TSource = Queryable.Intersect_MethodGroup.Intersect_1_T1
            @typing.overload
            def __call__(self, source1: IQueryable_1[Intersect_1_TSource], source2: IEnumerable_1[Intersect_1_TSource]) -> IQueryable_1[Intersect_1_TSource]:...
            @typing.overload
            def __call__(self, source1: IQueryable_1[Intersect_1_TSource], source2: IEnumerable_1[Intersect_1_TSource], comparer: IEqualityComparer_1[Intersect_1_TSource]) -> IQueryable_1[Intersect_1_TSource]:...


    # Skipped IntersectBy due to it being static, abstract and generic.

    IntersectBy : IntersectBy_MethodGroup
    class IntersectBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[IntersectBy_2_T1], typing.Type[IntersectBy_2_T2]]) -> IntersectBy_2[IntersectBy_2_T1, IntersectBy_2_T2]: ...

        IntersectBy_2_T1 = typing.TypeVar('IntersectBy_2_T1')
        IntersectBy_2_T2 = typing.TypeVar('IntersectBy_2_T2')
        class IntersectBy_2(typing.Generic[IntersectBy_2_T1, IntersectBy_2_T2]):
            IntersectBy_2_TSource = Queryable.IntersectBy_MethodGroup.IntersectBy_2_T1
            IntersectBy_2_TKey = Queryable.IntersectBy_MethodGroup.IntersectBy_2_T2
            @typing.overload
            def __call__(self, source1: IQueryable_1[IntersectBy_2_TSource], source2: IEnumerable_1[IntersectBy_2_TKey], keySelector: Expression_1[Func_2[IntersectBy_2_TSource, IntersectBy_2_TKey]]) -> IQueryable_1[IntersectBy_2_TSource]:...
            @typing.overload
            def __call__(self, source1: IQueryable_1[IntersectBy_2_TSource], source2: IEnumerable_1[IntersectBy_2_TKey], keySelector: Expression_1[Func_2[IntersectBy_2_TSource, IntersectBy_2_TKey]], comparer: IEqualityComparer_1[IntersectBy_2_TKey]) -> IQueryable_1[IntersectBy_2_TSource]:...


    # Skipped Join due to it being static, abstract and generic.

    Join : Join_MethodGroup
    class Join_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Join_4_T1], typing.Type[Join_4_T2], typing.Type[Join_4_T3], typing.Type[Join_4_T4]]) -> Join_4[Join_4_T1, Join_4_T2, Join_4_T3, Join_4_T4]: ...

        Join_4_T1 = typing.TypeVar('Join_4_T1')
        Join_4_T2 = typing.TypeVar('Join_4_T2')
        Join_4_T3 = typing.TypeVar('Join_4_T3')
        Join_4_T4 = typing.TypeVar('Join_4_T4')
        class Join_4(typing.Generic[Join_4_T1, Join_4_T2, Join_4_T3, Join_4_T4]):
            Join_4_TOuter = Queryable.Join_MethodGroup.Join_4_T1
            Join_4_TInner = Queryable.Join_MethodGroup.Join_4_T2
            Join_4_TKey = Queryable.Join_MethodGroup.Join_4_T3
            Join_4_TResult = Queryable.Join_MethodGroup.Join_4_T4
            @typing.overload
            def __call__(self, outer: IQueryable_1[Join_4_TOuter], inner: IEnumerable_1[Join_4_TInner], outerKeySelector: Expression_1[Func_2[Join_4_TOuter, Join_4_TKey]], innerKeySelector: Expression_1[Func_2[Join_4_TInner, Join_4_TKey]], resultSelector: Expression_1[Func_3[Join_4_TOuter, Join_4_TInner, Join_4_TResult]]) -> IQueryable_1[Join_4_TResult]:...
            @typing.overload
            def __call__(self, outer: IQueryable_1[Join_4_TOuter], inner: IEnumerable_1[Join_4_TInner], outerKeySelector: Expression_1[Func_2[Join_4_TOuter, Join_4_TKey]], innerKeySelector: Expression_1[Func_2[Join_4_TInner, Join_4_TKey]], resultSelector: Expression_1[Func_3[Join_4_TOuter, Join_4_TInner, Join_4_TResult]], comparer: IEqualityComparer_1[Join_4_TKey]) -> IQueryable_1[Join_4_TResult]:...


    # Skipped Last due to it being static, abstract and generic.

    Last : Last_MethodGroup
    class Last_MethodGroup:
        def __getitem__(self, t:typing.Type[Last_1_T1]) -> Last_1[Last_1_T1]: ...

        Last_1_T1 = typing.TypeVar('Last_1_T1')
        class Last_1(typing.Generic[Last_1_T1]):
            Last_1_TSource = Queryable.Last_MethodGroup.Last_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[Last_1_TSource]) -> Last_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Last_1_TSource], predicate: Expression_1[Func_2[Last_1_TSource, bool]]) -> Last_1_TSource:...


    # Skipped LastOrDefault due to it being static, abstract and generic.

    LastOrDefault : LastOrDefault_MethodGroup
    class LastOrDefault_MethodGroup:
        def __getitem__(self, t:typing.Type[LastOrDefault_1_T1]) -> LastOrDefault_1[LastOrDefault_1_T1]: ...

        LastOrDefault_1_T1 = typing.TypeVar('LastOrDefault_1_T1')
        class LastOrDefault_1(typing.Generic[LastOrDefault_1_T1]):
            LastOrDefault_1_TSource = Queryable.LastOrDefault_MethodGroup.LastOrDefault_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[LastOrDefault_1_TSource]) -> LastOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[LastOrDefault_1_TSource], predicate: Expression_1[Func_2[LastOrDefault_1_TSource, bool]]) -> LastOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[LastOrDefault_1_TSource], defaultValue: LastOrDefault_1_TSource) -> LastOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[LastOrDefault_1_TSource], predicate: Expression_1[Func_2[LastOrDefault_1_TSource, bool]], defaultValue: LastOrDefault_1_TSource) -> LastOrDefault_1_TSource:...


    # Skipped LongCount due to it being static, abstract and generic.

    LongCount : LongCount_MethodGroup
    class LongCount_MethodGroup:
        def __getitem__(self, t:typing.Type[LongCount_1_T1]) -> LongCount_1[LongCount_1_T1]: ...

        LongCount_1_T1 = typing.TypeVar('LongCount_1_T1')
        class LongCount_1(typing.Generic[LongCount_1_T1]):
            LongCount_1_TSource = Queryable.LongCount_MethodGroup.LongCount_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[LongCount_1_TSource]) -> int:...
            @typing.overload
            def __call__(self, source: IQueryable_1[LongCount_1_TSource], predicate: Expression_1[Func_2[LongCount_1_TSource, bool]]) -> int:...


    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[Max_1_T1]) -> Max_1[Max_1_T1]: ...

        Max_1_T1 = typing.TypeVar('Max_1_T1')
        class Max_1(typing.Generic[Max_1_T1]):
            Max_1_TSource = Queryable.Max_MethodGroup.Max_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[Max_1_TSource]) -> Max_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Max_1_TSource], comparer: IComparer_1[Max_1_TSource]) -> Max_1_TSource:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Max_2_T1], typing.Type[Max_2_T2]]) -> Max_2[Max_2_T1, Max_2_T2]: ...

        Max_2_T1 = typing.TypeVar('Max_2_T1')
        Max_2_T2 = typing.TypeVar('Max_2_T2')
        class Max_2(typing.Generic[Max_2_T1, Max_2_T2]):
            Max_2_TSource = Queryable.Max_MethodGroup.Max_2_T1
            Max_2_TResult = Queryable.Max_MethodGroup.Max_2_T2
            def __call__(self, source: IQueryable_1[Max_2_TSource], selector: Expression_1[Func_2[Max_2_TSource, Max_2_TResult]]) -> Max_2_TResult:...


    # Skipped MaxBy due to it being static, abstract and generic.

    MaxBy : MaxBy_MethodGroup
    class MaxBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[MaxBy_2_T1], typing.Type[MaxBy_2_T2]]) -> MaxBy_2[MaxBy_2_T1, MaxBy_2_T2]: ...

        MaxBy_2_T1 = typing.TypeVar('MaxBy_2_T1')
        MaxBy_2_T2 = typing.TypeVar('MaxBy_2_T2')
        class MaxBy_2(typing.Generic[MaxBy_2_T1, MaxBy_2_T2]):
            MaxBy_2_TSource = Queryable.MaxBy_MethodGroup.MaxBy_2_T1
            MaxBy_2_TKey = Queryable.MaxBy_MethodGroup.MaxBy_2_T2
            @typing.overload
            def __call__(self, source: IQueryable_1[MaxBy_2_TSource], keySelector: Expression_1[Func_2[MaxBy_2_TSource, MaxBy_2_TKey]]) -> MaxBy_2_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[MaxBy_2_TSource], keySelector: Expression_1[Func_2[MaxBy_2_TSource, MaxBy_2_TKey]], comparer: IComparer_1[MaxBy_2_TSource]) -> MaxBy_2_TSource:...


    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[Min_1_T1]) -> Min_1[Min_1_T1]: ...

        Min_1_T1 = typing.TypeVar('Min_1_T1')
        class Min_1(typing.Generic[Min_1_T1]):
            Min_1_TSource = Queryable.Min_MethodGroup.Min_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[Min_1_TSource]) -> Min_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Min_1_TSource], comparer: IComparer_1[Min_1_TSource]) -> Min_1_TSource:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Min_2_T1], typing.Type[Min_2_T2]]) -> Min_2[Min_2_T1, Min_2_T2]: ...

        Min_2_T1 = typing.TypeVar('Min_2_T1')
        Min_2_T2 = typing.TypeVar('Min_2_T2')
        class Min_2(typing.Generic[Min_2_T1, Min_2_T2]):
            Min_2_TSource = Queryable.Min_MethodGroup.Min_2_T1
            Min_2_TResult = Queryable.Min_MethodGroup.Min_2_T2
            def __call__(self, source: IQueryable_1[Min_2_TSource], selector: Expression_1[Func_2[Min_2_TSource, Min_2_TResult]]) -> Min_2_TResult:...


    # Skipped MinBy due to it being static, abstract and generic.

    MinBy : MinBy_MethodGroup
    class MinBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[MinBy_2_T1], typing.Type[MinBy_2_T2]]) -> MinBy_2[MinBy_2_T1, MinBy_2_T2]: ...

        MinBy_2_T1 = typing.TypeVar('MinBy_2_T1')
        MinBy_2_T2 = typing.TypeVar('MinBy_2_T2')
        class MinBy_2(typing.Generic[MinBy_2_T1, MinBy_2_T2]):
            MinBy_2_TSource = Queryable.MinBy_MethodGroup.MinBy_2_T1
            MinBy_2_TKey = Queryable.MinBy_MethodGroup.MinBy_2_T2
            @typing.overload
            def __call__(self, source: IQueryable_1[MinBy_2_TSource], keySelector: Expression_1[Func_2[MinBy_2_TSource, MinBy_2_TKey]]) -> MinBy_2_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[MinBy_2_TSource], keySelector: Expression_1[Func_2[MinBy_2_TSource, MinBy_2_TKey]], comparer: IComparer_1[MinBy_2_TSource]) -> MinBy_2_TSource:...


    # Skipped OfType due to it being static, abstract and generic.

    OfType : OfType_MethodGroup
    class OfType_MethodGroup:
        def __getitem__(self, t:typing.Type[OfType_1_T1]) -> OfType_1[OfType_1_T1]: ...

        OfType_1_T1 = typing.TypeVar('OfType_1_T1')
        class OfType_1(typing.Generic[OfType_1_T1]):
            OfType_1_TResult = Queryable.OfType_MethodGroup.OfType_1_T1
            def __call__(self, source: IQueryable) -> IQueryable_1[OfType_1_TResult]:...


    # Skipped OrderBy due to it being static, abstract and generic.

    OrderBy : OrderBy_MethodGroup
    class OrderBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[OrderBy_2_T1], typing.Type[OrderBy_2_T2]]) -> OrderBy_2[OrderBy_2_T1, OrderBy_2_T2]: ...

        OrderBy_2_T1 = typing.TypeVar('OrderBy_2_T1')
        OrderBy_2_T2 = typing.TypeVar('OrderBy_2_T2')
        class OrderBy_2(typing.Generic[OrderBy_2_T1, OrderBy_2_T2]):
            OrderBy_2_TSource = Queryable.OrderBy_MethodGroup.OrderBy_2_T1
            OrderBy_2_TKey = Queryable.OrderBy_MethodGroup.OrderBy_2_T2
            @typing.overload
            def __call__(self, source: IQueryable_1[OrderBy_2_TSource], keySelector: Expression_1[Func_2[OrderBy_2_TSource, OrderBy_2_TKey]]) -> IOrderedQueryable_1[OrderBy_2_TSource]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[OrderBy_2_TSource], keySelector: Expression_1[Func_2[OrderBy_2_TSource, OrderBy_2_TKey]], comparer: IComparer_1[OrderBy_2_TKey]) -> IOrderedQueryable_1[OrderBy_2_TSource]:...


    # Skipped OrderByDescending due to it being static, abstract and generic.

    OrderByDescending : OrderByDescending_MethodGroup
    class OrderByDescending_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[OrderByDescending_2_T1], typing.Type[OrderByDescending_2_T2]]) -> OrderByDescending_2[OrderByDescending_2_T1, OrderByDescending_2_T2]: ...

        OrderByDescending_2_T1 = typing.TypeVar('OrderByDescending_2_T1')
        OrderByDescending_2_T2 = typing.TypeVar('OrderByDescending_2_T2')
        class OrderByDescending_2(typing.Generic[OrderByDescending_2_T1, OrderByDescending_2_T2]):
            OrderByDescending_2_TSource = Queryable.OrderByDescending_MethodGroup.OrderByDescending_2_T1
            OrderByDescending_2_TKey = Queryable.OrderByDescending_MethodGroup.OrderByDescending_2_T2
            @typing.overload
            def __call__(self, source: IQueryable_1[OrderByDescending_2_TSource], keySelector: Expression_1[Func_2[OrderByDescending_2_TSource, OrderByDescending_2_TKey]]) -> IOrderedQueryable_1[OrderByDescending_2_TSource]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[OrderByDescending_2_TSource], keySelector: Expression_1[Func_2[OrderByDescending_2_TSource, OrderByDescending_2_TKey]], comparer: IComparer_1[OrderByDescending_2_TKey]) -> IOrderedQueryable_1[OrderByDescending_2_TSource]:...


    # Skipped Prepend due to it being static, abstract and generic.

    Prepend : Prepend_MethodGroup
    class Prepend_MethodGroup:
        def __getitem__(self, t:typing.Type[Prepend_1_T1]) -> Prepend_1[Prepend_1_T1]: ...

        Prepend_1_T1 = typing.TypeVar('Prepend_1_T1')
        class Prepend_1(typing.Generic[Prepend_1_T1]):
            Prepend_1_TSource = Queryable.Prepend_MethodGroup.Prepend_1_T1
            def __call__(self, source: IQueryable_1[Prepend_1_TSource], element: Prepend_1_TSource) -> IQueryable_1[Prepend_1_TSource]:...


    # Skipped Reverse due to it being static, abstract and generic.

    Reverse : Reverse_MethodGroup
    class Reverse_MethodGroup:
        def __getitem__(self, t:typing.Type[Reverse_1_T1]) -> Reverse_1[Reverse_1_T1]: ...

        Reverse_1_T1 = typing.TypeVar('Reverse_1_T1')
        class Reverse_1(typing.Generic[Reverse_1_T1]):
            Reverse_1_TSource = Queryable.Reverse_MethodGroup.Reverse_1_T1
            def __call__(self, source: IQueryable_1[Reverse_1_TSource]) -> IQueryable_1[Reverse_1_TSource]:...


    # Skipped Select due to it being static, abstract and generic.

    Select : Select_MethodGroup
    class Select_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Select_2_T1], typing.Type[Select_2_T2]]) -> Select_2[Select_2_T1, Select_2_T2]: ...

        Select_2_T1 = typing.TypeVar('Select_2_T1')
        Select_2_T2 = typing.TypeVar('Select_2_T2')
        class Select_2(typing.Generic[Select_2_T1, Select_2_T2]):
            Select_2_TSource = Queryable.Select_MethodGroup.Select_2_T1
            Select_2_TResult = Queryable.Select_MethodGroup.Select_2_T2
            @typing.overload
            def __call__(self, source: IQueryable_1[Select_2_TSource], selector: Expression_1[Func_2[Select_2_TSource, Select_2_TResult]]) -> IQueryable_1[Select_2_TResult]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Select_2_TSource], selector: Expression_1[Func_3[Select_2_TSource, int, Select_2_TResult]]) -> IQueryable_1[Select_2_TResult]:...


    # Skipped SelectMany due to it being static, abstract and generic.

    SelectMany : SelectMany_MethodGroup
    class SelectMany_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[SelectMany_2_T1], typing.Type[SelectMany_2_T2]]) -> SelectMany_2[SelectMany_2_T1, SelectMany_2_T2]: ...

        SelectMany_2_T1 = typing.TypeVar('SelectMany_2_T1')
        SelectMany_2_T2 = typing.TypeVar('SelectMany_2_T2')
        class SelectMany_2(typing.Generic[SelectMany_2_T1, SelectMany_2_T2]):
            SelectMany_2_TSource = Queryable.SelectMany_MethodGroup.SelectMany_2_T1
            SelectMany_2_TResult = Queryable.SelectMany_MethodGroup.SelectMany_2_T2
            @typing.overload
            def __call__(self, source: IQueryable_1[SelectMany_2_TSource], selector: Expression_1[Func_2[SelectMany_2_TSource, IEnumerable_1[SelectMany_2_TResult]]]) -> IQueryable_1[SelectMany_2_TResult]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[SelectMany_2_TSource], selector: Expression_1[Func_3[SelectMany_2_TSource, int, IEnumerable_1[SelectMany_2_TResult]]]) -> IQueryable_1[SelectMany_2_TResult]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[SelectMany_3_T1], typing.Type[SelectMany_3_T2], typing.Type[SelectMany_3_T3]]) -> SelectMany_3[SelectMany_3_T1, SelectMany_3_T2, SelectMany_3_T3]: ...

        SelectMany_3_T1 = typing.TypeVar('SelectMany_3_T1')
        SelectMany_3_T2 = typing.TypeVar('SelectMany_3_T2')
        SelectMany_3_T3 = typing.TypeVar('SelectMany_3_T3')
        class SelectMany_3(typing.Generic[SelectMany_3_T1, SelectMany_3_T2, SelectMany_3_T3]):
            SelectMany_3_TSource = Queryable.SelectMany_MethodGroup.SelectMany_3_T1
            SelectMany_3_TCollection = Queryable.SelectMany_MethodGroup.SelectMany_3_T2
            SelectMany_3_TResult = Queryable.SelectMany_MethodGroup.SelectMany_3_T3
            @typing.overload
            def __call__(self, source: IQueryable_1[SelectMany_3_TSource], collectionSelector: Expression_1[Func_3[SelectMany_3_TSource, int, IEnumerable_1[SelectMany_3_TCollection]]], resultSelector: Expression_1[Func_3[SelectMany_3_TSource, SelectMany_3_TCollection, SelectMany_3_TResult]]) -> IQueryable_1[SelectMany_3_TResult]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[SelectMany_3_TSource], collectionSelector: Expression_1[Func_2[SelectMany_3_TSource, IEnumerable_1[SelectMany_3_TCollection]]], resultSelector: Expression_1[Func_3[SelectMany_3_TSource, SelectMany_3_TCollection, SelectMany_3_TResult]]) -> IQueryable_1[SelectMany_3_TResult]:...


    # Skipped SequenceEqual due to it being static, abstract and generic.

    SequenceEqual : SequenceEqual_MethodGroup
    class SequenceEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[SequenceEqual_1_T1]) -> SequenceEqual_1[SequenceEqual_1_T1]: ...

        SequenceEqual_1_T1 = typing.TypeVar('SequenceEqual_1_T1')
        class SequenceEqual_1(typing.Generic[SequenceEqual_1_T1]):
            SequenceEqual_1_TSource = Queryable.SequenceEqual_MethodGroup.SequenceEqual_1_T1
            @typing.overload
            def __call__(self, source1: IQueryable_1[SequenceEqual_1_TSource], source2: IEnumerable_1[SequenceEqual_1_TSource]) -> bool:...
            @typing.overload
            def __call__(self, source1: IQueryable_1[SequenceEqual_1_TSource], source2: IEnumerable_1[SequenceEqual_1_TSource], comparer: IEqualityComparer_1[SequenceEqual_1_TSource]) -> bool:...


    # Skipped Single due to it being static, abstract and generic.

    Single : Single_MethodGroup
    class Single_MethodGroup:
        def __getitem__(self, t:typing.Type[Single_1_T1]) -> Single_1[Single_1_T1]: ...

        Single_1_T1 = typing.TypeVar('Single_1_T1')
        class Single_1(typing.Generic[Single_1_T1]):
            Single_1_TSource = Queryable.Single_MethodGroup.Single_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[Single_1_TSource]) -> Single_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Single_1_TSource], predicate: Expression_1[Func_2[Single_1_TSource, bool]]) -> Single_1_TSource:...


    # Skipped SingleOrDefault due to it being static, abstract and generic.

    SingleOrDefault : SingleOrDefault_MethodGroup
    class SingleOrDefault_MethodGroup:
        def __getitem__(self, t:typing.Type[SingleOrDefault_1_T1]) -> SingleOrDefault_1[SingleOrDefault_1_T1]: ...

        SingleOrDefault_1_T1 = typing.TypeVar('SingleOrDefault_1_T1')
        class SingleOrDefault_1(typing.Generic[SingleOrDefault_1_T1]):
            SingleOrDefault_1_TSource = Queryable.SingleOrDefault_MethodGroup.SingleOrDefault_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[SingleOrDefault_1_TSource]) -> SingleOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[SingleOrDefault_1_TSource], predicate: Expression_1[Func_2[SingleOrDefault_1_TSource, bool]]) -> SingleOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[SingleOrDefault_1_TSource], defaultValue: SingleOrDefault_1_TSource) -> SingleOrDefault_1_TSource:...
            @typing.overload
            def __call__(self, source: IQueryable_1[SingleOrDefault_1_TSource], predicate: Expression_1[Func_2[SingleOrDefault_1_TSource, bool]], defaultValue: SingleOrDefault_1_TSource) -> SingleOrDefault_1_TSource:...


    # Skipped Skip due to it being static, abstract and generic.

    Skip : Skip_MethodGroup
    class Skip_MethodGroup:
        def __getitem__(self, t:typing.Type[Skip_1_T1]) -> Skip_1[Skip_1_T1]: ...

        Skip_1_T1 = typing.TypeVar('Skip_1_T1')
        class Skip_1(typing.Generic[Skip_1_T1]):
            Skip_1_TSource = Queryable.Skip_MethodGroup.Skip_1_T1
            def __call__(self, source: IQueryable_1[Skip_1_TSource], count: int) -> IQueryable_1[Skip_1_TSource]:...


    # Skipped SkipLast due to it being static, abstract and generic.

    SkipLast : SkipLast_MethodGroup
    class SkipLast_MethodGroup:
        def __getitem__(self, t:typing.Type[SkipLast_1_T1]) -> SkipLast_1[SkipLast_1_T1]: ...

        SkipLast_1_T1 = typing.TypeVar('SkipLast_1_T1')
        class SkipLast_1(typing.Generic[SkipLast_1_T1]):
            SkipLast_1_TSource = Queryable.SkipLast_MethodGroup.SkipLast_1_T1
            def __call__(self, source: IQueryable_1[SkipLast_1_TSource], count: int) -> IQueryable_1[SkipLast_1_TSource]:...


    # Skipped SkipWhile due to it being static, abstract and generic.

    SkipWhile : SkipWhile_MethodGroup
    class SkipWhile_MethodGroup:
        def __getitem__(self, t:typing.Type[SkipWhile_1_T1]) -> SkipWhile_1[SkipWhile_1_T1]: ...

        SkipWhile_1_T1 = typing.TypeVar('SkipWhile_1_T1')
        class SkipWhile_1(typing.Generic[SkipWhile_1_T1]):
            SkipWhile_1_TSource = Queryable.SkipWhile_MethodGroup.SkipWhile_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[SkipWhile_1_TSource], predicate: Expression_1[Func_2[SkipWhile_1_TSource, bool]]) -> IQueryable_1[SkipWhile_1_TSource]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[SkipWhile_1_TSource], predicate: Expression_1[Func_3[SkipWhile_1_TSource, int, bool]]) -> IQueryable_1[SkipWhile_1_TSource]:...


    # Skipped Sum due to it being static, abstract and generic.

    Sum : Sum_MethodGroup
    class Sum_MethodGroup:
        def __getitem__(self, t:typing.Type[Sum_1_T1]) -> Sum_1[Sum_1_T1]: ...

        Sum_1_T1 = typing.TypeVar('Sum_1_T1')
        class Sum_1(typing.Generic[Sum_1_T1]):
            Sum_1_TSource = Queryable.Sum_MethodGroup.Sum_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[Sum_1_TSource], selector: Expression_1[Func_2[Sum_1_TSource, int]]) -> int:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Sum_1_TSource], selector: Expression_1[Func_2[Sum_1_TSource, typing.Optional[int]]]) -> typing.Optional[int]:...
            # Method Sum(source : IQueryable`1, selector : Expression`1) was skipped since it collides with above method
            # Method Sum(source : IQueryable`1, selector : Expression`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: IQueryable_1[Sum_1_TSource], selector: Expression_1[Func_2[Sum_1_TSource, float]]) -> float:...
            # Method Sum(source : IQueryable`1, selector : Expression`1) was skipped since it collides with above method
            # Method Sum(source : IQueryable`1, selector : Expression`1) was skipped since it collides with above method
            # Method Sum(source : IQueryable`1, selector : Expression`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, source: IQueryable_1[Sum_1_TSource], selector: Expression_1[Func_2[Sum_1_TSource, Decimal]]) -> Decimal:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Sum_1_TSource], selector: Expression_1[Func_2[Sum_1_TSource, typing.Optional[Decimal]]]) -> typing.Optional[Decimal]:...

        @typing.overload
        def __call__(self, source: IQueryable_1[float]) -> float:...
        # Method Sum(source : IQueryable`1) was skipped since it collides with above method
        # Method Sum(source : IQueryable`1) was skipped since it collides with above method
        # Method Sum(source : IQueryable`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: IQueryable_1[Decimal]) -> Decimal:...
        @typing.overload
        def __call__(self, source: IQueryable_1[typing.Optional[int]]) -> typing.Optional[int]:...
        # Method Sum(source : IQueryable`1) was skipped since it collides with above method
        # Method Sum(source : IQueryable`1) was skipped since it collides with above method
        # Method Sum(source : IQueryable`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: IQueryable_1[typing.Optional[Decimal]]) -> typing.Optional[Decimal]:...

    # Skipped Take due to it being static, abstract and generic.

    Take : Take_MethodGroup
    class Take_MethodGroup:
        def __getitem__(self, t:typing.Type[Take_1_T1]) -> Take_1[Take_1_T1]: ...

        Take_1_T1 = typing.TypeVar('Take_1_T1')
        class Take_1(typing.Generic[Take_1_T1]):
            Take_1_TSource = Queryable.Take_MethodGroup.Take_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[Take_1_TSource], count: int) -> IQueryable_1[Take_1_TSource]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Take_1_TSource], range: Range) -> IQueryable_1[Take_1_TSource]:...


    # Skipped TakeLast due to it being static, abstract and generic.

    TakeLast : TakeLast_MethodGroup
    class TakeLast_MethodGroup:
        def __getitem__(self, t:typing.Type[TakeLast_1_T1]) -> TakeLast_1[TakeLast_1_T1]: ...

        TakeLast_1_T1 = typing.TypeVar('TakeLast_1_T1')
        class TakeLast_1(typing.Generic[TakeLast_1_T1]):
            TakeLast_1_TSource = Queryable.TakeLast_MethodGroup.TakeLast_1_T1
            def __call__(self, source: IQueryable_1[TakeLast_1_TSource], count: int) -> IQueryable_1[TakeLast_1_TSource]:...


    # Skipped TakeWhile due to it being static, abstract and generic.

    TakeWhile : TakeWhile_MethodGroup
    class TakeWhile_MethodGroup:
        def __getitem__(self, t:typing.Type[TakeWhile_1_T1]) -> TakeWhile_1[TakeWhile_1_T1]: ...

        TakeWhile_1_T1 = typing.TypeVar('TakeWhile_1_T1')
        class TakeWhile_1(typing.Generic[TakeWhile_1_T1]):
            TakeWhile_1_TSource = Queryable.TakeWhile_MethodGroup.TakeWhile_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[TakeWhile_1_TSource], predicate: Expression_1[Func_2[TakeWhile_1_TSource, bool]]) -> IQueryable_1[TakeWhile_1_TSource]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[TakeWhile_1_TSource], predicate: Expression_1[Func_3[TakeWhile_1_TSource, int, bool]]) -> IQueryable_1[TakeWhile_1_TSource]:...


    # Skipped ThenBy due to it being static, abstract and generic.

    ThenBy : ThenBy_MethodGroup
    class ThenBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[ThenBy_2_T1], typing.Type[ThenBy_2_T2]]) -> ThenBy_2[ThenBy_2_T1, ThenBy_2_T2]: ...

        ThenBy_2_T1 = typing.TypeVar('ThenBy_2_T1')
        ThenBy_2_T2 = typing.TypeVar('ThenBy_2_T2')
        class ThenBy_2(typing.Generic[ThenBy_2_T1, ThenBy_2_T2]):
            ThenBy_2_TSource = Queryable.ThenBy_MethodGroup.ThenBy_2_T1
            ThenBy_2_TKey = Queryable.ThenBy_MethodGroup.ThenBy_2_T2
            @typing.overload
            def __call__(self, source: IOrderedQueryable_1[ThenBy_2_TSource], keySelector: Expression_1[Func_2[ThenBy_2_TSource, ThenBy_2_TKey]]) -> IOrderedQueryable_1[ThenBy_2_TSource]:...
            @typing.overload
            def __call__(self, source: IOrderedQueryable_1[ThenBy_2_TSource], keySelector: Expression_1[Func_2[ThenBy_2_TSource, ThenBy_2_TKey]], comparer: IComparer_1[ThenBy_2_TKey]) -> IOrderedQueryable_1[ThenBy_2_TSource]:...


    # Skipped ThenByDescending due to it being static, abstract and generic.

    ThenByDescending : ThenByDescending_MethodGroup
    class ThenByDescending_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[ThenByDescending_2_T1], typing.Type[ThenByDescending_2_T2]]) -> ThenByDescending_2[ThenByDescending_2_T1, ThenByDescending_2_T2]: ...

        ThenByDescending_2_T1 = typing.TypeVar('ThenByDescending_2_T1')
        ThenByDescending_2_T2 = typing.TypeVar('ThenByDescending_2_T2')
        class ThenByDescending_2(typing.Generic[ThenByDescending_2_T1, ThenByDescending_2_T2]):
            ThenByDescending_2_TSource = Queryable.ThenByDescending_MethodGroup.ThenByDescending_2_T1
            ThenByDescending_2_TKey = Queryable.ThenByDescending_MethodGroup.ThenByDescending_2_T2
            @typing.overload
            def __call__(self, source: IOrderedQueryable_1[ThenByDescending_2_TSource], keySelector: Expression_1[Func_2[ThenByDescending_2_TSource, ThenByDescending_2_TKey]]) -> IOrderedQueryable_1[ThenByDescending_2_TSource]:...
            @typing.overload
            def __call__(self, source: IOrderedQueryable_1[ThenByDescending_2_TSource], keySelector: Expression_1[Func_2[ThenByDescending_2_TSource, ThenByDescending_2_TKey]], comparer: IComparer_1[ThenByDescending_2_TKey]) -> IOrderedQueryable_1[ThenByDescending_2_TSource]:...


    # Skipped Union due to it being static, abstract and generic.

    Union : Union_MethodGroup
    class Union_MethodGroup:
        def __getitem__(self, t:typing.Type[Union_1_T1]) -> Union_1[Union_1_T1]: ...

        Union_1_T1 = typing.TypeVar('Union_1_T1')
        class Union_1(typing.Generic[Union_1_T1]):
            Union_1_TSource = Queryable.Union_MethodGroup.Union_1_T1
            @typing.overload
            def __call__(self, source1: IQueryable_1[Union_1_TSource], source2: IEnumerable_1[Union_1_TSource]) -> IQueryable_1[Union_1_TSource]:...
            @typing.overload
            def __call__(self, source1: IQueryable_1[Union_1_TSource], source2: IEnumerable_1[Union_1_TSource], comparer: IEqualityComparer_1[Union_1_TSource]) -> IQueryable_1[Union_1_TSource]:...


    # Skipped UnionBy due to it being static, abstract and generic.

    UnionBy : UnionBy_MethodGroup
    class UnionBy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[UnionBy_2_T1], typing.Type[UnionBy_2_T2]]) -> UnionBy_2[UnionBy_2_T1, UnionBy_2_T2]: ...

        UnionBy_2_T1 = typing.TypeVar('UnionBy_2_T1')
        UnionBy_2_T2 = typing.TypeVar('UnionBy_2_T2')
        class UnionBy_2(typing.Generic[UnionBy_2_T1, UnionBy_2_T2]):
            UnionBy_2_TSource = Queryable.UnionBy_MethodGroup.UnionBy_2_T1
            UnionBy_2_TKey = Queryable.UnionBy_MethodGroup.UnionBy_2_T2
            @typing.overload
            def __call__(self, source1: IQueryable_1[UnionBy_2_TSource], source2: IEnumerable_1[UnionBy_2_TSource], keySelector: Expression_1[Func_2[UnionBy_2_TSource, UnionBy_2_TKey]]) -> IQueryable_1[UnionBy_2_TSource]:...
            @typing.overload
            def __call__(self, source1: IQueryable_1[UnionBy_2_TSource], source2: IEnumerable_1[UnionBy_2_TSource], keySelector: Expression_1[Func_2[UnionBy_2_TSource, UnionBy_2_TKey]], comparer: IEqualityComparer_1[UnionBy_2_TKey]) -> IQueryable_1[UnionBy_2_TSource]:...


    # Skipped Where due to it being static, abstract and generic.

    Where : Where_MethodGroup
    class Where_MethodGroup:
        def __getitem__(self, t:typing.Type[Where_1_T1]) -> Where_1[Where_1_T1]: ...

        Where_1_T1 = typing.TypeVar('Where_1_T1')
        class Where_1(typing.Generic[Where_1_T1]):
            Where_1_TSource = Queryable.Where_MethodGroup.Where_1_T1
            @typing.overload
            def __call__(self, source: IQueryable_1[Where_1_TSource], predicate: Expression_1[Func_2[Where_1_TSource, bool]]) -> IQueryable_1[Where_1_TSource]:...
            @typing.overload
            def __call__(self, source: IQueryable_1[Where_1_TSource], predicate: Expression_1[Func_3[Where_1_TSource, int, bool]]) -> IQueryable_1[Where_1_TSource]:...


    # Skipped Zip due to it being static, abstract and generic.

    Zip : Zip_MethodGroup
    class Zip_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Zip_2_T1], typing.Type[Zip_2_T2]]) -> Zip_2[Zip_2_T1, Zip_2_T2]: ...

        Zip_2_T1 = typing.TypeVar('Zip_2_T1')
        Zip_2_T2 = typing.TypeVar('Zip_2_T2')
        class Zip_2(typing.Generic[Zip_2_T1, Zip_2_T2]):
            Zip_2_TFirst = Queryable.Zip_MethodGroup.Zip_2_T1
            Zip_2_TSecond = Queryable.Zip_MethodGroup.Zip_2_T2
            def __call__(self, source1: IQueryable_1[Zip_2_TFirst], source2: IEnumerable_1[Zip_2_TSecond]) -> IQueryable_1[ValueTuple_2[Zip_2_TFirst, Zip_2_TSecond]]:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[Zip_3_T1], typing.Type[Zip_3_T2], typing.Type[Zip_3_T3]]) -> Zip_3[Zip_3_T1, Zip_3_T2, Zip_3_T3]: ...

        Zip_3_T1 = typing.TypeVar('Zip_3_T1')
        Zip_3_T2 = typing.TypeVar('Zip_3_T2')
        Zip_3_T3 = typing.TypeVar('Zip_3_T3')
        class Zip_3(typing.Generic[Zip_3_T1, Zip_3_T2, Zip_3_T3]):
            Zip_3_TFirst = Queryable.Zip_MethodGroup.Zip_3_T1
            Zip_3_TSecond = Queryable.Zip_MethodGroup.Zip_3_T2
            Zip_3_TResult = Queryable.Zip_MethodGroup.Zip_3_T3
            Zip_3_TThird = Queryable.Zip_MethodGroup.Zip_3_T3
            @typing.overload
            def __call__(self, source1: IQueryable_1[Zip_3_TFirst], source2: IEnumerable_1[Zip_3_TSecond], resultSelector: Expression_1[Func_3[Zip_3_TFirst, Zip_3_TSecond, Zip_3_TResult]]) -> IQueryable_1[Zip_3_TResult]:...
            @typing.overload
            def __call__(self, source1: IQueryable_1[Zip_3_TFirst], source2: IEnumerable_1[Zip_3_TSecond], source3: IEnumerable_1[Zip_3_TThird]) -> IQueryable_1[ValueTuple_3[Zip_3_TFirst, Zip_3_TSecond, Zip_3_TThird]]:...



