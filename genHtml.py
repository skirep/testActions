import os
import datetime

def generate_html_page(directory):
    # Get the list of PNG files
    png_files = [file for file in os.listdir(directory) if file.lower().endswith('.png')]

    # Sort the files by creation date
    png_files.sort(key=lambda file: get_creation_date(os.path.join(directory, file)))

    # Create HTML content
    html_content = "<html>\n<body>\n<div align='center'>\n<h1>PNG Files in the Directory</h1>\n<table border='1'>\n<tr>\n<th>File Name</th>\n<th>Creation Date</th>\n<th>Link</th>\n</tr>\n"

    # Add a row for each PNG file
    for png_file in png_files:
        # Generate the full path of the file
        file_path = os.path.join(directory, png_file)

        # Get the creation date of the file
        creation_date = get_creation_date(file_path)

        # Add a row to the HTML table with the file name, creation date, and link
        html_content += f'<tr>\n<td>{png_file}</td>\n<td>{creation_date}</td>\n<td><a href="{file_path}" target="_blank">Link</a></td>\n</tr>\n'

    # Close HTML tags
    html_content += "</table>\n</div>\n</body>\n</html>"

    # Save the content to an HTML file named "index.html"
    with open("index.html", "w") as html_file:
        html_file.write(html_content)

def get_creation_date(file_path):
    # Get the creation date of the file
    creation_date_timestamp = os.path.getctime(file_path)
    creation_date = datetime.datetime.fromtimestamp(creation_date_timestamp)
    return creation_date.strftime("%Y-%m-%d %H:%M:%S")

# Specify the directory you want to analyze
current_directory = "."  # You can change this to the desired directory

# Generate the HTML page with the centered table and links, files sorted by creation date
generate_html_page(current_directory)

print("HTML page generated successfully. The file is named 'index.html'.")
