# Remote Windows Display Controller

The goal of this project is to create an app that allows the user to change the Display Configuration on Windows without actually having to be where the computer is.

Motivated by the fact that my computer has screens on multiple rooms attached to it. I find it annoying to turn on the TV and realize that the computer is not currently using the TV as a display.

# How to use it

Currently, you can only do 3 things:

1. See current configuration of active monitors

   1.1. GET /display/config/

2. Disable a monitor

   2.1. DELETE /display/{display_id}

   2.2 You can get display_id via the request at 1

3. Change the configuration of a monitor(even if it is disabled)

   3.1. POST /display/

   3.2. The basic format is

   ```json
   {
     "logical_name": "\\\\.\\DISPLAYNUMBER",
     "width": 1920,
     "height": 1080,
     "refresh_rate": 60
   }
   ```

   3.3. This is extremely unreliable. Sometimes not the desired monitor turns on, sometimes more than one monitor turns on. At the time of writing, I haven't been able to make it reliable enough. Still thinking on whether or not I will pursue it further. Currently, it is able to solve my problem, even though it is not necessarily easy.

# Problems and rants

I haven't been able to test this reliably enough to create an actual application that common users can use.

Some of the problems I had are listed beneath:

1.  Sometimes "EnumDisplayDevices" shows the same DeviceID for all Devices, and I still haven't been able to actually discover how to reproduce it. At the time of writing, it only happens when I disable my LG 4k Monitor

2.  Upon device activation, it seems Windows always activate the monitor with the smaller "Device" name.

3.  There is no way to previously know which "Device Name" Windows is going to give to your monitor. Or at least, I wasn't able to understand it well enough to work around it.

4.  Because of the above problems, the only way I was able to achieve my desired goal, which is to activate my TV as a Display, and disable the other monitors, was through steps to avoid each of the problems above.

    4.1. To reliably do it, I have to:

        4.1.1. Enable all displays at 1080p@60FPS

        4.1.2. Disable all undesired displays

        4.1.3. Change the configuration of the remaining displays to the actual desired effect.

    4.2 The above steps have to be done with a timeout between them, otherwise Windows may crash.

5.  At the time of writing, I haven't decided whether or not I will try to implement Scaling configuration

6.  Still have to do a frontend to the application. Currently, for development usage, I just use Postman(Desktop) and HTTPBot(mobile). They work well enough for me, but I can't expect the commmon user to go through the trouble of learning how to actually use it

7.  It's probably way better to do what I am trying to achieve through C++ or C# directly. I may or may not go to that route in the future.
