# Virtual Nutritionist

**Virtual Nutritionist** is an AI-powered web application designed to provide personalized meal plans based on user preferences, health goals, and dietary restrictions. Whether you're managing chronic conditions like diabetes, focusing on weight management, or aiming for a healthier lifestyle, Virtual Nutritionist helps by generating customized meal plans tailored to your needs.

This project is still in development and is currently open-source to encourage collaboration from developers, data scientists, and healthcare professionals. You can check out the live demo and contribute to the project to help improve its functionality!

## Features

- **Custom Meal Plans**: Generates personalized meal plans based on your health profile, preferences, and dietary restrictions.
- **Download as PDF**: Easily download your meal plan as a PDF for offline access.
- **APIs for Integration**: The app includes APIs that allow for integration with other services and platforms.
- **Open-Source**: Contributions are welcome! This project is open for collaboration to improve the code, add new features, or expand its healthcare capabilities.

## Live Demo

Check out the live version of Virtual Nutritionist: [https://virtual-nutritionist.onrender.com](https://virtual-nutritionist.onrender.com)

## Getting Started

### Prerequisites

To run the project locally, you’ll need the following:

- Python 3.8 or later
- Django (the project uses Django as the backend framework)
- Git

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/chidoziemanagwu/virtual_nutritionist.git
   cd virtual_nutritionist
   ```
2. **Create and activate a virtual environment**:
   ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
   ```
3. **Install the required dependencies**:
    ```
    bash
    pip install -r requirements.txt
    ```
4. **Run migrations**:
    ```
    bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. **Run the development server**:
  ```
  bash
  python manage.py runserver
  ```

The app should now be running locally on http://127.0.0.1:8000/

### API Endpoints
The application offers APIs for integration. Here are some of the available endpoints:

- **/api/generate-meal-plan/**: Generate a meal plan based on user preferences.
- **/api/download-pdf/**: Download the generated meal plan as a PDF.
  
Documentation for these APIs can be found in the docs/ directory or by visiting the live API documentation at the demo link.

### Contributing
We welcome contributions! Whether it’s fixing bugs, adding new features, or optimizing the AI algorithms, your help is appreciated. Please follow these steps to contribute:

- Fork the repository.
- Create a feature branch:
  ```
  bash
  git checkout -b feature/your-feature-name
  ```
- Commit your changes:
  ```
  bash
  git commit -m 'Add some feature'
  ```
- Push to the branch:
  ```
  bash
  git push origin feature/your-feature-name
  ```
- Open a pull request.
- 
Please make sure to update the tests and documentation as necessary.

### License
The Virtual Nutritionist is available under a dual licensing model:

- **Open-source version**: Licensed under the GNU General Public License (GPL) for non-commercial and community use. See the LICENSE file for more details.
- **Commercial version**: If you wish to use this software for proprietary or commercial purposes, a commercial license is available. Please contact [your email] for licensing options.

### Roadmap
Here are some upcoming features and improvements:

- **Integration with wearable devices**: Dynamic meal plans based on real-time data from fitness trackers or health apps.
- **Disease-specific meal plans**: Meal plans tailored to specific health conditions like hypertension or kidney disease.
- **Gamification**: Implementing a reward system to encourage users to stick to their health goals.
- **Community sharing**: Users will be able to share their meal plans and success stories.

### Contact
If you have any questions, feel free to contact me at **chidozie.managwu@gmail.com** or connect with me on [Connect with me on LinkedIn](https://www.linkedin.com/in/chidozie-managwu/).
