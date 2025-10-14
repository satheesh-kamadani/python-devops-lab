# Log file anlysis using for loop and extract the error logs

log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
    if "ERROR" in line:
        print(line)