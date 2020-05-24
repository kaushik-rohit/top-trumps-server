# Top Trumps Movie Edition Server (Python Flask)
![Code Quality](https://github.com/kaushik-rohit/top-trumps-server/workflows/Code%20Quality/badge.svg)
### Docker
To locally build and run the Server microservice, follow the following steps:

1) To build the docker image run ``sudo docker build -t image_name:latest .``
2) To run the docker image, use ``sudo docker run -d -p 5001:5001 image_name``

### Local execution
To locally start the Server Python application, run the following command from the top-level of this repository:
- ``python src/top_trumps.py``

### Accessibility
Access the server at http://0.0.0.0:5001/. This address & port are valid for both local execution as well as running docker images (as long as step 2) in the above section is applied).
