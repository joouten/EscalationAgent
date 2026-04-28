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
>
> **Verbose Summary:** Complete Sev 1 outage at Contoso Ltd. Primary suspect is Azure platform-level reconfiguration. Immediate actions: Resource Health check, Connectivity Checker, DAC connection. Escalate to Azure SQL Engineering if unresolved within 15 minutes.