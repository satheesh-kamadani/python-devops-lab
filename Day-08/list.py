# List
s3_buckets = ["dev_bucket", "qa_bucket", "uat_bucket"]

# Length of the list
s3_buckets_length = len(s3_buckets)
print(s3_buckets_length)

# Add new new bucket
s3_buckets.append("prod_bucket")

# Remove one bucket
s3_buckets.remove("uat_bucket")

# List slicing
updated_s3_buckets = s3_buckets[0:2]

print(s3_buckets)
print(updated_s3_buckets)

