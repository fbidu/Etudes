package main

import (
	"fmt"
	"net/http"
	"net/http/httptest"
	"testing"
)

const checkMark = "\u2713"
const ballotX = "\u2717"

var home = `{
"name": "Alderaan",
"rotation_period": "24",
"orbital_period": "364",
"diameter": "12500",
"climate": "temperate",
"gravity": "1 standard",
"terrain": "grasslands, mountains",
"surface_water": "40",
"population": "2000000000",
"residents": [
	"https://swapi.co/api/people/5/",
	"https://swapi.co/api/people/68/",
	"https://swapi.co/api/people/81/"
],
"films": [
	"https://swapi.co/api/films/6/",
	"https://swapi.co/api/films/1/"
],
"created": "2014-12-10T11:35:48.479000Z",
"edited": "2014-12-20T20:58:18.420000Z",
"url": "https://swapi.co/api/planets/2/"
}`

func mockServer() *httptest.Server {
	f := func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		w.Header().Set("Content-Type", "application/json")
		fmt.Fprintln(w, home)
	}

	return httptest.NewServer(http.HandlerFunc(f))
}

func TestTeapot(t *testing.T) {
	expectedStatus := http.StatusOK

	server := mockServer()
	defer server.Close()

	t.Log("Are we dealing with a teapot here?")
	{
		t.Logf("\tWhen dealing with the server, we expect it to be a teapot")
		resp, err := http.Get(server.URL)

		if err != nil {
			t.Fatal("\t\tWasn't able to reach the server!", ballotX, err)
		}
		t.Log("\t\tWas able to make the call!", checkMark)

		if resp.StatusCode != expectedStatus {
			t.Fatalf("\t\tShould receive a \"%d\" status. %v %v", expectedStatus,
				ballotX, resp.StatusCode)
		}

		t.Logf("\t\tShould receive a \"%d\" status. %v", expectedStatus, checkMark)
	}
}
