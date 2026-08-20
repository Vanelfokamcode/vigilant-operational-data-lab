# Vigilant Operational Data Lab

> From operational events to reliable decisions.

## What is this project?

Vigilant Operational Data Lab is a local-first learning project.
It simulates an order-processing service, controlled incidents, and the
operational data produced by the system:

- application events;
- structured logs;
- performance metrics;
- traces across services;
- incident evidence.

The goal is not to pretend to operate a real cloud platform.
The goal is to learn how technical events become trustworthy data for
reliability, governance, and later FinOps analysis.

## The story

An order API works correctly under normal conditions. Then a payment dependency
becomes slow or unavailable. Requests fail, retries can duplicate operations,
and asynchronous work accumulates.

This lab makes those failures visible and reproducible. Each chapter adds one
small capability: first the service, then its events, then its operational data,
then the rules used to investigate incidents.

## Learning path

1. Build the order API and its data contract.
2. Persist orders in PostgreSQL.
3. Generate structured operational events.
4. Measure failures and latency.
5. Model operational data for analysis.
6. Introduce controlled incidents.
7. Add reliability objectives and automation.

## Principles

- Local first: no cloud spend is required.
- Evidence first: every conclusion must be traceable to data.
- Small increments: one concern per chapter.
- No fake production claims: this is a learning lab.

## Stack

- Python / FastAPI
- PostgreSQL
- Docker Compose
- pytest
- DuckDB and dbt later in the project
- Prometheus, Grafana, and OpenTelemetry later in the project
