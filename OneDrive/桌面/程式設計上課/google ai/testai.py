import os
import google.generativeai as generativeai


generativeai.configure(api_key="AIzaSyCDi9YT7DVaU5Mlamv13xHGpRam0jNYIjY")
response = generativeai.GenerativeModel('gemin1-2.0-flash-exp').generate_content('response.text')
print(response.text)