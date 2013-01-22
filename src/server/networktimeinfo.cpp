/***************************************************************************
**                                                                        **
**  Copyright (C) 2013 Jolla Ltd.                                         **
**  Contact: Petri M. Gerdt <petri.gerdt@jollamobile.com>                 **
**                                                                        **
**     This file is part of Timed                                         **
**                                                                        **
**     Timed is free software; you can redistribute it and/or modify      **
**     it under the terms of the GNU Lesser General Public License        **
**     version 2.1 as published by the Free Software Foundation.          **
**                                                                        **
**     Timed is distributed in the hope that it will be useful, but       **
**     WITHOUT ANY WARRANTY;  without even the implied warranty  of       **
**     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.               **
**     See the GNU Lesser General Public License  for more details.       **
**                                                                        **
**   You should have received a copy of the GNU  Lesser General Public    **
**   License along with Timed. If not, see http://www.gnu.org/licenses/   **
**                                                                        **
***************************************************************************/

#include "networktimeinfo.h"

NetworkTimeInfo::NetworkTimeInfo(const QDateTime &dateTime,
                                 const int daylightAdjustment,
                                 const int offsetFromUtc,
                                 const qlonglong timestampSeconds,
                                 const qlonglong timestampNanoSeconds,
                                 const QString &mnc,
                                 const QString &mcc)
    : m_dateTime(dateTime), m_daylightAdjustment(daylightAdjustment),
      m_offsetFromUtc(offsetFromUtc),
      m_timestampSeconds(timestampSeconds),
      m_timestampNanoSeconds(timestampNanoSeconds),
      m_mnc(mnc), m_mcc(mcc)
{
}

NetworkTimeInfo::NetworkTimeInfo(const NetworkTimeInfo &other)
{
    m_dateTime = other.dateTime();
    m_daylightAdjustment = other.daylightAdjustment();
    m_offsetFromUtc = other.offsetFromUtc();
    m_timestampSeconds = other.timestamp()->tv_sec;
    m_timestampNanoSeconds = other.timestamp()->tv_nsec;
    m_mnc = other.mnc();
    m_mcc = other.mcc();
}

NetworkTimeInfo::NetworkTimeInfo()
{
}

NetworkTimeInfo::~NetworkTimeInfo()
{
}

QDateTime NetworkTimeInfo::dateTime() const
{
    return m_dateTime;
}

int NetworkTimeInfo::offsetFromUtc() const
{
    return m_offsetFromUtc;
}

int NetworkTimeInfo::daylightAdjustment() const
{
    return m_daylightAdjustment;
}

timespec* NetworkTimeInfo::timestamp() const
{
    struct timespec *ts = new timespec;
    ts->tv_sec = m_timestampSeconds;
    ts->tv_nsec = m_timestampNanoSeconds;
    return ts;
}

QString NetworkTimeInfo::mnc() const
{
    return m_mnc;
}

QString NetworkTimeInfo::mcc() const
{
    return m_mcc;
}

bool NetworkTimeInfo::isValid() const
{
    return m_dateTime.isValid();
}

QString NetworkTimeInfo::toString() const
{
    if (!m_dateTime.isValid())
        return QString("Invalid");

    return QString("%1, UTC offset: %2, DST: %3, MNC: %4, MCC: %5, Received: %6.%7")
            .arg(m_dateTime.toString())
            .arg(m_offsetFromUtc)
            .arg(m_daylightAdjustment)
            .arg(m_mnc)
            .arg(m_mcc)
            .arg(m_timestampSeconds)
            .arg(m_timestampNanoSeconds);
}
