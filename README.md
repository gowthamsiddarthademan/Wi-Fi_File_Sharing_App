# Wi-Fi File Sharing App

A simple web application built using **Flask** that allows you to share files between devices connected to the same Wi-Fi network. This app works dynamically between laptops and mobile devices, enabling easy file transfer without needing an internet connection.

### Features

- **Dynamic File Sharing**: Allows sharing files from **Laptop to Mobile** and **Mobile to Laptop** on the same local Wi-Fi network.
- **File Upload**: Upload files from the device to a server.
- **File Download**: View a list of uploaded files and download them to the device.
- **Simple UI**: Easy-to-use interface with custom CSS for an engaging user experience.
- **Offline Use**: Works without requiring an internet connection, leveraging a local Wi-Fi network.

### Technologies Used

- **Python**: Programming language for back-end logic.
- **Flask**: Web framework to build the app.
- **HTML/CSS**: Front-end design and styling.
- **Local File Storage**: Files are stored on the server (in a shared directory) and can be downloaded.

### Project Structure

```
file_sharing_app/
├── app.py                  # Flask application code
├── shared_files/           # Directory to store uploaded files
├── static/                 # Static files (CSS)
│   └── style.css           # Your custom styles
└── templates/              # HTML templates
    ├── home.html           # Home page template
    ├── upload.html         # Upload page template
    ├── upload_success.html # Success page after upload
    └── download.html       # Download page template
```


### How It Works

1. **Home Page**: The landing page (`home.html`) gives the user the option to upload files or view the list of uploaded files.
2. **Upload Page**: The user selects files and uploads them. Once the files are successfully uploaded, a confirmation page (`upload_success.html`) is shown.
3. **Download Page**: A list of available files is displayed (`download.html`), where the user can click to download any file.

### Directory and File Structure

- **app.py**: This is the main Flask application that handles routing for uploading, downloading, and listing files.
- **shared_files/**: This folder is where uploaded files are stored.
- **static/**: This folder contains the custom CSS (`style.css`) used for the styling of the pages.
- **templates/**: This folder contains the HTML templates for the app (home, upload, success, and download pages).

### Example UI

- **Home Page** (`home.html`):
  - Provides buttons to upload files and access the download list.
  
- **Upload Page** (`upload.html`):
  - Contains a file input field that lets users select and upload files.

- **Upload Success Page** (`upload_success.html`):
  - A confirmation page that informs the user that the files were successfully uploaded.

- **Download Page** (`download.html`):
  - Displays a list of files available for download.

### Customization

- You can customize the CSS styles to modify the look and feel of the app. The CSS file is located in `static/style.css`.
- To change the storage path of uploaded files, modify the `UPLOAD_FOLDER` variable in `app.py`.

### Contact me
- Email ID: gowthamsiddarthademan@gmail.com
- IG ID: @gowthamsiddarthademan

### Conclusion

This app provides an easy-to-use solution for sharing files between devices over a local Wi-Fi network. It’s a simple and efficient way to share files without the need for an internet connection. The app’s design is minimalistic, and the logic is built using Flask, Python’s lightweight web framework.
