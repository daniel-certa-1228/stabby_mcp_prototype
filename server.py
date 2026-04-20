import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types
from tools.query import list_tables

server = Server("stabby-mcp-prototype")


@server.list_tools()
async def list_tools():
    return [
        types.Tool(
            name="list_tables",
            description="Lists all tables in the database. Useful for understanding the data model.",
            inputSchema={"type": "object", "properties": {}},
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "list_tables":
        tables = list_tables()
        return [types.TextContent(type="text", text="\n".join(tables))]
    else:
        raise ValueError(f"Unknown tool: {name}")


async def main():
    async with stdio_server() as (r, w):
        await server.run(r, w, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
