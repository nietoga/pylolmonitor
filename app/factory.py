from typing import Type, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")


class Factory[T](ABC):
    @abstractmethod
    def instantiate(*args, **kwargs) -> T:
        pass


def factorify(T: Type[T], *default_args, **default_kwargs) -> Factory[T]:
    def merged_args(default_args, args):
        if len(args) >= len(default_args):
            return [*args]
        return [*args, *default_args[len(args) :]]

    def merged_kwargs(default_kwargs, kwargs):
        return {**default_kwargs, **kwargs}

    class CustomFactory(Factory[T]):
        def instantiate(*args, **kwargs) -> T:
            return T(
                *merged_args(default_args, args),
                **merged_kwargs(default_kwargs, kwargs),
            )

    return CustomFactory
