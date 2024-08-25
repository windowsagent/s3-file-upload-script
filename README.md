# s3-file-upload-script
# Instructions for Running `upload_file_to_s3_buckets.py`

### Prerequisites

1. **Python Installation**: Ensure that Python is installed on your system. You can check by running the following command in your terminal:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

2. **Install boto3**: The script uses the `boto3` library to interact with AWS S3. If you don't have `boto3` installed, you can install it using pip:
   ```bash
   pip install boto3
   ```

3. **AWS Credentials**: You need to have your AWS access key and secret access key. Set them as environment variables:

   - On **Linux/macOS**:
     ```bash
     export ACCESS_KEY='your-access-key'
     export AWS_SECRET_ACCESS_KEY='your-secret-access-key'
     ```

   - On **Windows**:
     ```cmd
     set ACCESS_KEY=your-access-key
     set AWS_SECRET_ACCESS_KEY=your-secret-access-key
     ```

### Steps to Run the Script

1. **Save the Script**: Save the provided Python code as `upload_file_to_s3_buckets.py`.

2. **Navigate to Script Directory**: Use the terminal or command prompt to navigate to the directory where the script is saved.

3. **Execute the Script**: Run the script using the following command:
   ```bash
   python upload_file_to_s3_buckets.py -f /path/to/your/file -n your-s3-bucket-name [-o your-object-name]
   ```
   - Replace `/path/to/your/file` with the actual path of the file you want to upload.
   - Replace `your-s3-bucket-name` with the name of your S3 bucket.
   - The `-o` flag is optional. If not specified, the file will be uploaded with its original filename.

### Example Command

```bash
python upload_file_to_s3_buckets.py -f /home/user/documents/myfile.txt -n my-bucket-name -o newfile.txt
```

In this example, the script will upload `myfile.txt` to the `my-bucket-name` S3 bucket and save it as `newfile.txt`. If the `-o` argument is not provided, the file will be saved as `myfile.txt` in the bucket.

### Additional Notes

- Ensure that your AWS credentials have the necessary permissions to upload files to the specified S3 bucket.
- If there are any issues related to credentials, the script will notify you. Double-check your environment variables if this happens.