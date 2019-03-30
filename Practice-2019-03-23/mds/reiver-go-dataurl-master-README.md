# go-dataurl

A library that provides tools to work with **data URLs**, as defined by [RFC 2397](http://www.faqs.org/rfcs/rfc2397.html),
for the Go programming language.

Here are some data URL examples:

* data:,Hello%20world!
* data:text/html;base64,PGh0bWw+PGhlYWQ+PHRpdGxlPlRlc3Q8L3RpdGxlPjwvaGVhZD48Ym9keT48cD5UaGlzIGlzIGEgdGVzdDwvYm9keT48L2h0bWw+Cg==

* data:text/plain;charset=utf-8,This%20is%20a%20test%21
* data:;charset=utf-8,This%20is%20a%20test%21
* data:text/plain,This%20is%20a%20test%21
* data:,This%20is%20a%20test%21

* data:text/plain;charset=utf-8;base64,VGhpcyBpcyBhIHRlc3Qh
* data:;charset=utf-8;base64,VGhpcyBpcyBhIHRlc3Qh
* data:text/plain;base64,VGhpcyBpcyBhIHRlc3Qh
* data:;base64,VGhpcyBpcyBhIHRlc3Qh


## Documention

Online documentation, which includes examples, can be found at: http://godoc.org/github.com/reiver/go-dataurl

[![GoDoc](https://godoc.org/github.com/reiver/go-dataurl?status.svg)](https://godoc.org/github.com/reiver/go-dataurl)


## Example
```
parcel, err := dataurl.Parse("data:,Hello%20world!")
if nil != err {
    //@TODO
}

fmt.Printf("Content: %q \n", parcel.String()) // parcel.String() == "Hello world!"
fmt.Printf("Media Type: %q \n", parcel.MediaType()) // parcel.MediaType() == "text/plain;charset=US-ASCII"
```

## Another example
```
// Note that dataurl.MustPasre() will panic() if there is an
// error when trying to parse the data URL!
parcel := dataurl.MustParse("data:,Hello%20world!")

fmt.Printf("Content: %q \n", parcel.String()) // parcel.String() == "Hello world!"
fmt.Printf("Media Type: %q \n", parcel.MediaType()) // parcel.MediaType() == "text/plain;charset=US-ASCII"
```

