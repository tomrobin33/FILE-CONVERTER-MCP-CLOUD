# start_http.py
import uvicorn
from mcp_proxy import serve_stdio_as_http
import subprocess
import sys

# 启动原 MCP 服务器
process = subprocess.Popen(
    [sys.executable, "file_converter_server.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)

# 包装成 HTTP 服务
serve_stdio_as_http(process.stdin, process.stdout, host="0.0.0.0", port=8000)
