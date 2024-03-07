package greetings

import (
	"errors"
	"fmt"
	"math/rand"
)

func Hello(name string) (string, error) {
	// return the greeting that embeds the name in a message.
	if name == "" {
		return "", errors.New("empty name")
	}

	message := fmt.Sprintf(randomFormat(), name)
	return message, nil

}

// hellos returns a map that associates each of the named people
// with a greeting message
func Hellos(names []string) (map[string]string, error) {
	// A map to associate names with messages
	messages := make(map[string]string)

	// loop through the received slice of names, and calling the Hello function on each name
	for _, name := range names {
		message, err := Hello(name)
		if err != nil {
			return nil, err
		}
		// in the map associate the retrieved message with the name
		messages[name] = message
	}
	return messages, nil
}

// randomFormat retuns one of a set of greeting messages. The returned
// message is selected at random
func randomFormat() string {
	// A slice of message formats
	formats := []string{
		"Hi, %v Welcome!",
		"Great to see you! %v",
		"Hail, %v, Well met!",
	}

	// Return a randomly selected message format by specifying a random index
	return formats[rand.Intn(len(formats))]
}
