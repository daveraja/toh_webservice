#!/usr/bin/env bash

curl -X 'POST' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "moves": 15,
  "pegs": [
    {
      "pegid": "a"
    },
    {
      "pegid": "b"
    },
    {
      "pegid": "c"
    }
  ],
  "disks": [
    {
      "diskid": 1
    },
    {
      "diskid": 2
    },
    {
      "diskid": 3
    },
    {
      "diskid": 4
    }
  ],
  "init": [
    {
      "diskid": 1,
      "pegid": "a"
    },
    {
      "diskid": 2,
      "pegid": "a"
    },
    {
      "diskid": 3,
      "pegid": "a"
    },
    {
      "diskid": 4,
      "pegid": "a"
    }
  ],
  "goal": [
    {
      "diskid": 1,
      "pegid": "c"
    },
    {
      "diskid": 2,
      "pegid": "c"
    },
    {
      "diskid": 3,
      "pegid": "c"
    },
    {
      "diskid": 4,
      "pegid": "c"
    }
  ]
}' | json_pp
