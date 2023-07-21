import pytesseract

plate_image = 'download.jpg'

plate_text = pytesseract.image_to_string(plate_image, config='--psm 11')

# Display the license plate text
print(plate_text)
