from mcp.server.fastmcp import FastMCP
from typing import List

# In-memory mock database with internship emails
internship_emails = [
    {
        "id": "E001",
        "sender": "careers@google.com",
        "subject": "Software Engineering Internship",
        "date": "2026-09-20",
        "content": "Your application for the Software Engineering Internship has been received."
    },
    {
        "id": "E002",
        "sender": "jobs@microsoft.com",
        "subject": "Internship Application Update",
        "date": "2026-09-22",
        "content": "Your internship application is currently under review."
    },
    {
        "id": "E003",
        "sender": "hr@amazon.com",
        "subject": "Amazon Internship Opportunity",
        "date": "2026-09-23",
        "content": "Applications are now open for the Software Development Engineer Internship."
    }
]

# Create MCP server
mcp = FastMCP("InternshipEmailAssistant")


# Tool: Search Internship Emails
@mcp.tool()
def search_internship_emails() -> str:
    """Search for internship-related emails."""

    if not internship_emails:
        return "No internship emails found."

    result = "Internship-related emails:\n\n"

    for email in internship_emails:
        result += (
            f"ID: {email['id']}\n"
            f"From: {email['sender']}\n"
            f"Subject: {email['subject']}\n"
            f"Date: {email['date']}\n\n"
        )

    return result


# Tool: Get Specific Email
@mcp.tool()
def get_email(email_id: str) -> str:
    """Get the details of a specific email."""

    for email in internship_emails:
        if email["id"] == email_id:
            return (
                f"From: {email['sender']}\n"
                f"Subject: {email['subject']}\n"
                f"Date: {email['date']}\n"
                f"Content: {email['content']}"
            )

    return "Email ID not found."


# Tool: Search Emails by Company
@mcp.tool()
def search_by_company(company: str) -> str:
    """Search internship emails from a specific company."""

    results = []

    for email in internship_emails:
        if company.lower() in email["sender"].lower() or \
           company.lower() in email["subject"].lower() or \
           company.lower() in email["content"].lower():

            results.append(email)

    if not results:
        return f"No internship emails found for {company}."

    output = f"Internship emails related to {company}:\n\n"

    for email in results:
        output += (
            f"ID: {email['id']}\n"
            f"From: {email['sender']}\n"
            f"Subject: {email['subject']}\n"
            f"Date: {email['date']}\n\n"
        )

    return output


# Resource: Internship Email
@mcp.resource("internship://emails")
def internship_resource() -> str:
    """Provide internship emails as a resource."""

    return search_internship_emails()


if __name__ == "__main__":
    mcp.run()