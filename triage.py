import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

ticket = """
Customer: John Smith
Company: Contoso Ltd
Issue: Azure SQL Database completely unavailable since 6am PST. 
500 users cannot access the application. Revenue impact estimated 
at $50,000 per hour. All connection attempts timing out. 
No recent changes deployed.
"""

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    tools=[
        {
            "type": "web_search_20250305",
            "name": "web_search"
        }
    ],
    system="""You are a Tier 3 Azure support engineer.
You MUST search the web for official Microsoft documentation 
to support your root cause and diagnostic steps.
You MUST respond in exactly this structure:

## Severity
- [severity level and justification]

## Root Cause
- [cause 1 with citation URL]
- [cause 2 with citation URL]
- [cause 3 with citation URL]

## Diagnostic Steps
- [step 1 with citation URL]
- [step 2 with citation URL]
- [step 3 with citation URL]

## Verbose Summary
[3-4 sentences maximum]""",
    messages=[
        {
            "role": "user",
            "content": f"Analyze this ticket:\n\n{ticket}"
        }
    ]
)

full_response = ""
for block in message.content:
    if block.type == "text":
        full_response += block.text

print("\n" + "="*60)
print("ESCALATION TRIAGE REPORT")
print("="*60)
print(full_response)
print("="*60 + "\n")