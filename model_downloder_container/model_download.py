import oci
import os
import re
#get input from environment variables
bucket = os.environ['bucket']
prefix = os.environ['prefix']
region = os.environ['region']
tenancy = os.environ['tenancy']
path = "/model"

#use OKE workload identities to grant permission for bucket access
signer = oci.auth.signers.get_oke_workload_identity_resource_principal_signer()
config = {'region':region, 'tenancy': tenancy}

object_storage = oci.object_storage.ObjectStorageClient(config=config, signer=signer)
ns = object_storage.get_namespace().data
#get a list of all objects in bucket/prefix
listfiles = object_storage.list_objects(ns,bucket,prefix=prefix+"/")
#print(listfiles.data.objects)
#download all objects in the bucket/prefix in the local directory
for filenames in listfiles.data.objects:
    get_obj = object_storage.get_object(ns,bucket,filenames.name)
    #remove prefix from object name
    file_name = re.sub('^(.*/)',"", filenames.name)
    #skip if empty object
    if file_name != '': 
        with open(path+'/'+file_name,'wb') as f:
            for chunk in get_obj.data.raw.stream(1024 * 1024, decode_content=False):
                f.write(chunk)
        print(f'downloaded "{filenames.name}" in "{path}" from bucket "{bucket}"')


