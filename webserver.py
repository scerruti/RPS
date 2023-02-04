"""
My Web Server Project

"""
from os import dup, fdopen
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from contextlib import redirect_stdout
import time
import mimetypes
import rps
import logging

files = []
features = {}


def print_about_me(path=''):
    """
    Copy this code to Idle or PyCharm.
    Create the 'about me' page for your web server.

    Requirements:
      1. Your about me page must have your first name but not your last name or other personal
         information including email or phone number.
      2. Your about me page must contain a paragraph about this assignment and the Python
         print function.
      3. Your about me page must have three interesting facts about you on separate lines.
      4. Your page must use well formatted HTML including a DOCSTRING

    Never put personal information on the internet. These web servers will only be available
    on the local network and only to people who know your IP address.

    Test your webserver by pointing your web browser to http://localhost:8080
    """

    # Step 1. define the problem: "Use Python print function to create a web page for my web server."

    # Step 2. Plan your solution
    #  a. write down what you know about the print function from lecture.
    #  b. write down interesting facts about yourself
    #  c. sketch by hand or build a prototype page using an HTML editor

    # Step 3. Try your plan
    #  a. review the constants in html_tags.py and import that file into this one.
    #  b. use print statements to create your about_me web page according to your plan

    # Step 4. Reflect
    #  a. test and debug your page, you can get help from a classmate or TA using our debugging
    #     procedures.
    #  b. compare the result to your output, do they match
    #  c. get feedback from two classmates, choose one suggestion to make your page better,
    #     document the change in the code and give credit
    #  d. check your work against the rubric before submitting
    print("Nothing to see here.", path)  # Remove this line


class MyServer(BaseHTTPRequestHandler):
    """
    MyServer is your own personal web server. Instead of serving web pages from files, though it
    can do that, it will be running Python programs and sending generated output to users.

    You probably will not understand much of this code at the start of the year, but as we progress
    through the material you will begin to be able to read and understand what is happening.
    """

    def do_GET(self):
        """
        When a visitor sends a URL to our webserver this function will be called to handle it.
        """
        url = urlparse(self.path)
        if url.path in files:
            self.send_response(200)
            self.send_header('Content-type', mimetypes.guess_type(url.path)[0])
            self.end_headers()

            # Open the file
            with open(url.path[1:], 'rb') as file:
                self.wfile.write(file.read())  # Read the file and send the contents

            return

        with redirect_stdout(os.fdopen(os.dup(self.wfile.fileno()), "w")):
            command = url.path[1:]
            arguments = parse_qs(url.query)
            if command in features.keys():
                features[command](arguments, self)

            else:
                self.send_html_header()

                print_about_me(self.path)

    def send_html_header(self):
        """
        send_html_header tells your web browser to expect an HTML response
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()


def start(host_name="localhost", port=8080):
    global files
    files = [os.path.join(dp, f)[1:] for dp, dn, fn in os.walk('.') for f in fn]
    logging.debug("Available files: ", files)
    web_server = HTTPServer((host_name, port), MyServer)
    logging.info("Server started http://%s:%s" % (host_name, port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    logging.info("Server stopped.")


def add_feature(name, function):
    features[name] = function


if __name__ == "__main__":
    start()
