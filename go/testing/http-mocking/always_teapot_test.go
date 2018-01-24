package always_teapot

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

const checkMark = "\u2713"
const ballotX = "\u2717"

func mockServer() *httptest.Server {
	f := func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusTeapot)
	}

	return httptest.NewServer(http.HandlerFunc(f))
}

func TestTeapot(t *testing.T) {
	expectedStatus := http.StatusTeapot

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
