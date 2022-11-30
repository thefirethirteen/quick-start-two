import os
import json
import sys

# Collect arguments
if len(sys.argv) != 3:
    print("Usage: python data_worker.py [package_name] [package_manager_name]")
    sys.exit()

package_name: str = sys.argv[1]
package_manager_name: str = sys.argv[2]

# Prepare dict
desired_packages: dict = {"packages": []}

# Load existing data or create new data file
data_file: str = "./data.json"

if os.path.isfile(data_file):
    with open(data_file, 'r') as data:
        desired_packages = json.load(data)
else:
    with open(data_file, 'x') as data:
        pass

# Add user input to dict
desired_packages["packages"].append({"package": package_name, "package_manager": package_manager_name})

# Write data into file
with open(data_file, 'w') as data:
    json.dump(desired_packages, data, indent=2)
