QT -= gui
QT += dbus

TEMPLATE = app
TARGET = fake-dialog-ui

VERSION = $$(TIMED_VERSION)

INCLUDEPATH += ../h

QMAKE_LIBDIR_FLAGS += -L../voland -L../lib
LIBS += -ltimed-voland -ltimed

CONFIG += iodata qmlog

SOURCES = fake-dialog-ui.cpp
HEADERS = fake-dialog-ui.h

INSTALLS += target
target.path = $$(DESTDIR)/usr/bin

QMAKE_CXXFLAGS  += -Wall -Wno-psabi
QMAKE_CXXFLAGS  += -Wall -Werror
