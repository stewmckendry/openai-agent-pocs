# As-Is Design

The online portal is built as a standard single page application. Customers
create shipments, print labels and track deliveries using their web browser.

**Authentication**
* Only email and password credentials are currently supported.
* User sessions are stored in secure cookies managed by the React frontend.

**Core Modules**
* **Shipment Manager** – allows creation of shipping labels and scheduling of
  pickups.
* **Tracking Dashboard** – displays the latest package status with data pulled
  from the sorting hubs every few minutes.

**Limitations**
* No integration yet with external identity providers.
* Notification preferences are spread across multiple pages, making it hard for
  users to manage them.
