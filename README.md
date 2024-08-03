# Soundseyf

Soundseyf is a Django-based web application dedicated to flamenco and classical guitar music. It offers users a platform to explore composers, their masterpieces, and engage with a community of music enthusiasts.

## Features

- Composer Database: Discover information about flamenco and classical guitar composers and their notable works.
- User Dashboard: Save your favorite composers and view them on your personalized dashboard.
- Community Blog: Join the Soundseyf blog community to discuss and share insights about guitar music.
- Disqus Commenting Service: Engage in discussions with the Disqus commenting system.
- Flamenco Palos: Explore different flamenco styles (palos) with detailed descriptions.
- Authentication: Secure login and registration to personalize your experience.

## Installation

1. Clone the repository:
  
   git clone <https://github.com/AisDisappeared/soundseyf.git>

2. Navigate to the project directory:
  
   cd soundseyf

3. Create and activate a virtual environment:
  
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. Install the required dependencies:
  
   pip install -r requirements.txt

5. Apply migrations:
  
   python manage.py migrate

6. Run the development server:
  
   python manage.py runserver

7. Visit <http://127.0.0.1:8000/> in your browser.

## Usage

- Browse Composers: Navigate to the composers section to explore profiles and masterpieces.
- Save Favorites: Log in to your account and save your favorite composers to your dashboard.
- Join the Blog Community: Contribute to and read blog posts in the community section.
- Commenting: Use the Disqus commenting system to interact with other users.

## Configuration

- Disqus: Configure Disqus ready code in your template .
- Authentication: Ensure email smtp settings are configured for Reset Password.

## Contributing

Contributions are welcome! If you have suggestions, bug fixes, or new features, please follow these steps:

- Fork the repository and clone your fork locally.
- Create a new branch for your changes.
- Make your changes and test thoroughly.
- Submit a pull request with a description of your changes.

Thank you for contributing!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [Aliseyfi0841@gmail.com](mailto:Aliseyfi0841@gmail.com).

