def call_tool(name):
    if name == "check_order":
        return {"status": "eligible"}
    elif name == "issue_refund":
        return {"status": "success"}
    return {"status": "unknown"}
