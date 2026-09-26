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

push into github :
in PS C:\Users\RAMYASRI\Desktop\mcp_server\my-mcp-server>
 git init
 git branch -M main
 git add .
 git status
 git commit -m "Build internship email MCP assistant"

 
  now create repo:mcp-internship-email-assistant:
  git remote add origin https://github.com/ramyasri848/mcp-internship-email-assistant.git
  git push -u origin main


  //in git status(checking):
  .venv should not be commited...
   should not upload .venv to GitHub because it contains the entire local Python environment—installed packages, executables, caches, and machine-specific  files.    It can be very large and isn't needed to run your project elsewhere.

   use( uv sync) to recreate the same environment..
   Run uv sync inside the cloned project folder, where pyproject.toml is located.

   project demonstrates:
   <img width="540" height="817" alt="image" src="https://github.com/user-attachments/assets/b0dd7564-fcfa-45c7-a0cc-a36bdc96c537" />


   step by step understanding:
   <img width="286" height="467" alt="image" src="https://github.com/user-attachments/assets/4259952b-ba09-419c-8e5b-0100d5d4d7d3" />

