# -*- coding: utf-8 -*-

from abc import ABCMeta
from typing import Any, Callable, NoReturn, TypeVar, Union, overload

from typing_extensions import Literal, final

from returns.primitives.monad import Monad

_MonadType = TypeVar('_MonadType', bound='Monad')
_ValueType = TypeVar('_ValueType')
_NewValueType = TypeVar('_NewValueType')


class Maybe(Monad[_ValueType], metaclass=ABCMeta):
    @overload
    @classmethod
    def new(cls, inner_value: Literal[None]) -> 'Nothing':  # type: ignore
        ...

    @overload  # noqa: F811
    @classmethod
    def new(cls, inner_value: _ValueType) -> 'Some[_ValueType]':
        ...

    def fmap(
        self,
        function: Callable[[_ValueType], _NewValueType],
    ) -> _MonadType:
        ...

    def bind(
        self,
        function: Callable[[_ValueType], _MonadType],
    ) -> _MonadType:
        ...

    def efmap(self, function) -> 'Some[_NewValueType]':
        ...

    def ebind(self, function) -> _MonadType:
        ...

    def value_or(
        self,
        default_value: _NewValueType,
    ) -> Union[_ValueType, _NewValueType]:
        ...

    def unwrap(self) -> Union[NoReturn, _ValueType]:
        ...

    def failure(self) -> Union[NoReturn, Literal[None]]:
        ...


@final
class Nothing(Maybe[Any]):
    _inner_value: Literal[None]

    def __init__(self, inner_value: Literal[None] = ...) -> None:
        ...

    def fmap(self, function) -> 'Nothing':  # type: ignore
        ...

    def bind(self, function) -> 'Nothing':  # type: ignore
        ...

    def efmap(
        self,
        function: Callable[[Literal[None]], '_NewValueType'],
    ) -> 'Some[_NewValueType]':
        ...

    def ebind(
        self,
        function: Callable[[Literal[None]], _MonadType],
    ) -> _MonadType:
        ...

    def value_or(self, default_value: _NewValueType) -> _NewValueType:
        ...

    def unwrap(self) -> NoReturn:
        ...

    def failure(self) -> Literal[None]:
        ...


@final
class Some(Maybe[_ValueType]):
    _inner_value: _ValueType

    def __init__(self, inner_value: _ValueType) -> None:
        ...

    def fmap(  # type: ignore
        self,
        function: Callable[[_ValueType], _NewValueType],
    ) -> 'Some[_NewValueType]':
        ...

    def bind(
        self,
        function: Callable[[_ValueType], _MonadType],
    ) -> _MonadType:
        ...

    def efmap(self, function) -> 'Some[_ValueType]':  # type: ignore
        ...

    def ebind(self, function) -> 'Some[_ValueType]':  # type: ignore
        ...

    def value_or(self, default_value: _NewValueType) -> _ValueType:
        ...

    def unwrap(self) -> _ValueType:
        ...

    def failure(self) -> NoReturn:
        ...