from rembg import remove
from PIL import Image

# Input and output file paths
ip = 'v2.jpeg'
op = 'clg.jpeg'

# Open input image
inp = Image.open(ip)

# Remove background
output = remove(inp)

# Convert the image to RGB (removes the alpha channel)
output = output.convert("RGB")

# Save the output image as JPEG
output.save(op)

# Open and display the saved image
Image.open(op).show()
