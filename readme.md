## Simple Tweepy Tute

* Install [tweepy](https://github.com/tweepy/tweepy)
```commandline
pip install tweepy
```

* Copy `config.ini.sample` to `config.ini`

* Configure `[twitter]` section with your [Twitter API](https://apps.twitter.com/) credentials 

* Configure `[filter]` section for `streaming` API request parameters: [`locations`](https://dev.twitter.com/streaming/overview/request-parameters#locations), [`track`](https://dev.twitter.com/streaming/overview/request-parameters#track). Default is harvesting any tweets related to Melbourne city.

* Run application `python main.py`. Better yet, use PyCharm and run.

### How to get bounding box for locations

* Use http://geojson.io or http://boundingbox.klokantech.com to get your city of interest or domain bounding box
* Usually there are 5 elements in [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) coordinate array. In that case, you will want index `0` and `2` as [an example](http://bl.ocks.org/d/321dea6a84864c1d2c7db3dc6cb8395f) follow:

```
[[
    [144.6075439453,-38.395491533],
    [145.2035522461,-38.395491533],
    [145.2035522461,-37.5990001506],
    [144.6075439453,-37.5990001506],
    [144.6075439453,-38.395491533]
]]


[144.6075439453,-38.395491533, 145.2035522461,-37.5990001506]

```