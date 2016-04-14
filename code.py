#!/system/sbin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server, demo_app

httpd = make_server('', 8086, demo_app)
sa = httpd.socket.getsockname()
print 'http://{0}:{1}/'.format(*sa)

# Respond to requests until process is killed
httpd.serve_forever()
