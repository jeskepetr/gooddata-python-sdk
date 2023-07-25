# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""

from gooddata_api_client.paths.api_v1_entities_workspaces_workspace_id_filter_contexts.post import CreateEntityFilterContexts
from gooddata_api_client.paths.api_v1_entities_workspaces_workspace_id_filter_contexts_object_id.delete import DeleteEntityFilterContexts
from gooddata_api_client.paths.api_v1_entities_workspaces_workspace_id_filter_contexts.get import GetAllEntitiesFilterContexts
from gooddata_api_client.paths.api_v1_entities_workspaces_workspace_id_filter_contexts_object_id.get import GetEntityFilterContexts
from gooddata_api_client.paths.api_v1_entities_workspaces_workspace_id_filter_contexts_object_id.patch import PatchEntityFilterContexts
from gooddata_api_client.paths.api_v1_entities_workspaces_workspace_id_filter_contexts_object_id.put import UpdateEntityFilterContexts


class ContextFiltersApi(
    CreateEntityFilterContexts,
    DeleteEntityFilterContexts,
    GetAllEntitiesFilterContexts,
    GetEntityFilterContexts,
    PatchEntityFilterContexts,
    UpdateEntityFilterContexts,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
