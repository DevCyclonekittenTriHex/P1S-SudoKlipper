import autonomous as auto
def RunFunction(string):
    if(string=="pX"):
        asyncio.Run(auto.MovePrinterX())

    
