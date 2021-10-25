# rule34mirror
> api mirror for rule34.xxx
## Use
> mirror link 

```https://rule34mirror.herokuapp.com/api?page=dapi&s=post&q=index&limit=10```
> original link 

```https://rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&limit=10```

## How it works
1. request > https://rule34mirror.herokuapp.com/api
2. server render https://rule34.xxx/index.php
3. out json struct