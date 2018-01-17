package main

import (
	"os"
	"text/template"
)

type Todo struct {
	Name        string
	Description string
}

func main() {
	td := Todo{"Hello, templates", "What can you do?"}

	t, err := template.New("todos").Parse("There is a task called {{.Name}}, with description {{.Description}}")

	if err != nil {
		panic(err)
	}

	err = t.Execute(os.Stdout, td)

	if err != nil {
		panic(err)
	}
}
