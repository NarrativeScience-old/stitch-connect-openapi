# ConnectionStepProps

A Properties object contains the properties necessary to complete a connection step. Returned within a Source or Destination object, these properties provide information about the configuration status of the connection. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the property. | [optional] 
**is_required** | **bool** | If true, the property is required for complete configuration. | [optional] 
**is_credential** | **bool** | If true, the property is a credential or otherwise sensitive data.  | [optional] 
**property_type** | **str** | Indicates the type of the property. Possible values are: user_provided - Indicates the property must be set by the user. read_only - Indicates the property is read-only and is not settable by the API. Generally, this is an internal field set inside of Stitch. system_provided_by_default - Indicates the property used to be system_provided: true, but can now be set by the API consumer. These are generally properties associated with OAuth for generating refresh and access tokens. Note: Use caution when setting these properties, as using incorrect values can put the source into a non-functioning state.  | [optional] 
**json_schema** | [**list[ConnectionStepPropsJsonSchema]**](ConnectionStepPropsJsonSchema.md) | Note: Data will only be returned for this array if property_type: user_provided or property_type: system_provided_by_default. If property_type: read_only, this property will be null. An array containing: type - A string indicating the expected data type of the property’s value. For example: boolean pattern - A string indicating the expected pattern of the property’s value. For example: ^\\\\d+$ anyOf - A series of arrays containing key-value pairs for the type and format combinations Stitch will accept as the property’s value  | [optional] 
**provided** | **bool** | If true, the property has been provided. For properties where property_type: user_provided, this indicates that the user has provided the property.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


