# URL Shortener

## Description

This URL Shortener is a simple web application built with Flask that allows users to convert long URLs into short, easy-to-share links. It generates unique short codes for each URL and provides a redirection service to the original long URL when the short URL is accessed.

## Features

- Shorten long URLs to concise, shareable links
- Randomly generated short URL codes
- Duplicate checking to ensure unique short URLs
- Simple web interface for URL shortening
- Redirection service from short URL to original long URL

## Technologies Used

- Python
- Flask
- HTML
- In-memory storage (Python dictionary)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Nikhilkps1904/URL-Shortner.git
   ```
2. Navigate to the project directory:
   ```
   cd URL-Shortner
   ```
3. Install Flask (if not already installed):
   ```
   pip install Flask
   ```

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```
2. Open your web browser and navigate to `http://localhost:5000`
3. Enter a long URL in the input field and click "Shorten"
4. Copy and share the generated short URL

## Project Structure

- `app.py`: Contains the main Flask application code
- `templates/index.html`: HTML template for the web interface

## How It Works

1. The application uses a Python dictionary (`shortened_url`) to store the mapping between short codes and original URLs.
2. When a user submits a URL, the `generate_short_url()` function creates a random 6-character code.
3. The application checks for duplicates and regenerates the code if necessary.
4. The short URL is returned to the user.
5. When a short URL is accessed, the application looks up the original URL and redirects the user.

## Limitations

- The current implementation uses in-memory storage, which means all shortened URLs are lost when the server restarts.
- There's no protection against creating multiple short URLs for the same long URL.

## Future Improvements

- Implement persistent storage (e.g., database) for shortened URLs
- Add user authentication and personal URL management
- Implement custom alias support for short URLs
- Add click tracking and analytics

## Contributing

Contributions to improve the URL Shortener are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

 MIT License

## Contact

[Nikhil K P S - nikhilkps1538@gmail.com

Project Link: [https://github.com/Nikhilkps1904/URL-Shortner](https://github.com/Nikhilkps1904/URL-Shortner)
