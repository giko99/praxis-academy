#!/bin/bash

Recipient="giko@students.unnes.ac.id"
subject="Greeting"
Message="Welcome to our site"
`mutt -s $Subject $Recipient <<< $Message`

