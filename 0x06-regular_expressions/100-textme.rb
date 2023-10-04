#!/usr/bin/env ruby
puts ARGV[0].scan(/((?<=from:)\S*[^\]\s])|((?<=to:)\S*[^]\s])|((?<=flags:)\S*[^]\s])/).join(",")
