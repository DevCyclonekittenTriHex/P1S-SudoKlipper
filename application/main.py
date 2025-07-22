import cherrypy
import asyncio

class MyApp:
    @cherrypy.expose
    def index(self):
        return open('site\\index.html')

    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def run(self):
        try:
            input_string = cherrypy.request.json.get('input_string', '')
            result = e()
            print(result)
            return {'result': result}
        except Exception as e:
            return {'error': str(e)}


    def e():
        print("HI")
        return "HI"



if __name__ == '__main__':
    cherrypy.quickstart(MyApp())
