#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import rospy
from sensor_msgs.msg import NavSatFix


class Print_gps:
    def __init__(self):
        rospy.init_node("print_gps")

        sub_gps = rospy.Subscriber(
            "mavros/global_position/global", NavSatFix, self.print_gps, queue_size=1
        )  # Fra Ardupilot

        # sub_gps = rospy.Subscriber(
        #     "gps/fix", NavSatFix, self.print_gps, queue_size=1
        # )  # FakeGPS

        self.rate = rospy.Rate(2)

    def print_gps(self, msg_gps):
        print("\nGPS data:")
        print("\tTidsstempel:")
        print("\t\tsekunder:", msg_gps.header.stamp.secs)
        print("\t\tnanosekunder:", msg_gps.header.stamp.nsecs)
        print(
            "\tbreddegrad:", msg_gps.latitude
        )  # Positivt tall er nord for ekvator, negativt er sør
        print(
            "\tlengdegrad:", msg_gps.longitude
        )  # Positivt tall er øst for Greenwich, negativt vest
        print(
            "\thøyde:".decode("utf-8"), msg_gps.altitude
        )  #  NaN hvis ingen høyde er tilgjengelig
        print("\tstatus gps:", msg_gps.status.status, end="")
        if msg_gps.status.status >= 0:
            print(" -- OK")
        else:
            print(" -- ikke fått gps fix".decode("utf-8"))


if __name__ == "__main__":
    try:
        p = Print_gps()
        while not rospy.is_shutdown():
            p.rate.sleep()

    except rospy.ROSInterruptException:
        pass
