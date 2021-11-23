
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:

    # setx AZURE_STORAGE_CONNECTION_STRING "<yourconnectionstring>" in CMD

    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    print(connect_str)

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a unique name for the container
    container_name = str(uuid.uuid4())

    # Create the container
    container_client = blob_service_client.create_container(container_name)

    # Quick start code goes here

    # Create a local directory to hold blob data
    local_path = "C:/Users/ozank/Desktop/AI arch/blob-quickstart-v12"
    #os.mkdir(local_path)

    # Create a file in the local data directory to upload and download
    local_file_name = "sentimentdata.csv"
    upload_file_path = os.path.join(local_path, local_file_name)

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container="my-container", blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)


    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)


    print("\nListing blobs...")

    # List the blobs in the container
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)


except Exception as ex:
    print('Exception:')
    print(ex)

