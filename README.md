# Payment System – Architecture & Separation of Concerns

## Overview

This project is a **modular payment system** designed with **clear separation of responsibilities** between services. The goal is to keep payment logic, external provider integrations, and developer management **decoupled**, secure, and scalable.

At a high level:

* **FastAPI** acts as the **Payment Gateway Layer**
* **Django** acts as the **Developer & Platform Management Layer** (to be built later)
* **Currencycloud** is the **external payment provider**

This separation ensures:

* No direct exposure of Currencycloud credentials
* Clean authentication boundaries
* Easier future expansion to other payment providers

---

## System Components

### 1. FastAPI Service (Payment Gateway Layer)

**Purpose:**

* Acts as the **only service that communicates directly with Currencycloud**
* Encapsulates all payment-provider-specific logic
* Provides a controlled internal API for payment operations

**Responsibilities:**

* Authenticate with Currencycloud (token-based login)
* Handle payment-related operations such as:

  * Account validation
  * Beneficiary management
  * FX quotes
  * Transfers / payments
* Enforce strict input validation (e.g., BIC/SWIFT format)
* Return normalized responses (provider-agnostic where possible)

**What FastAPI does NOT do:**

* Manage developer accounts
* Store or issue developer API keys
* Handle end-user authentication
* Expose Currencycloud credentials to external clients

**Why FastAPI:**

* High performance for IO-bound payment operations
* Clean async support
* Ideal for internal microservice communication

---

### 2. Django Service (Developer & Platform Layer – Future)

**Purpose:**

* Acts as the **public-facing backend** for developers and clients
* Manages access control and authentication

**Responsibilities:**

* Developer registration & onboarding
* API key generation, rotation, and revocation
* Rate limiting & usage tracking
* Permission checks (who can initiate payments)
* Auditing and logging
* Business rules & platform-level validation

**Communication Pattern:**

* Django authenticates incoming developer requests
* Django forwards **authenticated and authorized** requests to FastAPI
* Django never talks to Currencycloud directly

---

### 3. Currencycloud (External Provider)

**Purpose:**

* Executes real-world payment and FX operations

**Interaction Rules:**

* Only the **FastAPI service** communicates with Currencycloud
* Authentication uses Currencycloud-issued tokens
* Provider-specific errors are translated into platform-friendly responses

---

## Communication Flow

### Current (Initial Phase)

```
Client / Internal Caller
        │
        ▼
   FastAPI Service
        │
        ▼
   Currencycloud API
```

### Future (Planned Architecture)

```
Developer / Client
        │
        ▼
     Django API
 (API keys, auth,
  permissions)
        │
        ▼
   FastAPI Service
 (payments only)
        │
        ▼
   Currencycloud API
```

---

## Key Design Principles

### 1. Separation of Concerns

* **Django** = identity, trust, permissions
* **FastAPI** = payments & provider integration
* **Currencycloud** = execution engine

### 2. Security by Design

* Currencycloud credentials are isolated
* No external client can reach Currencycloud directly
* API keys are never used at the payment-provider layer

### 3. Provider Abstraction

* FastAPI can later support multiple providers
* Django remains unchanged if providers change

### 4. Scalability

* FastAPI can scale independently for payment load
* Django can scale for developer traffic

---

## Project Status

### Implemented

* FastAPI service skeleton
* Initial Currencycloud authentication
* Limited payment-related endpoints

### Planned

* Django developer backend
* API key issuance & validation
* Internal service-to-service authentication
* Expanded payment operations

---

## Future Improvements

* Add message signing between Django and FastAPI
* Introduce request idempotency
* Add webhook handling layer
* Implement provider failover

---

## Summary

This architecture intentionally avoids coupling business logic, authentication, and payment execution. By isolating Currencycloud inside FastAPI and placing developer management in Django, the system remains **secure, maintainable, and extensible** as the platform grows.
