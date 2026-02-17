🏢 Apartment Portal System

A full-stack Apartment Management Portal built using Angular, Flask, PostgreSQL, and Docker.

This application allows users to manage apartment listings with category support through a RESTful backend and a responsive Angular frontend.

📌 Project Overview

The Apartment Portal is a CRUD based web application that enables:

Adding new apartments

Viewing all apartment listings

Deleting apartments

Categorizing apartments (1BHK, 2BHK, 3BHK)

Backend API integration with database

Containerized deployment using Docker

The system follows a clean full stack architecture with proper separation of frontend, backend, and database layers.

🏗️ Architecture

Frontend
Angular application running on port 4200

Backend
Flask REST API running on port 5000

Database
PostgreSQL running inside Docker container

Containerization
Docker and Docker Compose used to orchestrate backend and database services

🛠️ Tech Stack
Frontend

Angular

TypeScript

HTML

CSS

HttpClient for API integration

Backend

Flask

Flask SQLAlchemy

Flask CORS

REST API design

Database

PostgreSQL

DevOps

Docker

Docker Compose

🚀 Features Implemented
Backend

GET /apartments

GET /apartments/<id>

POST /apartments

PUT /apartments/<id>

DELETE /apartments/<id>

GET /categories

Health check endpoint

Frontend

Add Apartment Form

Dynamic Category Dropdown

Apartment List Display

Delete Apartment Button

Real time API integration

🗂️ Project Structure
apartment-portal/
│
├── backend/
│   ├── app.py
│   └── Dockerfile
│
├── frontend/
│   └── app/
│
├── docker-compose.yml
└── README.md

⚙️ Prerequisites

Make sure the following are installed:

Docker Desktop

Node.js (v18 or above)

npm

Git

🐳 Running the Project with Docker
Step 1 — Start Backend and Database

Open terminal inside the project root directory and run:

docker-compose up --build


This will:

Build the Flask backend image

Start PostgreSQL container

Start Flask backend container

Backend will run at:

http://localhost:5000


You can test:

http://localhost:5000/health

💻 Running the Frontend

Open a new terminal and navigate to frontend folder:

cd frontend/app
npm install
npm start


Frontend will run at:

http://localhost:4200

🧪 Sample API Testing

Get all apartments:

GET http://localhost:5000/apartments


Create new apartment:

POST http://localhost:5000/apartments


Example JSON:

{
  "title": "New 2BHK",
  "price": 22000,
  "location": "Hyderabad",
  "category_id": 2
}

📦 Docker Services

The docker-compose file creates:

apartment_backend container

apartment_db container

Persistent PostgreSQL volume

🎯 Key Highlights

Full stack implementation

RESTful API architecture

PostgreSQL relational schema

Dockerized backend environment

Angular and Flask integration

Clean and modular code structure

🔮 Future Improvements

Edit Apartment UI

Apartment Search and Filter

Authentication and Authorization

Pagination

Deployment on cloud platform

👩‍💻 Author

SHobhitha Spandana S
Full Stack Developer
