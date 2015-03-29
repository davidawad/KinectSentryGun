# KinectSentryGun

![computers](https://github.com/DavidAwad/KinectSentryGun/blob/master/images/computers.jpg?raw=true)

## How it works
This app uses a Microsoft Kinect in order to watch any given area. What the app will do is while the camera is on, the sentry is "watching". 

While the sentry is watching any given area, the Kinect will know when a person's body has walked in front of the camera. If a person has walked in front of the camera then we will instantly send a signal to an automatic machine nerf gun. 

![initial teardown](https://github.com/DavidAwad/KinectSentryGun/blob/master/images/inital_teardown.jpg?raw=true)

The nerf gun is something we bought from walmart that we purchased in the beginning of the hackathon, we opened it and with the help of the PSU mentors reverse engineered the signals to launch the darts. 
![init 2](https://github.com/DavidAwad/KinectSentryGun/blob/master/images/gun_teardown2.jpg?raw=true)

![](https://github.com/DavidAwad/KinectSentryGun/blob/master/images/gun_teardown3.jpg?raw=true) 


###The nerf gun is being controlled by an Arduino Mega that has contacts which have been soldered and tied with electrical tape to the internals of the gun.
![](https://github.com/DavidAwad/KinectSentryGun/blob/master/images/gun_teardown4.jpg?raw=true)

![](https://github.com/DavidAwad/KinectSentryGun/blob/master/images/gun_teardown5.jpg?raw=true)

Every time we launch a dart we take a screenshot with the kinect, and then we tweet the photo of the person after they've been shot. 


The next thing we did was build up a flask backend that's monitoring the twitter account and keeping a counter of how many tweets have been made by the gun, aka how many 

This is my submission for HackPSU sponsored by MLH. Huge thanks to my teammates and other PSU students and mentors!! 

## Running the app




## Contributors 
[Mariam Tsilosani](https://www.facebook.com/tim.giblin.50?fref=ts&__mref=message_bubble)

[Tim Giblin](https://www.facebook.com/tim.giblin.50?fref=ts&__mref=message_bubble)

[Robert Casale](https://github/gearheads)

[Ben Green](https://github.com/benhgreen)

[George El-Mallakh](https://www.youtube.com/watch?v=Jkoeu_aSkjc)

Of Course [Alex Suirbely](I DON'T KNOW A LINK)

![HACK PSU Logo](http://www.hackpsu.org/images/hackpsu3-2.png) 

![Major League Hacking](http://mlh.io/assets/logos/mlh-small-text-21f0abdc906225a212cac33b7c6a5139.png) 

