# Full-Stack Task Management Application

This is a full-stack task management web application built with a modern tech stack.

## Tech Stack

**Backend:**
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication
- Pytest

**Frontend:**
- React (with Vite)
- React Router
- Axios
- TailwindCSS
- React Testing Library

**Deployment:**
- Backend: Render or Railway
- Frontend: Netlify or Vercel
- CI/CD: GitHub Actions
- Local Development: Docker & Docker Compose

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── auth/
│   │   ├── crud/
│   │   ├── db/
│   │   ├── schemas/
│   │   └── main.py
│   ├── tests/
│   ├── .env.example
│   ├── Dockerfile
│   ├── Procfile
│   ├── requirements.txt
│   └── start.sh
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── context/
│   │   ├── pages/
│   │   └── main.jsx
│   ├── .env
│   ├── Dockerfile
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── .github/
│   └── workflows/
│       └── ci.yml
├── docker-compose.yml
└── README.md
```

## Setup Instructions

### Prerequisites

- Docker and Docker Compose
- Node.js and npm (for local frontend development without Docker)
- Python (for local backend development without Docker)

### Local Development with Docker

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2.  **Create environment files:**
    - Copy `backend/.env.example` to `backend/.env` and fill in the values.
      ```bash
      cp backend/.env.example backend/.env
      ```
      **Note:** The `DATABASE_URL` should point to the `db` service in Docker Compose (e.g., `postgresql://user:password@db:5432/database`).
    - Create a `.env` file in the `frontend` directory and set `VITE_API_URL`.
      ```bash
      echo "VITE_API_URL=http://localhost:8000" > frontend/.env
      ```

3.  **Build and run the containers:**
    ```bash
    docker-compose up --build
    ```

    - The backend will be available at `http://localhost:8000`.
    - The frontend will be available at `http://localhost:5173`.

### Local Development without Docker

#### Backend

1.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r backend/requirements.txt
    ```

3.  **Set up the database:**
    - Make sure you have a PostgreSQL instance running.
    - Create a `.env` file in the `backend` directory and set the `DATABASE_URL`.

4.  **Run the application:**
    ```bash
    uvicorn app.main:app --reload --app-dir backend
    ```

#### Frontend

1.  **Install dependencies:**
    ```bash
    npm install --prefix frontend
    ```

2.  **Run the application:**
    ```bash
    npm run dev --prefix frontend
    ```

## Deployment

### Backend (Render/Railway)

1.  Push your code to a GitHub repository.
2.  Create a new web service on Render or Railway and connect it to your repository.
3.  Set the build command to `pip install -r requirements.txt`.
4.  Set the start command to `sh backend/start.sh`.
5.  Add the required environment variables from `.env.example`.
6.  Add a PostgreSQL database service and connect it to your backend.

### Frontend (Netlify/Vercel)

1.  Push your code to a GitHub repository.
2.  Create a new project on Netlify or Vercel and connect it to your repository.
3.  Set the build command to `npm run build --prefix frontend`.
4.  Set the publish directory to `frontend/dist`.
5.  Add the `VITE_API_URL` environment variable and point it to your deployed backend URL.

## Environment Variables

### Backend (`backend/.env`)

-   `DATABASE_URL`: The connection string for your PostgreSQL database.
-   `JWT_SECRET_KEY`: A secret key for signing JWTs.
-   `ALGORITHM`: The algorithm to use for JWTs (e.g., `HS256`).
-   `ACCESS_TOKEN_EXPIRE_MINUTES`: The expiration time for access tokens.

### Frontend (`frontend/.env`)

-   `VITE_API_URL`: The URL of the deployed backend API.

## Live Demo

-   **Backend:** [TODO: Add link to deployed backend]
-   **Frontend:** [TODO: Add link to deployed frontend]
