#!/usr/bin/env ruby
puts ARGV[0].scan(/((?<=from:)\S*[^\]\s])|((?<=to:)\S*[^]\s])|((?<=flags:)\S*[^]\s])/).join(",")
# look behind the 0 or more non white space character and not equal ']'
