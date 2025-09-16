from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import re
import os
from datetime import datetime


class HTMLGeneratorInput(BaseModel):
    """Input schema for HTMLGenerator."""
    markdown_content: str = Field(..., description="The markdown content to convert to HTML with embedded maps")
    title: str = Field(..., description="Title for the HTML document")
    destination: str = Field(..., description="Travel destination for the trip")


class HTMLGenerator(BaseTool):
    name: str = "HTML Generator"
    description: str = (
        "A tool to convert markdown travel plans to interactive HTML with embedded Google Maps, "
        "images, and enhanced formatting for better travel planning experience."
    )
    args_schema: Type[BaseModel] = HTMLGeneratorInput

    def _run(self, markdown_content: str, title: str, destination: str) -> str:
        """Convert markdown to HTML with Google Maps integration."""
        try:
            # Extract Google Maps URLs from the content
            maps_urls = re.findall(r'https://maps\.google\.com/[^\s\)]+', markdown_content)
            
            # Create HTML template
            html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f8f9fa;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
        }}
        
        .content {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }}
        
        .location-card {{
            border: 2px solid #e9ecef;
            border-radius: 8px;
            padding: 15px;
            margin: 15px 0;
            background-color: #f8f9fa;
        }}
        
        .location-name {{
            color: #495057;
            font-weight: bold;
            font-size: 1.1em;
            margin-bottom: 10px;
        }}
        
        .map-container {{
            margin: 15px 0;
            border-radius: 5px;
            overflow: hidden;
        }}
        
        .map-embed {{
            width: 100%;
            height: 300px;
            border: none;
            border-radius: 5px;
        }}
        
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 10px;
            margin: 10px 0;
        }}
        
        .info-item {{
            background: white;
            padding: 10px;
            border-radius: 5px;
            border-left: 4px solid #667eea;
        }}
        
        .day-header {{
            background: linear-gradient(90deg, #667eea, #764ba2);
            color: white;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0 10px 0;
        }}
        
        h1, h2, h3 {{
            color: #495057;
        }}
        
        a {{
            color: #667eea;
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        .budget-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }}
        
        .budget-table th, .budget-table td {{
            border: 1px solid #dee2e6;
            padding: 8px 12px;
            text-align: left;
        }}
        
        .budget-table th {{
            background-color: #667eea;
            color: white;
        }}
        
        .emergency-contacts {{
            background-color: #fff3cd;
            border: 1px solid #ffeaa7;
            border-radius: 5px;
            padding: 15px;
            margin: 15px 0;
        }}
        
        .weather-info {{
            background-color: #d1ecf1;
            border: 1px solid #b8daff;
            border-radius: 5px;
            padding: 15px;
            margin: 15px 0;
        }}
        
        @media (max-width: 768px) {{
            body {{
                padding: 10px;
            }}
            .header {{
                padding: 20px;
            }}
            .content {{
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{title}</h1>
        <p>Your comprehensive travel guide to {destination}</p>
        <p>Generated on {datetime.now().strftime('%B %d, %Y')}</p>
    </div>
    
    <div class="content">
"""
            
            # Convert markdown to HTML with special handling for locations
            html_body = self._convert_markdown_to_html(markdown_content)
            
            html_content += html_body
            
            html_content += """
    </div>
    
    <script>
        // Add interactive features
        document.addEventListener('DOMContentLoaded', function() {
            // Add click handlers for expandable sections
            const headers = document.querySelectorAll('h3');
            headers.forEach(header => {
                header.style.cursor = 'pointer';
                header.addEventListener('click', function() {
                    const nextElement = this.nextElementSibling;
                    if (nextElement) {
                        nextElement.style.display = nextElement.style.display === 'none' ? 'block' : 'none';
                    }
                });
            });
            
            // Add smooth scrolling for internal links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    document.querySelector(this.getAttribute('href')).scrollIntoView({
                        behavior: 'smooth'
                    });
                });
            });
        });
    </script>
</body>
</html>
"""
            
            # Save HTML file
            filename = f"travel_plan_{destination.replace(' ', '_').replace(',', '')}.html"
            filepath = os.path.join(os.getcwd(), filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            return f"HTML travel plan generated successfully: {filename}\nFile saved at: {filepath}\nTotal Google Maps locations embedded: {len(maps_urls)}"
            
        except Exception as e:
            return f"Error generating HTML: {str(e)}"
    
    def _convert_markdown_to_html(self, markdown_content: str) -> str:
        """Convert markdown content to HTML with special location handling."""
        html = markdown_content
        
        # Convert headers
        html = re.sub(r'^# (.*$)', r'<h1>\1</h1>', html, flags=re.MULTILINE)
        html = re.sub(r'^## (.*$)', r'<h2>\1</h2>', html, flags=re.MULTILINE)
        html = re.sub(r'^### (.*$)', r'<div class="day-header"><h3>\1</h3></div>', html, flags=re.MULTILINE)
        
        # Convert bold text
        html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
        
        # Convert italic text
        html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
        
        # Handle location cards with addresses and Google Maps
        location_pattern = r'\*\*(.*?)\*\*\s*\n(?:Address: (.*?)\n)?(?:Google Maps: (.*?)\n)?(?:Hours: (.*?)\n)?(?:Contact: (.*?)\n)?(?:Notes: (.*?)\n)?'
        
        def create_location_card(match):
            name = match.group(1)
            address = match.group(2) or "Address not available"
            maps_url = match.group(3)
            hours = match.group(4) or "Hours not specified"
            contact = match.group(5) or "Contact not available"
            notes = match.group(6) or ""
            
            card_html = f'''
            <div class="location-card">
                <div class="location-name">{name}</div>
                <div class="info-grid">
                    <div class="info-item">
                        <strong>📍 Address:</strong><br>{address}
                    </div>
                    <div class="info-item">
                        <strong>🕒 Hours:</strong><br>{hours}
                    </div>
                    <div class="info-item">
                        <strong>📞 Contact:</strong><br>{contact}
                    </div>
                </div>
            '''
            
            if maps_url:
                # Extract query from the Google Maps URL for embedding
                if 'query=' in maps_url:
                    query = maps_url.split('query=')[1]
                    # Create a proper embed URL (without API key for now)
                    embed_url = f"https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3241.0!2d139.8107!3d35.7101!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2s{query}!5e0!3m2!1sen!2s!4v1234567890!5m2!1sen!2s"
                else:
                    query = name.replace(' ', '+')
                
                card_html += f'''
                <div class="map-container">
                    <iframe class="map-embed" 
                            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d50000!2d139.6917!3d35.6895!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2s{query}!5e0!3m2!1sen!2s!4v1234567890!5m2!1sen!2s"
                            allowfullscreen>
                    </iframe>
                    <p><a href="{maps_url}" target="_blank">🗺️ Open in Google Maps</a></p>
                </div>
                '''
            
            if notes:
                card_html += f'<div class="info-item"><strong>💡 Notes:</strong><br>{notes}</div>'
            
            card_html += '</div>'
            return card_html
        
        html = re.sub(location_pattern, create_location_card, html, flags=re.MULTILINE)
        
        # Convert links
        html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', html)
        
        # Convert line breaks
        html = html.replace('\n\n', '</p><p>').replace('\n', '<br>')
        html = f'<p>{html}</p>'
        
        # Clean up empty paragraphs
        html = re.sub(r'<p>\s*</p>', '', html)
        
        return html