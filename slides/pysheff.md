name: pysheff
# Python Sheffield

####Contact:

Find Python Sheffield at:
* Twitter: @pysheff
* GoogleGroups: http://groups.google.com/group/python-sheffield
* Calendar: http://opentechcalendar.co.uk/group/236-python-sheffield

####Upcoming Sheffield events:
* Full(ish) lists here: http://sheffgeeks.github.io/
* Thu 26 Feb: Sheffield.js
* Sat 28 & Sun 01 Mar: Hack Weekend
* Tue 03 Mar: Dot Net Sheff
* Wed 04 Mar: Geeks in the Pub (not yet announced)
* Mon 09 Mar: Sheffield Ruby User Group (not yet announced)
* Tue 10 Mar: (def sheff) - no official meetup for March
* ...

???

Welcome to python sheffield.

Python Sheffield is @pysheff on twitter and you may subscribe to emails on our google group which is python dash sheffield.

We are now also using open tech calendar as the primary means to schedule events

Along with us you will also be able to find out about a good number of the local sheffield tech events by heading to the shefgeeks site. Some of the upcoming events are listed here.

Sheffield.js is a couple of days away.

Hack Weekend is a new monthly meetup of sorts where the idea is people turn up to do whatever projects they feel like.

I understand Dot Net Sheff is doing something arduino related this month.

I also understand def sheff is skipping a March meeting and will be back in April. However, there may be a social get together on that night anyway.

---
#Talk evening schedule:

#### Interactive data exploration using pandas and the ipython notebook
* Will Furness (@WillFurnass) 


#### How to ask about gender
* Chad (@kitation)


#### Asynchronous python web apps
* Gary Martin (@allegary)

#### Pub

---
name: title
class: inverse, middle
## Asynchronous Python Web Apps using WebSockets and Tornado

### Python Sheffield, February 2015

#### Gary Martin | [@allegary](https://twitter.com/allegary) | [garym on GitHub](https://github.com/garym) | [WANdisco](https://wandisco.com/)

???
As we go through this presentation, you will hopefully note that this is a fairly light introduction to the subject of asynchronous web development with a focus on some fun you can have with web sockets.

You will probably note that I hardly touch on the asynchronous side of things though I will be creating my application with tornado as the web framework.

I will give you a really vague idea about how web programming works in an idealised form.

Without any dates of references, none of this is meant to be any more than a vague idealised history.

Bear in mind that what we are after is the ability to create a rich web application like a messaging application of some sort.

---
name: staticpages
class: inverse, middle

- Words
--

- More Words
--

- **Bold Words**
- *Emphasised Words*
- <marquee>Moving Words</marquee>
???

In the beginning there was the word, after a while the word got bored, found some more words to be friends with and eventually web developers got around to herding them up between sets of html tags. 

--

- (Sorry - left in intentionally.)
---
name: webserver
class: inverse, middle

```
      Web Browser                    +-Servers--------------------+
                                     |                            |
 +--------------------+              |  Web server                |
 |< > X [___________] |              |   +------+                 | 
 +--------------------+              |   |      |                 |
 |                    | -------------+-> |      |                 |
 |                    | <------------+-- |      |                 |
 |                    |              |   |      |                 |
 |                    | -------------+-> |      |                 |
 |                    | <------------+-- |      |                 |
 |                    |              |   |      |                 |
 |                    | -------------+-> |      |                 |
 |                    | <------------+-- |      |                 |
 |                    |              |   |      |                 |
 |                    | -------------+-> |      |                 |
 |                    | <------------+-- |      |                 |
 |                    |              |   |      |                 |
 |                    | -------------+-> |      |                 |
 |                    | <------------+-- |      |                 |
 |                    |              |   |      |                 |
 |                    | -------------+-> |      |                 |
 |                    | <------------+-- |      |                 |
 |                    |              |   +------+                 |
 +--------------------+              +----------------------------+
```

???
It is hardly worth spending any time in this static world as we can hardly expect to be able to deal with live messages yet.

However, given a sprinkling of client side scripting, we do get a good way there.

In this very mich idealised diagram, we send a single request to the webserver, it decides what to do with the request and, hopefully you get a response back.

---
name: wsgiserver
class: inverse, middle

```
      Web Browser                    +-Servers--------------------+
                                     |                            |
 +--------------------+              |  Web server   WSGI server  |
 |< > X [___________] |              |   +------+      +------+   | 
 +--------------------+              |   |      |      |      |   |
 |                    | -------------+-> |      |      |      |   |
 |                    |              |   |      | ---> |      |   |
 |                    |              |   |      | <--- |      |   |
 |                    | <------------+-- |      |      |      |   |
 |                    |              |   |      |      |      |   |
 |                    | -------------+-> |      |      |      |   |
 |                    | <------------+-- |      |      |      |   |
 |                    |              |   |      |      |      |   |
 |                    | -------------+-> |      |      |      |   |
 |                    | <------------+-- |      |      |      |   |
 |                    |              |   |      |      |      |   |
 |                    | -------------+-> |      |      |      |   |
 |                    |              |   |      | ---> |      |   |
 |                    |              |   |      | <--- |      |   |
 |                    | <------------+-- |      |      |      |   |
 |                    |              |   |      |      |      |   |
 |                    |              |   |      |      |      |   |
 |                    |              |   +------+      +------+   |
 +--------------------+              +----------------------------+
```

