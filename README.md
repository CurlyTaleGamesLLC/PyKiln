# What is PyKiln? #

PyKiln is an open source web based kiln controller written in Micropython that runs on an ESP32.

This project is not complete just yet, but feedback and contributors are welcome.

# Quick Setup #

[Follow this video on how to set up your PyKiln](http://pykiln.com/get-started.html "Follow this video on how to set up your PyKiln")
(This isn't finished yet, but it will eventually live here)

# Screenshots #

![Home page of PyKiln, select a firing schedule to begin firing](/docs/images/01_home.png)
![Edit page of PyKiln, create, duplicate, import, export and delete firing schedules](/docs/images/02_edit.png)
![Logging page of PyKiln, view how past fires have gone as well as kiln statistics](/docs/images/03_logs.png)
![Settings page of PyKiln, set your preferred temperature, set up email notification, as well as other settings](/docs/images/04_settings.png)

# Getting Started

[Install Micropython + PyKiln on an ESP32](/getting-started.md "Install Micropython + PyKiln on an ESP32")

[Installing Development Tools](/gettings-started.md "Installing Development Tools")

## Libraries Used

We stand on the shoulders of giants. I used many libraries to piece together this project. Here are the high level ones, I'm sure there are more that I haven't listed.

* [Vue](https://github.com/vuejs/vue "Vue")
* [Vue Draggable](https://github.com/SortableJS/Vue.Draggable "Vue Draggable")
* [Chartjs](https://github.com/chartjs/Chart.js "Chartjs")
* [Axios](https://github.com/axios/axios "Axios")
* [Bootstrap 4](https://getbootstrap.com/ "Bootstrap 4")
* [jQuery](https://github.com/jquery/jquery "jQuery")
* [Popper](https://github.com/popperjs/popper-core "Popper")
* [Google Material Design Icons](https://github.com/google/material-design-icons "Google Material Design Icons")
* [Roboto - Christian Robertson](https://fonts.google.com/specimen/Roboto?preview.text_type=custom "Roboto - Christian Robertson")
* [MultithreadedSimpleHTTPServer](https://github.com/Nakiami/MultithreadedSimpleHTTPServer "MultithreadedSimpleHTTPServer")
* [Swagger UI](https://github.com/swagger-api/swagger-ui "Swagger UI")
* [MCP9600 MicroPython](https://github.com/CurlyTaleGamesLLC/Adafruit_MicroPython_MCP9600 "MCP9600 MicroPython")
* [picoweb](https://github.com/pfalcon/picoweb "picoweb")
* [Cookie Consent](https://github.com/osano/cookieconsent "Cookie Consent")


## Inspiration
This project was written from scratch, three times now actually, it used to run on a Raspberry Pi, but is being ported over to run on a ESP32 running Micropython. That said I wanted to give some shout outs to some people and projects that I've referenced:

- https://github.com/jbruce12000/kiln-controller
- https://github.com/apollo-ng/picoReflow
