# diff
An OMG service to diff text content. Uses google's [diff-match-patch](https://github.com/google/diff-match-patch).

# How to Run

### OMG-CLI

```bash 
$ npm install -g omg

$ omg validate 
$ omg exec diff t1:"thisisatext" t2:"thisisNOTatext"
```

### Storyscript 

```coffeescript
diff diff t1: "thisisatext" t2: "thisisNOTatext"
diff diff_raw t1: "thisisatext" t2: "thisisNOTatext"
```


The following show and example output for `GET /diff/?t1=This&t2=boo`

#### Example of parsed output via `/parse/`:

```diff
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