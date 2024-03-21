from PIL import Image, ImageDraw, ImageFont
import pytz  


from datetime import datetime, timedelta, timezone
import time  




while True:
  
  current_time = time.localtime()  
  current_clock = time.strftime("%H:%M:%S", current_time)  
  
  print("The current timezone is:", current_clock)  


  # Get the current Datetime  
  unaware_object = datetime.now()  
  print('Timezone naive:', unaware_object)  

  # Standard UTC timezone aware Datetime  
  aware_object = datetime.now(pytz.utc)  
  print('Timezone Aware:', aware_object)  





  dt_us_pacific = datetime.now(pytz.timezone('US/Pacific'))  
  dt_us_central = datetime.now(pytz.timezone('US/Central'))
  dt_us_eastern = datetime.now(pytz.timezone('US/Eastern'))
  
        

  

  '''
  # Create a new image with a white background  
  image = Image.new('RGB', (300, 140), color='white')
  # Create a drawing object
  draw = ImageDraw.Draw(image)
  # Specify the font and text to be added
  #font = ImageFont.load_default()
  #text = "Test Image"
  # Add text to the image
  #draw.text((10, 10), text, fill="black", font=font)
  
  # Save the image
  image.save("test_image.jpg")
  print("Test image created successfully!")
  '''
  
  # Open an image file
  image = Image.open("sampleDynamicTimeImage.jpg")
  image = Image.new('RGB', (300, 140), color='white')
  draw = ImageDraw.Draw(image)
  
  # Specify the font and text to be added
  #current_time = time.strftime("%H:%M:%S")
  
  
  font_path = "Roboto-Black.ttf"
  # Load the Roboto font with the specified size
  font = ImageFont.truetype(font_path, 40)
  
  text = "PST: " + str(dt_us_pacific.strftime("%H:%M :%S"))
  # Add text to the image
  draw.text((0, 0), text, fill="black", font=font)
  text = "EST: " + str(dt_us_eastern.strftime("%H:%M :%S"))
  draw.text((0, 35), text, fill="black", font=font)
  text = "CST: " + str(dt_us_central.strftime("%H:%M :%S"))
  draw.text((0, 70), text, fill="black", font=font)
  font = ImageFont.truetype(font_path, 20)
  text = "© V205 -Sample Dynamic Image"
  draw.text((0, 105), text, fill="black", font=font)
  text = "Use only with permission."
  draw.text((0, 120), text, fill="black", font=font)
  
  # Save the modified image
  image.save("sampleDynamicTimeImage.jpg")
  print("Modified image created successfully!")
  time.sleep(10)
  
  
  
  