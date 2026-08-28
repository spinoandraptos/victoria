import qcore
from qcore.helpers import yamlizer
import inspect

print("Registered custom YAML constructors:\n")

# Safe loop handling potential None keys
for tag, constructor in yamlizer.yaml.SafeLoader.yaml_constructors.items():
    print(f"🎯 Found Match!")
    print(f"Tag Name:   {tag}")
    print(f"Target:     {constructor}")
    try:
        print(f"File Path:  {inspect.getfile(constructor)}\n")
    except Exception:
        print(f"File Path:  Could not extract path directly.\n")
