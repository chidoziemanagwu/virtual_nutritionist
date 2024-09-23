# Virtual Nutritionist

Virtual Nutritionist is a Django-powered AI-based application designed to generate personalized meal plans, offer dietary advice, provide recipe suggestions, analyze nutritional content, and create grocery lists based on user preferences and health goals. It integrates AI models to assist users in achieving their health and dietary objectives.

## Features

- **Personalized Meal Planning:** Creates meal plans based on user preferences and health goals.
- **Dietary Advice:** Offers AI-powered recommendations for a healthier diet.
- **Recipe Suggestions:** Recommends recipes based on dietary needs and available ingredients.
- **Nutritional Content Analysis:** Analyzes the nutritional value of food items and meals.
- **Grocery List Creation:** Generates a shopping list based on the meal plan.
- **API-Driven:** The app interacts with AI models via secure APIs to enhance meal planning and dietary suggestions.
- **User Authentication:** Includes secure user authentication for personalized interactions.
- **TailwindCSS Integration:** Responsive and modern UI using TailwindCSS.
- **AWS Deployment:** Deployed on AWS with a CI/CD pipeline for continuous integration.

## Installation

### Prerequisites
- Python 3.8+
- Django 4.0+
- SQLite (for development)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chidoziemanagwu/virtual_nutritionist.git
   cd virtual_nutritionist

2. **Set up a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Set up environment variables:** Create a .env file in the root directory and add your environment-specific variables (e.g., secret keys, database settings, API keys).
5. **Run database migrations:**
   ```bash
   python manage.py migrate
6. **Start the development server:**
   ```bash
   python manage.py runserver

### API Documentation
We use Swagger for API documentation and testing. Once you have the project running locally, you can access the Swagger documentation at:

   ```bash
   http://localhost:8000/swagger/
```
### Example Endpoints
- GET /api/mealplan/ - Fetch personalized meal plans.
- POST /api/mealplan/create/ - Create a new meal plan.
- GET /api/recipes/ - Fetch recommended recipes.

### Deployment
We use AWS for deploying the Virtual Nutritionist application. The project includes a CI/CD pipeline via GitHub Actions, which automatically deploys changes to the AWS environment.

**Steps for Deployment:**
- Set up AWS credentials: Ensure that your AWS credentials are available in the environment where the application is deployed.
- Configure GitHub Actions: Ensure the .github/workflows directory is configured for automatic deployment.

### Technologies Used
- **Backend:** Django, Django REST Framework
- **Frontend:** TailwindCSS
- **Database:** SQLite (development), PostgreSQL (production)
- **Deployment:** AWS (EC2, S3)
- **API Documentation:** Swagger
- **CI/CD:** GitHub Actions

### Contribution Guidelines
Contributions are welcome! Please follow these steps:

- Fork the repository.
- Create a new feature branch (git checkout -b feature-branch-name).
- Commit your changes (git commit -m 'Add new feature').
- Push to the branch (git push origin feature-branch-name).
- Create a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Author
**Chidozie Managwu**

GitHub: @chidoziemanagwu
LinkedIn: Chidozie Managwu
