# S3DestinationFormProperties

An Amazon S3 connection writes data to a Amazon S3 database and corresponds to destination type: s3. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csv_delimiter** | **str** | csv delimiter character | [optional] 
**output_file_format** | **str** | Defines the type of file Stitch will write to the bucket. Possible values are: - csv, which will use CSV (.csv) files - jsonl, which will use JSON (.jsonl) files  | [optional] 
**s3_bucket** | **str** | The name of the Amazon S3 bucket Stitch will write to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


