QT -= gui
QT += dbus

TEMPLATE = app
TARGET = ticker

VERSION = $$(TIMED_VERSION)

INCLUDEPATH += ../h

QMAKE_LIBDIR_FLAGS += -L../lib
LIBS += -ltimed -lqmlog

SOURCES = ticker.cpp
HEADERS = ticker.h

INSTALLS += target qmtime-users
target.path = $$(DESTDIR)/usr/bin

qmtime-users.files = qmtime-users.sh
qmtime-users.path = $$(DESTDIR)/usr/bin

CONFIG(MEEGO) \
{
  message("MEEGO flag is set")
  DEFINES += __MEEGO__
} \
else \
{
  CONFIG += cellular-qt
  QMAKE_CXXFLAGS  += -Wall -Wno-psabi
}

CONFIG(dsme_dbus_if) {
    DEFINES += HAVE_DSME
}

QMAKE_CXXFLAGS  += -Wall
