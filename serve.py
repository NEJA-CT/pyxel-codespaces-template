from livereload import Server
server = Server()

# Watch everything in the workspace (adjust globs as needed)
server.watch('src/**/*')

# Serve the current folder at http://localhost:5500
# (Codespaces will auto-forward this port)
server.serve(root='.', host='0.0.0.0', port=5500, restart_delay=0.1)
