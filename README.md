# dreamstudio
A web server provides stable diffusion service.

## usage

1. fill `.env` file

```.env
STABILITY_KEY=sk-your-key
BAIDU_FANYI_APPID=your-baidu-fanyi-appid
BAIDU_FANYI_KEY=your-baidu-fanyi-key
PORT=5006
```

you can gain `STABILITY_KEY` from [dreamstudio](https://beta.dreamstudio.ai/).

and you can gain `BAIDU_FANYI` from [baidu-fanyi](https://fanyi-api.baidu.com/api/trans/product/desktop).

2. docker-compose

```sh
docker-compose up -d
```

3. access url and enjoy

access http://localhost:5006/?prompt=一幅美丽的奇异灯塔画作，将光芒照耀在汹涌的红色海洋中。greg rutkowski 和 thomas kinkade 的黄色配色方案，artstation网站上的流行趋势
