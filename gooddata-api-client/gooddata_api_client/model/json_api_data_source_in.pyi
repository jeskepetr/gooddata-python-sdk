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


class JsonApiDataSourceIn(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    JSON:API representation of dataSource entity.
    """


    class MetaOapg:
        required = {
            "attributes",
            "id",
            "type",
        }
        
        class properties:
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "schema",
                        "name",
                        "type",
                    }
                    
                    class properties:
                        
                        
                        class cachePath(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                items = schemas.StrSchema
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'cachePath':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        enableCaching = schemas.BoolSchema
                        
                        
                        class name(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class parameters(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                
                                class items(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        required = {
                                            "name",
                                            "value",
                                        }
                                        
                                        class properties:
                                            name = schemas.StrSchema
                                            value = schemas.StrSchema
                                            __annotations__ = {
                                                "name": name,
                                                "value": value,
                                            }
                                    
                                    name: MetaOapg.properties.name
                                    value: MetaOapg.properties.value
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                    
                                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "value", ], str]):
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                    
                                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "value", ], str]):
                                        return super().get_item_oapg(name)
                                    
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[dict, frozendict.frozendict, ],
                                        name: typing.Union[MetaOapg.properties.name, str, ],
                                        value: typing.Union[MetaOapg.properties.value, str, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'items':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            name=name,
                                            value=value,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'parameters':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        
                        
                        class password(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class schema(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class token(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class type(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def POSTGRESQL(cls):
                                return cls("POSTGRESQL")
                            
                            @schemas.classproperty
                            def REDSHIFT(cls):
                                return cls("REDSHIFT")
                            
                            @schemas.classproperty
                            def VERTICA(cls):
                                return cls("VERTICA")
                            
                            @schemas.classproperty
                            def SNOWFLAKE(cls):
                                return cls("SNOWFLAKE")
                            
                            @schemas.classproperty
                            def ADS(cls):
                                return cls("ADS")
                            
                            @schemas.classproperty
                            def BIGQUERY(cls):
                                return cls("BIGQUERY")
                            
                            @schemas.classproperty
                            def MSSQL(cls):
                                return cls("MSSQL")
                            
                            @schemas.classproperty
                            def PRESTO(cls):
                                return cls("PRESTO")
                            
                            @schemas.classproperty
                            def DREMIO(cls):
                                return cls("DREMIO")
                            
                            @schemas.classproperty
                            def DRILL(cls):
                                return cls("DRILL")
                            
                            @schemas.classproperty
                            def GREENPLUM(cls):
                                return cls("GREENPLUM")
                            
                            @schemas.classproperty
                            def AZURESQL(cls):
                                return cls("AZURESQL")
                            
                            @schemas.classproperty
                            def SYNAPSESQL(cls):
                                return cls("SYNAPSESQL")
                            
                            @schemas.classproperty
                            def DATABRICKS(cls):
                                return cls("DATABRICKS")
                        
                        
                        class url(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class username(
                            schemas.StrSchema
                        ):
                            pass
                        __annotations__ = {
                            "cachePath": cachePath,
                            "enableCaching": enableCaching,
                            "name": name,
                            "parameters": parameters,
                            "password": password,
                            "schema": schema,
                            "token": token,
                            "type": type,
                            "url": url,
                            "username": username,
                        }
                
                schema: MetaOapg.properties.schema
                name: MetaOapg.properties.name
                type: MetaOapg.properties.type
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["cachePath"]) -> MetaOapg.properties.cachePath: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["enableCaching"]) -> MetaOapg.properties.enableCaching: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["parameters"]) -> MetaOapg.properties.parameters: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["schema"]) -> MetaOapg.properties.schema: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["cachePath", "enableCaching", "name", "parameters", "password", "schema", "token", "type", "url", "username", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["cachePath"]) -> typing.Union[MetaOapg.properties.cachePath, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["enableCaching"]) -> typing.Union[MetaOapg.properties.enableCaching, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["parameters"]) -> typing.Union[MetaOapg.properties.parameters, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["schema"]) -> MetaOapg.properties.schema: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["token"]) -> typing.Union[MetaOapg.properties.token, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cachePath", "enableCaching", "name", "parameters", "password", "schema", "token", "type", "url", "username", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    schema: typing.Union[MetaOapg.properties.schema, str, ],
                    name: typing.Union[MetaOapg.properties.name, str, ],
                    type: typing.Union[MetaOapg.properties.type, str, ],
                    cachePath: typing.Union[MetaOapg.properties.cachePath, list, tuple, schemas.Unset] = schemas.unset,
                    enableCaching: typing.Union[MetaOapg.properties.enableCaching, bool, schemas.Unset] = schemas.unset,
                    parameters: typing.Union[MetaOapg.properties.parameters, list, tuple, schemas.Unset] = schemas.unset,
                    password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
                    token: typing.Union[MetaOapg.properties.token, str, schemas.Unset] = schemas.unset,
                    url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
                    username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *_args,
                        schema=schema,
                        name=name,
                        type=type,
                        cachePath=cachePath,
                        enableCaching=enableCaching,
                        parameters=parameters,
                        password=password,
                        token=token,
                        url=url,
                        username=username,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DATA_SOURCE(cls):
                    return cls("dataSource")
            __annotations__ = {
                "attributes": attributes,
                "id": id,
                "type": type,
            }
    
    attributes: MetaOapg.properties.attributes
    id: MetaOapg.properties.id
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["attributes", "id", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attributes", "id", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JsonApiDataSourceIn':
        return super().__new__(
            cls,
            *_args,
            attributes=attributes,
            id=id,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )
