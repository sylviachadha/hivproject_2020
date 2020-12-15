##-----------------------------------------
# Part 3 HTTP Server written in Python
##-----------------------------------------

import json
from http.server import BaseHTTPRequestHandler

from plots.Risk import get_risk_count_json
from plots.age import get_age_count_json
from plots.gender import get_sex_count_json
from plots.index_test import get_index_count_json
from plots.new_hiv_cases import get_hiv_count_json
from plots.partnerhiv import get_phiv_count_json
from plots.site import get_site_count_json
from plots.status import get_status_count_json


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.path)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # parsed_path = parse.urlparse(self.path)
        if self.path == "/python-new-hiv-cases":
            response = get_hiv_count_json()
            self.wfile.write(json.dumps(response).encode('utf-8'))

        elif self.path == "/python-hiv-cases-by-site":
            response = get_site_count_json()
            self.wfile.write(json.dumps(response).encode('utf-8'))

        elif self.path == "/python-hiv-cases-by-gender":
            response = get_sex_count_json()
            self.wfile.write(json.dumps(response).encode('utf-8'))

        elif self.path == "/python-hiv-cases-by-status":
            response = get_status_count_json()
            self.wfile.write(json.dumps(response).encode('utf-8'))

        elif self.path == "/python-risk-category":
            response = get_risk_count_json()
            self.wfile.write(json.dumps(response).encode('utf-8'))

        elif self.path == "/python-hiv-cases-by-age":
            response = get_age_count_json()
            self.wfile.write(json.dumps(response).encode('utf-8'))

        elif self.path == "/python-index-test-proportion":
            response = get_index_count_json()
            self.wfile.write(json.dumps(response).encode('utf-8'))

        elif self.path == "/python-partnerHiv":
            response = get_phiv_count_json()
            self.wfile.write(json.dumps(response).encode('utf-8'))


if __name__ == '__main__':
    from http.server import HTTPServer

    server = HTTPServer(('localhost', 8080), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
