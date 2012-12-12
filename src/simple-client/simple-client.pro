QT -= gui
QT += dbus

TEMPLATE = app
TARGET = simple-client

VERSION = $$(TIMED_VERSION)

INCLUDEPATH += ../h

QMAKE_LIBDIR_FLAGS += -L../lib -L../voland
LIBS += -ltimed -ltimed-voland -lqmlog

CONFIG += iodata

CONFIG += link_pkgconfig
PKGCONFIG += libpcrecpp

SOURCES = client.cpp

INSTALLS += target
target.path = $$(DESTDIR)/usr/bin

QMAKE_CXXFLAGS  += -Wall -Wno-psabi
QMAKE_CXXFLAGS  += -Wall -Werror
