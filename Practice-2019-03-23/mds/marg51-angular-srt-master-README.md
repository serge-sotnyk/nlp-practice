# angular-srt

AngularJS SRT parser and stringifier

# How to use

#### Load the dependency

```javascript
var app = angular.module('myApp', ['uto.srt']);
```

#### Use the service

`SrtService.parse(String)`

```javascript
app.controller('MyCtrl', function ($scope, SrtService) {
	$scope.subtitles = SrtService.parse("1\n00:00:01 --> 00:00:10\nHello every one !\n\n1\n00:00:10,100 --> 00:00:20\nIt's a beautiful day !");

	console.log($scope.subtitles);
	/*
	 [
		{id: 1, start: 1, end: 10, text: "Hello every one !"},
		{id: 2, start: 10.1, end: 20, text: "It's a beautiful day !"}
	]
	*/
});
```

`SrtService.stringify(Array)`

Does the opposite

### methods

- `SrtService.parse(String)`
- `SrtService.stringify(Array)`
- `SrtService.toSeconds(String)`
- `SrtService.toTimestamp(Number)`

