import random
import string
import json
import cherrypy


@cherrypy.expose
class Presupuesto(object):

    @cherrypy.tools.accept(media='application/json')
    @cherrypy.tools.json_in()
    def POST(self, length=8):
        #objects = cherrypy.request.json
        presupuesto = random.randint(500, 99999)
        return str(presupuesto)


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.config.update({'server.socket_port': 9090})
    cherrypy.quickstart(Presupuesto(), '/presupuesto', conf)

