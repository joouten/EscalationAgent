# IT Escalation Intelligence Agent

An AI-powered triage tool that analyzes enterprise support tickets and returns a structured escalation report with severity classification, ranked root causes, and diagnostic steps — all cited with official Microsoft documentation.

Built by a 25-year Microsoft Premier Support veteran using the Anthropic Claude API and Python.

---

## The Problem

A Tier 1 engineer receiving a Severity 1 Azure SQL outage ticket at 6am needs to make fast, accurate decisions under pressure. Researching root causes, pulling documentation, and structuring an escalation report manually takes 20-30 minutes. Every minute costs the customer money.

## The Solution

This agent takes a raw support ticket as input and returns in under 30 seconds:

- Severity classification with justification tied to Microsoft SLA definitions
- Three ranked root cause hypotheses with official Microsoft documentation links
- Three diagnostic steps with exact Azure Portal navigation paths and citations
- Verbose summary with recommended escalation path

## How It Works

1. Ticket text is passed to Claude via the Anthropic API
2. Claude uses the web search tool to retrieve current Microsoft documentation
3. A structured system prompt enforces consistent output format
4. Results are returned as a cited, actionable escalation report

## Example

**Input ticket:**

> Customer: John Smith | Company: Contoso Ltd
> Issue: Azure SQL Database completely unavailable since 6am PST.
> 500 users cannot access the application. Revenue impact: $50,000/hour.
> All connection attempts timing out. No recent changes deployed.

**Output:**

> **Severity:** CRITICAL (Sev 1) — Complete database unavailability, 500 users affected, $50,000/hour revenue impact. Meets Microsoft Severity A threshold.
>
> **Root Cause:**
> - Cause 1 — Azure Platform-Level Event — [Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-sql/database/troubleshoot-common-errors-issues)
> - Cause 2 — Resource Limit Exhaustion — [Microsoft Tech Community](https://techcommunity.microsoft.com/blog/fasttrackforazureblog/understanding-connectivity-issues-in-azure-sql-database/3790298)
> - Cause 3 — Firewall/NSG Misconfiguration — [Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-sql/database/firewall-configure)
>
> **Diagnostic Steps:**
> - Step 1 — Check Azure Resource Health → Azure Portal → SQL Database → Resource Health
> - Step 2 — Run Azure SQL Connectivity Checker
> - Step 3 — Attempt DAC Connection via SSMS

## Tech Stack

- Python 3.14
- Anthropic Claude API (claude-sonnet-4-6)
- Web search tool for real-time documentation retrieval
- python-dotenv for secure credential management

## Setup

Clone the repo and install dependencies:

    git clone https://github.com/joouten/EscalationAgent
    cd EscalationAgent
    pip install anthropic python-dotenv

Create a .env file in the project root:

    ANTHROPIC_API_KEY=your-key-here

Run the agent:

    python triage.py

## About

Built as part of a 90-day AI engineering curriculum targeting Forward Deployed AI Engineer roles. The domain expertise driving this tool comes from 25 years of Tier 3 escalation engineering at Microsoft, supporting enterprise customers on Azure infrastructure.

This project demonstrates:
- Anthropic API integration with tool use
- System prompt engineering for structured output
- Web search grounding for cited, verifiable AI responses
- Real-world domain knowledge applied to AI agent design