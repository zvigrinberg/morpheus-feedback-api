# Morpheus Feedback API

The **Morpheus Feedback API** is a Python Flask-based microservice designed to serve as an integration layer between the Quarkus-based Morpheus application and the Argilla backend. Its primary goal is to accept user feedback data from the Morpheus clients and forward it to the hosted Argilla instance using the Argilla Python SDK.

---

## Table of Contents

- [Features](#features)
- [Architecture Overview](#architecture-overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Running Locally](#running-locally)
- [Testing](#testing)
- [Deployment](#deployment)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Clean Separation of Concerns:** The Flask service encapsulates all Argilla-specific interactions.
- **Scalability & Extensibility:** Built using the application factory pattern, allowing easy expansion (e.g., additional endpoints or services).
- **Containerization Ready:** Comes with a Dockerfile and OpenShift deployment manifests for streamlined container-based deployment.
- **Secure Integration:** Sensitive configurations (like API keys) can be managed using environment variables or OpenShift Secrets.
- **Unit Tested:** Basic tests are provided to ensure the API endpoint operates as expected.

---

## Architecture Overview

The Morpheus Feedback API is designed as part of a multi-container Pod on OpenShift. The Pod includes:

- **Flask Service:** Serves as the external entry point for feedback data.
- **Argilla Server & Dependencies:** The Argilla backend (including Argilla Server, Worker, Redis, PostgreSQL, and Elasticsearch) runs as sidecar containers.
- **Internal Communication:** All containers communicate over the Pod’s local network, limiting external exposure.

---