

def parse_table(table_file, parsing_tool):  # todo: add parsing_tool
    title, url, xpath = parsing_tool(table_file)
    return {"title": title, "url": url, "xpath": xpath}