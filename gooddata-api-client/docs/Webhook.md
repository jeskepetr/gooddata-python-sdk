# Webhook

Webhook destination for notifications. The property url is required on create and update.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The destination type. | defaults to "WEBHOOK"
**has_token** | **bool, none_type** | Flag indicating if webhook has a token. | [optional] [readonly] 
**token** | **str, none_type** | Bearer token for the webhook. | [optional] 
**url** | **str** | The webhook URL. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

