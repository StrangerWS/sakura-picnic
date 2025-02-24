init -1000 python:
    tlotwDefaultPath = '../../res/'

init -998 python:
    def tlotwGetImage(file):
        return tlotwDefaultPath + "image/%s" % (file)
    def tlotwGetAchImage(file):
        return tlotwDefaultPath + "image/gui/ach/%s" % (file)
    def tlotwGetSnd(file):
        return tlotwDefaultPath + "sound/%s" % (file)
    def tlotwGetMusic(file):
        return tlotwDefaultPath + "music/%s" % (file)

# VisualFX
init:
    $ flash = Fade(.25, 0, .75, color="#fff")