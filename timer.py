import time
import sys

for i in range(59):
    sys.stdout.write(f"\rProcessing item {i}s")
    sys.stdout.flush()
    time.sleep(1)