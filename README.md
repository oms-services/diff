# diff
An OMG service to diff text content. Uses google's [diff-match-patch](https://github.com/google/diff-match-patch).

# How to Run

### OMG-CLI

```bash 
$ npm install -g omg

$ omg validate 
$ omg exec diff t1:"thisisatext" t2:"thisisNOTatext"
```

### StoryScript 

> TODO

### Mnual Build and Run 

```bash
# Setup 
$ virtualenv venv --python=python3.6
$ source venv/bin/activate 
$ pip install -r requirements.text

# To run tests
$ python -m unittest 

# To run dev server locally 
$ python app.py

# To run via Docker 
$ docker build -t diff . 
$ docker run diff
```

The following show and example output for `GET /diff/?t1=This&t2=boo`

#### Example of parsed output via `/parse/`:

```
{
    "diff": "@@ -1,4 +1,3 @@\n-This\n+boo\n",
    "type": "parsed"
}
```

#### Example of raw output via `/parse/raw/`:

```
{
    "diff": [
        [
            -1,
            "This"
        ],
        [
            1,
            "boo"
        ]
    ],
    "type": "raw"
}
```