???

Obviously we are interested in getting some server side code, preferably in python, even more obviously, to get some of our rich behaviour.

Python has long been used as a web programming language on the server side. For the most part this is currently helped by something called WSGI.

The Web Server Gateway Interface is a specification for a simple interface between a web server and Python web applications that originates from PEP 333.

This allows you (or more usually the web framework you choose) to code to that interface with the expectation that there are either modules or wrappers to allow you to serve the code on the webserver of your choice.

So, now the interaction between your browser and the server looks more like this.

Whenever the webserver recognises that there should be something to pass on to the web app, it will send it over, keep the connection open until your app hands back a response and so on.

Of course, the WSGI app may not be the only other server process involved in all this, there may be a database and any number of other services to complicate things.

---
name: longpolling
class: inverse, middle

```
      Web Browser                    +-Servers--------------------+
                                     |                            |
 +--------------------+              |  Web server   WSGI server  |
 |< > X [___________] |              |   +------+      +------+   | 
 +--------------------+              |   |      |      |      |   |
 |                    | -------------+-> |      | ---> |      |   |
 |                    | <------------+-- |      | <--- |      |   |
 |                    | -------------+-> |      | ---> |      |   |
 |                    | <------------+-- |      | <--- |      |   |
 |                    | -------------+-> |      | ---> |      |   |
 |                    | <------------+-- |      | <--- |      |   |
 |                    | -------------+-> |      | ---> |      |   |
 |                    | <------------+-- |      | <--- |      |   |
 |                    | -------------+-> |      | ---> |      |   |
 |                    | <------------+-- |      | <--- |      |   |
 |                    | -------------+-> |      | ---> |      |   |
 |                    | <------------+-- |      | <--- |      |   |
 |                    | -------------+-> |      | ---> |      |   |
 |                    | <------------+-- |      | <--- |      |   |
 |                    | -------------+-> |      | ---> |      |   |
 |                    | <------------+-- |      | <--- |      |   |
 |                    |              |   |      |      |      |   |
 |                    |              |   +------+      +------+   |
 +--------------------+              +----------------------------+
```

???

So, this is pretty much enough to make an instant chat application though you might need to live with a few restrictions and your perception of instantness may leave a bit to be desired.

First of all, the browser is going to be very much in control of working out when it should ask the server for whether there is a new message.

Given that there might not be anything specifically for your client to receive, most of these requests are just going to be "sorry no data" and given that result, to appear snappy, your browser will then be repeating the question very soon after that.

One improvement we can attempt here is to hold the request open for a much longer time, thus increasing our chances of being able to pass back a genuine update.

This is also not without problems. There are questions of how long it should be for a connection to timeout and there is also less indication to the browser that the server is well behaved as the timeout increases.

Anyway, at best, we are still expecting the browser to keep sending new requests after each real update.

So, now we want to turn the problem on its head...

---
name: websockets
class: inverse, middle

```
      Web Browser                    +-Servers--------------------+
                                     |                            |
 +--------------------+              |  Web server   WSGI server  |
 |< > X [___________] |              |   +------+      +------+   | 
 +--------------------+              |   |      |      |      |   |
 |                    | -------------+-> |      | ---> |      |   |
 |                    |              |   |      |      |      |   |
 |                    |              |   |      |      |      |   |
 |                    | <------------+-- |      | <--- |      |   |
 |                    |              |   |      |      |      |   |
 |                    |              |   |      |      |      |   |
 |                    |              |   |      |      |      |   |
 |                    |              |   |      |      |      |   |
 |                    | <------------+-- |      | <--- |      |   |
 |                    | <------------+-- |      | <--- |      |   |
 |                    |              |   |      |      |      |   |
 |                    | -------------+-> |      | ---> |      |   |
 |                    |              |   |      |      |      |   |
 |                    | <------------+-- |      | <--- |      |   |
 |                    | <------------+-- |      | <--- |      |   |
 |                    |              |   |      |      |      |   |
 |                    | <------------+-- |      | <--- |      |   |
 |                    |              |   +------+      +------+   |
 +--------------------+              +----------------------------+
```

???

Instead of the previous picture where the browser keeps pleading with the server for whether there is new data, we use websockets to set up a more permanent connection that is kept open as long as the browser and server wish to maintain the connection.

The connection is bi-directional and so our server can push notifications back to the browser where there is data to be sent.

No new request needs to be issued to ask for the next notification either.

So, apart from heartbeat traffic, we are now in a situation where we are only sending information in each direction when required and this is potentially a huge improvement.

Websockets are not the only way of looking at improving the problem, though they do happen to be one of the better supported. You may also want to learn about WebRTC and Server-Sent Events. Websockets are generally suitable where you require a bi-directional connection and you desire the server to be firmly involved in processing the data.

---
name: Demo1
class: inverse, middle, center

# Demo 1

???

You may want to note that I am using docker and fig for my development environment here. For anyone that uses vagrant, it is somewhat similar to that, allowing you to edit code locally and have that code executing in containers.


