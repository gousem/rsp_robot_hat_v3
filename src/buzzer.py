# This file is part of rsp_robot_hat_v3.
# Copyright (C) 2021 Hiwonder Ltd. <support@hiwonder.com>
#
# rsp_robot_hat_v3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rsp_robot_hat_v3 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# title           :buzzer.py
# author          :Hiwonder, LuYongping(Lucas)
# date            :20210205
# notes           :
# ==============================================================================


from ._common import GPIO


def set_state(new_state):
    GPIO.output(31, new_state)


GPIO.setup(31, GPIO.OUT)
set_state(0)
