# azure-ocr
Based on Polymer cheese app make OCR of scanned text


## Usage

The `words` property of `<azure-ocr>` component is a handy shortact that results list of recognized words for quick access by user:

Example of entire text:

> No Answer mutisme / silence The amorous subject suffers anxiety because the loved object replies scantily or not at all to his language (discourse or letters).

```js
["No", "Answer", "mutisme", "/", "silence", "The", "amorous", "subject", "suffers", "anxiety", "because", "the", "loved", "object", "replies", "scantily", "or", "not", "at", "all", "to", "his", "language", "(discourse", "or", "letters)."]
```

The `results` property of `<azure-ocr>` component will contain information about recognized and extracted text. For example:

```js
{
  "language": "en",
  "textAngle": 0,
  "orientation": "Up",
  "regions": [
    {
      "boundingBox": "182,131,608,267",
      "lines": [
        {
          "boundingBox": "183,131,324,59",
          "words": [
            {
              "boundingBox": "183,132,89,58",
              "text": "No"
            },
            {
              "boundingBox": "286,131,221,58",
              "text": "Answer"
            }
          ]
        },
        {
          "boundingBox": "182,233,277,30",
          "words": [
            {
              "boundingBox": "182,234,122,26",
              "text": "mutisme"
            },
            {
              "boundingBox": "324,233,16,30",
              "text": "/"
            },
            {
              "boundingBox": "362,233,97,26",
              "text": "silence"
            }
          ]
        },
        {
          "boundingBox": "182,294,608,32",
          "words": [
            {
              "boundingBox": "182,300,49,23",
              "text": "The"
            },
            {
              "boundingBox": "240,305,109,17",
              "text": "amorous"
            },
            {
              "boundingBox": "357,298,87,28",
              "text": "subject"
            },
            {
              "boundingBox": "452,296,82,24",
              "text": "suffers"
            },
            {
              "boundingBox": "542,296,91,28",
              "text": "anxiety"
            },
            {
              "boundingBox": "642,296,100,22",
              "text": "because"
            },
            {
              "boundingBox": "751,294,39,22",
              "text": "the"
            }
          ]
        },
        {
          "boundingBox": "184,329,578,33",
          "words": [
            {
              "boundingBox": "184,335,67,23",
              "text": "loved"
            },
            {
              "boundingBox": "260,334,75,28",
              "text": "object"
            },
            {
              "boundingBox": "345,333,80,29",
              "text": "replies"
            },
            {
              "boundingBox": "434,332,96,28",
              "text": "scantily"
            },
            {
              "boundingBox": "538,338,27,16",
              "text": "or"
            },
            {
              "boundingBox": "574,335,40,20",
              "text": "not"
            },
            {
              "boundingBox": "623,336,22,18",
              "text": "at"
            },
            {
              "boundingBox": "654,330,32,23",
              "text": "all"
            },
            {
              "boundingBox": "694,333,25,20",
              "text": "to"
            },
            {
              "boundingBox": "727,329,35,23",
              "text": "his"
            }
          ]
        },
        {
          "boundingBox": "184,368,396,30",
          "words": [
            {
              "boundingBox": "184,371,112,27",
              "text": "language"
            },
            {
              "boundingBox": "307,369,129,28",
              "text": "(discourse"
            },
            {
              "boundingBox": "445,374,27,17",
              "text": "or"
            },
            {
              "boundingBox": "481,368,99,25",
              "text": "letters)."
            }
          ]
        }
      ]
    }
  ]
}
```

## Author

@peterblazejewicz

