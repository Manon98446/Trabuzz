from collections.abc import Callable, MutableMapping
from typing import Any, ClassVar, NoReturn
from typing_extensions import TypedDict

from jmespath.functions import Functions

class Options:
    dict_cls: Callable[[], MutableMapping[Any, Any]] | None
    custom_functions: Functions | None
    def __init__(
        self, dict_cls: Callable[[], MutableMapping[Any, Any]] | None = None, custom_functions: Functions | None = None
    ) -> None: ...

class _Expression:
    expression: str
    interpreter: Visitor
    def __init__(self, expression: str, interpreter: Visitor) -> None: ...
    def visit(self, node: _TreeNode, *args, **kwargs) -> Any: ...

class Visitor:
    def __init__(self) -> None: ...
    def visit(self, node: _TreeNode, *args, **kwargs) -> Any: ...
    def default_visit(self, node: _TreeNode, *args, **kwargs) -> NoReturn: ...

class _TreeNode(TypedDict):
    type: str
    value: Any
    children: list[_TreeNode]

class TreeInterpreter(Visitor):
    COMPARATOR_FUNC: ClassVar[dict[str, Callable[[Any, Any], Any]]]
    MAP_TYPE: ClassVar[Callable[[], MutableMapping[Any, Any]]]
    def __init__(self, options: Options | None = None) -> None: ...
    def default_visit(self, node: _TreeNode, *args, **kwargs) -> NoReturn: ...
    def visit_subexpression(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_field(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_comparator(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_current(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_expref(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_function_expression(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_filter_projection(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_flatten(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_identity(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_index(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_index_expression(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_slice(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_key_val_pair(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_literal(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_multi_select_dict(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_multi_select_list(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_or_expression(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_and_expression(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_not_expression(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_pipe(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_projection(self, node: _TreeNode, value: Any) -> Any: ...
    def visit_value_projection(self, node: _TreeNode, value: Any) -> Any: ...

class GraphvizVisitor(Visitor):
    def __init__(self) -> None: ...
    def visit(self, node: _TreeNode, *args, **kwargs) -> str: ...
