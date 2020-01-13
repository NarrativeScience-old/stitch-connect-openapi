# ConnectionDetails

Contained in a Source or Destination Report Card object, the Details object contains information about a connection type’s availability within Stitch. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **bool** | Indicates whether the Stitch client who made the request has access to the connection. This value is based on the connection’s pricing_tier and pipeline_state. If the Stitch client is using a plan that doesn’t meet the pricing_tier requirement, the access value will be false. For example: If pricing_tier: enterprise,the Stitch client must be on an Enterprise plan to access the source. All connections with a pipeline_state value of deprecated will also have an access value of false.  | [optional] 
**default_scheduling_interval** | **int** | Applicable only to source report cards. The default frequency_in_minutes value for the source.  | [optional] 
**pricing_tier** | **str** | Indicates the type of Stitch plan required to use the connection. Possible values are: standard - Any Stitch plan can use the connection. premium - A Standard Stitch plan is required to use the connection. enterprise - An Enterprise Stitch plan is required to use the connection.  | [optional] 
**default_start_date** | **str** | Applicable only to source report cards. The default start_date value for the source.  | [optional] 
**pipeline_state** | **str** | The connection type’s release status in Stitch. Possible values are: alpha - The connection is in development and is not available in Stitch. beta - The connection is in open or closed beta and is available in Stitch. released - The connection is in general release and available in Stitch. deprecated - The connection has been deprecated and is no longer available in Stitch.  | [optional] 
**protocol** | **str** | The type of the connection. For example: snowflake or platform.facebook  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


