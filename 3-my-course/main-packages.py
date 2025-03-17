import subprocess

# Get the list of top-level packages
result = subprocess.run(['pip', 'list', '--not-required'], stdout=subprocess.PIPE, text=True)
print(result)
lines = result.stdout.splitlines()
print(lines)

# Create a requirements.txt file
with open('main_requirements.txt', 'w') as f:
    for line in lines[2:]:  # Skip the first two header lines
        package_info = line.split()
        if len(package_info) == 2:
            f.write(f"{package_info[0]}=={package_info[1]}\n")

print("main_requirements.txt created with top-level packages.")