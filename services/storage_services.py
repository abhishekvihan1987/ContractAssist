from cred.create_credentials import credentials, storage_client
import os 


class gcs_file_loader:
    def gcs_file_loader(self,bucketName:str, foldername:str=None):
        bucket = storage_client.bucket(bucketName)
        blobs = bucket.list_blobs(prefix=foldername)
        for blob in blobs:
            if blob.name.endswith("/"):
                continue

            blob.download_to_filename(blob.name)
        print("All the files downloaded succesfully")

gcs_file_object = gcs_file_loader()
gcs_file_object.gcs_file_loader('legaldocuments10','Contract/')



