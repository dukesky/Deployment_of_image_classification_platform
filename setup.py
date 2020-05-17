import boto3
import os
import sys
import zipfile
import shutil

REQUIREMENTS_BUCKET_NAME = os.environ.get("MODEL_BUCKET_NAME") 
REQUIREMENTS_KEY = os.environ.get("REQUIREMENT_FILE")

pkgdir = '/tmp/requirements'
TMP_DIR = '/tmp/_tmp_requirement'

os.mkdir(TMP_DIR)
#zip_requirements = '/tmp/lambda_requirements.zip'
REQUIREMENTS_PATH = os.path.join(TMP_DIR, REQUIREMENTS_KEY)


if not os.path.exists(pkgdir):
    tempdir = '/tmp/_temp-sls-py-req'
    if os.path.exists(tempdir):
        shutil.rmtree(tempdir)

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(REQUIREMENTS_BUCKET_NAME)
    print('downloading requirements.zip from S3 to ',REQUIREMENTS_PATH)
    bucket.download_file(REQUIREMENTS_KEY, REQUIREMENTS_PATH)

    print('finishing downloading and extracting...')
    zipfile.ZipFile(REQUIREMENTS_PATH, 'r').extractall(tempdir)
    print('finish extract and delete ',REQUIREMENTS_PATH)
#     os.remove('REQUIREMENTS_PATH')
    os.rename(tempdir, pkgdir)

    sys.path.append(pkgdir)
