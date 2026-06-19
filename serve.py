#!/usr/bin/env python3
"""Static file server with clean-URL fallback for the Flow Control Valves site.

Serves files from the project directory. If a request like /manufacturing has no
matching file, it transparently tries /manufacturing.html (mirroring `npx serve`).
"""
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class CleanURLHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        local = super().translate_path(path)
        # If the path has no extension and the file doesn't exist, try .html
        if not os.path.exists(local) and not os.path.splitext(local)[1]:
            html = local.rstrip("/\\") + ".html"
            if os.path.isfile(html):
                return html
        return local

    def end_headers(self):
        # Avoid stale cached images/CSS during development
        self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = ThreadingHTTPServer(("0.0.0.0", port), CleanURLHandler)
    print(f"Serving Flow Control Valves site on http://localhost:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
