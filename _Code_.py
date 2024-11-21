import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Total number of images and images to use in processing
total_images = 24
images_to_use = 4

def load_image_as_array(filepath):
    """Loads an image, converts it to RGB, and returns it as a NumPy array."""
    image = Image.open(filepath).convert("RGB")
    return np.array(image)

# Load and process selected images
images = [
    load_image_as_array(f'image_name_{i * (total_images // images_to_use)}.png')
    for i in range(images_to_use)
]

# Initialize the base zero-filled matrix
matrix_height, matrix_width = 512, 512  
output_matrix = np.zeros((matrix_height, matrix_width, 3), dtype=np.uint8)

# Mosaic pattern parameters
periods = 5
lines_per_period = matrix_height // periods
lines_per_block = lines_per_period // images_to_use

# List to track black separator line positions
black_line_positions = []

# Construct the mosaic pattern with black separators
for period in range(periods):
    for idx, image in enumerate(images):
        # Calculate the start and end of the current block
        start = idx * lines_per_block + period * lines_per_period
        end = (idx + 1) * lines_per_block + period * lines_per_period

        # Copy the corresponding block of the image to the output matrix
        output_matrix[start:end, :] = image[start:end, :]

        # Add a black separator line between blocks
        if idx < images_to_use - 1:
            separator_line = end - 1
            output_matrix[separator_line:separator_line + 1, :] = [0, 0, 0]
            black_line_positions.append(separator_line)

    # Add a black separator line after each period
    if period < periods - 1:
        separator_line = end
        output_matrix[separator_line:separator_line + 1, :] = [0, 0, 0]
        black_line_positions.append(separator_line)

# Print the output matrix shape and black line positions
print("Output matrix shape:", output_matrix.shape)
print("Black line positions:", black_line_positions)

# Display the resulting image
plt.imshow(output_matrix)
plt.axis('on')
plt.show()

# Save the resulting image
result_image = Image.fromarray(output_matrix)
result_image.save('output_image.png')
