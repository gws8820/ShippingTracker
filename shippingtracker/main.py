import os
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP()
t_key = os.getenv("t_key")

@mcp.tool()
def get_company_list():
    """
    Get Company List
    """
    try:
        response = requests.get("https://info.sweettracker.co.kr/api/v1/companylist", params = {"t_key": t_key})
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def track_shipping(company_code: str, tracking_invoice: str):
    """
    Track Shipping with Company Code and Tracking Invoice
    """
    try:
        response = requests.post("https://info.sweettracker.co.kr/api/v1/trackingInfo", params = {"t_key": t_key, "t_code": company_code, "t_invoice": tracking_invoice})
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()