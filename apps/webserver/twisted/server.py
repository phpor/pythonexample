# http://twistedmatrix.com/trac/

from twisted.web import server, resource
from twisted.internet import reactor, endpoints


class Counter(resource.Resource):
    isLeaf = True
    numberRequests = 0

    def render_get(self, request):
        self.numberRequests += 1
        request.setHeader(b"content-type", b"text/plain")
        content = u"I am request #{}\n".format(self.numberRequests)
        return content.encode("ascii")

endpoints.serverFromString(reactor, "tcp:8888").listen(server.Site(Counter()))
reactor.run()
