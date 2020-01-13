# HookNotification

A Hook Notification object contains information about a webhook configured in the account’s Post-load hook list. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The notification ID. | [optional] 
**client_id** | **int** | The ID of the Stitch client account. | [optional] 
**created_at** | **datetime** | The time at which the notification was created. | [optional] 
**modified_at** | **datetime** | The time at which the notification was last modified. | [optional] 
**disabled_at** | **datetime** | The time at which the notification was disabled. This will be null unless the notification has been disabled.  | [optional] 
**type** | **str** | The type of the notification. Possible values are: post_load  | [optional] 
**version** | **int** | The version of the hook service the notification is using. | [optional] 
**config** | [**HookNotificationConfig**](HookNotificationConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


