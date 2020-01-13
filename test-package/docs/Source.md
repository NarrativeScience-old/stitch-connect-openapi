# Source

An object representing a data source. Sources are the databases, APIs, and other data applications that Stitch replicates data from. Sources can be retrieved in a list or individually by ID. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for this source. | [optional] 
**created_at** | **str** | The time at which the source object was created. | [optional] 
**deleted_at** | **str** | The time at which the source object was deleted. | [optional] 
**display_name** | **str** | The display name of the source connection. | [optional] 
**name** | **str** | The name of the source connection, dynamically generated from &#x60;display_name&#x60;. The &#x60;name&#x60; corresponds to the destination schema name that the data from this source will be loaded into. Names must: - Contain only lowercase alphanumerics and underscores - Be unique within each Stitch client account  | [optional] 
**paused_at** | **str** | If the connection was paused by the user, the time the pause began. Otherwise, or if the connection is active, this will be &#x60;null&#x60;.  | [optional] 
**properties** | [**SourceFormProperties**](SourceFormProperties.md) |  | [optional] 
**report_card** | [**SourceReportCard**](SourceReportCard.md) |  | [optional] 
**stitch_client_id** | **int** | The ID of the Stitch client account. | [optional] 
**system_paused_at** | **str** | If the connection was paused by the system, the time the pause began. Otherwise, or if the connection is active, this will be null.  | [optional] 
**type** | **str** | The source type. | [optional] 
**updated_at** | **str** | The time at which the object was last updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


