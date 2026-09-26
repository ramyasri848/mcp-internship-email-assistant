A simple Model Context Protocol (MCP) server that lets an MCP host such as Claude Desktop search and read internship-related emails.

CURRENT FEATURES:
search_internship_emails() : shows all internship-related emails.
search_by_company(company) : searches emails for a company.
get_email(email_id) : returns the details of one email.

REQUIREMENTS:
Windows
Python 3.13+
uv
Claude Desktop
Internet connection for installing Python packages

 1.)INSTALL MCP;
>pip install mcp


2.)Install uv: path:C:\Users\RAMYASRI\Desktop\..in command prompt

next command in C:\Users\RAMYASRI\Desktop\mcp_server
pip install uv
or this
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

uv init my-mcp-server: in C:\Users\RAMYASRI\Desktop\mcp_server
 this will create README.md main.py pyproject.toml

uv run mcp install main.py
C:\Users\RAMYASRI\Desktop\mcp_server\my-mcp-server>uv run mcp install main.py
[09/26/26 16:08:26] INFO     Added server 'InternshipEmailAssistant' to Claude config                                                          claude.py:136
                    INFO     Successfully installed InternshipEmailAssistant in Claude app    



3.)next thing is go to claude desktop : enable the developer mode in claude: in developer -> add config add:
It should open the Claude MCP configuration JSON. Replace its contents with:
{
  "mcpServers": {
    "InternshipEmailAssistant": {
      "command": "C:\\Users\\RAMYASRI\\Desktop\\mcp_server\\my-mcp-server\\.venv\\Scripts\\python.exe",
      "args": [
        "C:\\Users\\RAMYASRI\\Desktop\\mcp_server\\my-mcp-server\\main.py"
      ]
    }
  }
}

3.)NOW U CAN WORK WITH CLAUDE;

