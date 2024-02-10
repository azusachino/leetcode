package http

import (
	"fmt"

	"github.com/valyala/fasthttp"
)

type MyHandler struct {
	foobar string
}

// HandleFastHTTP request handler in net/http style, i.e. method bound to MyHandler struct.
func (h *MyHandler) HandleFastHTTP(ctx *fasthttp.RequestCtx) {
	// notice that we may access MyHandler properties here - see h.foobar.
	fmt.Fprintf(ctx, "Hello, world! Requested path is %q. Foobar is %q",
		ctx.Path(), h.foobar)
}

// request handler in fasthttp style, i.e. just plain function.
func fastHTTPHandler(ctx *fasthttp.RequestCtx) {
	fmt.Fprintf(ctx, "Hi there! RequestURI is %q", ctx.RequestURI())
}

func Serve() {
	// pass bound struct method to fasthttp
	myHandler := &MyHandler{
		foobar: "foobar",
	}
	fasthttp.ListenAndServe(":8080", myHandler.HandleFastHTTP)

	// pass plain function to fasthttp
	fasthttp.ListenAndServe(":8081", fastHTTPHandler)

	requestHandler := func(ctx *fasthttp.RequestCtx) {
		// set some headers and status code first
		ctx.SetContentType("foo/bar")
		ctx.SetStatusCode(fasthttp.StatusOK)

		// then write the first part of body
		fmt.Fprintf(ctx, "this is the first part of body\n")

		// then set more headers
		ctx.Response.Header.Set("Foo-Bar", "baz")

		// then write more body
		fmt.Fprintf(ctx, "this is the second part of body\n")

		// then override already written body
		ctx.SetBody([]byte("this is completely new body contents"))

		// then update status code
		ctx.SetStatusCode(fasthttp.StatusNotFound)

		// basically, anything may be updated many times before
		// returning from RequestHandler.
		//
		// Unlike net/http fasthttp doesn't put response to the wire until
		// returning from RequestHandler.
	}
	fasthttp.ListenAndServe(":8082", requestHandler)
}
