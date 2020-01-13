# Destination

An object representing a destination. Destinations are the data warehouses into which Stitch writes data. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | The time at which the destination object was created.  | [optional] 
**deleted_at** | **str** | The time at which the destination object was deleted.  | [optional] 
**id** | **str** | A unique identifier for this destination. | [optional] 
**name** | **str** | The name for the destination. | [optional] 
**paused_at** | **object** | If the connection was paused by the user, the time the pause began. Otherwise, or if the connection is active, this will be null.  | [optional] 
**properties** | [**DestinationFormProperties**](DestinationFormProperties.md) |  | [optional] 
**report_card** | [**DestinationReportCard**](DestinationReportCard.md) |  | [optional] 
**stitch_client_id** | **int** | The ID of the Stitch client account.  | [optional] 
**system_paused_at** | **str** | If the connection was paused by the system, the time the pause began. Otherwise, or if the connection is active, this will be null.  | [optional] 
**type** | **str** | The destination type. Must be one of: azure_sqldw, postgres, redshift, s3, or snowflake.  | [optional] 
**updated_at** | **str** | The time at which the destination object was last updated.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


