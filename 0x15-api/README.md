# API

[requests detailed video](https://www.youtube.com/watch?v=tb8gHvYlCFs&t=300s)

[CSV File in Python](https://www.scaler.com/topics/how-to-create-a-csv-file-in-python/)

all scripts are similar to :

```js
fetch("https://jsonplaceholder.typicode.com/users/")
  .then((response) => response.json())
  .then((json) => console.log(json));
```

## Useful Notes:

1. `print(dir(requests))` to know all available methods for an object
2. To ensure that all the values in your CSV are enclosed in double quotes, you can adjust the CSV writer configuration by using the `csv.QUOTE_ALL` constant. This will quote all fields, regardless of their type.
