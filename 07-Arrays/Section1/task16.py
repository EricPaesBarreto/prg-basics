# Sort the data from lowest to highest value
distances_traveled = [120, 150, 180, 90, 200, 175, 160]
# Sort the data in descending order, from highest to lowest value
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
# Sort the data in ascending order
file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
   "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]

distances_traveled_sorted = sorted(distances_traveled)

print(distances_traveled_sorted)

daily_temperatures_sorted = sorted(daily_temperatures)[::-1]

print(daily_temperatures_sorted)

file_names_sorted = sorted(file_names)

print(file_names_sorted)