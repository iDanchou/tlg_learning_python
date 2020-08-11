from time import sleep
from progress.bar import Bar

def probar():
    with Bar('Launching...') as bar:
        for i in range(100):
            sleep(0.02)
            bar.next()
probar()