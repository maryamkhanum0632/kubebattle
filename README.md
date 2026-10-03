# ⚔️ KubeBattle — Kubernetes Failure & Recovery Lab

KubeBattle is a hands-on Kubernetes project designed to demonstrate
real Kubernetes behavior such as self-healing, scaling, rolling updates,
rollback, health checks, resource management, and debugging.

Instead of building another typical web application, this project focuses
on understanding how Kubernetes manages application workloads.

---

## 🎯 Project Purpose

The main purpose of KubeBattle is to practically test what Kubernetes does
when applications are scaled, updated, deleted, or checked for health.

The project runs locally using Minikube and Docker.

---

## 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │      Browser         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  NodePort Service    │
                    │ kubebattle-service    │
                    └──────────┬───────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
          ┌──────────┐   ┌──────────┐   ┌──────────┐
          │   Pod    │   │   Pod    │   │   Pod    │
          │ KubeBattle│   │ KubeBattle│  │ KubeBattle│
          └──────────┘   └──────────┘   └──────────┘
                │              │              │
                └──────────────┼──────────────┘
                               ▼
                    ┌──────────────────────┐
                    │     Deployment       │
                    │   Replica Management │
                    └──────────────────────┘
