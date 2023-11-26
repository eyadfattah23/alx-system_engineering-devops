# script to install flask.

package {'Flask':
  ensure   => '2.1.0',
  provider => pip3,
}

# install Werkzeug version 2.0.0

package {'werkzeug':
  ensure   => '0.16.1',
  provider => pip3,
}
