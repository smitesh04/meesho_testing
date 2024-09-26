start = 1
end = 20000
num_parts = 2

pincode = 400001

# Calculate the number of items in each part
items_per_part = (end - start + 1) // num_parts

# Initialize a list to store the range parts
range_parts = []

# Generate the range parts
for i in range(num_parts):
    part_start = start + i * items_per_part
    part_end = start + (i + 1) * items_per_part - 1 if i < num_parts - 1 else end
    range_parts.append((part_start, part_end))

# Print the range parts
for i, (part_start, part_end) in enumerate(range_parts):
    print(f'start "Part:{i+1}" python play_meesho_2.py {pincode} {part_start} {part_end}')