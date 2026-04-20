
#use lightweight python image
FROM python:3.9-slim

#set working directory
WORKDIR /app

# Copy app code
COPY app.py . 

# Expose port
EXPOSE 8080


# Run the app
CMD [ "python" , "app.py"]
