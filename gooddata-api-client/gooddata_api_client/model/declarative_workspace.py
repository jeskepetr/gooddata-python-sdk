"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gooddata_api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from gooddata_api_client.exceptions import ApiAttributeError


def lazy_import():
    from gooddata_api_client.model.declarative_custom_application_setting import DeclarativeCustomApplicationSetting
    from gooddata_api_client.model.declarative_setting import DeclarativeSetting
    from gooddata_api_client.model.declarative_single_workspace_permission import DeclarativeSingleWorkspacePermission
    from gooddata_api_client.model.declarative_user_data_filter import DeclarativeUserDataFilter
    from gooddata_api_client.model.declarative_workspace_hierarchy_permission import DeclarativeWorkspaceHierarchyPermission
    from gooddata_api_client.model.declarative_workspace_model import DeclarativeWorkspaceModel
    from gooddata_api_client.model.workspace_data_source import WorkspaceDataSource
    from gooddata_api_client.model.workspace_identifier import WorkspaceIdentifier
    globals()['DeclarativeCustomApplicationSetting'] = DeclarativeCustomApplicationSetting
    globals()['DeclarativeSetting'] = DeclarativeSetting
    globals()['DeclarativeSingleWorkspacePermission'] = DeclarativeSingleWorkspacePermission
    globals()['DeclarativeUserDataFilter'] = DeclarativeUserDataFilter
    globals()['DeclarativeWorkspaceHierarchyPermission'] = DeclarativeWorkspaceHierarchyPermission
    globals()['DeclarativeWorkspaceModel'] = DeclarativeWorkspaceModel
    globals()['WorkspaceDataSource'] = WorkspaceDataSource
    globals()['WorkspaceIdentifier'] = WorkspaceIdentifier


class DeclarativeWorkspace(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('id',): {
            'regex': {
                'pattern': r'^(?!\.)[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
            },
        },
        ('name',): {
            'max_length': 255,
        },
        ('description',): {
            'max_length': 255,
        },
        ('early_access',): {
            'max_length': 255,
        },
        ('prefix',): {
            'max_length': 255,
            'regex': {
                'pattern': r'^(?!\.)[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
            },
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'cache_extra_limit': (int,),  # noqa: E501
            'custom_application_settings': ([DeclarativeCustomApplicationSetting],),  # noqa: E501
            'data_source': (WorkspaceDataSource,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'early_access': (str,),  # noqa: E501
            'hierarchy_permissions': ([DeclarativeWorkspaceHierarchyPermission],),  # noqa: E501
            'model': (DeclarativeWorkspaceModel,),  # noqa: E501
            'parent': (WorkspaceIdentifier,),  # noqa: E501
            'permissions': ([DeclarativeSingleWorkspacePermission],),  # noqa: E501
            'prefix': (str,),  # noqa: E501
            'settings': ([DeclarativeSetting],),  # noqa: E501
            'user_data_filters': ([DeclarativeUserDataFilter],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'cache_extra_limit': 'cacheExtraLimit',  # noqa: E501
        'custom_application_settings': 'customApplicationSettings',  # noqa: E501
        'data_source': 'dataSource',  # noqa: E501
        'description': 'description',  # noqa: E501
        'early_access': 'earlyAccess',  # noqa: E501
        'hierarchy_permissions': 'hierarchyPermissions',  # noqa: E501
        'model': 'model',  # noqa: E501
        'parent': 'parent',  # noqa: E501
        'permissions': 'permissions',  # noqa: E501
        'prefix': 'prefix',  # noqa: E501
        'settings': 'settings',  # noqa: E501
        'user_data_filters': 'userDataFilters',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, name, *args, **kwargs):  # noqa: E501
        """DeclarativeWorkspace - a model defined in OpenAPI

        Args:
            id (str): Identifier of a workspace
            name (str): Name of a workspace to view.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            cache_extra_limit (int): Extra cache limit allocated to specific workspace. In case there is extra cache budget setup for organization, it can be split between multiple workspaces.. [optional]  # noqa: E501
            custom_application_settings ([DeclarativeCustomApplicationSetting]): A list of workspace custom settings.. [optional]  # noqa: E501
            data_source (WorkspaceDataSource): [optional]  # noqa: E501
            description (str): Description of the workspace. [optional]  # noqa: E501
            early_access (str): Early access defined on level Workspace. [optional]  # noqa: E501
            hierarchy_permissions ([DeclarativeWorkspaceHierarchyPermission]): [optional]  # noqa: E501
            model (DeclarativeWorkspaceModel): [optional]  # noqa: E501
            parent (WorkspaceIdentifier): [optional]  # noqa: E501
            permissions ([DeclarativeSingleWorkspacePermission]): [optional]  # noqa: E501
            prefix (str): Custom prefix of entity identifiers in workspace. [optional]  # noqa: E501
            settings ([DeclarativeSetting]): A list of workspace settings.. [optional]  # noqa: E501
            user_data_filters ([DeclarativeUserDataFilter]): A list of workspace user data filters.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.name = name
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, id, name, *args, **kwargs):  # noqa: E501
        """DeclarativeWorkspace - a model defined in OpenAPI

        Args:
            id (str): Identifier of a workspace
            name (str): Name of a workspace to view.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            cache_extra_limit (int): Extra cache limit allocated to specific workspace. In case there is extra cache budget setup for organization, it can be split between multiple workspaces.. [optional]  # noqa: E501
            custom_application_settings ([DeclarativeCustomApplicationSetting]): A list of workspace custom settings.. [optional]  # noqa: E501
            data_source (WorkspaceDataSource): [optional]  # noqa: E501
            description (str): Description of the workspace. [optional]  # noqa: E501
            early_access (str): Early access defined on level Workspace. [optional]  # noqa: E501
            hierarchy_permissions ([DeclarativeWorkspaceHierarchyPermission]): [optional]  # noqa: E501
            model (DeclarativeWorkspaceModel): [optional]  # noqa: E501
            parent (WorkspaceIdentifier): [optional]  # noqa: E501
            permissions ([DeclarativeSingleWorkspacePermission]): [optional]  # noqa: E501
            prefix (str): Custom prefix of entity identifiers in workspace. [optional]  # noqa: E501
            settings ([DeclarativeSetting]): A list of workspace settings.. [optional]  # noqa: E501
            user_data_filters ([DeclarativeUserDataFilter]): A list of workspace user data filters.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.name = name
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
