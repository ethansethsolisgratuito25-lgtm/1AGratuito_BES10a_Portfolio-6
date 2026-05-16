# Portfolio 5: Strings
# Course: BES10a
# Student: Ethan Seth S. Gratuito
# Project: PIChE-JCBU Certificate Data Extractor

print("--- PIChE-JCBU: Certificate Data Extractor ---")

# Simulating a raw data dump from a Google Form spreadsheet
raw_data = "Record: ID[2025-01-19748] | Name[ethan seth s. gratuito] | Event[che fest 2026 general knowledge quiz show]"
print(f"Raw Google Form Input: '{raw_data}'\n")

# 1. Parsing the Student ID using .find() and Slicing
# Finding the starting bracket, adding 3 to jump past "ID["
id_start = raw_data.find("ID[") + 3
id_end = raw_data.find("]", id_start)
student_id = raw_data[id_start:id_end]

# 2. Parsing the Name
name_start = raw_data.find("Name[") + 5
name_end = raw_data.find("]", name_start)
raw_name = raw_data[name_start:name_end]

# 3. Parsing the Event
event_start = raw_data.find("Event[") + 6
event_end = raw_data.find("]", event_start)
raw_event = raw_data[event_start:event_end]

# 4. String Cleaning (Whitespace & Case Conversion)
formatted_name = raw_name.strip().title()
formatted_event = raw_event.strip().title()

# 5. String Concatenation for the export file
# Creating a web-safe filename: "2025-01-19748_Che_Fest_2026_GeneralKnowledgeQuizShow.pdf"
event_no_spaces = formatted_event.replace(" ", "_")
export_filename = student_id + "_" + event_no_spaces + ".pdf"

# Final Output Formatting
print("--- Official Certificate Data ---")
print(f"Name on Certificate : {formatted_name}")
print(f"Student ID Number   : {student_id}")
print(f"Event Joined        : {formatted_event}")
print(f"Export File Name    : {export_filename}")
print("---------------------------------")
