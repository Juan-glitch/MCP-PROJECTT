# MCP Course Overview

This document summarises the "MCP: Build Rich-Context AI Apps with Anthropic" course by DeepLearning.AI.

## What is MCP?
- The Model Context Protocol (MCP) is an open standard from Anthropic (Nov 2024).
- It connects language models to external tools, APIs and data through a unified interface, similar to a "USB-C" port for AI integrations.
- MCP uses JSON-RPC 2.0 for communication between the client (in your app) and the server (exposing resources and prompt templates).

## Course Breakdown
- **Key Concepts** – Understand why MCP avoids the N×M integration problem.
- **Initial Build** – Create a chatbot with custom tools and make it MCP-compatible.
- **Server Deployment** – Launch a local MCP server using FastMCP and debug it with MCP Inspector.
- **Client Connection** – Integrate the MCP client so your bot can access tools dynamically.
- **Reference Servers** – Learn to use Anthropic's filesystem and fetch servers.
- **Claude Desktop** – Configure this environment to simplify your client logic.
- **Production Deployment** – Publish your MCP server and test it with Inspector or compatible clients.
- **MCP Roadmap** – Explore upcoming features like registries, discovery, auth and multi-agent setups.

## Outcome
By the end you can:
- Build AI apps that pull in dynamic context via external tools.
- Deploy and connect MCP servers locally or in the cloud.
- Use existing servers like filesystem and web scraping.

Future steps in this repository will follow this course to implement practical examples.
