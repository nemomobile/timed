CONFIG(MEEGO) \
{
  message("MEEGO flag is set")
  DEFINES += __MEEGO__
} \
else \
{
  message("MEEGO flag is not set, assuming HARMATTAN")
  CONFIG += cellular-qt
  CONFIG  += dsme_dbus_if
  QMAKE_CXXFLAGS  += -Wall -Wno-psabi
}

QT -= gui
QT += dbus

CONFIG += qmlog
CONFIG += link_pkgconfig

PKGCONFIG += contextprovider-1.0 libpcrecpp
CONFIG(dsme_dbus_if) {
    PKGCONFIG += dsme_dbus_if
}

TEMPLATE = app
TARGET = memory

VERSION = $$(TIMED_VERSION)

INCLUDEPATH += ../h

QMAKE_LIBDIR_FLAGS += -L../lib
LIBS += -ltimed

SOURCES = memory.cpp
HEADERS = memory.h

INSTALLS += target
target.path = $$(DESTDIR)/usr/bin

QMAKE_CXXFLAGS  += -Wall -Werror
