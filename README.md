
![Tests passing](https://github.com/RokSiEu/firefly-iii-invoice-ocr-veryfi/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/RokSiEu/firefly-iii-invoice-ocr-veryfi/branch/main/graph/badge.svg?token=OLT68B6GRV)](https://codecov.io/gh/RokSiEu/firefly-iii-invoice-ocr-veryfi)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

# Firefly III VeryFi Integration
<p align="center">
  <a href="https://firefly-iii.org/">
    <img src="https://raw.githubusercontent.com/firefly-iii/firefly-iii/develop/.github/assets/img/logo-small.png" alt="Firefly III" width="120" height="178">
  </a>
  <a href="">
    <img src="https://user-images.githubusercontent.com/30125790/212157486-bfd08c5d-9337-4b78-be6f-230dc63838ba.png#gh-light-mode-only" alt="VeryFi" width="200">
  </a>
</p>

## Overview
This repository provides a FastAPI-based service that acts as an intermediary between Firefly III and VeryFi. The service listens for webhook events from Firefly III whenever a new transaction is created, retrieves attached receipts (images), and processes them through VeryFi’s OCR API. The extracted data is then used to update the transaction description in Firefly III.

## Features
- **Webhook Handling**: Listens for Firefly III webhook events on new transactions.
- **Firefly III API Integration**:
  - Authenticates using a personal access token.
  - Retrieves transaction details and attachments.
  - Updates the transaction description with extracted data.
- **VeryFi API Integration**:
  - Authenticates using API credentials.
  - Uploads receipt images for OCR processing.
  - Retrieves and processes OCR-extracted data.
- **Error Handling & Logging**: Logs all request errors and responses for better debugging.
- **Lightweight Docker Container**: Easily deployable as a containerized service.

## Tech Stack
- **FastAPI** (for API handling)
- **Requests** (for making API calls)
- **Python-Dotenv** (for environment variables management)
- **Docker** (for containerization)

## Installation & Usage

### Prerequisites
- Docker installed on your machine.
- Firefly III instance with API access.
- VeryFi API credentials.

### Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/roksieu/firefly-iii-veryfi-integration.git
   cd firefly-iii-veryfi-integration
   ```

2. Create a `.env` file with the following variables:
   ```sh
   FIREFLY_HOST=https://your-firefly-instance.com
   FIREFLY_TOKEN=your_firefly_api_token

   VERYFI_CLIENT_ID=your_client_id
   VERYFI_CLIENT_SECRET=your_client_secret
   VERYFI_USERNAME=your_username
   VERYFI_API_KEY=your_api_key
   VERYFI_HOST=https://api.veryfi.com/api/v8

   FIREFLY_ATTACH_CSV=false  # Determines if OCR data will be in transaction notes or uploaded as a CSV attachment.
   ```

3. Build the Docker image:
   ```sh
   docker build -t fastapi-firefly-veryfi .
   ```

4. Run the container:
   ```sh
   docker run --env-file .env -p 8000:8000 fastapi-firefly-veryfi
   ```

### Running the Service

Once the container is running, the service will be available on `http://localhost:8000`. You can interact with the API using the following methods:

- **Check if the service is running:**
  ```sh
  curl http://localhost:8000/
  ```
- **Trigger a webhook manually (for testing):**
  ```sh
  curl -X POST "http://localhost:8000/webhook" -H "Content-Type: application/json" -d '{"transaction_id": 12345}'
  ```

### API Endpoints
- **`POST /webhook`**: Processes Firefly III transactions when a webhook is triggered.
  - Request Body:
    ```json
    {
      "transaction_id": 12345
    }
    ```
  - Response:
    ```json
    {
      "message": "Transaction updated successfully"
    }
    ```

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

