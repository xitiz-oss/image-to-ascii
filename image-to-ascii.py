from PIL import Image

# Improved ASCII characters for better gradient representation
ASCII_CHARACTERS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    """Resize the image to the given width while maintaining the aspect ratio."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def convert_to_grayscale(image):
    """Convert the image to grayscale."""
    grayscale_image = image.convert("L")
    return grayscale_image

def map_pixels_to_ascii(image):
    """Map the pixels of the image to ASCII characters."""
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARACTERS[pixel // 32] for pixel in pixels])
    return ascii_str

def generate_ascii_image(image_path, new_width=100):
    """Generate the ASCII representation of the image."""
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: {image_path} not found.")
        return
    except IOError:
        print(f"Error: {image_path} is not a valid image file.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Convert the image to ASCII
    print("Processing image...")
    resized_image = resize_image(image, new_width)
    grayscale_image = convert_to_grayscale(resized_image)
    ascii_str = map_pixels_to_ascii(grayscale_image)

    # Format the ASCII string into the image width
    pixel_count = len(ascii_str)
    ascii_image = "\n".join(ascii_str[i:i + new_width] for i in range(0, pixel_count, new_width))

    # Output the ASCII image
    print(ascii_image)

    # Save the ASCII image to a text file
    with open("ascii_image.txt", "w") as file:
        file.write(ascii_image)

    print("ASCII art has been saved to ascii_image.txt")

if __name__ == "__main__":
    image_path = input("Enter a valid pathname for the image: ")
    generate_ascii_image(image_path, new_width=200)
