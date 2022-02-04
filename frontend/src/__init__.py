from pyfyre.widgets import *
from pyfyre.ajax import Ajax
from pyfyre.pyfyre import runApp

class App(UsesState):
    def __init__(self):
        self.greet = "Welcome"
        self.posts = []

        self.get_posts()

    def get_posts(self):
        Ajax.get("http://localhost:8001/api/get_posts", then=self.display)

    def display(self, res):
        self.posts = res.json
        self.update()

    def build(self):

        def postView(i):
            return Container(
                className="flex flex-col text-xl w-8/12 mx-auto bg-[#222222] px-10 py-16 rounded-md",
                children=[
                    Text(self.posts[i]["fields"]["title"]),
                    Text(self.posts[i]["fields"]["description"]),
                ]
            )

        return Container(
            className="h-screen w-screen flex flex-col",
            children=[
                Text(
                    "PyFyre Django Full Stack Web App",
                    className="font-bold text-5xl mt-20 mx-auto"
                ),
                ListBuilder(
                    className="h-screen w-screen flex flex-col justify-start space-y-5 mt-10 text-white",
                    count=len(self.posts),
                    builder=postView
                )
            ]
        )

runApp(
    App(),
    mount="app-mount"
)