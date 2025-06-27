# Reference Architecture

The portal follows a lightweight microservice pattern. The components listed
below represent the baseline environment used for all feature development.

* **React frontend (TypeScript)** – provides client-side routing and state
  management for shipment creation, tracking and billing screens.
* **FastAPI backend** – serves REST APIs and interfaces with third-party
  logistics systems.
* **PostgreSQL** – stores user accounts, shipment records and audit logs.
* **Redis** – caches tracking updates and handles background tasks via Celery.
* **RabbitMQ** – queues events between microservices for label printing and
  notification delivery.
* **S3 compatible storage** – retains label images and customer-uploaded
  documents.

All services run in Docker containers and communicate over TLS. We deploy to a
Kubernetes cluster to ensure horizontal scalability.
