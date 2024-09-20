import re
# Define a function to replace ANSI codes with HTML
def ansi_to_html_converter(ansi_text):
    # Dictionary to map ANSI codes to HTML
    ansi_to_html = {
        '31': 'red',     # ANSI red
        '32': 'green',   # ANSI green
        '33': 'yellow',  # ANSI yellow
        '34': 'blue',    # ANSI blue
        '35': 'magenta', # ANSI magenta
        '36': 'cyan',    # ANSI cyan
    }
    
    # Function to replace ANSI codes with HTML
    def replace_ansi(match):
        color_code = match.group(1)
        color = ansi_to_html.get(color_code, 'black')
        return f'<span style="color:{color}; font-weight: bold;">' 
    
    # Remove/reset ANSI codes at the end of color blocks
    ansi_text = re.sub(r'\033\[0m', '</span>', ansi_text)
    
    # Replace ANSI color codes with HTML spans
    ansi_text = re.sub(r'\033\[([0-9]+)m', replace_ansi, ansi_text)
    ansi_text = ansi_text.replace("\n", "\n<br>")
    ansi_text = ansi_text.replace("  ", "&nbsp;&nbsp;")
    
    return f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: monospace;
                    font-size: 20px;
                    background-color: #f4f4f4;
                    margin: 40px;
                    padding: 20px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    line-height: 1.5;
                    text-align: left;
                }}
                strong {{
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <strong>{ansi_text}</strong>
        </body>
    </html>
    """