# YZV322E Tool Presentation: Docker Compose

---

## 🛠 What is Docker Compose?

**Docker Compose** is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

It simplifies the development workflow by:
*   **Orchestrating** multiple containers (e.g., App + Database).
*   **Managing networks and volumes** automatically.
*   **Ensuring environment consistency** across different development machines.

---

## Project Structure

```bash
├── .env
├── data
│   └── StudentPerformanceFactors.csv
├── docker-compose.yml
├── requirements.txt
├── screenshots
│   ├── ...
└── scripts
    └── push_data.py
```

---

## Prerequisites

Before running the demo, ensure your system meets the following requirements:

*   **Operating System:** Linux, macOS, or Windows (via WSL2).
*   **Docker Engine:** version 20.10 or higher.
*   **Installation:** 
    *   **Windows/Mac:** Docker Desktop (includes Compose).
    *   **Linux:** Docker Engine + Docker Compose Plugin.
*   **Hardware:** Minimum 4 GB RAM (8 GB recommended for the full course stack).

---

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/OmerTurk1/YZV322E-tool-presentation-demo
    cd YZV322E-tool-presentation-demo
    ```
2.  **Verify Docker Compose installation:**
    ```bash
    docker compose version
    ```

---

## Running the Demo

Follow these steps to deploy the environment and interact with the services:

1.  **Spin up the infrastructure** (Runs in the background):
    ```bash
    docker compose up -d
    ```

2.  **Populate the database:**
    Execute the Python script to push initial data to the postgre:
    ```bash
    python scripts/push_data.py
    ```

3.  **Monitor running services:**
    ```bash
    docker ps
    ```

4.  **Manage the lifecycle:**
    *   **Restart services:** `docker compose restart`
    *   **Stop services:** `docker compose stop`
    *   **Tear down and remove all containers and volumes:** `docker compose down -v`

---

## Expected Output

After running `docker compose up -d`, you should see all containers listed as "Running" or "Healthy." For visual verification, please see the `/screenshots` folder.

---

## Environment Variables (.env)

> **Note:** For the purpose of this course demo, a sample `.env` file is included below. In a production environment, these credentials should be kept secret and never committed to version control.
```bash
DB_USER=admin
DB_PASS=password123
DB_HOST=localhost
DB_PORT=5432
DB_NAME=tool_presentation_db
