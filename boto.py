import boto3

def upload_to_s3(file_path, bucket_name, object_name):
    """
    Upload a file to an S3 bucket.
    """
    s3_client = boto3.client('s3')
    
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"{file_path} uploaded successfully to S3 bucket: {bucket_name} with object name: {object_name}")
    except Exception as e:
        print(f"Error uploading {file_path} to S3 bucket: {bucket_name}. Error: {e}")

# Example usage
file_path = 'local_file.txt'  # Replace with the path to your local file
bucket_name = 'your_bucket_name'  # Replace with your bucket name
object_name = 'remote_file.txt'  # Replace with the name you want to give the file in S3

upload_to_s3(file_path, bucket_name, object_name)