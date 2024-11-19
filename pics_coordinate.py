import osxphotos
import csv

# Initialize the PhotosDB object to access the Photos database
photosdb = osxphotos.PhotosDB()

# Fetch all photos from the database
photos = photosdb.photos()

# Open a CSV file to write the data
with open('photo_coordinates.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([ 'Filename', 'Latitude', 'Longitude', 'Date'])

    # Iterate through each photo and get GPS coordinates
    for photo in photos:
            latitude = photo.latitude
            longitude = photo.longitude
            date = photo.date
            writer.writerow([ photo.original_filename, latitude, longitude, date])
  
print("Coordinates saved to 'photo_coordinates.csv'")
