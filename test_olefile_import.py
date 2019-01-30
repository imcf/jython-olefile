import sys

sys.path.insert(0, '__pyclasspath__/')
import io

def mark_print(to_print):
    print "=" * 160
    print to_print
    print "=" * 160


try:
    import olefile
except:
    mark_print("importing 'olefile' failed!")

try:
    io_type = type(io)
    print "'io' has type '%s'" % io_type
except NameError as err:
    print "'io' is not available in the namespace: %s" % err
    import io
    print dir(io)
    print io.__file__


mark_print("sys.path: %s" % sys.path)


# import io
# from olefile import __version__
from olefile import olefile

# mark_print("olefile.__version__: %s" % __version__)
mark_print("olefile.__version__: %s" % olefile.__version__)

# import olefile
# import olefile.olefile as olefile

mark_print("olefile.__file__: %s" % olefile.__file__)

sys.exit(0)
