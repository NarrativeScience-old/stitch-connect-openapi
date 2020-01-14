# AzureDestinationFormProperties

A Azure SQL Data Warehouse connection writes data to a Azure SQL Data Warehouse database and corresponds to destination type: azure_sqldw. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_storage_account_token** | **str** | An Azure Storage Access Key. This is used to access Azure Blob Storage, which Stitch uses to stage data for Polybase before loading it into an Azure SQL Data Warehouse destination.  | [optional] 
**azure_storage_sas_url** | **str** | An Azure Blob service Shared Access Signature (SAS) URL, which is used to grant Stitch restricted access to Azure Storage resources. These resources are used to load data into an Azure SQL Data Warehouse destination.  | [optional] 
**database** | **str** | The name of the logical database to connect to.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


