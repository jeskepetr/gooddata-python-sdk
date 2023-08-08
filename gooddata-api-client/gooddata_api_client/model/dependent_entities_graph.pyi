# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from gooddata_api_client import schemas  # noqa: F401


class DependentEntitiesGraph(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "nodes",
            "edges",
        }
        
        class properties:
            
            
            class edges(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['EntityIdentifier']:
                                return EntityIdentifier
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple['EntityIdentifier'], typing.List['EntityIdentifier']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'EntityIdentifier':
                            return super().__getitem__(i)
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, list, tuple, ]], typing.List[typing.Union[MetaOapg.items, list, tuple, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'edges':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class nodes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DependentEntitiesNode']:
                        return DependentEntitiesNode
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['DependentEntitiesNode'], typing.List['DependentEntitiesNode']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nodes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DependentEntitiesNode':
                    return super().__getitem__(i)
            __annotations__ = {
                "edges": edges,
                "nodes": nodes,
            }
    
    nodes: MetaOapg.properties.nodes
    edges: MetaOapg.properties.edges
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edges"]) -> MetaOapg.properties.edges: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodes"]) -> MetaOapg.properties.nodes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["edges", "nodes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edges"]) -> MetaOapg.properties.edges: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodes"]) -> MetaOapg.properties.nodes: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["edges", "nodes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        nodes: typing.Union[MetaOapg.properties.nodes, list, tuple, ],
        edges: typing.Union[MetaOapg.properties.edges, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DependentEntitiesGraph':
        return super().__new__(
            cls,
            *_args,
            nodes=nodes,
            edges=edges,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.dependent_entities_node import DependentEntitiesNode
from gooddata_api_client.model.entity_identifier import EntityIdentifier