# SourceReportCard

A Source Report Card object contains information about a source’s connection configuration. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_step** | **int** | The index (in the steps array) of the current step needed to configure the data source.  | [optional] 
**details** | [**ConnectionDetails**](ConnectionDetails.md) |  | [optional] 
**steps** | [**list[ConnectionStep]**](ConnectionStep.md) | A sequential list of Connection Step objects required to complete configuration for the connection type.  | [optional] 
**type** | **str** | The connection type. Ex: platform.mysql or platform.hubspot  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


