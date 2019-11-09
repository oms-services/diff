# diff

An OMS service to diff text content. Uses Google's
[diff-match-patch](https://github.com/google/diff-match-patch).

## How to Run

### OMS-CLI

```console
$ oms run diff -a t1="thisisatext" -a t2="thisisNOTatext"
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
