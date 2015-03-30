# KinectSentryGun

![computers](https://github.com/DavidAwad/KinectSentryGun/blob/master/images/computers.jpg?raw=true)

<a href="http://www.youtube.com/watch?feature=player_embedded&v=5VJsE5mrT44
" target="_blank"><img src="http://img.youtube.com/vi/5VJsE5mrT44/0.jpg" 
alt="youtube video" width="240" height="180" border="10" /></a>

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

![app-frontend](https://github.com/DavidAwad/KinectSentryGun/blob/master/images/FrontEndScreen.png?raw=true)

[Our Front-End](http://kinectsentrygun.projects.benhgreen.com/)

The next thing we did was build up a flask backend that's monitoring the twitter account and keeping a counter of how many shots have been made by the gun, (the number of tweets!). 

Our web app uses the BlockChain API in order to set up a virtual bitcoin wallet to charge 'users' after they have been shot in order to blackmail them into paying our wallet. The site also has a QR code that's generated that you can use to send bitcoin.  

![bitcoin](http://www.canbike.org/public/images/030114/Bitcoin_Logo_Horizontal_Dark-4800px.png)
![Blockchain](http://www.bitcoinweb.nl/wp-content/uploads/2014/02/Blockchain-logo.png)

With the bitcoin we can also store the bitcoin addresses we receive bitcoins with the tweets they are associated with inside of MongoDB so that we can then process users paying our backend wallet in order to delete their embarassing photos!

Once a user pays money to the backend, the tweet will be deleted, and we'll make some bitcoin!

## Hardware:
1. Microsoft Kinect 2
2. Nerf Dart Gun
3. Arduino UNO or Arduino Mega.


### Dependencies: 
1. Microsoft Kinect 2 SDK
2. Arduino IDE 
3. Python 2.7.8 or greater 

## Resources and Examples
1. Look at the Body Index Basics and /Color Basics in the Microsoft Kinect SDK Browser V2. This will explain how most of the code works.
2. Look at example and basic I/O in Arduino. 

#### This is our submission for HackPSU sponsored by MLH. Huge thanks to my teammates and other PSU students and mentors!! 

# Contributors 
##[Mariam Tsilosani](https://www.github.com/mariamtsilosani/)

##[Tim Giblin](https://www.facebook.com/tim.giblin.50?fref=ts&__mref=message_bubble)

##[Robert Casale](https://github/gearheads)

##[Ben Green](https://github.com/benhgreen)

##[George El-Mallakh](https://www.youtube.com/watch?v=Jkoeu_aSkjc)

# Special Thanks
##[Alex Suirbely](I DON'T KNOW A LINK)

##[Justin Keenan]()

## Mike Swift

![HACK PSU Logo](http://www.hackpsu.org/images/hackpsu3-2.png)

![Major League Hacking](http://mlh.io/assets/logos/mlh-small-text-21f0abdc906225a212cac33b7c6a5139.png) 

#### *A windows machine is required for the Kinect Binaries unfortunately! 
