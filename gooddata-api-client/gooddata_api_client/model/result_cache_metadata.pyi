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


class ResultCacheMetadata(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    All execution result's metadata used for calculation including ExecutionResponse
    """


    class MetaOapg:
        required = {
            "executionResponse",
            "resultSpec",
            "resultSize",
            "afm",
        }
        
        class properties:
        
            @staticmethod
            def afm() -> typing.Type['AFM']:
                return AFM
        
            @staticmethod
            def executionResponse() -> typing.Type['ExecutionResponse']:
                return ExecutionResponse
            resultSize = schemas.Int64Schema
        
            @staticmethod
            def resultSpec() -> typing.Type['ResultSpec']:
                return ResultSpec
            __annotations__ = {
                "afm": afm,
                "executionResponse": executionResponse,
                "resultSize": resultSize,
                "resultSpec": resultSpec,
            }
    
    executionResponse: 'ExecutionResponse'
    resultSpec: 'ResultSpec'
    resultSize: MetaOapg.properties.resultSize
    afm: 'AFM'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["afm"]) -> 'AFM': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["executionResponse"]) -> 'ExecutionResponse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resultSize"]) -> MetaOapg.properties.resultSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resultSpec"]) -> 'ResultSpec': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["afm", "executionResponse", "resultSize", "resultSpec", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["afm"]) -> 'AFM': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["executionResponse"]) -> 'ExecutionResponse': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resultSize"]) -> MetaOapg.properties.resultSize: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resultSpec"]) -> 'ResultSpec': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["afm", "executionResponse", "resultSize", "resultSpec", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        executionResponse: 'ExecutionResponse',
        resultSpec: 'ResultSpec',
        resultSize: typing.Union[MetaOapg.properties.resultSize, decimal.Decimal, int, ],
        afm: 'AFM',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ResultCacheMetadata':
        return super().__new__(
            cls,
            *_args,
            executionResponse=executionResponse,
            resultSpec=resultSpec,
            resultSize=resultSize,
            afm=afm,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.afm import AFM
from gooddata_api_client.model.execution_response import ExecutionResponse
from gooddata_api_client.model.result_spec import ResultSpec